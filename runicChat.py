from pythonosc.udp_client import SimpleUDPClient
import time

#create the strings used for maketrans
alphabet = "abcdefghijklmnopqrstuvwxyz.!?"
runes="ᚨᛒᛍᛞᛖᚬᚵᚺᛁᛃᚴᛚᛗᚾᛟᛕᛩᚱᛋᛏᛝᛡᚧᛪᛨᛄ᛫᛭᛭"
number="0123456789"
#settings for the OSC Client

client = SimpleUDPClient("127.0.0.1", 6000) #create the OSC client

#This was orginally going to be apart of a OSC Library which is why client is an input
#but decided until I actually have enough stuff to justify a entire VRC-OSC libray that this will just sit here
def sendChatbox(client, text, bypass):
    client.send_message("/chatbox/input", [text, bypass])

while(True): #the running loop
    print("----------------------------------")
    print("type (ext) to exit the program")
    userInput= input("please enter what you wish to say: ")

    #this if, else statement purely exists for the purpose of adding an in-program way to exit the loop
    if userInput=="ext":
        print("Exiting program")
        break
    else:
        #taking user input converting it to runes and sending it to VRChat
        #first in runic form then in english
        runeTable = userInput.maketrans(alphabet, runes, number)
        runicInput = userInput.translate(runeTable)
        print("your runic message is "+runicInput)
        print("Sending runes")
        sendChatbox(client, runicInput, True)
        print("waiting a second then sending english")
        time.sleep(1)
        sendChatbox(client, userInput, True)
        print("message has been sent program looping")
