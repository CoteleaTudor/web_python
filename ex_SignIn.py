# Create a function called signIn()
# This function should take two parameters: username and password
# This function should also contain a local variable: a list of dictionaries which holds the correct username and password for 3 users
# The function should loop through the list of 3 users and in case the username and password parameters does not correspond to any of the users - return None, else - return the dictionary that represents that user

def signIn(username, password):
    # dam dictionarul cu useri
    list_users = [
        {"username":"user_nr_1", "password":"pass_1"},
        {"username":"user_nr_2", "password":"pass_2"},
        {"username":"user_nr_3", "password":"pass_3"}
        ]
    
    # dam un for pentru a parcurge toata lista de useri + conditia cu if (pct. 3 din exerciriu)
    for i in list_users:
        if i["username"] == username and i["password"] == password:
            return i
    return None
           
signIn ("user_nr_2", "pass_2")