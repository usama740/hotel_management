import os
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken

class CustomRefreshToken(RefreshToken):
    def for_user(self, user):
        refresh = super().for_user(user)

        # Set refresh token expiry (from .env file)
        refresh.set_exp(lifetime=timedelta(minutes=int(os.getenv("REFRESH_TOKEN_LIFETIME", 1440))))

        # Set custom access token expiry
        access_token = refresh.access_token
        access_token.set_exp(lifetime=timedelta(minutes=int(os.getenv("ACCESS_TOKEN_LIFETIME", 5))))

        return refresh
