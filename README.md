# WalletCasino

Dive into the vast ocean of blockchain wallets! While the odds of hitting a jackpot with a non-zero balance might be slim, with WalletCasino, you can test your luck across multiple networks. 🎰
![img.png](imgs_for_readme%2Fimg.png)
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

To customize the behavior of this tool, adjust settings in the `src/config.py` file or set environment variables:

1. **BSC Nodes**: A list of BSC node endpoints. The default includes several from Binance.

2. **ETH Nodes**: Endpoint(s) for connecting to Ethereum nodes.

3. **Number of Threads**: Configure concurrency for wallet generation and checking. The default is 16.

4. **Logging**: Determine if logging is active. It is enabled by default.

5. **Network Choice**: Specify whether to check the Ethereum network. It is turned off by default.

6. **File with Wallets**: This file contains seed phrases with the default name 'raw.txt'. Each phrase should be on a separate line.

To override the default settings via environment variables, execute:

```bash
export BSC_NODES=https://your-bsc-node-endpoint.com/
export ETH_NODES=https://your-eth-node-endpoint.com/
export FILE_WITH_WALLETS=path/to/your/file.txt
```

For a full list of adjustable parameters and their defaults, please check `src/config.py`.

## Usage

1. Once settings are adjusted, select the desired script:

   - For random wallet checking:

    ```bash
    python wallet_checker.py
    ```

   - For file checking:

    ```bash
    python file_checker.py
    ```

2. When a wallet with transactions is found, a message is displayed in the console. Wallet data will be saved in a separate file "wallets_with_transactions.log"

## License

This project is licensed under the MIT License.