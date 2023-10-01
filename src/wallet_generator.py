import logging

from bip_utils import (
    Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes,
    Bip39MnemonicGenerator, Bip39WordsNum
)
from web3 import Web3
from .config import BSC_NODE_ENDPOINT, WALLETS_WITH_BALANCE_FILENAME, LOGGING_ENABLE

logging.basicConfig(filename="wallets.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")


class BSCWalletGenerator:
    """
    A class to generate Binance Smart Chain wallets and check their balances.
    """

    def __init__(self) -> None:
        self._w3 = Web3(Web3.HTTPProvider(BSC_NODE_ENDPOINT))
        self._mnemonic = ""
        self._address = ""
        self._public_key = ""
        self._private_key = ""
        self._balance_in_wei = 0.0

    def create_and_check_wallet(self) -> bool:
        """Main function to generate and validate the wallet."""
        self._generate_seed_phrase()
        self._generate_wallet_from_seed()
        has_balance = self._check_balance()

        if LOGGING_ENABLE:
            logging.info(self._generate_log_message())

        if has_balance:
            self._save_wallet_to_file(self._generate_log_message())
            return has_balance

    def _generate_log_message(self) -> str:
        """Generate the log message."""
        return f"Seed Phrase: {self._mnemonic}, Address: {self._address}, " \
               f"Public Key: {self._public_key}, Private Key: {self._private_key}, " \
               f"Balance: {self._balance_in_wei} wei"

    def _generate_seed_phrase(self) -> None:
        """Generate a new mnemonic seed phrase."""
        self._mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)

    def _generate_wallet_from_seed(self) -> None:
        """Generate the wallet details from the seed phrase."""
        bip_obj = self._create_bip44_from_mnemonic(self._mnemonic)
        self._private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(
            0).PrivateKey()
        self._public_key = self._private_key.PublicKey()
        self._address = self._public_key.ToAddress()
        self._convert_keys_to_hex()

    @staticmethod
    def _create_bip44_from_mnemonic(mnemo: str):
        """Create a BIP44 object from the mnemonic."""
        seed_bytes = Bip39SeedGenerator(mnemo).Generate()
        return Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN)

    def _check_balance(self) -> bool:
        """Check if the wallet has a balance."""
        self._balance_in_wei = self._w3.eth.get_balance(self._address)
        return self._balance_in_wei != 0

    def _convert_keys_to_hex(self) -> None:
        """Convert public and private keys to hex format."""
        self._public_key = self._public_key.RawCompressed().ToHex()
        self._private_key = self._private_key.Raw().ToHex()

    @staticmethod
    def _save_wallet_to_file(message: str) -> None:
        """Save the wallet details to a file if it has a balance."""
        with open(WALLETS_WITH_BALANCE_FILENAME, "a") as file:
            file.write(message + "\n")
