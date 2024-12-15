# Read Files, strip newline
with open('d2Input.txt') as file:
  reports = file.read().strip().split('\n')
  
safeCount = 0
reportList = []
for report in reports:

  listAsInt = list(map(int, report.split()))
  listLength = len(listAsInt) - 1

  safeValues = 0
  ascending = 0
  descending = 0
  for i in range(0, listLength):
    valueDifference = abs(listAsInt[i + 1] - listAsInt[i])
    if(listAsInt[i] < listAsInt[i+1]):
      descending += 1
    else:
      ascending += 1
    
    if(valueDifference <= 3 and valueDifference >=1):
      safeValues += 1

  if (ascending == 0 or descending == 0) and safeValues == listLength:
    safeCount += 1

print("Safe # of Reports: ", safeCount)