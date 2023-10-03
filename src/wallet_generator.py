import logging

from bip_utils import (
    Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes,
    Bip39MnemonicGenerator, Bip39WordsNum
)
from web3 import Web3

from src.config import BSC_NODES, ETH_NODES, LOGGING_ENABLE, CHECK_ETH
from src.node_rotator import NodeRotator

logging.basicConfig(filename="wallets.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")


class WalletGenerator:
    """
    A class to generate Binance Smart Chain and Ethereum wallets and check their balances.
    """

    bsc_rotator = NodeRotator(BSC_NODES)
    eth_rotator = NodeRotator(ETH_NODES)

    def __init__(self, bsc_node_url=None, eth_node_url=None) -> None:
        if not bsc_node_url:
            bsc_node_url = self.bsc_rotator.get_next_node()
        if not eth_node_url:
            eth_node_url = self.eth_rotator.get_next_node()

        self.bsc_w3 = Web3(Web3.HTTPProvider(bsc_node_url))
        self.eth_w3 = Web3(Web3.HTTPProvider(eth_node_url))
        self._reset_wallet_properties()

    @staticmethod
    def run_mnemonics_processor(mnemonics_list):
        bsc_node = WalletGenerator.bsc_rotator.get_next_node()
        eth_node = WalletGenerator.eth_rotator.get_next_node()
        generator = WalletGenerator(bsc_node, eth_node)
        generator.process_mnemonics(mnemonics_list, CHECK_ETH)

    def create_and_check_wallet(self, mnemo: str = None, check_eth: bool = CHECK_ETH) -> bool:
        """Main function to generate and validate the wallet."""
        if mnemo is None:
            mnemo = self._generate_seed_phrase()

        self._generate_wallet_from_seed(mnemo)
        self._update_transaction_counts(check_eth)

        if LOGGING_ENABLE:
            self._log_wallet_details(check_eth)

        if self.has_transactions(check_eth):
            self._update_balances(check_eth)
            self._convert_keys_to_hex()
            self._save_wallet_with_transactions_to_file()

            return True

    def process_mnemonics(self, mnemonics: list, check_eth: bool = True) -> None:
        for mnemo in mnemonics:
            self.create_and_check_wallet(mnemo, check_eth)

    @staticmethod
    def _generate_seed_phrase() -> str:
        """Generate a new mnemonic seed phrase."""
        return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)

    @staticmethod
    def _generate_bip44_obj(mnemo: str, coin_type: Bip44Coins):
        """Generate a BIP44 object from the mnemonic."""
        seed_bytes = Bip39SeedGenerator(mnemo).Generate()
        return Bip44.FromSeed(seed_bytes, coin_type)

    def _generate_wallet_from_seed(self, mnemo: str) -> None:
        """Generate the wallet details from a given seed phrase."""
        bip_obj = self._generate_bip44_obj(mnemo, Bip44Coins.BINANCE_SMART_CHAIN)
        self._mnemonic = mnemo
        self._private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(
            0).PrivateKey()
        self._public_key = self._private_key.PublicKey()
        self._address = self._public_key.ToAddress()

    def _get_balance(self, w3) -> float:
        """Generalized method to fetch balance."""
        return float(w3.eth.get_balance(self._address))

    def _convert_keys_to_hex(self) -> None:
        """Convert public and private keys to hex format."""
        self._public_key = self._public_key.RawCompressed().ToHex()
        self._private_key = self._private_key.Raw().ToHex()

    def _update_transaction_counts(self, check_eth: bool = True) -> None:
        """Update the transaction counts for BSC and Ethereum networks."""
        self._bsc_tx_count = self.bsc_w3.eth.get_transaction_count(self._address)
        self._eth_tx_count = self.eth_w3.eth.get_transaction_count(self._address) if check_eth else 0

    def _update_balances(self, check_eth: bool = True) -> None:
        """Update the balances for BSC and Ethereum networks."""
        self._bsc_balance = self._get_balance(self.bsc_w3)
        self._eth_balance = self._get_balance(self.eth_w3) if check_eth else 0.0

    def _log_wallet_details(self, check_eth: bool = True) -> None:
        log_msg = f"Seed Phrase: {self._mnemonic}, BSC Transactions: {self._bsc_tx_count}"
        if check_eth:
            log_msg += f", ETH Transactions: {self._eth_tx_count}"
        logging.info(log_msg)

    def _save_wallet_with_transactions_to_file(self) -> None:
        log_message = f"BSC Balance: {self._bsc_balance} wei, " \
                      f"ETH Balance: {self._eth_balance} wei, " \
                      f"Seed Phrase: {self._mnemonic}, " \
                      f"Address: {self._address}, " \
                      f"Public Key: {self._public_key}, " \
                      f"Private Key: {self._private_key}, " \
                      f"BSC Transactions: {self._bsc_tx_count}, " \
                      f"ETH Transactions: {self._eth_tx_count}"

        with open("wallets_with_transactions.log", "a") as file:
            file.write(log_message + "\n")
        print(f"BSC Balance: {self._bsc_balance} wei, ETH Balance: {self._eth_balance} wei")

    def _reset_wallet_properties(self) -> None:
        self._mnemonic = ""
        self._address = ""
        self._public_key = ""
        self._private_key = ""
        self._bsc_balance = 0.0
        self._eth_balance = 0.0
        self._bsc_tx_count = 0
        self._eth_tx_count = 0

    def has_transactions(self, check_eth: bool = True) -> bool:
        return self._bsc_tx_count > 0 or (self._eth_tx_count > 0 and check_eth)
