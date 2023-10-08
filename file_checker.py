import threading
from src.config import NUMBER_OF_THREADS
from src.wallet_generator import WalletGenerator


def divide_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def start_threads_for_mnemonics(divided_mnemonics_phrases):
    threads = []
    for mnemonics_list in divided_mnemonics_phrases:
        # Используем статический метод run_mnemonics_processor из WalletGenerator
        thread = threading.Thread(target=WalletGenerator.run_mnemonics_processor, args=(mnemonics_list,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    print("Bot started")

    with open("raw.txt", "r") as file:
        all_mnemonics = [mnemonic.strip() for mnemonic in file.readlines()]

    chunk_size = len(all_mnemonics) // NUMBER_OF_THREADS
    divided_mnemonics = list(divide_list(all_mnemonics, chunk_size))

    start_threads_for_mnemonics(divided_mnemonics)
