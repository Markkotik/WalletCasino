import os

# Endpoints to connect to the BSC nodes. Can be overridden by an environment variable.
BSC_NODES = os.environ.get('BSC_NODES', ';'.join([
    'https://bsc-dataseed1.binance.org/',
    'https://bsc-dataseed2.binance.org/',
    'https://bsc-dataseed3.binance.org/',
    'https://bsc-dataseed4.binance.org/',
])).split(';')

# Endpoints to connect to the ETH nodes. Can be overridden by an environment variable.
ETH_NODES = os.environ.get('ETH_NODES', ';'.join([
    'https://eth.public-rpc.com',
])).split(';')

# Filename to save the details of wallets with a non-zero balance.
WALLETS_WITH_BALANCE_FILENAME = os.environ.get('WALLETS_WITH_BALANCE_FILENAME', "wallets_with_balance.txt")

# Number of concurrent threads to run for wallet generation and checking.
NUMBER_OF_THREADS = int(os.environ.get('NUMBER_OF_THREADS', 16))

# Variable to enable logging. Logging is disabled by default
LOGGING_ENABLE = os.environ.get('LOGGING_ENABLE', True)

# Variable to check Ethereum or not
CHECK_ETH = os.environ.get('CHECK_ETH', False)
