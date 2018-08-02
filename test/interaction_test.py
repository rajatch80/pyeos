import unittest

from src.interaction import Client
from src.config import CHAIN_URL, WALLET_URL
import test.fixtures as fixtures


class Interactiontest(unittest.TestCase):

    def setUp(self):
        self.client = Client(CHAIN_URL, WALLET_URL)

    def test_push_action(self):
        pushed_action = self.client.push_action(
            fixtures.PUSH_ACTION_DATA["account_name"],
            fixtures.PUSH_ACTION_DATA["action"],
            fixtures.PUSH_ACTION_DATA["wallet_public_keys"],
            **fixtures.PUSH_ACTION_DATA["data"]
        )
        self.assertNotEqual(len(pushed_action), 0)


if __name__ == '__main__':
    unittest.main()
