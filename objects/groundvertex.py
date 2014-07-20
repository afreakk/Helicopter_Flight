"""generated 2D terrain"""
import noise


def get_terrain(top_margin, width_margin, (screen_width, screen_height),
                itter_width, distance):
    """gets random terrainNN"""
    pos_wght = 0.01/2.0
    dist_wght = 0.01/2.0
    height_amp = 70.0
    width_margin = int(width_margin)
    gen_terrain = lambda x: (x, top_margin +
                             noise.pnoise1(x*pos_wght+distance*dist_wght)
                             * height_amp)
    terrain = [gen_terrain(x) for x in xrange
               (-width_margin, screen_width+width_margin, itter_width)]
    # round of bottom
    terrain.append((screen_width+width_margin, screen_height))
    terrain.append((-width_margin, screen_height))
    return [terrain]
