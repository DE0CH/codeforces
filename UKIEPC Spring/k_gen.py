import random
import sys

seed = sys.argv[1]
random.seed(seed)
len = random.randint(1, 20)
for _ in range(len):
    print(random.choice(['N', 'E', 'S', 'W']), end='')
print()