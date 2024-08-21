# Step 1: Create a list of Olympic events
olympic_events = ['100m Sprint', 'Long Jump', 'High Jump', 'Marathon', 'Swimming']

# Step 2: Create a list of new events
new_events = ['Surfing', 'Skateboarding', 'Climbing', 'Basketball 3x3']

# Step 3: Attach the list of new events to the original list
olympic_events.extend(new_events)

# Step 4: Print the final list
print(olympic_events)
