import os

api_key = os.environ["STRIPE_WEBHOOK_SECRET"]

print(api_key)