import csv
# comma separated value

with open("YA_Books.csv", mode="r") as bookfile:
    # mode "r" means read!

    books = csv.reader(bookfile)
    # skip header row
    next(books)

    most_recent_published = 0 # starting low so that we actally capture the first book
    
    lowest_rating = 5 # starting high to find the worst rating out of all the books 3.52

    highest_rating = 5 # starting low to find the best rating out of all the books 4.52

    for book in books:
        title = book[0]
        author = book[1]
        rating = book[6]

    #     # print all authors that begin with the letter "M"
    #     if author.startswith("M"):
    #         print(author)

    #     # get most recently published book
    #     year = int(book[2])
    #     if year > most_recent_published:
    #         most_recent_published = year
    #         most_recent_book = book
    # print(f"Most recently published: {most_recent_book}")

    #     # get the book with the worst rating
    #     rating = float(book[6])
    #     if lowest_rating > rating:
    #         lowest_rating = rating
    #         lowest_book_rating = book
    #       
    # # print book with worst rating
    # print(f"Lowest book rating: {lowest_book_rating}")
         
          # get the book with the best rating
        ratingtwo = float(book[6])
        if highest_rating < ratingtwo:
            highest_rating = ratingtwo
            highest_book_rating = book
    # print book with the best rating
    print(f"Highest Book rating:  {highest_rating}")
