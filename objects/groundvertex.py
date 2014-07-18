"""generated 2D terrain"""
import noise


def get_terrain(top_spacing, (screen_width, screen_height),
                itter_width, distnz):
    """gets random terrainNN"""
    pos_str = 0.01/2.0
    dist_str = 0.01/2.0
    amplitude = 70.0
    distnz *= dist_str
    terrain = []
    spacing = 100
    x_pos = -spacing
    while x_pos < screen_width+spacing:
        terrain.append((x_pos, top_spacing+noise.pnoise1(x_pos*pos_str+distnz)
                        * amplitude))
        x_pos += itter_width
    terrain.append((x_pos, top_spacing+noise.pnoise1(x_pos*pos_str+distnz)
                    * amplitude))
    # round of square
    terrain.append((x_pos, screen_height))
    terrain.append((0, screen_height))
    return [terrain]
