import requests
import json
from typing import Optional

from medinet.exceptions import MediNetError

class AuthenticationService:
    """Authentication service for MediNet"""

    AUTHORIZATION_SERVER_URL = "https://auth-api.gisprod.aws.greenwayhealth.com/oauth2/auth-code"
    TOKEN_SERVER_URL = "https://auth-api.gisprod.aws.greenwayhealth.com/oauth2/token"
    FHIR_SERVER_URL = "https://fhir-api.fhirprod.aws.greenwayhealth.com/fhir/R4"

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_authorization_url(self) -> str:
        """Get the authorization URL for the user to authenticate"""
        return f"{self.AUTHORIZATION_SERVER_URL}?response_type=code&client_id={self.client_id}&scope=user%2FPatient.read%20openid%20fhirUser&redirect_uri={self.redirect_uri}&aud={self.FHIR_SERVER_URL}"

    def exchange_code_for_token(self, code: str) -> dict:
        """Exchange the authorization code for an OAuth access token"""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        response = requests.post(self.TOKEN_SERVER_URL, headers=headers, data=data)

        if response.status_code != 200:
            raise MediNetError("Failed to exchange authorization code for access token")

        return response.json()

    def get_patient_data(self, access_token: str) -> dict:
        """Get patient data from the FHIR server using the access token"""
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        }

        response = requests.get(f"{self.FHIR_SERVER_URL}/Patient", headers=headers)

        if response.status_code != 200:
            raise MediNetError("Failed to get patient data from FHIR server")

        return response.json()
