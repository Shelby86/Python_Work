import json

while True:

    # Lets make a menu:
    menu = "Please choose from the following menu: \n" \
           "To see books that have been read, enter r: \n" \
           "To add a book to the read list, enter: a \n" \
           "To search the read book list by title, enter t: \n" \
           "To add a book by title only, enter at: \n" \
           "To see all book titles, enter rt: \n" \
           "To delete a book, enter d:  \n" \
           "To quit, enter: q: \n"


    def get_book_titles():
        with open("books.json", "r") as book_list:
            book_list = json.load(book_list)
            titles = []
            for book in book_list:
                title = book["title"]
                titles.append(title)
            return titles


    def add_book():
        title = input("Please enter the books's title: ").strip().title()
        author = input("Please enter the books's author: ").strip().title()
        year = input("Please enter the books publication year: ").strip()
        all_books = get_all_books()
        new_book = {
            "title": title,
            "author": author,
            "year": year
        }
        all_books.append(new_book)
        with open("books.json", "w") as reading_list:
            json.dump(all_books, reading_list)


    def get_all_books():
        with open("books.json", "r") as book_list:
            books = json.load(book_list)
            return books


    def print_all_books():
        books = get_all_books()
        print(books)


    def add_book_title():
        title = input("Please enter the books title: ").strip().title()
        author = "not entered"
        year = "not entered"
        new_book = {
            "title": title,
            "author": author,
            "year": year
        }
        book_list = get_all_books()
        book_list.append(new_book)
        with open("books.json", "w") as file:
            json.dump(book_list, file)


    def print_all_book_titles():
        books = get_book_titles()
        print(books)


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
        books = get_all_books()
        for book in books:
            if user_title in book.values():
                books.remove(book)
                print(f"{user_title} has been deleted")
                with open("books.json", "w") as file:
                    json.dump(books, file)


    def mark_as_read():
        pass


    # SET THE OPTIONS HERE
    # Lets make a variable for the user option
    # user_option = input(menu).lower().strip()

    user_option = input(menu)

    # Let's code in the quit option first:
    if user_option == 'q':
        break
    elif user_option == "r":
        print_all_books()
    elif user_option == "a":
        add_book()
        print("Book added")
    elif user_option == "at":
        add_book_title()
    elif user_option == "t":
        search_titles()
    elif user_option == "rt":
        print_all_book_titles()
    elif user_option == "d":
        del_book_by_title()
    # elif user_option == "read":
    #     mark_as_read()
    else:
        print("That is not a valid option")











