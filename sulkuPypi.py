import requests
import time

base_url = "https://moibe-sulku-fastapi-docker.hf.space/"
userfile = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="
#Ojo, cuando el userfile termina con símbolo igual y supongo que también si empieza, causa problemas, la solución, ...
#... implementar más adelante desde ser agregar un caractér delimitador y despúes quitarlo, esto para evitar problemas...
#... con el símbolo =, ? y &. Dicho problema solo sucede cuando lo recibe como query params no como path params.
work = "picswap"


def getTokens(userfile):

    method = "getTokens/"

    api_url = base_url + method + userfile

    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

def authorize(tokens, work):

    method = "authorize/"

    api_url = base_url + method + str(tokens) + "/" + work

    print("Apiurl es: ", api_url)
    
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        autorizacion = response.json()
        print("Autorización:", autorizacion)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return autorizacion

def debitTokens(userfile, work):

    method = "debitTokens/"

    api_url = base_url + method + userfile + "/" + work

    print("Apiurl es: ", api_url)
    
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

def debitTokensQ(userfile, work):

    #debitTokens pero con QueryParams, (los query params sirve para ocasiones en los que usas dos de un mismo query param para abtener el resultado de un AND o rangos como...
    #... clima por ejemplo.)
    method = "debitTokens?"

    api_url = base_url + method + "userfile=" + userfile + "&" + "work=" +  work

    print("Apiurl es: ", api_url)
    
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

if __name__ == "__main__":
    getTokens(userfile)
    authorize(18,'picswap')
    debitTokens(userfile, work)
    #debitTokensQ(userfile, work)
    #pass