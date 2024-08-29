from solvers import backtracking
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
  
def main():
  
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        return
  
    filename = sys.argv[1]
  
    map, colors = read_problem(filename)
    regions = list(map.keys())

    coloring = backtracking.solve_map_coloring(map, regions, colors)

    if coloring:
        print("Valid coloring:")
        for region, color in coloring.items():
            print(f"{region}: {color}")
    else:
        print("No valid coloring found.")
        
if __name__ == "__main__":
  main()