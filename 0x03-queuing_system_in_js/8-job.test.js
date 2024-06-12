const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
    let queue;

    /**
     * Sets up the test environment before running the test cases.
     * Initializes the Kue queue and enters test mode.
     */
    before(() => {
        queue = kue.createQueue();
        kue.Job.rangeByType('push_notification_code_3', 'inactive', 0, -1, 'asc', (err, jobs) => {
            jobs.forEach((job) => job.remove());
        });
        queue.testMode.enter();
    });

    /**
     * Clears the test queue after each test case to ensure a clean state.
     */
    afterEach(() => {
        queue.testMode.clear();
    });

    /**
     * Exits the test mode after all test cases are completed.
     */
    after(() => {
        queue.testMode.exit();
    });

    /**
     * Exits the test mode after all test cases are completed.
     */
    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
    });

    /**
     * Tests that createPushNotificationsJobs creates jobs with valid job data.
     */
    it('should create jobs with valid job data', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });

    it('should log job events', (done) => {
        const jobs = [
            {
                phoneNumber: '4153518782',
                message: 'This is the code 7890 to verify your account'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        const job = queue.testMode.jobs[0];

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
            done();
        }).on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err.message}`);
            done(err);
        }).on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });

        job.complete();
    });
});
