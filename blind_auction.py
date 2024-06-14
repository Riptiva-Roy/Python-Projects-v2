from replit import clear  
from art import logo

print(logo)

bid_dict = {}  

name1 = input("What is your name? ")
bid1 = input("What is your bid? ")
bid_dict[name1] = int(bid1)

def ask_for_more_bidders():
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    return answer == 'yes'

while ask_for_more_bidders():
    clear()
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    bid_dict[name] = int(bid)

highest_bidder = max(bid_dict, key=bid_dict.get)
highest_bid = bid_dict[highest_bidder]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
