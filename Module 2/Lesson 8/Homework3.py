books = [
    {'title': 'Python Guide', 'price': 150, 'is_available': True},
    {'title': 'Data Science Basics', 'price': 220, 'is_available': False},
    {'title': 'Web Development', 'price': 95, 'is_available': True}
]

book_available = list(filter(lambda book: book.get("is_available") == True, books))
book_discount = list(map(lambda book: {**book, "price": book.get("price") * 0.9}, book_available))

print(book_discount)
