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
for i in range(0, len(left_list)):
  similarity_score += right_list.count(left_list[i]) * left_list[i]

# Solution
print(similarity_score)