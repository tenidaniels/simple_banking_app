# Functions
# Dictionaries(our database)
# input validation
# conditional logic


# Database
# this is where we store all user accounts
users_database= {
    'alex':{'password': 'pass123', 'name': 'Alex Johnson', 'balance': 1000.0, 'age':13},
    'sarah': {'password': 'sarah465', 'name': 'Sarah Williams', 'balance': 2500.0, 'age': 14},
    'mike': {'password': 'mike768', 'name': 'Mike Davies', 'balance': 500.0, 'age': 15}
}

#Login

def login():
    """Function to check if username and password are correct
    Returns: username if successful and none if failed"""

    print("\n")
    print("Login to your bank account")
    print("=" *50)

    username= input("Enter your username: ").lower()
    password= input("Enter your password:")

    if username not in users_database:
        print("\n username not found !.  Try again")
        return None

    if users_database[username]['password'] != password:
        print("\n wrong password!, Try again")
        return None

    #success
    print(f"\n welcome back, {users_database[username]['name']}")
    return username




login()


