# 11-1-2026 11:31pm - Session 1 Start
I have looked at the requirements for Project 2.
I will need at least 2 entries per session to record my thoughts for the devlog.
We will be simulating a bank using threads, semaphores, and shared memory.
I plan to code the whole project in python and in one main.py file.

For this first session, I just plan to look at making threads.
I have made a repo on GitHub and will upload all the project information to the repo.
The plan is to at least start with main.py and create threads.

# 11-2-2026 12:19pm - Session 1 End
I created main.py.
I found out how to make basic threads with python. 
I made a function that prints when a threads starts and finishes for now.
It works with the three teller threads that I tested. 
So far main.py runs and prints when the three tellers start and finish.
In the next session I plan to add shared bank resources.
I will probably experiment with semaphores to control how multiple threads access them.

# 11-2-2026 8:11pm - Session 2 Start
Right now I have main.py working with three tellers using the threading Python module.
main.py only creates teller threads and doesn't have any shared bank resources yet
I looked at the example programs to see how semaphores work and how they can control access to shared variables.
I will probably need semaphores for the safe, manager, door, and waiting line.
In this session I will try to add shared bank resources to main.py.

# 11-2-2026 9:04pm - Session 2 End
I added shared bank resources to main.py.
I created 50 customers and made semaphores for the safe, manager, door, and waiting line.
The safe and door allow two threads at a time.
The manager and waiting line only allow one thread at a time.
I tested the safe semaphore using the three teller threads from the last session.
I ran into some bugs.
I forgot to release a semaphore and I had acquire() and release() in the wrong order so a teller aquired access to the safe but never released it.
The bugs were fixed and the program ran eventually ran successfully.
I noticed that the third teller had to wait until one of the first two tellers released the safe.

# 11-3-2026 8:02pm - Session 3 Start
Right now, main.py has semaphores for the safe, manager, door, and waiting line.
The program currently only tests how three tellers access the safe.
I plan to work on communication between one customer and one teller.
I will have just one customer and one teller to keep things simple.
The customer will join the waiting line and signal the teller that someone is waiting.
The teller will then select the customer from the queue, and the customer will introduce itself.
I will use semaphores to make sure both threads communicate in the correct order.

# 11-3-2026 9:28pm - Session 3 End
The code should allow one customer and one teller to communicate.
It stores customer information and I added semaphores to control when the customer gets selected.
I was able to get some basic customer-teller interaction.
There are currently some bugs.
The program now gets stuck and hangs while getting a teller.
The teller waits indefinitely for a customer and the customer cannot proceed after being selected.
I plan to fix these bugs in the next session before adding more tellers and customers.

# 11-4-2026 4:37pm - Session 4 Start
Last session I worked on communication between one customer and one teller.
The program currently gets stuck because of some bugs.
I think the bugs are because of some synchronization issues.
I plan to fix these issues first and make sure one customer and one teller can communicate and finish correctly.

After fixing the bugs, I plan to update the program to handle three tellers and multiple customers.
I will start by testing with three customers, then increase it to five and ten.
I hope to have three tellers serving multiple customers without getting stuck and have all threads terminate correctly.

# 11-4-2026 5:42pm - Session 4 End
I fixed the three synchronization bugs from the last session.
I added the missing release() calls for customers_waiting, line_lock, and the semaphore.
This fixed the issue where the program would get stuck waiting for a customer or teller.
I updated main.py to create three teller threads and multiple customer threads.
Tellers can now continue serving customers instead of stopping after one.
The program now currently works and the tellers were able to serve multiple customers using a shared waiting line.