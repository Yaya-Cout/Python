"""Tanslate SMS language to French."""
import enchant
import sys
smsdic = {"cc": "Coucou, ", "cv": "Ça va ?", "tfq": "Tu fait quoi ?",
          "pq": "Pourquoi ?", "c": "C'est", "t": "Tu est", "xd": "😂",
          "yep": "Oui", "k": "Ok", "nan": "Non", "yes": "Oui"}
args = sys.argv[1:]
if args != []:
    argstr = ""
    for item in args:
        argstr += item + " "
    msg = argstr
    print(msg)
else:
    # msg = "cc cv tfq pq c t XD yep K Saluut"
    msg = input("Message : ")
msgparsed = msg.split(" ")
autocorrect = enchant.Dict("fr")
for item in range(len(msgparsed)):
    word = msgparsed[item]
    if word.lower() in smsdic:
        msgparsed[item] = " " + smsdic[word.lower()] + " "
    elif msgparsed[item] != "":
        if not autocorrect.check(word):
            msgparsed[item] = autocorrect.suggest(word)[0]
msgtrans = ""
for word in msgparsed:
    msgtrans += word
print(msgtrans)
