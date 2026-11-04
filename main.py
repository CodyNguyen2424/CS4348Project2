import threading
import time
import random
from collections import deque

NUM_TELLERS = 3
NUM_CUSTOMERS = 50

# Shared bank resources
safe_sem = threading.Semaphore(2)
manager_sem = threading.Semaphore(1)
door_sem = threading.Semaphore(2)
line_lock = threading.Semaphore(1)

# When customers arrive
customers_waiting = threading.Semaphore(0)
waiting_line = deque()


def teller_worker(teller_id):
    print(f"Teller {teller_id} []: ready to serve")
    print(f"Teller {teller_id} []: waiting for a customer")

    customers_waiting.acquire()

    line_lock.acquire()
    customer_info = waiting_line.popleft()
    line_lock.release()

    customer_id = customer_info["id"]
    customer_info["teller_id"] = teller_id

    # Wait for customer introduction
    customer_info["introduced"].acquire()
    print(f"Teller {teller_id} [Customer {customer_id}]: serving a customer")

    customer_info["acknowledged"].release()
    print(f"Teller {teller_id} []: thread finished")


def customer_worker(customer_id):
    # Keep signals separate for each customer
    customer_info = {
        "id": customer_id,
        "teller_id": None,
        "called": threading.Semaphore(0),
        "introduced": threading.Semaphore(0),
        "acknowledged": threading.Semaphore(0)
    }

    print(f"Customer {customer_id} []: getting in line.")

    line_lock.acquire()
    waiting_line.append(customer_info)

    print(f"Customer {customer_id} []: selecting a teller.")

    customer_info["called"].acquire()
    teller_id = customer_info["teller_id"]

    print(f"Customer {customer_id} [Teller {teller_id}]: selects teller")
    print(f"Customer {customer_id} [Teller {teller_id}]: introduces itself")
    customer_info["introduced"].release()

    customer_info["acknowledged"].acquire()
    print(f"Customer {customer_id} []: thread finished")


def main():
    teller_threads = []
    customer_threads = []

    for teller_id in range(1):
        teller = threading.Thread(target=teller_worker, args=(teller_id,))
        teller_threads.append(teller)
        teller.start()

    for customer_id in range(1):
        customer = threading.Thread(target=customer_worker, args=(customer_id,))
        customer_threads.append(customer)
        customer.start()

    # Wait for customer and teller threads
    for customer in customer_threads:
        customer.join()

    for teller in teller_threads:
        teller.join()

    print("All threads finished")


if __name__ == "__main__":
    main()
