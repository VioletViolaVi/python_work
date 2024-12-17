# Format Specifiers - vid followed

# Notes:
    # format specifiers -> {values:flags}
    # {value:.2f} / {value:.0f} / {value:.5f} etc. -> for decimal places (adds 0's if not enough nums @ end)
    # {value:7} / {value:6} / {value:2} etc. -> adds spaces in front to total 7, 6 and 2 spaces in output
    # {value:07} / {value:06} / {value:02} etc. -> adds 0's instead of spaces in output
    # {value:<8} / {value:<4} / {value:<3} etc. -> aligns output to left (space added on end as needed)
    # #

chocolate_price = 5632.89534
ice_cream_price = 2156.253626
juice_price = -6532.0763

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