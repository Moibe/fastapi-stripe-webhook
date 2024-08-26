import os
import time
import stripe
import uvicorn
from fastapi import FastAPI, Request, Header
import sulkuPypi

app = FastAPI()

#Local on Windows.
#stripe.api_key = os.environ["STRIPE_KEY"]
#API_KEY secret.
stripe.api_key = os.getenv("STRIPE_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

string_key = stripe.api_key
# This is a terrible idea, only used for demo purposes!
app.state.stripe_customer_id = None

@app.get("/")
def start(): 

    print(stripe.api_key)
    print(webhook_secret)

    autorizacion = sulkuPypi.authorize(19, 'picswap')

    print("Autorización: ", autorizacion)

    return {f"Status":"Deployed"}

@app.post("/webhook")
async def webhook_received(request: Request, stripe_signature: str = Header(None)):
    
    #Local on Windows
    #webhook_secret = os.environ["STRIPE_WEBHOOK_SECRET"]

    print("Entré al webhook...")
    
    data = await request.body()
    
    
    print("Entré al try...")
    event = stripe.Webhook.construct_event(
        payload=data,
        sig_header=stripe_signature,
        secret=webhook_secret
    )
    event_data = event['data']


    event_type = event['type']
    print("Voy a imprimir el event type:")
    print(event_type)
    time.sleep(1)

    if event_type == 'checkout.session.completed':
        print('checkout session completed')
    elif event_type == 'invoice.paid':
        print('invoice paid')
    elif event_type == 'invoice.payment_failed':
        print('invoice payment failed')
    else:
        print(f'unhandled event: {event_type}')
    
    
    
    return {"status": "success"}

   




if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)