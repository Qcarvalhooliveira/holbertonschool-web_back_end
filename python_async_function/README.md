# **Python - Async** :computer:

## **Description:** :speech_balloon:

* Python's async is a programming approach that allows asynchronous execution of tasks without blocking the main program's flow. It leverages the async and await keywords to create asynchronous functions (coroutines), enabling efficient handling of I/O-bound operations and concurrent tasks. This enables better resource utilization and responsiveness in applications involving operations like network requests, database access, or file I/O. The asyncio library in Python facilitates the management of asynchronous code execution by providing tools to create, schedule, and coordinate asynchronous tasks.

## **What we should learn from this project:** :bookmark_tabs:

* async and await syntax
* How to execute an async program with asyncio
* How to run concurrent coroutines
* How to create asyncio tasks
* How to use the random module

## **Tasks:** :books:

#### **0. The basics of async**

* Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

#### **1. Let's execute multiple coroutines at the same time with async**

* Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

#### **2. Measure the runtime**

* Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

#### **3. Tasks**

* Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.

#### **4. Tasks**

* Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.


## **Author** :black_nib:

* **Queise Carvalho de Oliveira** - [Queise Oliveira](https://github.com/Qcarvalhooliveira)
