import fbchat
from fbchat import Client
from fbchat.models import *
from getpass import getpass

username = input("Enter your Facebook username: ")
password = getpass("Enter your Facebook password: ")
client = fbchat.Client(username, password)

num_friends = int(input("How many friends do you want to message? "))
for i in range(num_friends):
    name = input("Enter the name of your friend: ")
    friends = client.search_for_users(name)
    if not friends:
        print(f"Could not find a friend with name {name}")
        continue
    friend = friends[0]
    message = input("Enter your message: ")
    sent = client.send(Message(text=message), thread_id=friend.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")
    else:
        print("Failed to send message")

client.logout()
