from brownie import accounts, config, SimpleToken

initial_Supply = 1000000000000000000000000000
token_name = "SimpleToken"
token_symbol = "STN"


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = SimpleToken.deploy(
        initial_Supply, {"from": account}, publish_source=True)
