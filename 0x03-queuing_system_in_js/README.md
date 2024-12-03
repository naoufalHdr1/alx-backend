# 0x03. Queuing System in JS
`#Back-end` `#JavaScript` `#ES6` `#Redis` `#NodeJS` `#ExpressJS` `#Kue`

## Project Overview
This project aims to implement a queuing system using JavaScript, Node.js, Redis, and Kue. The main objective is to build a basic Express app that interacts with a Redis server and handles tasks using Kue as a queue system.

## Learning Objectives
By the end of this project, you should be able to:

- Run a Redis server on your machine.
- Perform basic Redis operations using the Redis client.
- Use a Redis client with Node.js for operations.
- Store hash values in Redis.
- Handle asynchronous operations with Redis.
- Use Kue as a queue system in your application.
- Build a basic Express application that interacts with a Redis server.
- Integrate a queue system in the Express app using Redis and Kue.

## Resources
Before starting, review the following resources:
- [Redis Quick Start](https://redis.io/docs/getting-started/)
- [Redis Client Interface](https://www.npmjs.com/package/redis)
- [Redis Client for Node.js](https://www.npmjs.com/package/redis)
- [Kue (Deprecated but Still in Use)](https://github.com/Automattic/kue)

### Required Files for the Project:
- `package.json`: Contains metadata and dependencies.
- `.babelrc`: Babel configuration for JavaScript transpiling.

## Installation Instructions

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/queuing-system-js.git
    cd queuing-system-js
    ```
2. Install the required dependencies:
    ```bash
    npm install
    ```
3. Start the Redis server:
- Ensure you have Redis installed. If not, follow the Redis installation guide.
- Run Redis server:
    ```bash
    redis-server
    ```
4. Start the Node.js application:
    ```bash
    npm start
    ```
5. You can now interact with the Redis server and use the queuing system.

## Usage
The app creates a simple queuing system that allows you to add tasks to a queue and process them asynchronously.

- To add tasks to the queue: The app exposes a route that triggers the addition of tasks to the queue.
- To process tasks in the queue: The app uses Kue to handle tasks asynchronously and process them.

## Testing
To ensure your application is functioning correctly, you can use manual testing or integrate unit testing as per your project needs.

## Tasks

### Task: Install a Redis instance

1. Download, extract, and compile `Redis` version `6.0.10` or higher.
2. Start the `Redis` server in the background.
3. Test `Redis` by using the `PING` command and `set/get` a key-value pair ("Holberton" -> "School").
4. Stop the `Redis` server by killing the process.
5. Copy the `dump.rdb` file into the root of the Queuing project.

**Requirement:**
- Running get Holberton should return "School".

### Task 1: Node Redis Client

1. Install the `node_redis` library using npm.
2. Write a script `0-redis_client.js` using Babel and ES6 syntax. The script should:
    - Connect to the `Redis` server running locally.
    - Log a success message when the connection is successful: "Redis client connected to the server".
    - Log an error message when the connection fails: "Redis client not connected to the server: `ERROR_MESSAGE`".
3. Ensure that you use the `import` keyword to import the `Redis` library.

**Expected Behavior:**
- When `Redis` is not running, it should log the error message.
- When `Redis` is running, it should log the success message.

### Task 2: Node Redis client and basic operations

1. In the file `1-redis_op.js`, copy the code from `0-redis_client.js`.
2. Add two functions:
    - **setNewSchool:**
        - Accepts two arguments: `schoolName` and `value`.
        - Sets the value for the key `schoolName` in Redis.
        - Displays a confirmation message using `redis.print`.
    - **displaySchoolValue:**
        - Accepts one argument: `schoolName`.
        - Logs the value for the key `schoolName` to the console.
3. At the end of the file, call:
    - displaySchoolValue('Holberton')
    - setNewSchool('HolbertonSanFrancisco', '100')
    - displaySchoolValue('HolbertonSanFrancisco')

**Requirements:**
- Use callbacks for Redis operations (no promises or async/await).

### Task 3: Node Redis client and async operations

1. Copy the code from `1-redis_op.js` to a new file named `2-redis_op_async.js`.
2. Use `promisify` to modify the function `displaySchoolValue`:
    - Convert it to use ES6 `async/await` syntax instead of callbacks.
3. Ensure the output is the same as in `1-redis_op.js`.

**Expected Behavior:**
- The code should still display the school values, set a new value, and log the results, but now using `async/await` for asynchronous operations.

### Task 4: Node Redis client and advanced operations

1. Create a new file named `4-redis_advanced_op.js`.
2. Create Hash:
    - Use `hset` to store the following key-value pairs in a hash with the key `HolbertonSchools`:
        - Portland=50
        - Seattle=80
        - New York=20
        - Bogota=20
        - Cali=40
        - Paris=2
    - Use redis.print to confirm each hset operation.
3. Display Hash:
    - Use hgetall to retrieve and display the entire hash stored in Redis.

**Expected Output:**
- The hash values are stored successfully, and the displayed object matches the stored values.

### Task 5: Node Redis client publisher and subscriber

in the file `5-subscriber.js`
1. Create a Redis client.
2. Log: `"Redis client connected to the server"` on connect, and `"Redis client not connected to the server: ERROR_MESSAGE"` on error.
3. Subscribe to `holberton school channel`.
4. Log received messages. If the message is `"KILL_SERVER"`, unsubscribe and quit.

In the file `5-publisher.js`
1. Create a Redis client.
2. Log: `"Redis client connected to the server"` on connect, and `"Redis client not connected to the server: ERROR_MESSAGE"` on error.
3. Define `publishMessage(message, time)`:
    - After `time` ms, log `"About to send MESSAGE"` and publish to `holberton school channel`.

### Task 6: Create the Job creator

- Sets up a `push_notification_code` queue with Kue.
- Defines `sendNotification(phoneNumber, message)` to log notification details.
- Processes jobs by calling `sendNotification` with job data.
- Works with `6-job_creator.js` to handle notifications concurrently.

**Purpose:**
- Efficient background job handling for notifications.

### Task 7: Create the Job processor

1. Setup:
- Creates Kue queue `push_notification_code`.
- Defines `sendNotification(phoneNumber, message)`.
2. Processing:
- Listens on the queue and logs notifications.
3. Logs:
- Creator: `Notification job created: JOB_ID`.
- Processor: `Sending notification to PHONE_NUMBER, with message: MESSAGE`.

### Task 8: Track progress and errors with Kue: Create the Job creator

- **Data Setup:** Defines an array `jobs` with phone numbers and verification messages.
- **Queue Creation:** Initializes the `push_notification_code_2` queue with Kue.
- **Job Handling:**
    - Iterates through `jobs` to create a new job for each item in the array.
    - Logs messages for each job lifecycle

**Purpose:**
- Bulk job creation and monitoring for notifications.

### Task 9: Track progress and errors with Kue: Create the Job processor

1. Blacklist:
- Includes `4153518780` and `4153518781`.
2. sendNotification Function:
- Tracks job progress (0%, 50%, complete).
- Fails if the phone number is blacklisted.
3. Queue:
- Processes `push_notification_code_2` with 2 jobs concurrently.

**Logs:**
- Success: `Sending notification to PHONE_NUMBER, with message: MESSAGE`.
- Failure: `Notification job #ID failed: Phone number PHONE_NUMBER is blacklisted`.
