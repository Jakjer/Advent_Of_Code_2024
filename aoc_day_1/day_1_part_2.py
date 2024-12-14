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

# Calculate similarity score
similarity_score = 0
list_length = len(left_list)
for i in range(0, list_length):
  right_list_instance_count = right_list.count(left_list[i])
  similarity_score += right_list_instance_count * left_list[i]

# Solution
print(similarity_score)