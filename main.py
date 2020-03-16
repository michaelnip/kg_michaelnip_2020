# Helper function
def tallyChars(s):
  tally = []
  mapping = {}
  for char in s:
    if mapping.get(char) == None:
      tally.append(1)
      mapping[char] = len(tally) - 1
    else:
      tally[mapping[char]] += 1
  tally.sort(reverse=True)
  return tally

# Retrieve string arguments
import sys
if len(sys.argv) != 3:
  print('Error: Invalid number of arguments provided')
  exit(-1)
s1 = sys.argv[1]
s2 = sys.argv[2]

# Check edge case
if len(s1) > len(s2):
  print('false')
  exit(0)

# Determine and print answer
t1 = tallyChars(s1)
t2 = tallyChars(s2)
remaining = 0
for i in range(len(t1)):
  if i < len(t2):
    if t2[i] < t1[i]:
      print('false')
      exit(0)
    remaining += t2[i] - t1[i]
  else:
    if remaining < t1[i] or t1[i] > 1:
      print('false')
      exit(0)
    remaining -= t1[i]
print('true')
