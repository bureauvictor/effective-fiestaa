import os


#def GreetTheUser():
 # username = ''
  
  #print(f'I am a {username} using github. Just want to greet you!!')


#if __name__ == "__main__":
 #   GreetTheUser()

def main():
    nombre = os.getenv('USERNAME', 'usuario')
    print(f"Hola {nombre} desde GitHub")

if __name__ == "__main__":
    main()
