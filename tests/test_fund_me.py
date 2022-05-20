import pytest
from scripts.helpful_script import get_acc, LOCAL_BLOCKCHAIN_ENVIRONMENT
from scripts.deploy import deploy_fund_me
from brownie import accounts, network, exceptions


def test_can_fund_and_withdraw():
    acc = get_acc()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    transaction = fund_me.fund({"from": acc, "value": entrance_fee})
    transaction.wait(1)
    assert fund_me.addressToAmountFunded(acc.address) == entrance_fee
    transaction2 = fund_me.withdraw({"from": acc})
    transaction2.wait(1)
    assert fund_me.addressToAmountFunded(acc.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("Only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
