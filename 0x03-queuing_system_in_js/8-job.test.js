import { expect } from 'chai';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
    let queue;
    let logSpy;

    beforeEach(() => {
        queue = kue.createQueue();
	    queue.testMode.enter();
        logSpy = sinon.spy(console, 'log');         // Spy on console.log
    });

    afterEach(() => {
        queue.testMode.clear(); // Clear the test queue
        queue.testMode.exit();  // Exit test mode
        sinon.restore();        // Restore spied methods
    });

    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs(42, queue)).to.throw('Jobs is not an array');
    });

    it('should create two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account',
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4321 to verify your account',
            },
        ];

        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs).to.have.lengthOf(2); // Correct check
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    });

    it('should handle job events (complete, failed, progress)', (done) => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account',
            },
        ];

        createPushNotificationsJobs(jobs, queue);

        // Get the first job from testMode.jobs
        const job = queue.testMode.jobs[0];

        // Manually trigger events on the job object
        setTimeout(() => {
            try {
                job.emit('progress', 50);
                expect(logSpy.calledWithMatch(/Notification job .* 50% complete/)).to.be.true;

                job.emit('complete');
                expect(logSpy.calledWithMatch(/Notification job .* completed/)).to.be.true;

                job.emit('failed', new Error('Test Error'));
                expect(logSpy.calledWithMatch(/Notification job .* failed: Test Error/)).to.be.true;

                done();
            } catch (error) {
                done(error);
            }
        }, 50);
    });
});

