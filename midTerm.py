'''
Ask the user for a book title, author, year
Store the titles as into a csv
You can use an f string to store a value
Remember csv files end with \n
'''

class ReadingList:

    def __init__(self):
        self.on_load()

    def on_load(self):
        with open("./books.csv", "r") as csv:
            self.books = {}
            for book in csv.readlines():
                title, author, year = book.strip().split(",")
                # books is a dictionary
                # mapping the title of the book to a dictionary
                # of the book's details
                self.books[title] = {
                    "title":title,
                    "author": author,
                    "year": year
                }



    def add_book(self):
        title = input("Enter the book's title: ").strip().titile()
        author = input("Enter the book's author: ").strip().title()
        year = input("Enter the year published: ").strip()

        with open("books.csv", "a") as library:
            library.write(f"{title},{author},{year} \n")

    def see_all_books(self):
        for book in self.books.values():
            print(f"{book['title']}, {book['author']}, {book['year']}")


    def retrieve_book(self):
        user_title = input("Please enter the book title: ").strip().title()
        if user_title in self.books:
            found_book = self.books[user_title]
            print()
            print(f"{found_book['title']}, {found_book['author']}, {found_book['year']}".strip())
            print()
        else:
            print("\nThat book has not been added yet\n")

    # q = quit
    # s = see reading list
    # a = add book to list
    # r = retireve book by title

def main():
    books = ReadingList()
    while True:
        user_option = input("\nPlease select from the following menu:\n"
                        "To add a book, enter a \n"
                        "To see full reading list, enter s \n"
                        "To retrieve a book, enter r \n"
                        "To exit the menu, enter q \n"
                        "Option: \n").strip().lower()

        if user_option == "q":
            break
        elif user_option == "a":
            books.add_book()
        elif user_option == "s":
            books.see_all_books()
        elif user_option == "r":
             books.retrieve_book()
        else:
            print("That is not a valid option")


main()