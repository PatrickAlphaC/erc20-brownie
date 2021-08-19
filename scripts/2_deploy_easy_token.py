from brownie import accounts, config, EasyToken
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20 = EasyToken.deploy({"from": account})
