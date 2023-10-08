# WalletCasino

Dive into the vast ocean of blockchain wallets! While the odds of hitting a jackpot with a non-zero balance might be slim, with WalletCasino, you can test your luck across multiple networks. 🎰

## Overview

WalletCasino is an advanced tool that can generate and check wallet balances for both Binance Smart Chain (BSC) and Ethereum networks. When you come across a wallet with transactions, the tool immediately saves the wallet details into a separate file. 

One of the notable features is the node rotation mechanism. This boosts the request rate, ensuring that you're not limited by the restrictions of a single node.

## Setting Up

### Prerequisites

Before starting, ensure you have Python and pip installed.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Markkotik/WalletCasino.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WalletCasino
    ```

3. Set up a virtual environment (optional, but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

You can fine-tune the tool's behavior using the `src/config.py` file or environment variables:

1. **BSC Nodes**: List of BSC node endpoints. Defaults include several from Binance.

2. **ETH Nodes**: Endpoint(s) to connect to the Ethereum nodes.

3. **Number of Threads**: Adjust the concurrency for wallet generation and checking.

4. **Logging**: Control whether logging is enabled or not.

5. **Network Choice**: Decide if you want to check the Ethereum network.

For environment variables, you can override defaults. For instance:

```bash
export BSC_NODES=https://your-bsc-node-endpoint.com/
export ETH_NODES=https://your-eth-node-endpoint.com/
```

Please refer to `src/config.py` for all the adjustable parameters and their default values.

## Usage

1. Once you have configured the settings, run the script:

    ```bash
    python wallet_checker.py
    ```

2. Monitor the output or the designated file to check if any wallet with a balance has been found.

## License

This project is licensed under the MIT License.