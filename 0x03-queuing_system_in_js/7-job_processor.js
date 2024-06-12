const kue = require('kue');

const queue = kue.createQueue();

const blacklist = [4153518780 , 4153518781];

function sendNotification(phoneNumber, message, job, done) {
    // Track progress
    job.progress(0, 100);

    if (blacklist.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Track job progress
    job.progress(50, 100);

    // log message
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // end job
    done();

}

// Process the queue 'push_notification_code_2'
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
