from nada_dsl import *


def nada_main():
    # Define parties (bidders)
    bidder1 = Party(name="Bidder1")
    bidder2 = Party(name="Bidder2")
    bidder3 = Party(name="Bidder3")

    # Define secret bid inputs
    bid1 = SecretInteger(Input(name="bid1", party=bidder1))
    bid2 = SecretInteger(Input(name="bid2", party=bidder2))
    bid3 = SecretInteger(Input(name="bid3", party=bidder3))

    # Compute the highest bid
    highest_bid = max(bid1, max(bid2, bid3))

    # Output the highest bid to all participants
    return [Output(highest_bid, "highest_bid", [bidder1, bidder2, bidder3])]

