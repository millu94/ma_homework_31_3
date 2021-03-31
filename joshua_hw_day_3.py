#Given a list of users, create a function to find the user with a user_id of 4.


users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

def find_user_ID(list, user_id):
    for user in list:
        if user["user_id"] == user_id:
            return user

    return "Not found"

print(find_user_ID(users, 4))
    