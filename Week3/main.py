from custom_classes import MediaItem

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