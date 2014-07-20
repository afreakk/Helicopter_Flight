"""generating a random tree and returns vertexesz"""
from core.utils import translate
from core.geometry import get_tree_square, get_square


def get_tree_vx(max_width, min_width, itter_width, itter_height,
                points=[], start_iter_height=None, tree_pointyness=1.9):
    """recursive tree builder"""
    if start_iter_height is None:
        start_iter_height = itter_height
        # reset list, at begining of every non-recursive function function call
        points = []
    if max_width > min_width:
        itter_height += start_iter_height*2
        ratio = itter_height / float(itter_width)
        ratio /= ratio/tree_pointyness
        height_chunk = get_tree_square(max_width, start_iter_height, ratio)
        translate((0, -itter_height), height_chunk)
        points.append(height_chunk)
        next_width = max_width - itter_width
        return get_tree_vx(next_width, min_width, itter_width,
                           itter_height, points, start_iter_height)
    else:
        bottom = get_square(max_width+itter_width, start_iter_height)
        translate((0, -start_iter_height), bottom)
        points.append(bottom)
        return points
