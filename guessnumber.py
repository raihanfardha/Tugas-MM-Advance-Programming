tries = 1
guess = 500
modif = [500, 250, 125, 63, 32, 16, 8, 4, 2, 1]

def newGame() :
  tries = 1
  guess = 500

  print("Pilih sebuah angka dari 1 sampai 1000")
  print("Apakah angkanya lebih besar dari", guess,"?")

def higher(guess, tries) :
  guess = guess + modif[tries]
  return guess

def lower(guess, tries) :
  guess = guess - modif[tries]
  return guess

tebakan = 500
newGame()
exit = False
while (exit!=True) and (tries<=10) and (tebakan>0) and (tebakan<1000) :
    ans = input("(Y/T/OK)")
    if (ans == "Y") :
        tebakan = higher(tebakan, tries)
        print("Apakah angkanya lebih besar dari", tebakan,"?")
        if (tebakan == 1000) :
            print("Angka Anda adalah 1000 atau lebih")
    elif (ans == "T") :
        tebakan = lower(tebakan, tries)
        print("Apakah angkanya lebih besar dari", tebakan,"?")
        if (tebakan == 0) :
            print("Angka Anda adalah 0 atau kurang")
    elif (ans == "OK") :
        print("Angka Anda adalah", tebakan)
        exit = True
    print("counter : ", tries)
    tries = tries + 1
