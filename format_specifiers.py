# Format Specifiers - vid followed

# Notes:
    # format specifiers -> {values:flags}
    # {value:.2f} / {value:.0f} / {value:.5f} etc. -> for decimal places (adds 0's if not enough nums @ end)
    # {value:7} / {value:6} / {value:2} etc. -> adds spaces in front to total 7, 6 and 2 spaces in output
    # {value:07} / {value:06} / {value:02} etc. -> adds 0's instead of spaces in output
    # {value:<8} / {value:<4} / {value:<3} etc. -> aligns output to LEFT (space added ON END as needed)
    # {value:>8} / {value:>4} / {value:>3} etc. -> aligns output to RIGHT (space added AT FRONT as needed)
    # {value:^22} etc. -> centers output (space added EITHER SIDE as needed)
    # {value: } -> used for +VE numbers 
    # {value:+} -> adds '+' sign in front of +VE values only (-ve values remain -ve)
    # {value:-} -> adds '-' sign in front of -VE values only (+ve values remain +ve)
    # {value:,} -> adds ',' for 'thousands' numbers (e.g: 1,560 | 2,000 | 6,085 | etc.) 
    # {value:^30,.2f} / {value:+,.5f} / {value:-25,.3f} etc. ->  can be mixed w/ diff combinations

chocolate_price = 5632.89534
ice_cream_price = 2156.253626
juice_price = -6532.0763

# default
print(f"Default chocolate price: £{chocolate_price}")
print(f"Default ice cream price: £{ice_cream_price}")
print(f"Default juice price: £{juice_price}")

print(" --- next ---")

# decimal places
print(f"9 decimal places: £{chocolate_price:.9f}")
print(f"2 decimal places: £{ice_cream_price:.2f}")
print(f"1 decimal place: £{juice_price:.1f}")

print(" --- next ---")

# adding spaces in front
print(f"20 spaces total: £{chocolate_price:20}")
print(f"21 spaces total: £{ice_cream_price:21}")
print(f"15 spaces total: £{juice_price:15}")

print(" --- next ---")

# adding 0's in front
print(f"20 spaces total: £{chocolate_price:020}")
print(f"21 spaces total: £{ice_cream_price:021}")
print(f"15 spaces total: £{juice_price:015}")

print(" --- next ---")

# left justify
print(f"left justified: £{chocolate_price:<20}")
print(f"left justified: £{ice_cream_price:<21}")
print(f"left justified: £{juice_price:<15}")

print(" --- next ---")

# right justify
print(f"right justified: £{chocolate_price:>20}")
print(f"right justified: £{ice_cream_price:>21}")
print(f"right justified: £{juice_price:>15}")

print(" --- next ---")

# centre align
print(f"centre aligned: £{chocolate_price:^22}")
print(f"centre aligned: £{ice_cream_price:^22}")
print(f"centre aligned: £{juice_price:^22}")

print(" --- next ---")

# display '+' for +ve values
print(f"centre aligned: £{chocolate_price:+}")
print(f"centre aligned: £{ice_cream_price:+}")
print(f"centre aligned: £{juice_price:+}")

print(" --- next ---")

# display ' ' for +ve values
print(f"centre aligned: £{chocolate_price: }")
print(f"centre aligned: £{ice_cream_price: }")
print(f"centre aligned: £{juice_price: }")

print(" --- next ---")

# display '-' for -ve values
print(f"centre aligned: £{chocolate_price:-}")
print(f"centre aligned: £{ice_cream_price:-}")
print(f"centre aligned: £{juice_price:-}")

print(" --- next ---")

# thousand separator
print(f"centre aligned: £{chocolate_price:,}")
print(f"centre aligned: £{ice_cream_price:,}")
print(f"centre aligned: £{juice_price:,}")

print(" --- next ---")

# mix up
print(f"centre aligned: £{chocolate_price:^30,.2f}")
print(f"centre aligned: £{ice_cream_price:+,.5f}")
print(f"centre aligned: £{juice_price:-25,.3f}")
