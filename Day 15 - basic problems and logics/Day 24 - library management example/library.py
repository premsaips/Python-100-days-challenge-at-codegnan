#Books and users
books = {
    101: ["Python Basics", "Prem Sai", 5],
    102: ["Data Structures", "Sai Kumar", 3],
    103: ["Machine Learning Intro", "Rahul Sharma", 7],
    104: ["Web Development Guide", "Anjali Rao", 4],
    105: ["Database Systems", "Kiran Reddy", 6],
    106: ["Operating Systems", "Manoj Kumar", 2],
    107: ["Computer Networks", "Sneha Patel", 8],
    108: ["Artificial Intelligence", "Vikram Singh", 5],
    109: ["Cyber Security Essentials", "Arjun Das", 9],
    110: ["Cloud Computing", "Nithya Rani", 3]
}

users = {
    1001:{'name':'prem', 'books_id':[101,102,103]},
    1002:{'name':'sai', 'books_id':[104,105,106]}
}

#person
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#books
class Book:
    def __init__(self,id, name, author):
        self.id = id
        self.name = name
        self.author = author

#users
class Users(Person):
    def __init__(self, id, name):
        super().__init__(id, name)

class Admin(Person):
    def __init__(self, id:int, name):
        super().__init__(id, name)

    def Add_book(self, book_obj:Book, quantity:int):
        if book_obj.id not in books:
            books[book_obj.id] = [book_obj.name,book_obj.author, quantity]
            return f'{book_obj.name} has been added successfully'
        
        return f'Book already exists'

    #add new user
    def add_user(self, user_obj:Users):
        if user_obj.id not in users:
            users[user_obj.id] = {'name':user_obj.name, 'books_id':[]}
            return f'{user_obj.name} has been added successfully'
        
        return f'User already exists'



    def delete_book(self, bookid):
        if bookid in books:
            books.pop(bookid)
            return f'Book is {bookid} removed successfully'
        return f'Book id {bookid} does not exist'

    def barrow_book(self, userid, *bookids):
        if userid in users:
            avl_books = []
            unavl_books = []   
            for bookid in bookids:
                if bookid in books:
                    if books[bookid][2] > 0:
                        avl_books.append({bookid:books[bookid][0]})
                        books[bookid][2] -= 1
                        users[userid]['books_id'].append(bookid)
                    else:
                        unavl_books.append({bookid:books[bookid][0]})
                else:
                    unavl_books.append({bookid:books[bookid][0]})
            return f'Available books are: {avl_books} and unavailable books are: {unavl_books}'
        return "user not found"
                    

    def return_book(self, userid, *bookids):
        if userid in users:   
            for bookid in bookids:
                if bookid in books and users[userid]['books_id']:
                    books[bookid][2] += 1 # increment of quantity
                    users[userid]['books_id'].remove(bookid) #-->remove book from user
            
            return f'Books returned successfully'
        return "user not found"
                    
         

    def all_books(self):
        return books
            

    def all_users(self):
        return len(users)
    

#main
if __name__ == "__main__":
    print("Welcome to Library Management System")

    admin = Admin(101, "premsai")

    while True:
        print("select your operation: \n1. Add book \n2. Register user \n3.Barrow book \n4.Return book \n5.View all books \n6.Total users \n7.Delete book \n8.Exit from library")
        choice = int(input("Enter your choice"))
        if choice == 1:
            bookid = int(input("Enter book id"))
            name = input("Enter book name")
            author = input("Enter author name")
            quantity = int(input("Enter quantity"))
            # creating book obj
            book_obj = Book(bookid, name, author)
            #add book to library
            print(admin.Add_book(book_obj, quantity))
        elif choice == 2:
            user_id = int(input("Enter user id"))
            user_name = input("Enter user name")
            user_obj = Users(user_id, user_name) #--> creating user object
            print(admin.add_user(user_obj))# --> adding user
        elif choice == 3:
            print("your selected option is barrow")
            user_id = int(input("enter user id"))
            book_ids = list(map(int, input("enter book ids").split()))
            print(admin.barrow_book(user_id, *book_ids))
        elif choice == 4:
            print("you have selected return")
            user_id = int(input("enter user id"))
            book_ids = list(map(int, input("enter book ids").split()))
            print(admin.return_book(user_id, *book_ids))
        elif choice == 5:
            print("you have selected view all books")
            all_books = admin.all_books()
            for bookid, details in all_books.items():
                print(f'Book id: {bookid} | Book name: {details[0]} | Author: {details[1]} | Quantity: {details[2]}')
        elif choice == 6:
            print("you have selected total users")
            print(admin.all_users())
        elif choice == 7:
            print("you have selected delete book")
            bookid = int(input("enter book id:"))
            print(admin.delete_book(bookid))
        elif choice == 8:
            print("you have selected exit from library")
            print("bye...!Thank you for using library management system")
            break
        else:
            print("Invalid choice, enter choice in between (1 -8)")



    
