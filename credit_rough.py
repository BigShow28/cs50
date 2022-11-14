# Needs to be refactored

n = input("Enter num: ")

c = 1
n2 = []
t_sum = 0
c_sum = 0

if len(n) % 2 == 0:
  for i in range(len(n)):
    if i % 2 == 0:
      c = 2 * int(n[i])
      n2.append(c)

  e_sum = 0

  for i in n2:
    if i < 10:
      e_sum = e_sum + i
    else:
      e_sum = e_sum + 1 + (i%10)

  o_sum = 0

  for i in range(len(n)):
    if i % 2 != 0:
      o_sum = o_sum + int(n[i])

  t_sum = e_sum + o_sum

  c_sum = t_sum % 10

else:
  for i in range(len(n)):
    if i % 2 != 0:
      c = 2 * int(n[i])
      n2.append(c)

  o_sum = 0

  for i in n2:
    if i < 10:
      o_sum = o_sum + i
    else:
      o_sum = o_sum + 1 + (i%10)

  e_sum = 0

  for i in range(len(n)):
    if i % 2 == 0:
      e_sum = e_sum + int(n[i])

  t_sum = o_sum + e_sum

  c_sum = t_sum % 10

if c_sum == 0:
  fd_num = int(n[0])
  sd_num = int(n[1])
  if fd_num == 3 and (sd_num == 4 or sd_num == 7):
    print("AMEX")
  elif fd_num == 5 and 1 <= sd_num <= 5:
    print("MASTERCARD")
  elif fd_num ==4:
    print("VISA")
  else:
    print("INVALID")
else:
  print("INVALID")
