import json
from src.config import WALLET_API_ENUM, WALLET_URL, WALLET_API
from src.helpers.utils import make_post_request


class WalletClient:

    def __init__(self, wallet_url=WALLET_URL):
        self.base_url = wallet_url + WALLET_API

    def create_wallet(self, wallet_name):
        """
        Creates a new wallet with the given name.
            :param wallet_name(string): name of the wallet to create
        """
        url = self.base_url + WALLET_API_ENUM.get('CREATE_WALLET')
        return make_post_request(url, json.dumps(wallet_name))

    def open_wallet(self, wallet_name):
        """
        Opens an existing wallet of the given name.
            :param wallet_name(string): name of the wallet to create
        """
        url = self.base_url + WALLET_API_ENUM.get('OPEN_WALLET')
        return make_post_request(url, json.dumps(wallet_name))

    def lock_wallet(self, wallet_name):
        """
        Locks an existing wallet of the given name.
            :param wallet_name(string): name of the wallet to create
        """
        url = self.base_url + WALLET_API_ENUM.get('LOCK_WALLET')
        return make_post_request(url, json.dumps(wallet_name))

    def unlock_wallet(self, wallet_name, password):
        """
        Unlocks an existing wallet of the given name.
            :param wallet_name(string): name of the wallet to create
            :param password(string): password for the given wallet
        """
        url = self.base_url + WALLET_API_ENUM.get('UNLOCK_WALLET')
        payload = [wallet_name, password]
        return make_post_request(url, json.dumps(payload))

    def import_key(self, wallet_name, key):
        """
        Unlocks an existing wallet of the given name.
            :param wallet_name(string): name of the wallet to create
            :param key(string): key to import in the wallet. It will be a private key
        """
        url = self.base_url + WALLET_API_ENUM.get('IMPORT_KEY')
        payload = [wallet_name, key]
        return make_post_request(url, json.dumps(payload))

    def sign_transaction(self, transaction, keys, _id=""):
        """
        Signs a transaction.
            :param transaction: transaction to be signed
            :param keys: public keys to cross check the transaction
            :param id: ID for the chain this transaction is targeted towards.
        """
        url = self.base_url + WALLET_API_ENUM.get('SIGN_TRANSACTION')
        payload = [transaction, keys, _id]
        return make_post_request(url, json.dumps(payload))
