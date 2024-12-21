# Dictionaries

# key:value
country_capitals = {
    "United Kingdom": "London",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Ghana": "Accra"
}

# retrieves value from key in dictionary
print(country_capitals.get("China")) # 'Beijing' returned, key is present
print(country_capitals.get("USA")) # 'None' (default) returned, there's no 'USA' key
print(country_capitals.get("Ghana", "Absent")) # 'Accra' returned, key is present
print(country_capitals.get("Singapore", "Absent")) # 'Absent' (custom) returned, there's no 'Singapore' key
print(country_capitals.get("New Zealand", "Not a key")) # 'Not a key' returned, there's no 'New Zealand' key



print(" --- next --- ")



# conditional statements regarding presence of keys
location = country_capitals.get("USA")
if location == None:
    print("This country is not a key")
else:
    print(f"Hello {location}! 👋")



print(" --- next --- ")






# # get assistance
# print(dir(country_capitals))
# print(help(country_capitals))
