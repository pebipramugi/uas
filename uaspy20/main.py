from core.baseapp import BaseApp
from core.search_helper import SearchHelper
from data_model.author import Author
from view.view_book import ViewBook
from data_model.book import Book
from data_model.publication import Publication

class MainApp(BaseApp):
    def _init_(self):
        self.books = []
        self.InputBook = []
        self.ViewBook = []
        BaeApp._init_(self)

class ViewBook(Book):
    def _init_(self):
        vBook = ViewBook (self, Book)
        vBook.list_book()

    if __name__ == "__main__":
        app = MainApp()
        app.run()

    @property
    def list_book(self):
        return self.list_book
    def add_book(self):
        return self.add_book()
    def search_book(self):
        return self.search_book()
