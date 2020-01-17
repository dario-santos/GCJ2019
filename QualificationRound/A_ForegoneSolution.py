# Date: 17/01/2020 - dd/mm/yyyy
# This resolution passes the 3 test sets
# Score : 6pts + 10pts + 1pts

def separate(number):
    A, B = '',''
    
    for c in number: 
        if c is '4':
            A, B = '2' + A, '2' + B
        else:
            A, B = c + A, '0' + B
    
    return A, B.lstrip('0')

# Main

tests = int(input())

for i in range(1, tests + 1):
  n = input()
  A, B = separate(n[::-1])

  print("Case #{}: {} {}".format(i, A, B))
