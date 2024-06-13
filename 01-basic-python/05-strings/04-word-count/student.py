# Write your code here
def word_count(string):
    if len(string) > 0:
        lijst = string.split(" ")
        return len(lijst)
    return 0