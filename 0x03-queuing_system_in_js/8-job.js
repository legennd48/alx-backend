const kue = require('kue');

/**
 * Creates push notification jobs in the queue.
 * 
 * @param {Array} jobs - An array of job objects.
 * @param {Object} queue - The Kue queue instance.
 * @throws {Error} - Throws an error if jobs is not an array.
 */

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData).save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            }
        });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        }).on('failed', (error) => {
            console.log(`Notification job ${job.id} failed: ${error.message}`);
        }).on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });
}

module.exports = createPushNotificationsJobs;
