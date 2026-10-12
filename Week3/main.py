from custom_classes import MediaItem, Book, DVD

book = MediaItem("Clean Code", "Robert C. Martin")
movie = MediaItem("Inception", "Christopher Nolan")

print("--- Library items ---")
print(book)
print(movie)

print("\n--- Checking out the book ---")
print(book.checkout())
print(book)

print("\n--- Trying to check out the same book again ---")
print(book.checkout())

print("\n--- Final status ---")
print(book)
print(movie)

print("\n=== Part 3: Inheritance ===")

novel = Book("Dune", "Frank Herbert", 412)
print(novel)

dvd = DVD("Interstellar", "Christopher Nolan", 169)
print(dvd)

print("\n--- Checking out the DVD ---")
print(dvd.checkout())
print(dvd)

print("\n--- Trying to check out the same DVD again ---")
print(dvd.checkout())