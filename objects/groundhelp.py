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
    """gets closest y value of points to point"""
    distance_sets = zip([abs(point[0] - the_point[0]) for point in points],
                        [x for x in range(len(points))])
    closest = heapq.nsmallest(sample_width, distance_sets, key=lambda x: x[0])
    closest = [points[x[1]][1] for x in closest]
    average = reduce(lambda x, y: x+y, closest) / sample_width
    return average
