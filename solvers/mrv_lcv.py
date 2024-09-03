from termcolor import colored

def is_valid(map, region, color, color_assignment):
    """Verifica si el color es válido para la región dada,
    asegurando que los vecinos no tengan el mismo color."""
    for neighbor in map[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def get_mrv_region(regions, map, colors, color_assignment, verbose=False):
    """Heurística MRV: Devuelve la región no asignada con el menor número de colores válidos disponibles."""
    unassigned = [region for region in regions if region not in color_assignment]
    mrv_region = min(unassigned, key=lambda region: len([color for color in colors if is_valid(map, region, color, color_assignment)]))
    
    if verbose:
        print(colored(f"\nSe selecciona la región '{mrv_region}' utilizando MRV, con la menor cantidad de colores válidos disponibles.", "cyan"))
        
    return mrv_region

def least_constraining_value(region, map, colors, color_assignment, verbose=False):
    """Ordena los colores según la heurística de valor menos restrictivo."""
    sorted_colors = sorted(colors, key=lambda color: sum(
        1 for neighbor in map[region] if is_valid(map, neighbor, color, color_assignment)))
    
    if verbose:
        print(colored(f"Para la región '{region}', los colores se ordenan por LCV: {sorted_colors}.", "yellow"))
    return sorted_colors

def solve_map_coloring(map, regions, colors, color_assignment=None, verbose=False):
    """Soluciona el problema del coloreo de mapas utilizando backtracking con heurísticas."""
    if color_assignment is None:
        color_assignment = {}

    if len(color_assignment) == len(regions):
        return color_assignment

    # Selecciona la región usando la heurística MRV
    current_region = get_mrv_region(regions, map, colors, color_assignment, verbose)

    for color in least_constraining_value(current_region, map, colors, color_assignment, verbose):
        if is_valid(map, current_region, color, color_assignment):
            if verbose:
                print(colored(f"Se asigna el color '{color}' a la región '{current_region}'.", color.lower()))
                
            color_assignment[current_region] = color
            result = solve_map_coloring(map, regions, colors, color_assignment, verbose)
            if result:
                return result
            if verbose:
                print(colored(f"Backtracking: El color '{color}' no funcionó para la región '{current_region}', se elimina la asignación.", "red"))
            del color_assignment[current_region]  # Backtrack
        elif verbose:
            print(colored(f"El color '{color}' no es válido para la región '{current_region}' debido a conflicto con un vecino.", "magenta"))

    return None