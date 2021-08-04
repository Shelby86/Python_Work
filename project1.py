'''
Users should be able to add a book to their reading list by providing a book title, an author's name,
and a year of publication.
The program should store information about all of these books in a Python list.
Users should be able to display all the books in their reading list,
 and these books should be printed out in a user-friendly format.
Users should be able to select these options from a text menu,
and they should be able to perform multiple operations without restarting the program.
You can see an example of a working menu in the post on while loops (day 8).
'''

# Input takes for fucking ever

# Thing 1
# For now I will add a Tuple called new entry:

new_book = ("This Book", "Steve Stevenson", 2008)

# I will seperate out new book into title, author, year. I think I'll need it later
# title, author, year = new_book

# I will define an empty list for read books
# read_books = []

# Now I will add the tuple to the list
# read_books.append(new_book)
# print(read_books)

# Now I see I have a list containing a tuple. I can change the tuple to anything later.

# Now that we have the basics of the back end, lets configure the front end:

while True:

    # Lets make a menu:
    menu = "Please choose from the following menu: \n" \
           "To see books that have been read, enter r: \n" \
           "To add a book to the read list, enter: a \n" \
           "To quit, enter: q: \n"

    read_books = []

    def add_book():
        title = input("Please enter the books's title: ").strip().title()
        author = input("Please enter the books's author: ").strip().title()
        year = input("Please enter the books publication year: ").strip()
        # Since this is a csv, use commas
        new_book = f"{title}, by {author}, published in {year}"
        with open ("read_books.csv", "a") as books:
            books.write(new_book + "\n")

    def list_all_books():
        with open("read_books.csv", "r") as book_list:
            print(book_list.read())

    # Lets make a variable for the user option
    user_option = input(menu).lower().strip()

    # Let's code in the quit option first:
    if user_option == 'q':
        break
    elif user_option == "r":
        list_all_books()
    elif user_option == "a":
        add_book()
        print("Book added")
    else:
        print("That is not a valid option")






