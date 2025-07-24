import os
import socket

def defineAmbiente():
    if local_check():
        print("Entorno Local...")        
        import bridges        
        llave = bridges.llave 
        webhook = bridges.webhook
    else:
        print("Entorno remoto listo...")        
        llave = os.getenv("STRIPE_KEY") #Acceso a HF
        webhook = os.getenv("STRIPE_WEBHOOK_SECRET")
        print(f"La llave es {llave} y el webhook es {webhook}.")

    return llave, webhook

def local_check():
    hostname = socket.gethostname()
    #r-moibe-nowme
    print("Hostname: ", hostname)
    #Estoy usando el nombre de la app para identificar que estoy corriendola en HF.
    if "-nowme" in hostname:
        print("Ejecutando api en el servidor.")
        return False
    else:
        print("Ejecutando api en local.")
        return True