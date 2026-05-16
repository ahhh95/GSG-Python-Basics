is_username = True
is_password = True
is_user_role_admin = True
is_user_role_moderator = False
is_user_role_user = False

username = input("Enter your username: ")
if is_username == True:
    password = input("Enter your password: ")
    if is_password == True:
        if is_user_role_admin == True:
            print("Welcome Admin")
        elif is_user_role_moderator == True:
            print("Welcome Moderator")
        elif is_user_role_user == True:
            print("Welcome User")
        else:
            print("Unknown role")
    else:
        print("Wrong password")
else:
    print("User not found")
