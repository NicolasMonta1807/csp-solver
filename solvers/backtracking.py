'''
Solution based on jaiswalchitransh project
https://github.com/jaiswalchitransh/CSP-Map-coloring-using-Backtracking/tree/main
'''

import random

def is_valid(map, region, color, color_assignment):
    # A color is valid if it is different from the colors of its neighbors
    for neighbor in map[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def solve_map_coloring(map, regions, colors, color_assignment={}, verbose=False):
    # If all regions are assigned a color, problem is solved
    if len(color_assignment) == len(regions):
        return color_assignment

    # Select the next region that is not yet assigned a color randomly
    unassigned_regions = [region for region in regions if region not in color_assignment ]
    current_region = random.choice(unassigned_regions)

    for color in colors:
        # Print the attempt if verbose is enabled
        if verbose:
            print(f"Trying to assign {color} to {current_region}")

        # Check if the color is valid for the current region
        if is_valid(map, current_region, color, color_assignment):
            color_assignment[current_region] = color

            # Print the successful assignment if verbose is enabled
            if verbose:
                print(f"Assigned {color} to {current_region}")

            result = solve_map_coloring(map, regions, colors, color_assignment, verbose)

            # If a valid coloring is found, return it
            if result is not None:
                return result
            # Otherwise, backtrack
            else:
                # Print the backtrack step if verbose is enabled
                if verbose:
                    print(f"Backtracking from {current_region}")

                del color_assignment[current_region]

    return None
