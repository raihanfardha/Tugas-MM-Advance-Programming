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

tebakan = 0
newGame()
exit = False
while (exit!=True) and (tries<=10) :
    ans = input("(Y/T/OK)")
    if (ans == "Y") :
        tebakan = higher(tebakan, tries)
        print("Apakah angkanya lebih besar dari", tebakan,"?")
    elif (ans == "T") :
        tebakan = lower(tebakan, tries)
        print("Apakah angkanya lebih besar dari", tebakan,"?")
    elif (ans == "OK") :
        print("Angka Anda adalah", tebakan)
        exit = True
    tries = tries + 1
