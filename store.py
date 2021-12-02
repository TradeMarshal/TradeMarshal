E_Bookstore = [{"Id": 10001, "Title": "Things Fall Apart", "Author": "Chinue Achiebe", "Genre": "Poetry", "Category": "History", "Available Copies": 25, "Description": "True Life story", "Book-price": 1500, "loan intrest": 100},
                {"Id": 10002, "Title": "Love Was The Excuse", "Author": "Sineliswe Sibeko", "Genre": "Play", "Category": "Drama", "Available Copies": 20, "Description": "Toxic Relationships Are Made Up Of Psychopaths", "Book-Price": 3450, "loan intrest": 10},
                {"Id": 10004, "Title": "The Life And Times Of A Black Man", "Author": "Jeremy Mason", "Genre": "Poetry", "Category": "drama", "Available Copies": 13, "Description": "What It Means To Be a Black Man", "Book-Price": 8950, "loan intrest": 100},
                {"Id": 10005, "Title": "My Children! My Africa", "Author": "Athol Fugard", "Genre": "Poetry", "Category": "Drama", "Available Copies": 47, "Description": "education and not violence is the answer to south africa's problem", "Book-Price": 1450, "loan intrest": 100},
                {"Id": 10005, "Title": "The Lion And The Jewel", "Author": "Wole Soyinka", "Genre": "comedy", "Category": "Drama", "Available Copies": 65, "Description": "How The Lion Hunts The Jewel Of Baroka", "Book-Price": 8450, "loan intrest": 100},
                {"Id": 10005, "Title": "Betrayal In The City", "Author": "Francis Imbuga", "Genre": "Play", "Category": "Drama", "Available Copies": 54, "Description": "It Is An Incisive Examination Of The Problems Of independence And Freedom in Post-Colonial African States", "Book-Price": 6750, "loan intrest": 100},
                {"Id": 10005, "Title": "Our Husband Has Gone Mad Again", "Author": "Ola Rotimi", "Genre": "Poetry", "Category": "Drama", "Available Copies": 22, "Description": "A Former Military Major, Takes To Politices.His motives Have Far More To Do With vanity And patriotism", "Book-Price": 9850, "loan intrest": 100},]

def Login():
    ADMIN_USER = "TradeMarshal"
    ADMIN_KEYCODE = "OfficialKvng"


E_bookstore1 = E_Bookstore
Temp = []
order = ""


def AdminLoginWindow():
    print("====================")
    print("Display Menu")
    print("Upload Books")
    print("Manage/Update BookStore")
    print("Manage SalesRecords")
    print("manage LoanedBooksRecord")
    print("LogOut")
    print("====================")

def AdminDisplayMenuWindow():
    print("Id\tTitle\tAuthor\tGenre\tCategory\tAvailable Copies\tDescription\tBook-Price\tLoan Intrest")
    print("=====")
    for d in E_Bookstore:
        print(f'{d["Id"]}\t{d["Title"]}\t{d["Author"]}\t{d["Genre"]}\t{d["Category"]}\t{d["Avaiable Copies"]}\t{d["Description"]}\t{d["Book-Price"]}\t{d["Loan Intrest"]}')


def UploadBooks():
    n = int(input("Enter The Number Of Books To Upload : "))
    for i in range(n):
        New_Id = int(input("Enter Id : "))
        New_Title = input("Enter Title : ")
        New_Author = input("Enter Author : ")
        New_Genre = input("Enter Genre : ")
        New_Category = input("Enter Category : ")
        New_Available_Copies = int(input("Enter Available Copies : "))
        New_Description = input("Enter Description : ")
        New_Book_Price = int(input("Enter Book-Price : "))
        New_Loan_Intrest = int(input("Enter Loan Intrest : "))
        d = [{"Id": New_Id, "Title": New_Title, "Author": New_Author, "Genre": New_Genre, "Category": New_Category, "Available Copies": New_Available_Copies, "Description": New_Description, "Book-Price": New_Book_Price, "Loan Intrest": New_Loan_Intrest}]
        E_Bookstore.extend(d)
        AdminDisplayMenuWindow()


def RemoveProducts():
    BookId = int(input("Enter the Id needed to be deleted : "))
    Found = False
    for d in E_Bookstore:
        Found = d["Id"] == BookId
        if Found != True:
            Temp.append(d)
            continue
        if Found == True:
            d["Available Copies"] -= 1
    print("deleting item.....")
    if len(Temp) == d:
        print(f'{BookId} not found')
    else:
        print(f"{BookId}'s one Available is removed from the list")
    AdminDisplayMenuWindow()


