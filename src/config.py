import os

# =======================
# NODE CONFIGURATIONS
# =======================

# Binance Smart Chain nodes. Default Binance nodes, override with 'BSC_NODES'.
BSC_NODES = os.environ.get('BSC_NODES', ';'.join([
    'https://bsc-dataseed1.binance.org/',
    'https://bsc-dataseed2.binance.org/',
    'https://bsc-dataseed3.binance.org/',
    'https://bsc-dataseed4.binance.org/',
])).split(';')

# Ethereum nodes. Default public endpoint, override with 'ETH_NODES'.
ETH_NODES = os.environ.get('ETH_NODES', ';'.join([
    'https://eth.public-rpc.com',
])).split(';')

# =======================
# TOOL CONFIGURATIONS
# =======================

# Concurrent threads for wallet tasks. Default is 16, override with 'NUMBER_OF_THREADS'.
NUMBER_OF_THREADS = int(os.environ.get('NUMBER_OF_THREADS', 16))

# Logging status. Default is enabled, override with 'LOGGING_ENABLE'.
LOGGING_ENABLE = os.environ.get('LOGGING_ENABLE', True)

# Check Ethereum network or not. Default is false, override with 'CHECK_ETH'.
CHECK_ETH = os.environ.get('CHECK_ETH', False)
