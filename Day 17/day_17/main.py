# Defines a new class using the class keyword
class User:

    # Defines the init function that is called each time a new object is created
    def __init__(self, user_id, username):
        # The attribute id is initialized with the value of the parameter user_id
        self.id = user_id

        # The attribute username is initialized with the value of the parameter username
        self.username = username

        # The attribute followers is initialized to 0
        self.followers = 0

        # The attribute following is initialized to 0
        self.following = 0

    # Defines the method follow
    def follow(self, user):
        """Refresh followers counts when a user follow another user"""

        # Increments by 1 the followers attribute for the followed user
        user.followers += 1

        # Increments by 1 the following attribute for the following user
        self.following += 1


# It is possible to add attributes to an object even if they were not declared in the class' init function
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Bob"

# print(user_1.username)

# Creates two new User objects
user_1 = User("001", "Bob")
user_2 = User("002", "Jake")

# Uses the method follow with user_1
user_1.follow(user_2)

# Prints followers and following attributes for both users
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
