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
    print(f"Teller {teller_id} []: thread started")

    # Test safe capacity
    safe_sem.acquire()
    print(f"Teller {teller_id} []: acquired safe access")

    time.sleep(1.0)

    print(f"Teller {teller_id} []: releasing safe access")
    safe_sem.release()

    print(f"Teller {teller_id} []: thread finished")


def main():
    teller_threads = []

    # Start teller threads
    for teller_id in range(NUM_TELLERS):
        teller = threading.Thread(target=teller_worker, args=(teller_id,))
        teller_threads.append(teller)
        teller.start()

    # Wait for threads to finish
    for teller in teller_threads:
        teller.join()

    print("All teller threads finished")


if __name__ == "__main__":
    main()
