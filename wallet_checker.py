import threading

from src.config import NUMBER_OF_THREADS
from src.wallet_generator import WalletGenerator


def run_wallet_generator():
    generator = WalletGenerator()
    if generator.create_and_check_wallet():
        print(f"Wallet with transactions found!")


if __name__ == "__main__":
    print("Bot started")

    while True:
        threads = []
        for _ in range(NUMBER_OF_THREADS):
            thread = threading.Thread(target=run_wallet_generator)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
