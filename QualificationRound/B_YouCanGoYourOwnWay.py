# Date: 17/01/2020 - dd/mm/yyyy
# This resolution passes the 3 test sets
# Score : 5pts + 9pts + 10pts

# Input format:
# T : Number of tests
# S : Size of path
# P : Path

def translate(path):
    my_path = ''    
    for c in path:
        my_path += 'S' if c is 'E' else 'E'
    return my_path
    
# Main
tests = int(input())

for i in range(1, tests + 1):
  board = input()
  n = input()
  
  print("Case #{}: {}".format(i, translate(n)))
