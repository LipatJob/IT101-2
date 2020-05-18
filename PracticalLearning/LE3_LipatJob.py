"""
#Create and print a dictionary
thisdict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year": 1964
}
print(thisdict)

#Accessing Items
#access the items of a dictionary
#by referring to it's key name,
#inside square brackets

x = thisdict['Model']
print(x)

#There is also a method called get()
#that will give you the same result

x = thisdict.get("Model")
print(x)

#Change Values 
#Change the value of a specific item
#by refering to it's key name

thisdict['Year'] = 2018
print(thisdict)

#Adding Items
#Is done by using a new index key
#and assigning a value to it

thisdict['Color'] = "Red"
print(thisdict)

#Removing Items
#pop() method removes the items with the specified key name

thisdict.pop("Model")
print(thisdict)

#popitem() method removes the last inserted item
#(in versions before 3.7, a random item is removed instead)
thisdict.popitem()
print(thisdict)

#del keyword removes the
#item with the specified key name

del thisdict["Year"]
print(thisdict)

#del keyword can also delete the dictionary completely
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists
"""


studentList = {"last":[],"first":[]}
ctr = 0
def menu():
    print("1 = Add Student")
    print("2 = View Student List")
    print("3 = Delete Student Record")
    print("4 = Update Student Record")
    print("X = Exit")
    choice = input("Enter your choice: ").upper()
    return choice

def main():
    global ctr
    while True:
        choice = menu()
        if choice == "1":
            ctr = ctr + 1
            last_name = input("Enter Last Name: ")
            first_name = input("Enter First Name: ")
            studentList["last"].append(last_name)
            studentList["first"].append(first_name)
            #print(studentList)
        elif choice == "2":
            for i in range(ctr):
                print(i + 1, end = " ");
                print(studentList["last"][i] + ", "  + studentList["first"][i])
        elif choice == "3":
            sno = int(input("Enter number to delete: "))
            if sno < 1 or sno > ctr:
                print("Invalid Number!")
            else:
                studentList["last"].pop(sno - 1)
                studentList["first"].pop(sno - 1)
                ctr = ctr - 1
        elif choice == "4":
            sno = int(input("Enter number to update: "))
            if sno < 1 or sno > ctr:
                print("Invalid Number!")
            else:
                for x in studentList:
                    c = input("Update " + x + " Y/N? ")
                    if c.upper() == "Y":
                        newData = input("Enter " + x + ": ")
                        studentList[x][sno - 1] = newData
        elif choice == "X":
            break;
        print()
main()