pwd = input("what is your master password ?")


def view():
    pass 

view()

def add():
    pass

while True:
    mode = input("would you like to add a new password or view existing ones (view, add)?")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("INVALID MODE")
        continue