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