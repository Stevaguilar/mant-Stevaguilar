import random
import string


"""Funcion para generar contraseñas aleatorias de entre 4 y 16 caracteres que puede incluir
minúsculas, mayúsculas, números y caracteres especiales."""
#Se define la funcion
def generatePassword():
    """Se declara una variable password que utiliza la libreria random y string y concatena
    digits, ascii_letters y punctuation"""
    password = "".join([random.SystemRandom().choice(string.digits +
    string.ascii_letters + string.punctuation) for i in range(random.randrange(4,17))])
    """Se agrega un for con un rango de numeros aleatorios entre 4 y 17, ya que el tipo range(a,n)
    funciona con el rango entre a y n-1 de esta forma se  cumple con el rango solicitado de entre
    4 y 16 caracteres"""
#Se imprime la variable con la cadena aleatoria generada
    print (password)
        
#Se llama la funcion
generatePassword()
