# Random Numbers

# Notes:
    # - random.randint() used to get random whole numbers

import random

# # get help info on random module
# print(help(random))


print()
print("========= new ========= ")
print()


# gets random whole numbers (between 1 and 12 inclusively)
card_matching_game_num = random.randint(1, 12) # both start & end numbers are inclusive
print(f"card_matching_game_num: {card_matching_game_num}")

# gets random whole numbers for dice
dice = random.randint(1, 6)
print(f"dice number: {dice}")

# gets random whole numbers between 0 and 100 inclusively
count_to_hundred = random.randint(0, 100)
print(f"count_to_hundred: {count_to_hundred}")

# testing: can get random whole NEGATIVE numbers also
minus_nums = random.randint(-5, -1)
print(f"minus_nums: {minus_nums}")


print()
print("========= new ========= ")
print()


# random.randint() using variables
start_num = 1
end_num = 10
rand_num_1_to_10 = random.randint(start_num, end_num)
print(f"rand_num_1_to_10: {rand_num_1_to_10}")

# coin flipping
heads = 1
tails = 2
coin_side = random.randint(heads, tails)
print(f"coin_side: {coin_side}")
if coin_side == 1:
    print("heads!")
else:
    print("tails!")
