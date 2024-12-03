import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs(123, queue)).to.throw('Jobs is not an array');
    });

    it('should create two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account',
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 5678 to verify your account',
            },
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });

    it('should log when a job is created', (done) => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account',
            },
        ];

        const spy = (msg) => {
            expect(msg).to.contain('Notification job created:');
            done();
        };

        // Mock console.log
        const originalLog = console.log;
        console.log = spy;

        createPushNotificationsJobs(jobs, queue);

        console.log = originalLog;
	done();
    });
});

