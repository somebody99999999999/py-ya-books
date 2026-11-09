import csv
# comma separated value

with open("YA_Books.csv", mode="r") as bookfile:
    # mode "r" means read!

    books = csv.reader(bookfile)
    # skip header row
    next(books)

    most_recent_published = 0 # starting low so that we actally capture the first book
    
    worst_rating = 0 # starting low to find the worst rating out of all the books 3.52

    for book in books:
        title = book[0]
        author = book[1]
        rating = book[6]
        # print all authors that begin with the letter "M"
        # if author.startswith("M"):
        #     print(author)

        # get most recently published book
        year = int(book[2])
        if year > most_recent_published:
            most_recent_published = year
            most_recent_book = book

        # get the book with the worst rating:
        rating = int(book[6])
        if rating > int(book[6]):
            

    # print(f"Most recently published: {most_recent_book}")
    # print book with worst rating
