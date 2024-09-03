def is_valid(map, region, color, color_assignment):
    # A color is valid if it is different from the colors of its neighbors
    for neighbor in map[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def get_mrv_region(regions, map, colors, color_assignment):
    # Returns the unassigned region with the fewest valid colors available
    unassigned = [region for region in regions if region not in color_assignment]
    return min(unassigned, key=lambda region: len([color for color in colors if is_valid(map, region, color, color_assignment)]))

def least_constraining_value(region, map, colors, color_assignment):
    # Order colors using the Least Constraining Value heuristic
    return sorted(colors, key=lambda color: sum(
        1 for neighbor in map[region] if is_valid(map, neighbor, color, color_assignment)))

def solve_map_coloring(map, regions, colors, color_assignment=None, verbose=False):
    # Solves the map coloring problem using backtracking with heuristics
    if color_assignment is None:
        color_assignment = {}

    if len(color_assignment) == len(regions):
        return color_assignment  # All regions are assigned a color, problem solved

    # Select the next region using the Most Restricted Variable heuristic
    current_region = get_mrv_region(regions, map, colors, color_assignment)

    for color in least_constraining_value(current_region, map, colors, color_assignment):
        # Print the attempt if verbose is enabled
        if verbose:
            print(f"Trying to assign {color} to {current_region}")

        if is_valid(map, current_region, color, color_assignment):
            color_assignment[current_region] = color

            # Print the successful assignment if verbose is enabled
            if verbose:
                print(f"Assigned {color} to {current_region}")

            result = solve_map_coloring(map, regions, colors, color_assignment, verbose)
            if result:
                return result
            
            # Backtrack
            del color_assignment[current_region]

            # Print the backtrack step if verbose is enabled
            if verbose:
                print(f"Backtracking from {current_region}")

    return None
