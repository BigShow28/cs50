import sys

def main():
  while True:
    card_num = input("Enter card number: ")
    try:
      if int(card_num) > 0:
        check_card(card_num)
        break
    except ValueError:
      continue

def check_card(card_num):
  if len(card_num) < 13 or len(card_num) > 16:
    print("Invalid.")
    sys.exit(0)

  else:

main()
