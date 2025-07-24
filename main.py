import time
import stripe
from fastapi import FastAPI, Request, Header
import sulkuPypi
import globales
import herramientas

app = FastAPI()

string_key = globales.llave
# This is a terrible idea, only used for demo purposes!
app.state.stripe_customer_id = None

@app.get("/")
def start(): 
    return {f"Status":"Deployed"}

@app.post("/webhook")
async def webhook_received(request: Request, stripe_signature: str = Header(None)):    
    
    webhook_secret = globales.webhook 

    data = await request.body()
    print("data ready")
    
    print("Construyendo el evento:")
    
    try:         
        event = stripe.Webhook.construct_event(
            payload=data,
            sig_header=stripe_signature,
            secret=webhook_secret
        )
        print("Evento construido...")        

    except Exception as e:     
        print("Excepción es: ", e)         

    event_data = event['data']['object']     
    event_type = event['type']
    print("Voy a imprimir el event type:")
    print(event_type)
    
    if event_type == 'charge.succeeded':
        print('charge succeed')
        herramientas.registrar_evento(event_type)
        print(event_data)
        print("Ready")
        time.sleep(80)
        print(event_data['created'])
        print(event_data['id'])
        print(event_data['payment_intent'])
        print(event_data['payment_method'])
        print(event_data['receipt_url'])
        
        # autorizacion = sulkuPypi.authorize(19, 'picswap')
        # print("Autorización: ", autorizacion)
    else:
        print(f'unhandled event: {event_type}')      
    
    return {"status": "success"}

# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True)