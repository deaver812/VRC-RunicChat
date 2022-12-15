#create the strings used for maketrans
alphabet = "abcdefghijklmnopqrstuvwxyz.!?"
runes="ᚨᛒᛍᛞᛖᚬᚵᚺᛁᛃᚴᛚᛗᚾᛟᛕᛩᚱᛋᛏᛝᛡᚧᛪᛨᛄ᛫᛭᛭"
#get what the user intends to translate
userInput= input("What is it to translate?: ")
#make the translation table
runeTable = userInput.maketrans(alphabet, runes)
#translate, send to user, and wait for exit
print(userInput.translate(runeTable))
input("press any key to exit: ")
