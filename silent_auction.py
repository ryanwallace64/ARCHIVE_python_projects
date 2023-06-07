from replit import clear

# Print title art
from art import logo
print(logo)

more_bidders = True
bids = {}

# function to input each bidder and associated bid. Then clear screen
def new_bid():
    global more_bidders
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    more_bids = input("Are there more bidders? 'yes' or 'no': ")
    if more_bids == "no":
        more_bidders = False
    clear()

# Continue accepting new bids until user enters specifies
while more_bidders:
    new_bid()

high_bidder = ""
high_bid = 0

# Find highest bidder from dictionary
for bidder in bids:
    if bids[bidder] > high_bid:
        high_bidder = bidder
        high_bid = bids[bidder]
        
# Print winner statement
print(f"The winner is {high_bidder} who bid ${high_bid}! Congratulations!")