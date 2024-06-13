# Write your code here
def keys_with_value(dictionary,value):
    havevalue = []
    for key in dictionary:
        if dictionary.get(key) == value:
            havevalue.append(key)
    return havevalue