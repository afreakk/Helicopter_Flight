"""Helper functions for keeping objects on ground"""
import heapq


def ground_catch_obj(obj, ground_points, sample_width,
                     seizure_limit=5, height_skew=0):
    """places an object to closest ground y value.."""
    old_y = obj.position[1]
    new_y = avg_closest_y(ground_points, obj.position, sample_width)
    move_y = (new_y - old_y)
    if abs(move_y) > seizure_limit:
        obj.loc_translate((0, move_y+height_skew))


def avg_closest_y(points, the_point, sample_width):
    """gets average y value of nearest x points to the_point's x value\
       points = [(x,y), (x,y), (x,y)....] point = (x,y)"""
    first, second = lambda x: x[0], lambda y: y[1]
    distances = zip([abs(first(point)-first(the_point)) for point in points],
                    [x for x in range(len(points))])
    nearest_sets = heapq.nsmallest(sample_width, distances, key=first)
    nearest_y_values = [second(points[x[1]]) for x in nearest_sets]
    average_y = reduce(lambda x, y: x+y, nearest_y_values) / sample_width
    return average_y