def Availableproducts():
    Total = 0
    print("\n")
    for d in E_Bookstore:
        print(f'{d["Title"]} = {d["Available Copies"]}')
        Total += (d["Available Copies"])
    print("\nTotal Avialable Copies is : ", Total)


def MonthlyIncome():
    Total = 0
    for d in E_Bookstore:
        Total += ((d["Available Copies"] * d["Book-Price"]) - (d["Available Copies Remaining"] * d["Loan Intrest"]))
    print("\nTotal Income is : ", Total)


def LogoutWindow():
    Login()


def AdminOptions():
    Choice = int(input("Please enter user choice : "))
    if Choice == 1:
        AdminDisplayMenuWindow()
        print("\n====================\n")
        AdminLoginWindow()
        print("\n====================\n")
        AdminOptions()
    elif Choice == 2:
        AdminDisplayMenuWindow()
        print("\n====================\n")
        UploadBooks()
        print("\n====================\n")
        AdminLoginWindow()
        print("\n====================\n")
        AdminOptions()
    elif Choice == 3:
        AdminDisplayMenuWindow()
        print("\n====================\n")
        RemoveProducts()
        print("\n====================\n")
        AdminLoginWindow()
        print("\n====================\n")
        AdminOptions()
    elif Choice == 4:
        Availableproducts()
        print("\n====================\n")
        AdminLoginWindow()
        print("\n====================\n")
        AdminOptions()
    elif Choice == 5:
        MonthlyIncome()
        print("\n====================\n")
        AdminLoginWindow()
        print("\n====================\n")
        AdminOptions()
    elif Choice == 6:
        LogoutWindow()
    else:
        print("\n Invalid Choice. Please enter valid choice ")
        print("\n====================\n")
        AdminLoginWindow()
        print("\n====================\n")
        AdminOptions()


def UserLoginWindow():
    print("\n====================\n")
    print("1.Display Menu")
    print("2.Place Order")
    print("Cancel Order")
    print("Request For A Book-Loan")
    print("LogOut")
    print("\n====================\n")


def UserDispalyMenuWindow():
    print("Id\tTitle\tAuthor\tGenre\tCategory\tAvailable Copies\tDescription\tBook-Price\tLoan Intrest")
    print("\n====================\n")
    for d in E_Bookstore:
        print(f'{d["Id"]}\t{d["Title"]}\t{d["Author"]}\t{d["Genre"]}\t{d["Category"]}\t\t{d["Available Copies"]}\t{d["Description"]}\t\t{d["Book-Price"]}\t\t{d["Loan Intrest"]}')


def User_Id():
    UserDispalyMenuWindow()
    Book_Id = int(input("\n Enter the Id : "))


def PlaceOrder():
    Order_Number = 10
    UserDispalyMenuWindow()
    Book_Id = int(input("\n Enter the Id : "))


    for d in E_Bookstore:
        if d["Id"] == Book_Id:
            print("\nId\tTitle\tAuthor\tGenre\tCategory\tAvailable Copies\tDescription\tBook-Price\tLoan Intrest")
            print("\n====================\n")
            print(f'{d["Id"]}\t{d["Title"]}\t{d["Author"]}\t{d["Genre"]}\t{d["Category"]}\t\t{d["Available Copies"]}\t{d["Description"]}\t\t{d["Book-Price"]}\t\t{d["Loan Intrest"]}')
            Order = '{d["Id"]}\t{d["Title"]}\t{d["Author"]}\t{d["Genre"]}\t{d["Category"]}\t\t{d["Available Copies"]}\t{d["Description"]}\t\t{d["Book-Price"]}\t\t{d["Loan Intrest"]}'
            Confirm = input("\n Do you want to place an order on the above shown Books : Y/N ")


            if Confirm == 'Y' or Confirm == 'y':
                print("\n Successfully placed an order on this book {} {}".format(d["Id"], d["Title"]))
                Order_Number += 1
                print("Your order number is : ", Order_Number)
                d["Available Copies"] -= 1
                break


            elif Confirm == 'N' or Confirm == 'n':
                print("The order is not placed. You can carry on with your already made purchase. Have A Nice Day And Enjoy Your Reading!!!")
                break
            else:
                print("\n You have entered a wrong option, Please kindly enter again\n")
                Confirm = input("\n Do you still want to place an order on the above shown books? : Y/N ")
                break


        if d["Id"] != Book_Id:
            print("\n You have entered an invalid Id, Please kindly enter  a valid Id\n")
            User_Id()
        print("\n Available Copies : \n")
        UserDispalyMenuWindow()


