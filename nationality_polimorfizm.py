class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):
        print(f"Title: {self.title} - {self.author.name}")

author = Author('<NAME>', 'National Laboratory')
book = Book('The Book', author)

print(author.name)
book.get_info_book()



