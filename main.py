import threading
import time

NUM_TELLERS = 3


def teller_worker(teller_id):
    print(f"Teller {teller_id} []: thread started")

    time.sleep(1.0)

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
