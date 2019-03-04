# let's put it in the fridge

shopping_list=[]
def show_help():
    print("\nWHAT DO YOU WANNA pick up?")
    print("""
          Enter 'DONE' to stop adding items.
          Enter 'SHOW' to see your list of items.
          """)
def show_list():
        # print out ourlist
    print("Here is what you got")

    for item in shopping_list:
        print(item)

def add_food_to_list(new_item):
        # add new item to list
        shopping_list.append(new_item)
        print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()
while True:
    #ask for new items
    new_item= input("> ")
    #able to quit the app
    if new_item== "DONE":
        show_list()
        break
    elif new_item=="SHOW":
        show_list()
        continue
    add_food_to_list(new_item)







#
# inputString = input('Enter something: ')
# print('The thing i entered is:', inputString)
