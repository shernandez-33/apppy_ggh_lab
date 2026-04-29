print("Hola Mundo, Git y GitHub, ensayo de laboratorio")

def suma(s1:int, s2:int)-> int:
    print(f"La suma es: {s1+s2}")


# Primer ensayo con dataclasses en python3.

from dataclasses import dataclass

@dataclass
class User:
    username: str
    login: str
    passwd: str
    email: str


if __name__ == "__main__":
    
    cody = User("Sergio Hernández","shernandez","abcd567", "shernandez@gmail.com")
    
    print(cody.username)
    print(cody.login)
    print(cody.passwd)
    print(cody.email)
    
    print("Cambiando valores de los atributos...")
    
    cody.username = "Sergio L. Hernández"
    cody.login = "shernandez33"
    cody.passwd = "abCD1234+"
    cody.email = "shernandezramos33@gail.com"
    
    print(cody.username)
    print(cody.login)
    print(cody.passwd)
    print(cody.email)
    

