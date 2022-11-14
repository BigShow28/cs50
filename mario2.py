def main():
  while True:
    try:
      n = int(input("Enter num: "))
      if n > 0 and n < 9:
        height(n)
        break
    except ValueError:
      continue

def height(n):
  while n > 0:
    for i in range(n):
      print(" "*(n-1) + "#"*(i+1) + "  " + "#"*(i+1))
      n = n - 1

main()
