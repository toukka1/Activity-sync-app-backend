from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class TokenRequest(BaseModel):
    code: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str

@router.post("/exchange-token")
async def exchange_token(request: TokenRequest):
    try:
        response = requests.post(
            "https://www.strava.com/oauth/token",
            data={
                "client_id": os.getenv("STRAVA_CLIENT_ID"),
                "client_secret": os.getenv("STRAVA_CLIENT_SECRET"),
                "code": request.code,
                "grant_type": "authorization_code",
            },
        )

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to exchange token") from e

@router.post("/refresh-token")
async def refresh_token(request: RefreshTokenRequest):
    try:
        response = requests.post(
            "https://www.strava.com/oauth/token",
            data={
                "client_id": os.getenv("STRAVA_CLIENT_ID"),
                "client_secret": os.getenv("STRAVA_CLIENT_SECRET"),
                "refresh_token": request.refresh_token,
                "grant_type": "refresh_token",
            },
        )

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to refresh token") from e
