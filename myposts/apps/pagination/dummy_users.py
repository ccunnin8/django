from models import User

email = "another_email@gmail.com"

users  =[
    {
    "first_name": "Sally",
    "last_name": "Smith"
    },
    {
    "first_name": "Sandry",
    "last_name": "Smith",

    },
    {
    "first_name": "Mandy",
    "last_name": "Smith",
    },
    {
    "first_name": "Mindy",
    "last_name": "Smith",
    },
    {
    "first_name": "Bindy",
    "last_name": "Smith"
    },
    {
    "first_name": "Puddin'",
    "last_name": "Smith",
    },
    {
    "first_name": "Plistjaleena",
    "last_name": "Smith",
    },
    {
    "first_name": "Bazakalooma",
    "last_name": "Smith" }
]

for user in users:
    User.objects.create(
    first_name=user["first_name"],
    last_name=user["last_name"],
    email=email
    )

print("DONE")
