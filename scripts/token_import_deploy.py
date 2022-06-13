from brownie import accounts, config, TokenImports 

# 100
initial_supply = 1000000000000000000000
token_name = "TOKEN"
token_symbol = "TKN"

def main():
    account = accounts[0]
    erc20 = TokenImports.deploy(initial_supply, {"from": account})
