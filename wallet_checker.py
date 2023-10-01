import threading

from src.config import NUMBER_OF_THREADS
from src.wallet_generator import BSCWalletGenerator


def run_wallet_generator():
    generator = BSCWalletGenerator()
    if generator.create_and_check_wallet():
        print(f"Non-zero balance found!")


if __name__ == "__main__":
    while True:
        threads = []
        for _ in range(NUMBER_OF_THREADS):
            thread = threading.Thread(target=run_wallet_generator)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
