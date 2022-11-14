'''
def main():
  while True:
    try:
      n = int(input("Enter num: "))
      if n > 0 and n < 9:
        height(n)
        break
    except ValueError:
      continue


def main():
  while True:
    try:
      s_size = int(input("Start size: "))
      if s_size < 9:
        continue
      else:
        e_size = int(input("End size:"))
        if e_size > s_size:
          population(s_size, e_size)
          break
    except ValueError:
      continue
'''

i = 1

while True:
    print(i)
    i = i + 1
    if(i > 5):
        break
