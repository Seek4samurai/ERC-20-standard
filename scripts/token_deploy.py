from brownie import accounts, config, TokenERC20

# 100
initial_supply = 1000000000000000000000
token_name = "TOKEN"
token_symbol = "TKN"

def main():
    # account = accounts[0]
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(initial_supply, token_name, token_symbol, {"from": account})
