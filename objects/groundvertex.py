"""generated 2D terrain"""
import noise


def get_terrain(top_spacing, (screen_width, screen_height),
                itter_width, distnz):
    """gets random terrainNN"""
    pos_str = 0.001
    dist_str = 0.01
    amplitude = 100.0
    distnz *= dist_str
    terrain = []
    x_pos = 0
    while x_pos < screen_width:
        terrain.append((x_pos, top_spacing+noise.pnoise2(x_pos*pos_str, distnz)
                        * amplitude))
        x_pos += itter_width
    terrain.append((x_pos, top_spacing+noise.pnoise2(x_pos*pos_str, distnz)
                    * amplitude))
    # round of square
    terrain.append((x_pos, screen_height))
    terrain.append((0, screen_height))
    return [terrain]
