from solvers import backtracking, mrv_lcv
from termcolor import colored
import sys

def read_problem(file):
  try:
    with open(file, 'r') as f:
      lines = f.readlines()
      map = {}
      colors = []
      
      read_colors = False
      read_map = False
      
      for line in lines:
        line = line.strip()
        
        if line == "colors":
          read_colors = True
          continue
        
        if line == "map":
          read_map = True
          read_colors = False
          continue
        
        if read_colors:
          colors = line.split(",")
          
        if read_map and line:
          region, neighbors = line.split(':')
          neighbors = neighbors.split(',')
          map[region] = neighbors
          
      return map, colors
  except Exception as e:
    print(f"Error reading file: {e}")
    return None
  
def print_solution(solution):
    # Prints using termcolor for better visualization
    for region, color in solution.items():
        print(f"{region}: {colored(color, color)}")

def main():
  
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        return
  
    filename = sys.argv[1]
  
    map, colors = read_problem(filename)
    regions = list(map.keys())

    backtracking_solution = backtracking.solve_map_coloring(map, regions, colors)

    print("-------------------------------------------")
    print("Solving with backtracking")
    if backtracking_solution:
        print("Valid coloring:")
        print_solution(backtracking_solution)
    else:
        print("No valid coloring found for backtracking.")
    print("-------------------------------------------")
            
    print("-------------------------------------------")
    print("Solving with Most Restricted Variable + Least Constraining Value")
    mrv_solution = mrv_lcv.solve_map_coloring(map, regions, colors)
    if mrv_solution:
        print("Valid coloring:")
        print_solution(mrv_solution)
    else:
        print("No valid coloring found for MRV+LCV.")
    print("-------------------------------------------")
          
if __name__ == "__main__":
  main()