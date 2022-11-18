print("Крестики-нолики")

pole = list(range(1,10))

def draw_pole(pole):
   for a in range(3):
      print(pole[0+a*3], pole[1+a*3], pole[2+a*3],)

def take_input(igrok):
   p = False
   while not p:
      otwet = input("Ход " + igrok+"")
      try:
         otwet = int(otwet)
      except:
         print("Некорректный ввод")
         continue
      if otwet >= 1 and otwet <= 9:
         if(str(pole[otwet-1]) not in "XO"):
            pole[otwet-1] = igrok
            p = True
         else:
            print("Эта клетка занята")
      else:
        print("Введите число от 1 до 9.")

def check_win(pole):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if pole[each[0]] == pole[each[1]] == pole[each[2]]:
          return pole[each[0]]
   return False

def main(pole):
    hod = 0
    win = False
    while not win:
        draw_pole(pole)
        if hod % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        hod += 1
        if hod > 4:
           t = check_win(pole)
           if t:
              print(t, "выиграл!")
              win = True
              break
        if hod == 9:
            print("Ничья!")
            break
    draw_pole(pole)
main(pole)
