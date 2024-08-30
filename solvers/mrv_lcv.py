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

def solve_map_coloring(map, regions, colors, color_assignment=None):
    # Solves the map coloring problem using backtracking with heuristics
    if color_assignment is None:
        color_assignment = {}

    if len(color_assignment) == len(regions):
        return color_assignment    # Selecciona la región usando la heurística MRV


    # Selects next region using Most Restricted Variable heuristic
    current_region = get_mrv_region(regions, map, colors, color_assignment)

    for color in least_constraining_value(current_region, map, colors, color_assignment):
        if is_valid(map, current_region, color, color_assignment):
            color_assignment[current_region] = color
            result = solve_map_coloring(map, regions, colors, color_assignment)
            if result:
                return result
            del color_assignment[current_region]  # Backtrack

    return None
  