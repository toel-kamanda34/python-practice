todos = []
while True:
    user_action = input("Type add,show or exit: ")
    #"add" != "add " ,strip method removes all the white spaces
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        #used the bitwise operator or | so if the user types show or display  the rest of the code executes
        case 'show' | 'display':
            #if we print todos we get a list, with square brackets and quitation marks,use for loop to unpack it
            for item in todos:
                #use the title method to capitalize, each word capitalized
                item = item.title()
                print(item)
        case 'exit':
            break
        #execute line when none of the case is matched
        case _:
            print("You entered an unkown command")

print("bye")

    



