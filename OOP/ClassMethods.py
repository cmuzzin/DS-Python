class Youtube:
    def __init__(self, username: str, subscribers = 0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    def subsribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

        

user1 = Youtube("Chris")
user2 = Youtube("Joe")
print(user2.subscriptions)
user1.subsribe(user2)
print(user1.username, user1.subscribers, user1.subscriptions)
print(user2.subscriptions, user2.subscribers)