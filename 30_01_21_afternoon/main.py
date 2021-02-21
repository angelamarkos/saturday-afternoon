# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Book:
    def __init__(self, title, author, published_date):
        self.__title = title
        self.author = author
        self.published_date = published_date

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def to_string(self):
        return f'{self.title}-{self.author}'

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(Book, key):
                setattr(Book, key, value)




def hello():
    return 'Hello'

def division(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return a/b

def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book = Book('Raven', 'Edgar allan poe', 'Jan 01 1900')
    print(book.to_string())
    book.update_info(title='Rav')
    print(book.to_string())
    book.update_info(title='Ravi')
    print(book.to_string())
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
