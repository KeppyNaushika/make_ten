# python3

import itertools

def calc(old, new, oper, how_to_calc_ten):
  if oper == "a":
    int_return = old + new
    how_to_calc_ten = how_to_calc_ten + " + " + str(new)
  if oper == "b":
    int_return = old * new
    how_to_calc_ten = "( " + how_to_calc_ten + " ) * " + str(new)
  if oper == "c":
    int_return = old - new
    how_to_calc_ten = how_to_calc_ten + " - " + str(new)
  if oper == "d":
    int_return = new - old
    how_to_calc_ten = str(new) + " - ( "  + how_to_calc_ten + " )"
  if oper == "e":
    int_return = old / new
    how_to_calc_ten = "( " + how_to_calc_ten + " ) / " + str(new)
  if oper == "f":
    int_return = new / old
    how_to_calc_ten = str(new) + " / ( "  + how_to_calc_ten + " )"
  return [int_return, how_to_calc_ten]

while True:
  list_int_input = []
  for i in range(4):
    while True:
      int_input = input(f"{i + 1}番目の数字を入力してください >>> ")      
      if int_input in [str(j) for j in range(10)]:
        list_int_input.append(int(int_input))
        break
      else:
        print("値が不正です")
  permutations_list_int_input = list(itertools.permutations(list_int_input))
  product_set_oper = list(itertools.product("abcdef", repeat=3))

  bool_ten = False
  for list_ints in permutations_list_int_input:
    for set_oper in product_set_oper:
      int_old = list_ints[0]
      how_to_calc_ten = str(int_old)
      bool_continue = False
      for i, oper in enumerate(set_oper):
        int_new = list_ints[i + 1]
        try:
          return_calc = calc(int_old, int_new, oper, how_to_calc_ten)
        except ZeroDivisionError:
          bool_continue = True
          continue
        int_old         = return_calc[0]
        how_to_calc_ten = return_calc[1]
      if int_old == 10 and bool_continue is False:
        print(">> " + how_to_calc_ten + " = " + str(int_old) )
        bool_ten = True

    for set_oper in product_set_oper:
      bool_continue = False
      try:
        calc0 = calc(list_ints[0], list_ints[1], set_oper[0], str(list_ints[0]))
      except ZeroDivisionError:
        bool_continue = True
        continue
      try:
        calc1 = calc(list_ints[2], list_ints[3], set_oper[2], str(list_ints[2]))
      except ZeroDivisionError:
        bool_continue = True
        continue
      try:
        calc2 = calc(calc0[0], calc1[0], set_oper[1], "")
      except ZeroDivisionError:
        bool_continue = True
        continue
      if calc2[0] == 10 and bool_continue is False:
        if set_oper[1] == "a":
          how_to_calc_ten = calc0[1] + " + " + calc1[1]
        if set_oper[1] == "b":
          how_to_calc_ten = "( " + calc0[1] + " ) * ( " + calc1[1] + " )"
        if set_oper[1] == "c":
          how_to_calc_ten = "( " + calc0[1] + " ) - ( " + calc1[1] + " )"
        if set_oper[1] == "d":
          how_to_calc_ten = "( " + calc1[1] + " ) - ( " + calc0[1] + " )"
        if set_oper[1] == "e":
          how_to_calc_ten = "( " + calc0[1] + " ) / ( " + calc1[1] + " )"
        if set_oper[1] == "f":
          how_to_calc_ten = "( " + calc1[1] + " ) / ( " + calc0[1] + " )"
        print("<< " + how_to_calc_ten + " = " + str(calc2[0]) )
        bool_ten = True



  if bool_ten is not True:
    print("10をつくることはできませんでした")
