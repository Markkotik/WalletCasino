# WalletCasino

Chance of finding a wallet with a balance is microscopic, but hey, why not try your luck? 🎰

## Description
WalletCasino is a tool designed to generate and check Binance Smart Chain (BSC) wallets. Its primary objective is to create wallets and verify their balances. When a non-zero balance is discovered, the wallet details are saved to a separate file.

## Installation Instructions
Clone the repository:

    git clone [repository URL]

Install the necessary dependencies:

    pip install -r requirements.txt

## How to Use

### Configuration:
Directly modify settings in src/config.py.
Alternatively, set environment variables to override default settings. For example:

    export BSC_NODE_ENDPOINT=https://your-node-endpoint.com/

### Run the Script:

    python wallet_checker.py

Ensure you refer to src/config.py for details on available environment variable overrides.

## License

MIT License
