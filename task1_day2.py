no_books = int(input("Enter number of books to be purchased: "))
if no_books==1:
    points = 6
elif no_books==2:
    points = 16
elif no_books==3:
    points = 32
elif no_books>=4:
    points = 60
else:
    points = 0

print("points awarded = ",points)