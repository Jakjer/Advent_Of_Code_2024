# Read Files
with open('day_1_input.txt') as file:
  lines = file.readlines()

left_list = []
right_list = []

# Split input, sort arrays
for line in lines:  
  left_list.append(int(line.split()[0]))
  right_list.append(int(line.split()[1]))

left_list.sort()
right_list.sort()

# Calculate answers
total_distance = 0
for i in range(0, len(left_list)):
  total_distance += abs(left_list[i] - right_list[i])
  
# Solution
print(total_distance)