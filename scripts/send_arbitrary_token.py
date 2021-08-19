from brownie import accounts, config, Contract, EasyToken
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20_address = "Insert ERC20 Address here"
    recipient = "Insert address of recipient here"
    # This will be how many tokens to send in WEI
    amount = 1000000000000000000  # 1 token
    erc20 = Contract.from_abi("Arbitrary ERC20", erc20_address, abi=EasyToken.abi)
    tx = erc20.transfer(recipient, amount, {"from": account})
    tx.wait(1)
