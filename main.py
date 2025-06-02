from fastapi import FastAPI, Request, Query
from fastapi.responses import RedirectResponse
import os, requests, urllib.parse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SHOPIFY_API_KEY = os.getenv("3daa90c6bfaa87792e218d301ade8921")
SHOPIFY_API_SECRET = os.getenv("6700c01b26649989b4c4957bdf5b29f2")
REDIRECT_URI = os.getenv("https://fastapi-shopify-app.onrender.com/auth/callback")  # should be https://your-app.onrender.com/auth/callback

@app.get("/auth")
def auth(shop: str):
    scopes = "read_products,write_products"
    params = {
        "client_id": SHOPIFY_API_KEY,
        "scope": scopes,
        "redirect_uri": REDIRECT_URI,
        "state": "secure-random-state",
        "grant_options[]": "per-user"
    }
    auth_url = f"https://{shop}/admin/oauth/authorize?" + urllib.parse.urlencode(params)
    return RedirectResponse(auth_url)

@app.get("/auth/callback")
def auth_callback(code: str = Query(...), shop: str = Query(...)):
    token_url = f"https://{shop}/admin/oauth/access_token"
    payload = {
        "client_id": SHOPIFY_API_KEY,
        "client_secret": SHOPIFY_API_SECRET,
        "code": code
    }
    response = requests.post(token_url, json=payload)
    access_token = response.json().get("access_token")
    return {
        "access_token": access_token,
        "shop": shop,
        "message": "App installed and token received!"
    }
