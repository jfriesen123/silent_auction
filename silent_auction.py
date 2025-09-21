logo = '''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
# Create an empty dictionary to add players to
name_and_bids = {}
add_another_bid = True

# Create a loop to add names and bids until there are no more bidders
while add_another_bid:
    # Input for player name and bid
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    # Add name and bid to dictionary
    name_and_bids[name] = bid
    
    #  Loop to keep repeating until told no 
    go_again = input("Are thee any other bidders? Type 'yes' or 'no'. ")

    if go_again == 'yes':
        print("\n" * 100)
    if go_again == 'no':
        add_another_bid = False

# for each player(key) in the dictionary, take their bid (value) and convert it to an integer and
# compare the values
# add the value to highest_bid variable if it is higher than the previous
# update the name of the winner

highest_bid = 0
winner = ''

for player in name_and_bids:
    if name_and_bids[player] > highest_bid:
        winner = player
        highest_bid = name_and_bids[player]


print(f"The winner is {winner} with a bid of ${highest_bid}")