def CancelOrder():
    Found = False
    Temp = []
    Order_Id = input("Enter the order Id : ")
    for d in E_Bookstore:
        Found = d["Id"] == Order_Id
        if Found != True:
            Temp.append(d)
    if len(Temp) == d:
        print(f'{Order_Id} Was Not Found')
    else:
        print(f'{Order_Id} Was Removed From The Placed Order')


def RequestForBookLoan():
    Loan_Number = 10
    UserDispalyMenuWindow()
    Book_Id = int(input("\n Enter the book Id you want to loan : "))


    for d in E_Bookstore:
        if d["Id"] == Book_Id:
            print("\nId\tTitle\tAuthor\tGenre\tCategory\tAvailable Copies\tDescription\tBook-Price\tLoan Intrest")
            print("\n====================\n")
            print(f'{d["Id"]}\t{d["Title"]}\t{d["Author"]}\t{d["Genre"]}\t{d["Category"]}\t\t{d["Available Copies"]}\t{d["Description"]}\t\t{d["Book-Price"]}\t\t{d["Loan Intrest"]}')
            Loan = '{d["Id"]}\t{d["Title"]}\t{d["Author"]}\t{d["Genre"]}\t{d["Category"]}\t\t{d["Available Copies"]}\t{d["Description"]}\t\t{d["Book-Price"]}\t\t{d["Loan Intrest"]}'
            Confirm = input("\n Do you want to borrow the above shown Books : Y/N ")


            if Confirm == 'Y' or Confirm == 'y':
                print("\n You have successfully loaned this book {} {}".format(d["Id"], d["Loan Intrest"]))
                Loan_Number += 1
                print("Your Loan number is : ", Loan_Number)
                d["Available Copies"] -= 1
                break


            elif Confirm == 'N' or Confirm == 'n':
                print("The loan was declined. You can carry on with your already made purchase if you made any. Have A Nice Day And Enjoy Your Reading!!!")
                break
            else:
                print("\n You have entered a wrong option, Please kindly enter again\n")
                Confirm = input("\n Do you still want to loan the above shown books? : Y/N ")
                break


        if d["Id"] != Book_Id:
            print(" You have entered an invalid Id, Please kindly enter  a valid Id")
            User_Id()
        print("\n Available Copies : \n")
        UserDispalyMenuWindow()


def UserChoiceOptions():
    Choice = int(input("Please enter user's choice : "))
    if Choice == 1:
        UserDispalyMenuWindow()
        print("\n====================\n")
        UserLoginWindow()
        print("\n====================\n")
        UserChoiceOptions()
    elif Choice == 2:
        PlaceOrder()
        print("\n====================\n")
        UserLoginWindow()
        print("\n====================\n")
        UserChoiceOptions
    elif Choice == 3:
        CancelOrder()
        print("\n====================\n")
        UserLoginWindow()
        print("\n====================\n")
        UserChoiceOptions()
    elif Choice == 4:
        RequestForBookLoan()
        print("\n====================\n")
        UserLoginWindow()
        print("\n====================\n")
        UserChoiceOptions()
    elif Choice == 5:
        LogoutWindow()
    else:
        print("Invalid Choice, Please Kindly Enter A Valid Choice")


def Login():
    Tp = input("Login Admin/Login User [Type A To Login The Admin/ Type U To Login The User] : ")
    if Tp == 'A' or Tp == 'a':
        Password = input("Enter A Valid Password : ")
        if Password == "OfficialKvng":
            AdminLoginWindow()
            AdminOptions()
        else:
            print("Invalid Password. Please Kindly Enter A Valid Password")

    elif Tp == 'U' or Tp == 'u':
        Password = input("Enter A Valid Password : ")
        if (Password == "OfficialKvng2"):
            UserLoginWindow()
            UserChoiceOptions()
        else:
            print("Invalid Password. Please Kindly Enter A Valid Password To Avoid Slap")
    else:
        print("Inavlid User Login. Please Enter A Valid User Login Or I Go Block You")



Login()