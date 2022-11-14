def main():
  while True:
    try:
      s_size = int(input("Start size: "))
      if s_size < 9:
        continue
      else:
        e_size = int(input("End size: "))
        if e_size > s_size:
          population(s_size, e_size)
          break
        else:
          continue
    except ValueError:
      continue

def population(s_size, e_size):
  years = 0

  while(s_size < e_size):
    s_size = round(s_size + (s_size / 3) - (s_size / 4))
    print(s_size)
    years = years + 1

  print("Years:", years)

main()
