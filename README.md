# CS4348 Project 2

## How to Run

Clone the repo.

Make sure python3 is installed.

Open terminal and run:

```bash
python3 main.py
```

## How the Program Works

1. The program starts three teller threads and waits until all three are ready.
2. It starts 50 customer threads. Each customer chooses a deposit or withdrawal and waits 0 to 100 milliseconds before arriving.
3. Customers enter through a door that allows two customers at a time.
4. Each customer joins a shared waiting line. An available teller selects a customer from the line.
5. The customer introduces itself and tells the teller which transaction it wants.
6. For a withdrawal, the teller gets manager permission first. Only one teller can use the manager at a time. This takes 5 to 30 milliseconds.
7. Both deposits and withdrawals use the safe. Only two tellers can use the safe at a time. Processing takes 10 to 50 milliseconds.
8. The customer waits until its transaction is complete, leaves the teller, and exits through the door.
9. After all 50 customers finish and leave, the program signals all three tellers to stop and closes the bank.

## Main Functions

- `main()` starts customer and teller threads, waits for them using `join()`, and closes the bank.
- `teller_worker()` serves customers, gets manager permission for withdrawals, and uses the safe.
- `customer_worker()` handles customer arrival, waiting in line, transaction requests, and departure.
- `print_action()` uses a semaphore to keep printed messages from mixing together.

## Shared Resources

- `safe_sem` allows two tellers inside the safe at once.
- `manager_sem` allows one teller to access the manager at once.
- `door_sem` allows two customers to use the door at once.
- `line_lock` protects the shared customer waiting line.
- `print_lock` prevents output lines from mixing.
- `customers_waiting` notifies tellers when a customer joins the line.
- `tellers_ready` lets the program wait until all three tellers are ready.
- `waiting_line` is a `deque` that holds customers waiting to be served.

## Files

- `main.py` - Complete bank simulation
- `devlog.md` - Development notes for each coding session
- `README.md` - Instructions and project overview
