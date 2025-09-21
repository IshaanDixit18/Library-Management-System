import logging
import time
from typing import List

from colorama import Fore, Style


# Custom formatter with color
class CustomFormatter(logging.Formatter):
    """
    A custom logging formatter that adds color to log messages based on their severity level.
    """

    LOG_COLORS: dict[str, str] = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA,
    }

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log message with appropriate color based on the log level.

        Args:
            record (LogRecord): The log record to format.

        Returns:
            str: The formatted log message with color.
        """
        log_color: str = self.LOG_COLORS.get(record.levelname, "")
        reset_color: str = Style.RESET_ALL
        log_message: str = super().format(record)
        return f"{log_color}{log_message}{reset_color}"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

for handler in logging.root.handlers:
    handler.setFormatter(
        CustomFormatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    )


class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        availability (bool): Whether the book is available for borrowing.
    """

    def __init__(self, title: str, author: str, availability: bool) -> None:
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            availability (bool): The availability status of the book.
        """
        self.title: str = title
        self.author: str = author
        self.availability: bool = availability


class Member:
    """
    Represents a library member.

    Attributes:
        name (str): The name of the member.
        borrowed_books (list): A list of books borrowed by the member.
    """

    def __init__(self, name: str, borrowed_books: List[str]) -> None:
        """
        Initialize a Member instance.

        Args:
            name (str): The name of the member.
            borrowed_books (list): A list of books borrowed by the member.
        """
        self.name: str = name
        self.borrowed_books: List[str] = []


class Library:
    """
    Represents a library that manages books and members.

    Attributes:
        books (list): A list of books in the library.
        members (list): A list of members registered in the library.
    """

    def __init__(self) -> None:
        """
        Initialize a Library instance with default books and members.
        """
        self.books: List[Book] = [
            Book("1984", "George Orwell", True),
            Book("To Kill a Mockingbird", "Harper Lee", True),
            Book("The Great Gatsby", "F. Scott Fitzgerald", True),
            Book("Pride and Prejudice", "Jane Austen", True),
            Book("The Catcher in the Rye", "J.D. Salinger", True),
            Book("The Hobbit", "J.R.R. Tolkien", True),
            Book("Fahrenheit 451", "Ray Bradbury", True),
        ]
        self.members: List[Member] = [
            Member("Ishaan", []),
            Member("Alice", []),
            Member("Bob", []),
            Member("Charlie", []),
            Member("David", []),
        ]

    def add_book(self, newbook: Book) -> List[Book]:
        """
        Add a new book to the library.

        Args:
            books (list): The current list of books.
            newbook (Book): The new book to add.

        Returns:
            list: The updated list of books.
        """
        self.books.append(newbook)
        return self.books

    def add_member(self, members: List[Member], newmember: Member) -> None:
        """
        Add a new member to the library.

        Args:
            members (list): The current list of members.
            newmember (Member): The new member to add.
        """
        self.members.append(newmember)

    def borrow_book(self, book_title: str, member_name: str) -> None:
        """
        Allow a member to borrow a book if available.

        Args:
            book_title (str): The title of the book to borrow.
            member_name (str): The name of the member borrowing the book.
        """
        book_found: bool = False
        user_found: bool = False
        for books in self.books:
            if books.title.lower() == book_title.lower() and books.availability:
                book_found = True
                break

        for members in self.members:
            if members.name.lower() == member_name.lower():
                user_found = True
                logging.info(f"Member: {member_name} is a registered member")
                break
        if not book_found:
            logging.warning(
                f"Book: {book_title} is not in the library "
            )
        elif not book_found and user_found:
            logging.warning(f"Book: {book_title} is not in the library")
            logging.info("Please come again later. Thank you!")
        elif book_found and not user_found:
            logging.warning(f"Member: {member_name} is not a registered member")
            logging.info(f"Registering new member: {member_name}")
            time.sleep(5)  # Simulate processing time
            self.members.append(Member(member_name, []))
            logging.info(f"Member: {member_name} has been registered successfully")
            logging.info(f"Book: {book_title} is available for borrowing")
            logging.info(f"Assigning Book: {book_title} to member: {member_name}")
            time.sleep(5)
            for book in self.books:
                if book.title == book_title:
                    logging.info(
                        f"Success! {member_name} has borrowed the book: {book_title}"
                    )
                    for member in self.members:
                        if member.name == member_name:
                            member.borrowed_books.append(book_title)
                            book.availability = False

        else:
            logging.info(f"Book: {book_title} is available for borrowing")
            logging.info(f"Assigning Book: {book_title} to member: {member_name}")
            for book in self.books:
                if book.title == book_title:
                    logging.info(
                        f"Success! {member_name} has borrowed the book: {book_title}"
                    )
                    for member in self.members:
                        if member.name == member_name:
                            member.borrowed_books.append(book_title)
                            book.availability = False

    def return_book(self, book_title: str, member_name: str) -> None:
        """
        Allow a member to return a borrowed book.

        Args:
            book_title (str): The title of the book to return.
            member_name (str): The name of the member returning the book.
        """
        for member in self.members:
            if member.name == member_name and book_title in member.borrowed_books:
                member.borrowed_books.remove(book_title)
                for book in self.books:
                    if book.title == book_title:
                        book.availability = True

    def display_available_books(self) -> None:
        """
        Display the list of available books in the library.

        Args:
            books (list): The list of books in the library.
        """
        logging.info("The list of available books is as follows:\n")
        for book in self.books:
            if book.availability:
                logging.info(f"Book: {book.title} by Author: {book.author}")
        print("\n")

    def display_borrowed_books(self) -> None:
        """
        Display the list of borrowed books in the library.

        Args:
            books (list): The list of books in the library.
        """
        logging.info("The list of borrowed books is as follows:\n")
        for book in self.books:
            if not book.availability:
                logging.info(
                    f"Book: {book.title} by Author: {book.author} is not available"
                )

    def display_members(self) -> None:
        """
        Display the list of members and their borrowed books.

        Args:
            members (list): The list of members in the library.
        """
        for member in self.members:
            logging.info(
                f"Member: {member.name}, Borrowed Books: {member.borrowed_books}"
            )


my_library = Library()
my_library.borrow_book("1984", "Ishaan")
my_library.display_borrowed_books(my_library.books)
my_library.borrow_book("The Great Gatsby", "Alice")
my_library.display_borrowed_books(my_library.books)
# my_library.display_members(my_library.members)
my_library.return_book("1984", "Ishaan")
my_library.display_borrowed_books(my_library.books)
my_library.borrow_book("the Hobbit", "Praharsh")


