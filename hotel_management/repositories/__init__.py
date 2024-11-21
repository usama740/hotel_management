"""
This module imports the repository classes for managing menu, user, and reservation data.
These repositories provide methods to interact with the corresponding models, 
including creating, retrieving, updating, and deleting records.

Repositories:
- MenuRepository: Handles operations related to menu items.
- UserRepository: Handles operations related to users.
- ReservationRepository: Handles operations related to reservations.
"""

# Importing the repository classes
from .menu_repository import MenuRepository
from .user_repository import UserRepository
from .reservation_repository import ReservationRepository