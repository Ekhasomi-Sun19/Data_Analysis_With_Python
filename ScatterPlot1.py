import json
import matplotlib.pyplot as plt

# Load data from json file
with open('users.json') as file:
    users = json.load(file)

#Initialize list to store usernames and user interests
usernames = []
user_interests = []

#Extract usernames and user interests from the data
for user in users:
    username = user['userName']
    interests = user['userInterests']
    usernames.append(username)
    user_interests.append(interests)


#Create a figure and axes for the plot
fig, ax = plt.subplots()

#Generate x-axis values using the range of usernames
x = range(len(usernames))

#Define a dictionary to map questions to colors 
questions_colors = {
    'q1': 'red',
    'q2': 'blue',
    'q3': 'green',
    'q4': 'orange',
    'q5': 'purple',
    'q6': 'brown',
    'q7': 'pink',
    'q8': 'gray',
    'q9': 'olive',
    'q10': 'cyan'

}

# Plot scatter points for each user's interests
for i, interest in enumerate(user_interests):
    #Extract the questions from interests
    x_values = list(interest.keys()) 

    #Extract the interest levels
    y_values = list(interest.values()) 

    # Assign colors based on questions
    color = [questions_colors[q] for q in x_values] 

    # Plot scatter point
    ax.scatter([x[i]] * len(x_values), y_values, c=color) 

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(usernames, rotation=45)

#Set x-axis label, y-axis label, and plot title
ax.set_xlabel('User')
ax.set_ylabel('Interest Level')
ax.set_title('User Interests')

# Create custom legend for the questions and colors
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label=q, markerfacecolor=questions_colors[q])
    for q in questions_colors
]

ax.legend(handles=legend_elements, title='Questions')

#Adjust the layout and display the plot
plt.tight_layout()
plt.show()