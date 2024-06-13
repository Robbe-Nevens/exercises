# Write your code here
def create_dictionary(keys,values):
    dictionaire = dict()
    for i in range(0,len(keys)):
        dictionaire[keys[i]] = values[i]
    return dictionaire