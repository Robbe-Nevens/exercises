# Write your code here
def add_indices(xs):
    if len(xs) > 0:
        indices = []
        for i in range(0,len(xs)+1):
            indices.append(i)
        indices = list(zip(indices, xs))
        return indices
    return []