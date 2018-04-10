from apps.users.models import User, UserManager

password="123456789"
birthday="04/01/1990"
email="@gmail.com"
users = [
    {
        "name": "Corey Cunningham",
        "alias": "Corey",
    },
    {
        "name": "Fred Barnes",
        "alias": "Fred",
    },
    {
        "name": "Julie Sanders",
        "alias": "Jules"
    },
    {
        "name": "Alice Wonderful",
        "alias": "Alice"
    },
    {
        "name": "Dawn Superfield",
        "alias": "Dawn"
    },
    {
        "name": "Robert Downy",
        "alias": "Bob"
    }
]

for user in users:
    user["email"] = user["name"] + "email"
    user["password"] = password
    user["birthday"] = birthday
    User.objects.create(user)

print("DONE")
