# Format Specifiers - vid followed

# Notes:
    # format specifiers -> {values:flags}
    # {value:.2f} / {value:.0f} / {value:.5f} etc. for decimal places (adds '0's if not enough nums @ end)
    # 
    # 
    # #

# prices
chocolate_price = 5632.89534
ice_cream_price = 2156.253626
juice_price = -6532.0763

print(f"chocolate price: £{chocolate_price:.9f}")
print(f"ice cream price: £{ice_cream_price:.2f}")
print(f"juice price: £{juice_price:.1f}")
