# Крестики нолики
X = Y = X1 = Y1 = ' '
line_zero = ['-', '-', '-']
line_one = ['-', '-', '-']
line_two = ['-', '-', '-']

def hod_X (X, Y):

  X = int(input('Введи координату КРЕСТИКА по X и не жульничай!'))
  Y = int(input('Введи координату КРЕСТИКА по Y и не жульничай! '))
  if Y == 0:
    if X == 0:
      line_zero[0] = 'X'
    elif X == 1:
      line_zero[1] = 'X'
    elif X == 2:
      line_zero[2] = 'X'
  elif Y == 1:
      if X == 0:
        line_one[0] = 'X'
      elif X == 1:
        line_one[1] = 'X'
      elif X == 2:
        line_one[2] = 'X'
  elif Y == 2:
      if X == 0:
        line_two[0] = 'X'
      elif X == 1:
        line_two[1] = 'X'
      elif X == 2:
        line_two[2] = 'X'
  else: print ('Твоя координата вне поля!')


  print('Ваше игровое поле: ')
  print(' ', 0, 1, 2)
  print(0, line_zero[0], line_zero[1], line_zero[2])
  print(1, line_one[0], line_one[1], line_one[2])
  print(2, line_two[0], line_two[1], line_two[2])




def hod_0 (X1, Y1):

  X1 = int(input('Введи координату НОЛИКА по X и не жульничай!'))
  Y1 = int(input('Введи координату НОЛИКА по Y и не жульничай! '))
  if Y1 == 0:
    if X1 == 0:
      line_zero[0] = '0'
    elif X1 == 1:
      line_zero[1] = '0'
    elif X1 == 2:
      line_zero[2] = '0'
  elif Y1 == 1:
      if X1 == 0:
        line_one[0] = '0'
      elif X1 == 1:
        line_one[1] = '0'
      elif X1 == 2:
        line_one[2] = '0'
  elif Y1 == 2:
      if X1 == 0:
        line_two[0] = '0'
      elif X1 == 1:
        line_two[1] = '0'
      elif X1 == 2:
        line_two[2] = '0'
  else: print ('Ваша координата вне поля!')


  print('Ваше игровое поле: ')
  print(' ', 0, 1, 2)
  print(0, line_zero[0], line_zero[1], line_zero[2])
  print(1, line_one[0], line_one[1], line_one[2])
  print(2, line_two[0], line_two[1], line_two[2])

hod_X (X,Y)
hod_0 (X1,Y1)
hod_X (X,Y)
hod_0 (X1,Y1)
hod_X (X,Y)
hod_0 (X1,Y1)
hod_X (X,Y)
hod_0 (X1,Y1)
hod_X (X,Y)

print('Конец игры! Сердечно поздравляю победителя! ;)')


