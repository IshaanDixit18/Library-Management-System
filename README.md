# Library Management System

A simple Python Library Management System built using Object-Oriented Programming (OOP) principles. This project demonstrates class composition, logging with colored output, and basic library operations such as adding books/members, borrowing/returning books, and displaying information.

## Features

- **Book, Member, and Library classes** for clear separation of concerns
- **Add books and members** to the library
- **Borrow and return books** with status updates
- **Display available and borrowed books**
- **Display members and their borrowed books**
- **Colored logging output** for better readability in the terminal

## Requirements

- Python 3.8+
- [colorama](https://pypi.org/project/colorama/) for colored terminal output

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```

2. Install dependencies:
    ```bash
    pip install colorama
    ```

## Usage

Run the main script:
```bash
python app.py
```

You can modify the `my_library` object in `app.py` to test different scenarios, such as borrowing/returning books or adding new members.

## Example Output

```
INFO - The list of borrowed books is as follows:
INFO - Book: 1984 by Author: George Orwell is not available
INFO - Success! Alice has borrowed the book: The Great Gatsby
INFO - Book: The Great Gatsby by Author: F. Scott Fitzgerald is not available
```

## Project Structure

```
.
├── app.py
└── README.md
```

## License

This project is for educational purposes.
