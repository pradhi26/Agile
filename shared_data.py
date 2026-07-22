# ==========================================
# Tourist Booking System
# Shared Data
# ==========================================

# Logged in user
current_user = None

# Selected package
selected_package = None

# -----------------------------
# Users
# -----------------------------
users = [
    {
        "name": "Administrator",
        "email": "admin@gmail.com",
        "password": "admin123",
        "role": "Admin"
    }
]

# -----------------------------
# Tourist Packages
# -----------------------------
packages = [
    {
        "id": 1,
        "destination": "Goa",
        "duration": "4 Days / 3 Nights",
        "price": 12000,
        "rating": 4.8
    },
    {
        "id": 2,
        "destination": "Ooty",
        "duration": "3 Days / 2 Nights",
        "price": 6500,
        "rating": 4.5
    },
    {
        "id": 3,
        "destination": "Manali",
        "duration": "5 Days / 4 Nights",
        "price": 15000,
        "rating": 4.9
    },
    {
        "id": 4,
        "destination": "Kerala",
        "duration": "4 Days / 3 Nights",
        "price": 9000,
        "rating": 4.6
    },
    {
        "id": 5,
        "destination": "Kodaikanal",
        "duration": "2 Days / 1 Night",
        "price": 4500,
        "rating": 4.4
    }
]

# -----------------------------
# Bookings
# -----------------------------
bookings = []

# -----------------------------
# Reviews
# -----------------------------
reviews = []