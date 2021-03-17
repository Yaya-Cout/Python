"""Tanslate SMS language to French."""
import sys

import enchant

# import tempfile
# import os

smsdic = {
    "cc": "Coucou, ",
    "cv": "Ça va ?",
    "tfq": "Tu fait quoi ?",
    "pq": "Pourquoi ?",
    "c": "C'est",
    "t": "Tu est",
    "xd": "😂",
    "yep": "Oui",
    "k": "Ok",
    "nan": "Non",
    "nop": "Non",
    "nope": "Non",
    "yes": "Oui",
    "oupsy": "Oups",
    "dacc": "D'accord",
    "ya": "Il y a",
    "qqc": "Quelque chose",
    "pb": "Problème",
    "pd": "Pendent",
    "jtd": "Je te dis",
    "jt": "J'était",
    "jv": "Je vait",
    "tv": "Tu veux",
    "azerty": "Rien",
    "js": "Je suis",
    "jp": "Je pense",
    "ts": "Tu sait",
    "tk": "Ne t'inquiète pas",
    "jsp": "Je ne sis pas",
}


def in_dic(key) -> bool:
    """Get if value is in dic."""
    for keyfor in smsdic:
        value = smsdic[keyfor]
        if key in value:
            return True
    return False


def smstranslate(rawmsg):
    """Translate SMS language."""
    for item in range(len(rawmsg)):
        raword = rawmsg[item]
        if raword.lower() in smsdic:
            rawmsg[item] = " " + smsdic[raword.lower()] + " "
    return rawmsg


def correct(tocheckmsg):
    """Correct message."""
    autocorrect = enchant.Dict("fr")
    # smstr = ""
    for item in smsdic:
        autocorrect.add_to_session(item)
        # smstr += item + "\n"
    # with tempfile.NamedTemporaryFile(delete=False, mode="r+") as tmp:
    #     print(tmp.name)
    #     tmp.write(smstr)
    #     pwl = enchant.request_pwl_dict(tmp.name)
    #     autocorrect = enchant.DictWithPWL("fr", tmp.name)

    for item in range(len(tocheckmsg)):
        tocheckword = tocheckmsg[item]
        if tocheckmsg[item] != "":
            if not autocorrect.check(tocheckword) and in_dic(tocheckword):
                print(tocheckword)
                try:
                    tocheckmsg[item] = autocorrect.suggest(tocheckword)[0]
                except IndexError:
                    continue
    return tocheckmsg


args = sys.argv[1:]
if args != []:
    ARGSTR = ""
    for item in args:
        ARGSTR += item + " "
    msg = ARGSTR
    print(msg)
else:
    # msg = "cc cv tfq pq c t XD yep K Saluut"
    msg = input("Message : ")
msgparsed = msg.split(" ")
msgparsed = smstranslate(msgparsed)
msgparsed = correct(msgparsed)
msgparsed = smstranslate(msgparsed)
MSGTRANS = ""
for word in msgparsed:
    MSGTRANS += word
print(MSGTRANS)
