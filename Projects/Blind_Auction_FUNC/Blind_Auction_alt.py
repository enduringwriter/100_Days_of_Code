#Blind Auction
# alternative version with for loop and if conditions to find the highest bidder, instead of using max() function
# also includes teacher's version of using False conditions and an elif condition at the end

from clear_screen import clear

bids = {}
bidding_finished = False

# find highest bidder using max() fuction
# def find_highest_bidder(bids_list):       # could use "bids" for "bids_list", as it doesn't seem to cause any errors
#     winner_name = max(bids_list, key=bids_list.get)
#     highest_bid = max(bids_list.values())
#     print(f"The winner is {winner_name} with a bid of ${highest_bid}")

def find_highest_bidder(bids_list):
    highest_bid = 0
    winner_name = ""
    for bidder in bids_list:        # looping a dictionary iterates through the keys i.e. "bidder1" in {"bidder1" = $150}
        bid_amount = bids_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner_name = bidder        # winner_name = bidder b/c loop iterates through the keys and not key-value pairs
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("Name of bidder: ")
    price = int(input(f"{name}'s bid: $"))
    bids[name]=price
    
    continue_bidding = input("Are there any other bidders? Y/N \n").lower()
    if continue_bidding == "n":
        clear()
        bidding_finished = True
        find_highest_bidder(bids)
    elif continue_bidding == 'y':
        clear()
