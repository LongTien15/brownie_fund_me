from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.helpful_script import get_acc, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT


def deploy_fund_me():
    acc = get_acc()
    # Pass pricefeed address

    # if on persistent network like rinkeby, use the associated address
    # else, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": acc},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
