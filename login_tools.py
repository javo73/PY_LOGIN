def user_check(user_dict, user, pswd):
    #Checking User vs Dictionary
    if(user in user_dict):
        print('Username already in use')
        return False
    else:
        return True


def login_check(user_dict, user, pswd):
    #Checking Login/Pass vs a Dictionary
    if(user in user_dict and pswd == user_dict[user]):
        return True
    else:
        return False


