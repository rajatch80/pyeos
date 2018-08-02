CHAIN_URL = "http://0.0.0.0:7777"
WALLET_URL = "http://0.0.0.0:5555"

CHAIN_API = "/v1/chain"
WALLET_API = "/v1/wallet"

CHAIN_API_ENUM = {
    # Chain endpoints
    "GET_INFO": "/get_info",
    "GET_BLOCK": "/get_block",
    "GET_TABLE_ROWS": "/get_table_rows",
    "GET_ACCOUNT": "/get_account",
    "GET_CODE": "/get_code",
    "GET_REQUIRED_KEYS": "/get_required_keys",
    "ABI_JSON_TO_BIN": "/abi_json_to_bin",

    # Push ENUMs
    "PUSH_BLOCK": "/push_block",
    "PUSH_TRANSACTION": "/push_transaction",
    "PUSH_TRANSACTIONS": "/push_transactions",

    # History
    "GET_TRANSACTION": "/get_transaction",
    "GET_ACTIONS": "/get_actions"
}

WALLET_API_ENUM = {
    "CREATE_WALLET": "/create",
    "OPEN_WALLET": "/open",
    "LOCK_WALLET": "/lock",
    "UNLOCK_WALLET": "/unlock",
    "IMPORT_KEY": "/import_key",
    "SIGN_TRANSACTION": "/sign_transaction",
    "CREATE_KEY": "/create_key"
}