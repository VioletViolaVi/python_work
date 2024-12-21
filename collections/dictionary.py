# Dictionaries

# key:value
country_capitals = {
    "United Kingdom": "London",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Ghana": "Accra",
}

# retrieves value from key in dictionary
print(country_capitals.get("China"))
print(country_capitals.get("USA")) # 'None' returned if no key



print(" --- next --- ")



# conditional statements regarding presence of keys
location = country_capitals.get("USA")
if location == None:
    print("This country is not a key")
else:
    print(f"Hello {location}! 👋")

# # get assistance
# print(dir(country_capitals))
# print(help(country_capitals))
