def main():
  while True:
    try:
      change = float(input("Change owed: "))
      if change > 0:
        cents = int(round(change * 100))
        get_coins(cents)
        break
    except ValueError:
      continue

def get_coins(cents):
  coins = 0
  while cents > 0:
    if cents >= 25:
      cents = cents - 25
      coins = coins + 1
      continue

    elif cents >= 10:
      cents = cents - 10
      coins = coins + 1
      continue

    elif cents >= 5:
      cents = cents - 5
      coins = coins + 1
      continue

    elif cents >= 1:
      cents = cents - 1
      coins = coins + 1
      continue

  print(coins)

main()
