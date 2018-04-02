from models import User

email = "another_email@gmail.com"

users  =[
    {
    "first_name": "Maria",
    "last_name": "Sanchez"
    },
    {
    "first_name": "Julia",
    "last_name": "Sanchez",

    },
    {
    "first_name": "Cristian",
    "last_name": "Sanchez",
    },
    {
    "first_name": "Raul",
    "last_name": "Sanchez",
    },
    {
    "first_name": "Mariana",
    "last_name": "Sanchez"
    },
    {
    "first_name": "Maria'",
    "last_name": "Gomez",
    },
    {
    "first_name": "Julia",
    "last_name": "Gomez",
    },
    {
    "first_name": "Brayden",
    "last_name": "Jackson" }
]

for user in users:
    User.objects.create(
    first_name=user["first_name"],
    last_name=user["last_name"],
    email=email
    )

print("DONE")
