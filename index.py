import sqlite3
import random
import string

def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_user(username, password):
    cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
    con.commit()
    print("User created successfully.")

def authenticate_user(username, password):
    cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return True
    else:
        return False

def add_link(username, link):
    generated_link = url + generate_random_string()
    cursor.execute("INSERT INTO LinksTable (user_id, link, generated_link) VALUES (?, ?, ?)", (username, link, generated_link))
    con.commit()
    print("Link added successfully.")

def get_user_links(username):
    cursor.execute("SELECT * FROM LinksTable WHERE user_id = ?", (username,))
    user_links = cursor.fetchall()
    if user_links:
        for link in user_links:
            print(link)
    else:
        print("No links found for this user.")

def delete_link(username, link_id):
    cursor.execute("DELETE FROM LinksTable WHERE user_id = ? AND link_id = ?", (username, link_id))
    con.commit()
    print("Link deleted successfully.")

def update_link(username, link_id, new_link):
    cursor.execute("UPDATE LinksTable SET link = ? WHERE user_id = ? AND link_id = ?", (new_link, username, link_id))
    con.commit()
    print("Link updated successfully.")

url = "https://ranjaninidhi.com/"

con = sqlite3.connect("database.db")
cursor = con.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS LinksTable (
                    link_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    link TEXT,
                    generated_link TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                )''')


while True:
    choice = input("1. Login\n2. Create User\nEnter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if authenticate_user(username, password):
            print("Login successful.")
            while True:
                operation = input("1. Add Link\n2. View Links\n3. Delete Link\n4. Update Link\n5. Logout\nEnter operation: ")
                if operation == "1":
                    link = input("Enter link: ")
                    add_link(username, link)
                elif operation == "2":
                    get_user_links(username)
                elif operation == "3":
                    link_id = input("Enter link ID to delete: ")
                    delete_link(username, link_id)
                elif operation == "4":
                    link_id = input("Enter link ID to update: ")
                    new_link = input("Enter new link: ")
                    update_link(username, link_id, new_link)
                elif operation == "5":
                    break
                else:
                    print("Invalid operation.")
        else:
            print("Invalid username or password.")
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        create_user(username, password)
    else:
        print("Invalid choice.")
