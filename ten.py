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
      if int_old == 10 and bool_continue == False:
        print(how_to_calc_ten + " = " + str(int_old) )
        bool_ten = True
        answer = how_to_calc_ten + " = 10"

  if bool_ten is not True:
    print("10をつくることはできませんでした")

