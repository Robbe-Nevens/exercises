def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs,ys):
    return {element for element in xs if element in ys}