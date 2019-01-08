nums = []
n = int(input("How many numbers you want to input? "))

for i in range(n):
    nums.append(int(input(">")))

print("Max: %d\nMin: %d" % (max(nums), min(nums)))

