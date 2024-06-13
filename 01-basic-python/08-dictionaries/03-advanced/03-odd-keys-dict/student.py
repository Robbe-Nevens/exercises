# Write your code here
def odd_keys_dict(dictionary):
    odd = dict()
    for key in dictionary:
        if key%2!=0:
            odd[key] = dictionary.get(key)
    return odd



