a = open("text.txt","w")
print("blender",file=a)
a.close()

import os
if os.path.exists("text.txt"):
    a = open("text.txt","r")
    q = a.read()
    print(q)
    a.close()
