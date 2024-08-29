'''
Solution based on jaiswalchitransh project
https://github.com/jaiswalchitransh/CSP-Map-coloring-using-Backtracking/tree/main
'''

def is_valid(map, region, color, color_assignment):
    # A color is valid if it is different from the colors of its neighbors
    for neighbor in map[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True


def solve_map_coloring(map, regions, colors, color_assignment={}):
    # If all regions are assigned a color, problem is solved
    if len(color_assignment) == len(regions):
        return color_assignment

    # Find the next region that is not yet assigned a color
    current_region = [r for r in regions if r not in color_assignment][0]

    for color in colors:
        # Check if the color is valid for the current region
        if is_valid(map, current_region, color, color_assignment):
            color_assignment[current_region] = color
            result = solve_map_coloring(map, regions, colors, color_assignment)
            # If a valid coloring is found, return it
            if result is not None:
                return result
            # Otherwise, backtrack
            del color_assignment[current_region]

    return None


