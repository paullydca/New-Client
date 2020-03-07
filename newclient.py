import os

client = input("What is the Client's Name?")


root = 'c:\\Users\PaullyD\OneDrive\Oh Hey Website\Client Work'
path = f"{root}/{client}"
folders = ['1. Design Assets', '2. Content', '3. Documents']
subfold = folders
subfolders = ['1. Logo', '2. Stock Photos', '3. Social Media']
subby = subfolders
docfold = ['1. Contract', '2. Scope']
docy = docfold

try:
    print (subfold)
    for fold in subfold: 
        os.makedirs(os.path.join(path,str(fold)))
    print (subby)
    for subz in subby:
        os.makedirs(os.path.join(path, "1. Design Assets", str(subz))) 
    print (docy)
    for docz in docy:
        os.makedirs(os.path.join(path, "3. Documents", str(docz)))   
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)
