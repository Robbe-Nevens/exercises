# Write your code here
def contains_duplicates(xs):
    setxs = set(xs)
    if len(xs) != len(setxs):
        return True
    else:
        return False