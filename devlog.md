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

# 11-5-2026 8:17pm - Session 5 Start
main.py is able to handle three tellers and multiple customers.
The bugs I had were fixed in the last session so now the program does not hang anymore.
Right now the customers cannot request transactions yet.
I plan to add deposit and withdrawal transactions in this session.
I also plan to use more semaphores to make sure the teller asks for the transaction before the customer responds.
I will add another signal so the teller knows when the customer leaves.

# 11-5-2026 10:46pm - Session 5 End
I updated main.py to handle deposit and withdrawal transactions.
I randomly assigned each customer a transaction and stored it in customer_info.
I added more semaphores so the teller can ask for the transaction and wait for the customer to respond.
I also added transaction_finished and left_teller so customers wait until their transactions are finished and tellers wait until customers leave before serving someone else.

I tested the program with 10 customers and three tellers.
The program ran successfully and all 10 customers finished their transactions without getting stuck.
All three teller threads also terminated correctly.
I plan to add manager permission for withdrawal transactions next.

# 11-13-2026 7:57pm - Session 6 Start
The program can now handle three tellers and multiple customers requesting transactions.
I also added semaphores to make sure customers wait until their transactions are finished before leaving.
Right now, both deposits and withdrawals are handled the same way.
I am going to add manager permission for withdrawals before they can be processed.

I plan to update teller_worker() to check if a transaction is a withdrawal.
If it is a withdrawal, the teller will need to get permission from the manager before continuing.
I will make sure only one teller can access the manager at a time.
Deposit transactions should not need manager permission.

# 11-13-2026 8:20pm - Session 6 End
I updated teller_worker() to require manager permission for withdrawal transactions.
I used manager_sem to make sure only one teller can access the manager at a time.
Deposit transactions skip the manager and continue normally.

The program ran successfully and all customers completed their transactions without getting stuck.
The withdrawals received manager permission before continuing, and all three teller threads terminated correctly.
Next, I plan to implement safe access for both deposits and withdrawals.

# 11-14-2026 5:58pm - Session 7 Start
I have manager permission for withdrawal transactions now.
Deposit transactions skip the manager and continue normally.
Right now, the program still uses a fixed delay to simulate transactions and does not use the safe semaphore yet.

I plan to update teller_worker() so both deposits and withdrawals need to access the safe.
I will use safe_sem to make sure only two tellers can enter the safe at a time.
If two tellers are already using the safe, the third teller will have to wait.
I will add messages for when a teller approaches, enters, and leaves the safe.
I hope to have both transactions using the safe without exceeding its capacity or causing the program to get stuck.

# 11-14-2026 6:21pm - Session 7 End
I updated teller_worker() so both deposit and withdrawal transactions use the safe.
I used safe_sem to make sure only two tellers can enter the safe at a time.
I also added messages for when a teller approaches, enters, and leaves the safe.
Withdrawals still need manager permission before entering the safe.
The transaction delay and the manager delay is a random delay between 10 and 50 milliseconds.

The program ran successfully and all customers finished their transactions without getting stuck.
The safe semaphore limits access to two tellers at a time, and the manager semaphore only allows one teller at a time.
After this I will probably plan to add customer arrival delays and use door_sem to control customers entering and leaving the bank.

# 11-14-2026 11:52pm - Session 8 Start
I have added safe access for both deposit and withdrawal transactions.
The program now uses safe_sem to make sure only two tellers can enter the safe at a time.
Withdrawals still need manager permission before using the safe.
Right now, customers join the waiting line immediately, and the program does not use door_sem yet.

I plan to add synchronization so the bank only opens when all three tellers are ready.
I plan to use door_sem to make sure only two customers can enter or leave the bank at a time.
Customers will need to acquire the door semaphore before entering or leaving and release it afterward.

# 11-15-2026 12:54pm - Session 8 End
I updated main.py to handle bank opening and customer entrance.
I added tellers_ready to make sure all three tellers are ready before customers can enter the bank.
I also added random arrival delays between 0 and 100 milliseconds.
I used door_sem to make sure only two customers can enter or leave the bank at a time.

The program ran successfully and all customers completed their transactions and left the bank without getting stuck.
The door semaphore limits how many customers can use the entrance at once.

# 11-15-2026 3:39pm - Session 9 Start
I added bank opening synchronization and customer entrance restrictions.
The program now waits until all three tellers are ready before starting customers.
I also added random customer arrival delays and used door_sem to limit how many customers can enter or leave at the same time.

I plan to increase the simulation to 50 customers instead of the current 10 customers I have been using for testing.
I will keep the three teller threads and make sure they can continue serving customers from the shared waiting line.
I also plan to check that customers wait when all tellers are busy and that each customer finishes their transaction before leaving.
The program already uses join() to wait for customers and None in the waiting queue to stop tellers.

# 11-15-2026 4:12pm - Session 9 End
I updated main.py to run the full simulation with 50 customers instead of 10.
I kept the three teller threads and used the shared waiting line to handle customer transactions.
I also kept join() to make sure all customers finish and leave the bank before shutting down the tellers.
I updated the teller shutdown messages to say they are leaving for the day.
I also added a final message to print when the bank closes.

I tested the program with 50 customers and three tellers.
The program ran successfully and all 50 customers completed their transactions and left the bank without getting stuck.
All three teller threads also terminated correctly.
The bank closing message printed after all customers and tellers finished.

The next session I plan to create the README and do a final check on the project requirepments.