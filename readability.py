text = input("Text: ")

l = []
e = [' ', '.', ',', '?', '!', '/', "'", '"', ':', ';', '-']
s = 0
p = 0

for i in text:
  if i in e:
    if i == ' ':
      s = s + 1
      continue
    elif i == '.' or i == '?' or i == '!':
      p = p + 1
      continue
    else:
      continue
  else:
    l.append(i)

letters = len(l)

words = s + 1

sentences = p

L = (letters / words) * 100
S = (sentences / words) * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
  print("Before Grade 1")
elif index > 16:
  print("Grade 16+")
else:
  print("Grade", index)
