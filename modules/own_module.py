# Own Module - custom made

# - this module is used in the module.py file

# adds 2 numbers together
def add_num(num_1, num_2):
    # using int() can help ensure a number is returned even if user entered a string
    return int(num_1) + int(num_2) 

# squares number passed through
def squaring_num(num):
    # using int() can help ensure a number is returned even if user entered a string
    return int(num) ** 2

# finds length of string
def count_str_chars(string):
    # using str() can help ensure a string is returned even if user entered a number
    return len(str(string))

# converts data into list
def convert_to_list(item):
    container = []
    for i in item:
        container.append(i)
    return container    
    # return list(item) # faster way
