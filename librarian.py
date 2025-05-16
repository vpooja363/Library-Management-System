from storage import read_csv, write_csv, append_csv
from datetime import datetime, timedelta
import uuid

def add_book():
    print("\n=== Add Book ===")
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Copies: "))
    book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "CopiesTotal": copies,
        "CopiesAvailable": copies
    }
    append_csv("books.csv", book, book.keys())
    print("✅ Book added.")

def issue_book():
    isbn = input("ISBN to issue: ")
    member_id = input("Member ID: ")
    books = read_csv("books.csv")
    for book in books:
        if book["ISBN"] == isbn and int(book["CopiesAvailable"]) > 0:
            book["CopiesAvailable"] = str(int(book["CopiesAvailable"]) - 1)
            write_csv("books.csv", books, book.keys())

            today = datetime.today()
            due = today + timedelta(days=14)
            loan = {
                "LoanID": str(uuid.uuid4())[:8],
                "MemberID": member_id,
                "ISBN": isbn,
                "IssueDate": today.strftime("%Y-%m-%d"),
                "DueDate": due.strftime("%Y-%m-%d"),
                "ReturnDate": ""
            }
            append_csv("loans.csv", loan, loan.keys())
            print(f"✔ Book issued. Due on {due.strftime('%d-%b-%Y')}")
            return
    print("❌ Book not available.")

def return_book():
    loan_id = input("Loan ID to return: ")
    loans = read_csv("loans.csv")
    for loan in loans:
        if loan["LoanID"] == loan_id and loan["ReturnDate"] == "":
            loan["ReturnDate"] = datetime.today().strftime("%Y-%m-%d")
            write_csv("loans.csv", loans, loan.keys())

            books = read_csv("books.csv")
            for book in books:
                if book["ISBN"] == loan["ISBN"]:
                    book["CopiesAvailable"] = str(int(book["CopiesAvailable"]) + 1)
                    write_csv("books.csv", books, book.keys())
                    break
            print("✔ Book returned.")
            return
    print("❌ Loan not found or already returned.")

def view_overdues():
    print("\n=== Overdue Books ===")
    loans = read_csv("loans.csv")
    today = datetime.today().date()
    for loan in loans:
        if loan["ReturnDate"] == "" and datetime.strptime(loan["DueDate"], "%Y-%m-%d").date() < today:
            print(loan)