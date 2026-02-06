

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_issued = False   # private

    def issue(self):
        if self.__can_issue():
            self.__is_issued = True
            return True
        return False

    def return_book(self):
        self.__is_issued = False

    # private method
    def __can_issue(self):
        return not self.__is_issued

    def get_status(self):
        return "Issued" if self.__is_issued else "Available"

    # method meant to be overridden
    def get_type(self):
        return "Generic Book"

    def __str__(self):
        return f"[{self.book_id}] {self.title} - {self.get_type()} - {self.get_status()}"



class PhysicalBook(Book):
    def __init__(self, book_id, title, author, shelf_no):
        super().__init__(book_id, title, author)
        self.shelf_no = shelf_no

    def get_type(self):
        return "Physical Book"


class EBook(Book):
    def __init__(self, book_id, title, author, file_size):
        super().__init__(book_id, title, author)
        self.file_size = file_size

    def get_type(self):
        return "E-Book"




class Member:
    def __init__(self, member_id, name, max_books):
        self.member_id = member_id
        self.name = name
        self._max_books = max_books        # protected
        self._issued_books = []            # protected

    def can_issue(self):
        return len(self._issued_books) < self._max_books

    def _add_book(self, book):
        self._issued_books.append(book)

    def _remove_book(self, book):
        self._issued_books.remove(book)

    def get_role(self):
        return "General Member"


class StudentMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, max_books=3)

    def get_role(self):
        return "Student"


class FacultyMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, max_books=5)

    def get_role(self):
        return "Faculty"




class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book added: {book.title}")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member registered: {member.name} ({member.get_role()})")

    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book or not member:
            print("Invalid book or member ID")
            return

        if not member.can_issue():
            print(f"{member.name} reached issue limit")
            return

        if book.issue():
            member._add_book(book)
            print(f"{book.title} issued to {member.name}")
        else:
            print("Book already issued")

    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if book and member and book in member._issued_books:
            book.return_book()
            member._remove_book(book)
            print(f"{book.title} returned by {member.name}")
        else:
            print("Invalid return operation")

    def show_books(self):
        print("\n Library Books ")
        for book in self.books.values():
            print(book)

library = Library()

library.add_book(PhysicalBook(1, "Clean Code", "Robert Martin", "A12"))
library.add_book(EBook(2, "Atomic Habits", "James Clear", "5MB"))

library.add_member(StudentMember(101, "Het"))
library.add_member(FacultyMember(102, "Dr. Sharma"))

library.issue_book(1, 101)
library.issue_book(2, 102)

library.issue_book(2, 101)

library.show_books()

library.return_book(1, 101)

library.show_books()