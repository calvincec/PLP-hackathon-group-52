password = "Calvince"
door_state = "close"
import datetime
ltime = datetime.datetime.now()

while True:
    choice = input("enter open to open the door and close to close the door and quit to exit: ")
    if choice.upper()==door_state.upper():
        print("The dooor is already ",choice+"ed")
        print("The door was last ", choice+"ed"+" at "+str(ltime))
        continue
    else:
        if choice.upper()=="OPEN":
            new_password = input("Enter the password: ")
            if new_password != password:
                print("Wrong password, try again: ")
                continue
            else:
                door_state = "open"
                print("The door was last closed at "+str(ltime))
                print("The door is now open")
                ltime = datetime.datetime.now()
                continue
                
        elif choice.upper()=="QUIT":
            break
        elif choice.upper()=="CLOSE":
            door_state = "close"
            print("The door was last opened at "+str(ltime))
            print("The door is now locked")
            ltime = datetime.datetime.now()
            continue
        else:
            print("Invalid input")
            continue

