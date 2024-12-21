# Dictionaries

# Notes:
    # - 

# key:value
country_capitals = {
    "United Kingdom": "London",
    "Japan": "Tokyo",
    "Ghana": "Accra",
    "China": "Beijing",
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



# updating dictionaries
    # - can add key:value
    # - can edit key:value
country_capitals.update(
    {
        "South Africa" : "Cape Town", # added on
        "United Kingdom": "Manchester", # edited
        "Angola": "Luanda", # added on
    }
)
print(country_capitals)



print(" --- next --- ")



# removing key:value
country_capitals.pop("United Kingdom")
country_capitals.pop("Ghana")
print(country_capitals)



print(" --- next --- ")



# removing LAST key:value
country_capitals.popitem()
print(country_capitals)
print(country_capitals.popitem()) # returns removed key:value as tuple '(..., ...)'



print(" --- next --- ")



# removing ALL key:value
country_capitals.clear() 
print(country_capitals)



print(" --- next --- ")



# retrieves ONLY keys from dictionary
print(country_capitals.keys()) # returns list, dict_keys[..., ..., ...,]

# iterates through dict_keys[..., ..., ...,]
for key in country_capitals.keys():
    print(key)



print(" --- next --- ")



# retrieves ONLY values from dictionary
print(country_capitals.values()) # returns list, dict_keys[..., ..., ...,]

# # iterates through dict_keys[..., ..., ...,]
for value in country_capitals.values():
    print(value)



print(" --- next --- ")



# makes key:value tuples in dict_keys[ (..., ...), (..., ...), (..., ...) ] list
print(country_capitals.items())
print(" --- --- ")

for item in country_capitals.items():
    print(item) # brings out tuple items
print(" --- --- ")

for key, value in country_capitals.items():
    print(f"key: {key} value: {value}") # brings out 2 separate strings for both variables -> key, value
print(" --- --- ")

# extra practice iterating out more than 1 value via for loops
tests = (["happy", "sad"], ["angry", "upset"], ["scared", "excited"], ["calm", "bored"])
for test1, test2 in tests:
    print(f"test1: {test1}, test2: {test2}")
print(" --- --- ")


# # get assistance
# print(dir(country_capitals))
# print(help(country_capitals))
