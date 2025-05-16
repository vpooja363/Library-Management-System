import bcrypt
from datetime import date
from storage import read_csv, append_csv
from utils import generate_member_id

def register_member():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    member_id = generate_member_id()
    member = {
        "MemberID": member_id,
        "Name": name,
        "PasswordHash": hash_pw,
        "Email": email,
        "JoinDate": str(date.today())
    }
    append_csv("members.csv", member, member.keys())
    print(f"✅ Registered with Member ID: {member_id}")

def register_librarian():
    print("\n=== Librarian Sign-Up ===")
    name = input("Full Name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm = input("Confirm Password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        return

    hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    librarian_id = "lib" + generate_member_id()

    for row in read_csv("librarians.csv"):
        if row["Email"] == email:
            print("❌ Email already registered.")
            return

    librarian = {
        "LibrarianID": librarian_id,
        "Name": name,
        "PasswordHash": hash_pw,
        "Email": email
    }

    append_csv("librarians.csv", librarian, librarian.keys())
    print(f"✅ Librarian account created. Your ID is: {librarian_id}")

def login(role):
    print(f"\n=== {role.capitalize()} Login ===")
    user_id = input("Enter ID: ")
    password = input("Enter Password: ")

    filename = "librarians.csv" if role == "librarian" else "members.csv"
    id_field = "LibrarianID" if role == "librarian" else "MemberID"

    for row in read_csv(filename):
        if row[id_field] == user_id and bcrypt.checkpw(password.encode(), row["PasswordHash"].encode()):
            print(f"✅ Login successful. Welcome, {row['Name']}!")
            return row

    print("❌ Invalid ID or password.")
    return None