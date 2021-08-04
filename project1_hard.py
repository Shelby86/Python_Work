''''
- Add a check
  if book has been added, alert the user
- allow the user to search by title
- mark a book as read using the title only (just match first instance)
- delete a book by title only (just the first instance)
- apparently to delete you need to overwrite the entire file
-
'''

while True:

    # Lets make a menu:
    menu = "Please choose from the following menu: \n" \
           "To see books that have been read, enter r: \n" \
           "To add a book to the read list, enter: a \n" \
           "To search the read book list by title, enter t: \n" \
           "To add a book by title only, enter at: \n" \
           "To see all book titles, enter rt: \n" \
           "To delete a book, enter d:  \n" \
           "To mark a book as read, enter: read"\
           "To quit, enter: q: \n"


    def get_book_titles():
        with open("read_books.csv", "r") as book_list:
            line = book_list.readlines()
            list_of_titles = []
            for entry in line:
                book = entry.split(",")
                title = book[0]
                list_of_titles.append(title)
                for title in list_of_titles:
                    if title == "\n":
                        list_of_titles.remove(title)
            print(list_of_titles)
            return list_of_titles

    def add_book():
        title = input("Please enter the books's title: ").strip().title()
        author = input("Please enter the books's author: ").strip().title()
        year = input("Please enter the books publication year: ").strip()
        new_book = f"{title}, by {author}, published in {year}"
        with open ("read_books.csv", "a") as books:
            books.write(new_book)

    def list_all_books():
        with open("read_books.csv", "r") as book_list:
            print(book_list.read())
            print()

    def add_book_title():
        title = input("Please enter the books title: ").strip().title()
        author = "not entered"
        year = "not entered"
        new_book = f"{title}, by {author}, published in {year}"
        with open ("read_books.csv", "a") as books:
            books.write(new_book)

    def search_titles():
        title = input("Please enter the book title: ").strip().title()
        a = get_book_titles()
        print(a)
        if title in a:
            print("That book has already been added")
            print()
        else:
            print("That book has not been added yet.")
            print()

    def del_book_by_title():
        user_title = input("Please enter the title of the book you wish to delete: ").strip().title()
        # Read the books by lines and store the lines
        with open("read_books.csv", "r") as book_list:
            # book is a list
            books = book_list.readlines()
        for entry in books:
            if user_title in entry:
                books.remove(entry)
                # Now overwrite the file with the remaining entries
                with open("read_books.csv", "w") as file:
                    for book in books:
                        file.write(book)
            else:
                print("No entry for that book exists")
                print()
                
    def mark_as_read():
        pass

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
    elif user_option == "at":
        add_book_title()
    elif user_option == "t":
        search_titles()
    elif user_option == "rt":
        get_book_titles()
    elif user_option == "d":
        del_book_by_title()
    elif user_option == "read":
        mark_as_read()
    else:
        print("That is not a valid option")




