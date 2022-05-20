from brownie import FundMe
from scripts.helpful_script import get_acc


def fund():
    fund_me = FundMe[-1]
    acc = get_acc()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": acc, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    acc = get_acc()
    fund_me.withdraw({"from": acc})


def main():
    fund()
    withdraw()
