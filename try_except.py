while(True):
  try:
      a = float(input('type only a number : '))
      break
  except ValueError:
      print('sorry not number')
