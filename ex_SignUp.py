
import re # modulul apeleaza functii pentru a cauta un șir pentru o anumita potrivire, se va folosi --> match


def signUp(username, email, password):
   
    # conditia cu str
    if not all(map(lambda x: type(x) == str, [username, email, password])):
        raise TypeError("Toti parametrii trebuie sa fie de tip 'str'.")   # raise - exception
   
    # conditia cu nr de caratere
    if not 5 <= len(username) <= 12:
        raise ValueError("Username trebuie sa aiba mai mult de 5 caractere si mai putin de 12 caractere.")

    # conditia cu gasirea caracterelor
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        raise ValueError("Username trebuie sa fie contina litere si cifre.")
   
    # conditia cu gasirea caracterelor
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Emailul nu este valid.")
    
    # conditia cu nr de caratere
    if len(password) < 8:
        raise ValueError("Password trebuie sa fie mai mare de 8 caractere.")
    
    # returnam dictionar
    return {"username": username, "email": email, "password": password} # returnam dictionar
   
    # apelam funcia cu transmiterea datelor
try:
    result = signUp("Cotelea", "coteleatudor@gmail.com", "+/*-135554899dvbgb")
    print(result)
except Exception as e:
    print(e)

   # print("Username: ", username)
   # print("Email: ", email)
   # print("Password: ", password)
   
signUp("turdor", "coteleatudor@gmail.com", "135554899")