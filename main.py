import csv
# comma separated value

with open("YA_Books.csv", mode="r") as bookfile:
    # mode "r" means read!

    books = csv.reader(bookfile)

    for book in books:
        print(book)