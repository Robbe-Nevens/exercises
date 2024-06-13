# Write your code here
def merge_dicts(dict1, dict2):
    for key in dict2:
        dict1[key] = dict2.get(key)
    return dict1