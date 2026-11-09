import csv
# comma separated value

with open("YA_Books.csv", mode="r") as bookfile:
    # mode "r" means read!

    books = csv.reader(bookfile)

    most_recent_published = 9999 # starting high so that we actally capture the first book

    for book in books:
        title = book[0]
        author = book[1]
        # print all authors that begin with the letter "M"
        # if author.startswith("M"):
        #     print(author)

        # get most recently published book
        year = int(book[2])
        if year < most_recent_published:
            most_recent_published = year
            most_recent_book = book

        print(f"Most recently published: {book}")
