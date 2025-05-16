from storage import read_csv

def search_catalogue():
    keyword = input("Search keyword (title/author): ").lower()
    books = read_csv("books.csv")
    for book in books:
        if keyword in book["Title"].lower() or keyword in book["Author"].lower():
            print(book)

def view_loans(member_id):
    print(f"\n=== Loans for {member_id} ===")
    loans = read_csv("loans.csv")
    for loan in loans:
        if loan["MemberID"] == member_id:
            print(loan)