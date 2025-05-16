from auth import register_member, register_librarian, login
from librarian import add_book, issue_book, return_book, view_overdues
from member import search_catalogue, view_loans

def librarian_menu():
    while True:
        print("\n=== Librarian Dashboard ===")
        print("1. Add Book\n2. Issue Book\n3. Return Book\n4. View Overdue\n5. Logout")
        choice = input("> ")
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            view_overdues()
        else:
            break

def member_menu(member):
    while True:
        print("\n=== Member Dashboard ===")
        print("1. Search Catalogue\n2. My Loans\n3. Logout")
        choice = input("> ")
        if choice == "1":
            search_catalogue()
        elif choice == "2":
            view_loans(member["MemberID"])
        else:
            break

def main():
    print("📚 Welcome to the Library System")
    while True:
        print("\nLogin as:")
        print("1. Librarian\n2. Member\n3. Register Member\n4. Register Librarian\n5. Exit")
        choice = input("> ")
        if choice == "1":
            user = login("librarian")
            if user:
                librarian_menu()
        elif choice == "2":
            user = login("member")
            if user:
                member_menu(user)
        elif choice == "3":
            register_member()
        elif choice == "4":
            register_librarian()
        else:
            break

if __name__ == "__main__":
    main()