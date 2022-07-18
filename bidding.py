from biddinglogo import logo
print(logo)

bidder_dict = {}
# set variable to keep track of bidding for while loop

bidding_over = False

# find the highest-bidder


def highest_bidder(bidding_record):
    # bidding_record={"sam":400,"angela:500"}
    highest_bid = 0
    winner = ""
    for bid in bidding_record:
        bid_amount = bidding_record[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} with bid amount of {highest_bid} $")


# to continue bidding
while not bidding_over:
    bidder = input("Enter your name bidder. ")
    bidder_amount = int(input("Enter your bid amount $."))
    # adding key-value to dict
    bidder_dict[bidder] = bidder_amount
    new_bidder = input("Are there any new bidder ?")
    if new_bidder == "yes":
        bidding_over = False
    else:
        bidding_over = True


highest_bidder(bidder_dict)
print(bidder_dict)
