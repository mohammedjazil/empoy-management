empoye = []

def add_person():
    name = input("enter the person :")
    age = input ("enter your age :")
    phone = int(input("enter your phone number :"))
    
    list = {"name":name,"age":age ,"phone":phone}
    empoye.append(list)
    print("empoyee added successfully")
    

def display_person():
    if not empoye:
        print("no empoyee to display")
    else:
        print("empoyee")
        for i in empoye:
            print(f"name:{i['name']},age: {i['age']},phone: {i['phone']}")
            
def search_person():
    search_name = input("enter the searching name :")
    for i in empoye:
        if i['name'] == search_name:
            print(f"name:{i['name']},age: {i['age']},phone: {i['phone']}")
        else:
            print("empoyee not found ")


def delete_person():
    search_delete = input("enter name to delete :")
    for i in empoye:
        if i['name'] == search_delete:
            empoye.remove(i)
            print(f"delete {i['name']} successfuly ")

    
def main():
    while True:
        print("1. add a person :")
        print("2. display person:")
        print("3. delete a person:")
        print("4. search a person")
        print("5. exit :")
        
        choice=input("enter a choice (1-5):")
        
        if choice == "1":
            add_person()
            
        elif choice == "2":
            display_person()
            
        elif choice == "3":
            delete_person()
            
        elif choice == "4":
            search_person()
            
        elif choice == "5":
            print("have a nice day ")
            break
        
        else:
            print("enter invalid key")
            
if __name__ == "__main__":
    main()