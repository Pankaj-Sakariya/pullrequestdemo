import json

# Step 3: Read demo.json file
with open('demo.json') as file:
    data = json.load(file)

# Step 5: Print out values
for item in data:
    for key, value in item.items():
        print(value)
