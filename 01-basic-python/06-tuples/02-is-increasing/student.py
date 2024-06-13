# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    ns = list(zip(ns,ms))
    for (x,y) in ns:
        print((x,y))
        if x > y:
            return False
    return True

