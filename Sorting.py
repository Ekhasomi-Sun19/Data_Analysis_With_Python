import pandas as pd
import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('userInterests.json', 'r') as file:
    data = json.load(file)

# Extract user interests
user_interests = [user['userInterests'] for user in data]

# Create a DataFrame from user interests
df = pd.DataFrame(user_interests)

# Set the order of columns
column_order = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
df = df[column_order]

# Save the DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Plot the DataFrame
df.plot()
plt.show()
