print(".............welcome.............")


import subprocess


print("Press key ")
print("1:chrome")
print("2:control_panel")
print("3:cmd")
print("4:file explorer")


ch = input("enter you choice : ")


if int(ch) == 1:
    print("chrome")
    subprocess.getoutput("start chrome")
elif int(ch) == 2:
    print("control_panel")
    subprocess.getoutput("start control")
elif int(ch) == 3:
    print("cmd")
    subprocess.getoutput("start cmd")
elif int(ch) == 4:
    print("file explorer")
    subprocess.getoutput("start explorer")
else:
    print("not valid")
    
print("end")
