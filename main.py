import threading
import time
import random
from collections import deque

NUM_TELLERS = 3
NUM_CUSTOMERS = 50
TEST_CUSTOMERS = 10

# Shared bank resources
safe_sem = threading.Semaphore(2)
manager_sem = threading.Semaphore(1)
door_sem = threading.Semaphore(2)
line_lock = threading.Semaphore(1)
print_lock = threading.Semaphore(1)

customers_waiting = threading.Semaphore(0)
waiting_line = deque()


def print_action(message):
    print_lock.acquire()
    print(message)
    print_lock.release()


def teller_worker(teller_id):
    while True:
        print_action(f"Teller {teller_id} []: ready to serve")
        print_action(f"Teller {teller_id} []: waiting for a customer")

        customers_waiting.acquire()

        line_lock.acquire()
        customer_info = waiting_line.popleft()
        line_lock.release()

        # Stop once no customers remain
        if customer_info is None:
            print_action(f"Teller {teller_id} []: thread finished")
            break

        customer_id = customer_info["id"]
        customer_info["teller_id"] = teller_id
        customer_info["called"].release()

        # Wait for customer introduction
        customer_info["introduced"].acquire()
        print_action(f"Teller {teller_id} [Customer {customer_id}]: serving a customer")

        print_action(f"Teller {teller_id} [Customer {customer_id}]: asks for transaction")
        customer_info["transaction_requested"].release()

        customer_info["transaction_given"].acquire()
        transaction = customer_info["transaction"]
        print_action(f"Teller {teller_id} [Customer {customer_id}]: handling {transaction} transaction")

        time.sleep(0.05)

        print_action(f"Teller {teller_id} [Customer {customer_id}]: finishes {transaction} transaction.")
        print_action(f"Teller {teller_id} [Customer {customer_id}]: wait for customer to leave.")
        customer_info["transaction_finished"].release()

        # Serve next customer after departure
        customer_info["left_teller"].acquire()


def customer_worker(customer_id):
    transaction = random.choice(["deposit", "withdrawal"])

    # Keep signals separate for each customer
    customer_info = {
        "id": customer_id,
        "teller_id": None,
        "transaction": transaction,
        "called": threading.Semaphore(0),
        "introduced": threading.Semaphore(0),
        "transaction_requested": threading.Semaphore(0),
        "transaction_given": threading.Semaphore(0),
        "transaction_finished": threading.Semaphore(0),
        "left_teller": threading.Semaphore(0)
    }

    print_action(f"Customer {customer_id} []: wants to perform a {transaction} transaction")
    print_action(f"Customer {customer_id} []: getting in line.")

    line_lock.acquire()
    waiting_line.append(customer_info)
    line_lock.release()

    print_action(f"Customer {customer_id} []: selecting a teller.")
    customers_waiting.release()

    customer_info["called"].acquire()
    teller_id = customer_info["teller_id"]

    print_action(f"Customer {customer_id} [Teller {teller_id}]: selects teller")
    print_action(f"Customer {customer_id} [Teller {teller_id}]: introduces itself")
    customer_info["introduced"].release()

    customer_info["transaction_requested"].acquire()
    print_action(f"Customer {customer_id} [Teller {teller_id}]: asks for {transaction} transaction")
    customer_info["transaction_given"].release()

    # Wait until teller finishes transaction
    customer_info["transaction_finished"].acquire()
    print_action(f"Customer {customer_id} [Teller {teller_id}]: leaves teller")
    customer_info["left_teller"].release()

    print_action(f"Customer {customer_id} []: thread finished")


def main():
    teller_threads = []
    customer_threads = []

    # Start three teller threads
    for teller_id in range(NUM_TELLERS):
        teller = threading.Thread(target=teller_worker, args=(teller_id,))
        teller_threads.append(teller)
        teller.start()

    for customer_id in range(TEST_CUSTOMERS):
        customer = threading.Thread(target=customer_worker, args=(customer_id,))
        customer_threads.append(customer)
        customer.start()

    # Wait for all customers
    for customer in customer_threads:
        customer.join()

    # Wake tellers so each can exit
    line_lock.acquire()
    for teller_id in range(NUM_TELLERS):
        waiting_line.append(None)
    line_lock.release()

    for teller_id in range(NUM_TELLERS):
        customers_waiting.release()

    for teller in teller_threads:
        teller.join()

    print_action("All threads finished")


if __name__ == "__main__":
    main()
