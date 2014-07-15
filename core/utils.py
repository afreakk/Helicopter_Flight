""" utilities"""


def get_deltatime(clock):
    """gets delta time"""
    mill_sec = clock.tick()
    return mill_sec / 1000.0


def almost_equal(value_a, value_b, epsilon):
    """returns true if valA and valB is within epsilon range of eachother"""
    if value_a > value_b - epsilon:
        if value_a < value_b + epsilon:
            return True
    return False


def vector_add(vec_a, vec_b):
    """ adds two (2D)vectors(tuples) and returns answer"""
    return (vec_a[0]+vec_b[0], vec_a[1]+vec_b[1])


def vector_div(vec, div):
    """divides a 2d vector by div"""
    return (vec[0]/div, vec[1]/div)


def translate((x_velocity, y_velocity), points):
    """Translates vertex list of tuples by x and y velocity"""
    for elm in xrange(len(points)):
        points[elm] = vector_add(points[elm], (x_velocity, y_velocity))


def not_in_scene(points, screen_width, screen_height):
    """checks if list of vectors is outside scene"""
    flat_list = []
    peel_list(points, flat_list)
    for point in flat_list:
        if point[0] > screen_width:
            return (+1, +0)
        elif point[0] < +0:
            return (-1, +0)

        elif point[1] > screen_height:
            return (+0, +1)
        elif point[1] < 0:
            return (+0, -1)
    return (0, 0)


def any_x_below(points, value):
    """checks if any x-points of a tuple vector is below value"""
    flat_list = []
    peel_list(points, flat_list)
    for point in flat_list:
        if point[0] < value:
            return True
    return False


def peel_list(unorganized, merged_points):
    """peels a list and makes a flat tuple array"""
    if isinstance(unorganized, tuple):
        merged_points.append(unorganized)
    else:
        for points in unorganized:
            peel_list(points, merged_points)
