#!c:\tools\Python\Python35\python.exe -u
''' My Clipboard Dictionary
' Usage: clip add <key> : Copies text currently in the clipboard to our dictionary
'       clip del <key>
'        clip list : Lists all keywords from the dictionalry
'        clip <key> : Copies the text contained with the key to the clipboard for further use
'''

''' Using pyperclip: pyperclip.copy(a) ; b = pyperclip.paste() '''
''' Using shelve: https://docs.python.org/3/library/shelve.html
    with shelve.open('spam') as db:
        db['eggs'] = 'eggs'  
'''

import shelve,pyperclip,sys,pprint,os

WORKDIR = "c:\devworks\PycharmProjects\mkdev"
os.chdir(WORKDIR)


if len(sys.argv) == 1:
    print(''' My Clipboard Dictionary
        ' Usage: clip add <key> : Copies text currently in the clipboard to our dictionary
        '        clip list : Lists all keywords from the dictionalry
        '        clip <key> : Copies the text contained with the key to the clipboard for further use
        ''')


elif len(sys.argv) == 2 and sys.argv[1] == "list":
    with shelve.open('textblocks') as textblocks:
        keys = textblocks.keys()
        for key in keys:
            print(key)
        searchword = input()
        print(searchword)

        if searchword in textblocks.keys():
            textbody = textblocks[searchword]
            print("Copied to clipboard: " + textbody)
            pyperclip.copy(textbody)
        else:
            print("Key not found")

elif len(sys.argv) >2 and sys.argv[1] == "add":
    with shelve.open('textblocks') as textblocks:
        textblocks[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) >2 and sys.argv[1] == "del":
    with shelve.open('textblocks') as textblocks:
        del textblocks[sys.argv[2]]


elif len(sys.argv) == 2 and sys.argv[1] != "list":
    with shelve.open('textblocks') as textblocks:
        searchword = sys.argv[1]

        if sys.argv[1] in textblocks.keys():
            textbody = textblocks[sys.argv[1]]
            print("Copied to clipboard: " + textbody)
            pyperclip.copy(textbody)
        else:
            print("Key not found")