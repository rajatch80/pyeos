from src.rpc_api.chain import ChainClient
from src.rpc_api.wallet import WalletClient
from src.config import CHAIN_URL, WALLET_URL


class Client:

    def __init__(self, chain_url=CHAIN_URL, wallet_url=WALLET_URL):
        self.chain_api = ChainClient(CHAIN_URL)
        self.wallet_api = WalletClient(WALLET_URL)
    
    def push_action(self, account_name, action, wallet_public_keys, **data):
        """
        Interact with actions defined in the EOS smart contract
            :param account_name(string): name of account
            :param action(string): name of the action deifined in contract
            :param data(dict): dict containing the required parameters for the given action
        """
        # Convert data into binary
        bin_data = self.chain_api.abi_json_to_bin(account_name, action, **data)
        if "binargs" not in bin_data:
            return bin_data
        bin_data = bin_data["binargs"]
        # Get info for the latest block
        latest_block = self.chain_api.get_info()
        if "head_block_num" not in latest_block:
            return latest_block
        head_block_num = latest_block["head_block_num"]
        # Get block specific information
        head_block_info = self.chain_api.get_block(head_block_num)
        if "block_num" not in head_block_info:
            return head_block_info

        timestamp = head_block_info["timestamp"]
        # TODO: find a better way to change this timestamp
        expiration = timestamp[:14] + str(int(timestamp[14:16])+2) + timestamp[16:]
        transaction = {
            "ref_block_num": head_block_num,
            "ref_block_prefix": head_block_info["ref_block_prefix"],
            "expiration": expiration,
            "actions": [{
                "account": account_name,
                "name": action,
                "authorization": [{
                    "actor": account_name,
                    "permission": "active"
                }],
                "data": bin_data
            }],
            "signatures": []
        }
        # Get the required Keys
        required_keys = self.chain_api.get_required_keys(transaction, wallet_public_keys)
        if "required_keys" not in required_keys:
            return required_keys
        required_keys = required_keys["required_keys"]
        # Sign the transaction
        signatures = self.wallet_api.sign_transaction(transaction, required_keys)
        if "signatures" not in signatures:
            return signatures
        # Push the transaction
        pushed_transaction = self.chain_api.push_transaction(transaction, signatures["signatures"])
        if "transaction_id" not in pushed_transaction:
            return pushed_transaction
        return pushed_transaction["transaction_id"]
