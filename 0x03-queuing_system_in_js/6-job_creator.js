import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '123456789',
  message: 'Hello, this is your notification message.'
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.log('Error creating job:', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log(`Notification job completed`);
});

job.on('failed', (errMessage) => {
  console.log(`Notification job failed`, errMessage);
});
