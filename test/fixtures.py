INFO_KEYS = [
    "head_block_time", "virtual_block_cpu_limit", "server_version",
    "last_irreversible_block_id", "head_block_id", "head_block_num",
    "block_cpu_limit", "last_irreversible_block_num",
    "virtual_block_net_limit", "block_net_limit", "head_block_producer"
]

ACCOUNT_DICT_KEYS = [
    "account_name", "voter_info", "last_code_update", "total_resources",
    "permissions", "net_limit", "net_weight", "privileged", "ram_usage",
    "ram_quota", "cpu_weight", "delegated_bandwidth", "created", "cpu_limit"
]

BLOCK_KEYS = [
    "confirmed", "producer_signature", "header_extensions", "previous",
    "block_num", "transaction_mroot", "transactions", "timestamp", "id",
    "action_mroot", "block_extensions", "ref_block_prefix", "schedule_version",
    "new_producers", "producer"
]

ABI_JSON_TO_ABI_KEYS = [
    "binargs"
]

PUSH_ACTION_DATA = {
    "account_name": "mynewaccount",
    "action": "create",
    "wallet_public_keys": [
        "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
        "EOS6P6UqBWame18vke6YvWYcBxK6ikL1KUvq6RyKtB83t2mgZbgux",
        "EOS77mdrRoS32zhRdkRddgY7WoED9r13MFCoNomEps8bFZxVs5hXj"
    ],
    "data": {
        "author": "mynewaccount",
        "id": 6,
        "description": "fifth task"
    }
}
