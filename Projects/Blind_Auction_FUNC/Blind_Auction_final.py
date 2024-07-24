#Blind Auction

# from Users.keithstateson.Documents.My Documents.E Data Science.100DaysCoding.predefined_functions.clear_screen" import clear
# from "/Users/keithstateson/Documents/My Documents/E Data Science/100DaysCoding/predefined_functions.clear_screen" import clear
from clear_screen import clear
from art import logo
print(logo)

bids = {}
bidding = True

# find highest bidder using max() fuction
def find_highest_bidder(bids_list):       # could use "bids" for "bids_list", as it doesn't seem to cause any errors
    winner_name = max(bids_list, key=bids_list.get)
    highest_bid = max(bids_list.values())
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")

# def find_highest_bidder(bids_list):
#     highest_bid = 0
#     winner_name = ""
#     for bidder in bids_list:        # looping a dictionary iterates through the keys i.e. "bidder1" in {"bidder1" = $150}
#         bid_amount = bids_list[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner_name = bidder        # winner_name = bidder b/c loop iterates through the keys and not key-value pairs
#     print(f"The winner is {winner_name} with a bid of ${highest_bid}")

while bidding == True:
    name = input("Name of bidder: ")
    price = int(input(f"{name}'s bid: $"))
    bids[name]=price
    
    continue_bidding = input("Are there any other bidders? Y/N \n").lower()
    if continue_bidding == "n":
        bidding = False
        clear()
        find_highest_bidder(bids)
    else:
        clear()
