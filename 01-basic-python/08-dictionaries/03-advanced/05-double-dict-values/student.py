# Write your code here
def double_dict_values(dictiionary):
    double = dict()
    for key in dictiionary:
        double[key] = dictiionary.get(key)*2
    return double