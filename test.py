def del_book_by_title():
        # title = input("Please enter the title of the book you wish to delete").strip().title()
        title = "Blue Book"
        # Read the books by lines and store the lines
        with open("read_books.csv", "r") as book_list:
            book = book_list.readlines()


del_book_by_title()
