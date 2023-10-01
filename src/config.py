import os

# Endpoint to connect to the BSC node. Can be overridden by an environment variable.
BSC_NODE_ENDPOINT = os.environ.get('BSC_NODE_ENDPOINT', 'https://bsc-dataseed1.binance.org/')

# Filename to save the details of wallets with a non-zero balance.
WALLETS_WITH_BALANCE_FILENAME = os.environ.get('WALLETS_WITH_BALANCE_FILENAME', "wallets_with_balance.txt")

# Number of concurrent threads to run for wallet generation and checking.
NUMBER_OF_THREADS = int(os.environ.get('NUMBER_OF_THREADS', 20))

# Variable to enable logging. Logging is disabled by default
LOGGING_ENABLE = os.environ.get('LOGGING_ENABLE', False)
