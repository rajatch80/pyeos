import json
from src.config import CHAIN_API_ENUM, CHAIN_URL, CHAIN_API
from src.helpers.utils import make_post_request


class ChainClient:

    def __init__(self, chain_url=CHAIN_URL):
        self.base_url = chain_url + CHAIN_API

    def get_info(self):
        """
        Returns an object containing various details about the blockchain.
        """
        url = self.base_url + CHAIN_API_ENUM.get('GET_INFO')
        return make_post_request(url)

    def get_account(self, account_name):
        """
        Returns an object containing various details about a specific account on the blockchain.
            :param account_name: name of account in blockchain
        """
        url = self.base_url + CHAIN_API_ENUM.get('GET_ACCOUNT')
        payload = {
            "account_name": account_name
        }
        return make_post_request(url, json.dumps(payload))

    def get_block(self, block_num_or_id):
        """
        Returns an object containing various details about a specific block on the blockchain.
            :param block_num_or_id: id or block number
        """
        url = self.base_url + CHAIN_API_ENUM.get('GET_BLOCK')
        payload = {
            "block_num_or_id": str(block_num_or_id)
        }
        return make_post_request(url, json.dumps(payload))

    def abi_json_to_bin(self, account_name, action, **kwargs):
        """
        Serializes json to binary hex.
        The resulting binary hex is usually used for the data field in push_transaction.
            :param account_name: name of acocunt
            :param action: name of action (function defined in contract)
            :param kwargs: action parameters
        """
        url = self.base_url + CHAIN_API_ENUM.get('ABI_JSON_TO_BIN')
        payload = {
            "code": account_name,
            "action": action,
            "args": kwargs
        }
        return make_post_request(url, json.dumps(payload))

    def get_required_keys(self, transaction, available_keys):
        """
        Returns the required keys needed to sign a transaction.
            :param transaction: transaction object
            :param available_keys: available public keys
        """
        url = self.base_url + CHAIN_API_ENUM.get('GET_REQUIRED_KEYS')
        payload = {
            "transaction": transaction,
            "available_keys": available_keys
        }
        return make_post_request(url, json.dumps(payload))

    def push_transaction(self, transaction, signatures):
        """
        Applies a transaction in json format to the blockchain
            :param transaction: transaction to push
        """
        url = self.base_url + CHAIN_API_ENUM.get('PUSH_TRANSACTION')
        payload = {
            "compression": "none",
            "transaction": transaction,
            "signatures": signatures
        }
        return make_post_request(url, json.dumps(payload))
