from scripts.helpfull_scripts import get_account
from brownie import TokenV1, Contract
from web3 import Web3


def main():
    account = get_account()
    erc20_address = input("Insert ERC20 address: ")
    recipient = input("Insert recipient address: ")
    amount = input("Insert amount: ")
    amount_towei = Web3.toWei(amount, 'ether')
    erc20 = Contract.from_abi(
        "Arbitrary ERC20", erc20_address, abi=TokenV1.abi)
    tx = erc20.transfer(recipient, amount, {"from": account})
    tx.wait(1)
