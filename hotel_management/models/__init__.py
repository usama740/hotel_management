"""
This package contains the models used in the application.
Each model represents a database table and encapsulates its structure and behavior.
"""

# Import all models here to ensure they are registered with Django's ORM
from .menu import Menu
from .reservation import Reservation
from .user import User
