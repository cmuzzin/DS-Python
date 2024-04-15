# class StarCookie:
#     def __init__(self, color: str, weight: int) -> None:
#         print("The cookie is ready...")
#         self.color = color
#         self.weight = weight
 
# star_cookie1 = StarCookie("Red", 15)
# print(star_cookie1.color, star_cookie1.weight)


class Youtube:
    def __init__(self, username: str, subscribers = 0):
        self.username = username
        self.subscribers = subscribers

user1 = Youtube("Chris")
print(user1.username, user1.subscribers)

user2 = Youtube("Jon")
user2.subscribers = 5
print(user2.subscribers)