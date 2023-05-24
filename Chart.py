import json
import matplotlib.pyplot as plt


with open('users.json') as file:
    users = json.load(file)


usernames = []
user_interests = []


for user in users:
    username = user['userName']
    interests = user['userInterests']
    usernames.append(username)
    user_interests.append(interests)

fig, ax = plt.subplots()
x = range(len(usernames))


for i, interest in enumerate(user_interests):
    ax.bar(x[i], interest.values())

ax.set_xticks(x)
ax.set_xticklabels(usernames, rotation = 45)
ax.set_xlabel('User')
ax.set_ylabel('Interest Level')
ax.set_title('User Interests')

plt.tight_layout()
plt.show()