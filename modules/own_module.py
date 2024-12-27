# Own Module - custom made

# - this module is used in the module.py file

# adds 2 numbers together
def add_num(num_1, num_2):
    return num_1 + num_2

# squares number passed through
def square_num(num):
    return num ** 2

# finds length of string
def count_str_char(str):
    return len(str)

# converts data into list
def convert_to_list(item):
    container = []
    for i in item:
        container.append(i)
    return container    
    # return list(item) # faster way
