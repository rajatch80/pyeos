import unittest

from src.rpc_api.chain import ChainClient
from src.config import CHAIN_URL
import test.fixtures as fixtures


class Chaintest(unittest.TestCase):
    def setUp(self):
        self.chain_client = ChainClient(CHAIN_URL)

    def test_get_info(self):
        info = self.chain_client.get_info()
        for key in fixtures.INFO_KEYS:
            self.assertIn(key, info)

    def test_get_account(self):
        account = self.chain_client.get_account("eosio")
        for key in fixtures.ACCOUNT_DICT_KEYS:
            self.assertIn(key, account)
        self.assertEqual(account["account_name"], "eosio")
        self.assertIsInstance(account["permissions"], list)
        self.assertIsInstance(account["net_limit"], dict)
        self.assertIsInstance(account["cpu_limit"], dict)

    def test_get_block(self):
        block_by_number = self.chain_client.get_block(2)
        block_by_id = self.chain_client.get_block(
            "0000000130d70e94e0022fd2fa035cabb9e542c34ea27f572ac90b5a7aa3d891")
        for key in fixtures.BLOCK_KEYS:
            self.assertIn(key, block_by_number)
            self.assertIn(key, block_by_id)
        self.assertEqual(block_by_number["block_num"], 2)
        self.assertEqual(
            block_by_id["id"],
            "0000000130d70e94e0022fd2fa035cabb9e542c34ea27f572ac90b5a7aa3d891")
        self.assertNotEqual(block_by_number["block_num"],
                            block_by_id["block_num"])
        self.assertNotEqual(block_by_number["id"], block_by_id["id"])

    def test_abi_json_to_abi(self):
        test_args = {
            "author": "mynewaccount",
            "id": 4,
            "description": "second task"
        }
        binargs = self.chain_client.abi_json_to_bin("mynewaccount", "create",
                                                    **test_args)
        for key in fixtures.ABI_JSON_TO_ABI_KEYS:
            self.assertIn(key, binargs)
        self.assertNotEqual(len(binargs["binargs"]), 0)


if __name__ == '__main__':
    unittest.main()
