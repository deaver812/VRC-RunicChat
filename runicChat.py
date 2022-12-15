from pythonosc.udp_client import SimpleUDPClient
import time

#create the strings used for maketrans
alphabet = "abcdefghijklmnopqrstuvwxyz.!?"
runes="ᚨᛒᛍᛞᛖᚬᚵᚺᛁᛃᚴᛚᛗᚾᛟᛕᛩᚱᛋᛏᛝᛡᚧᛪᛨᛄ᛫᛭᛭"
number="0123456789"
#settings for the OSC Client
ip="127.0.0.1"
port=6000

client = SimpleUDPClient(ip, port) #create the OSC client
run=True

def sendChatbox(client, text, bypass):
    client.send_message("/chatbox/input", [text, bypass])

while(run==True):
    print("----------------------------------")
    print("type (ext) to exit the program")
    userInput= input("please enter what you wish to say: ")
    if userInput=="ext":
        print("Exiting program")
        run=False
    else:
        #the running loop taking user input and sending it to VRChat
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
