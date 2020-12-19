import os
import string
import platform
if platform.system()=="windows":
    os.system("cls")
else:
    os.system("cls")

req_file=input("enter your file to search: ")

if platform.system()=="windows":
    posible_drives=string.ascii_uppercase
    valid_drives=[]
    #print(posible_drives)
    for each_drive in posible_drives:
        if os.path.exists(each_drive+":\\"):
            #print(each_drive)
            valid_drives.append(each_drive+":\\")
    print(valid_drives)
    for each_drive in valid_drives:
        for r,d,f in os.walk(each_drive):
            for each_file in f:
                if each_file==req_file:
                    print(os.path.join(r,each_file))

else:
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file==req_file:
                print(os.path.join(r,each_file))