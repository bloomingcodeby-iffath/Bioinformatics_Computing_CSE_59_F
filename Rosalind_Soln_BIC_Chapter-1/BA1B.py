text = input().strip()
k = int(input())

count = {}

for i in range(len(text) - k + 1):
    pattern = text[i:i+k]
    count[pattern] = count.get(pattern, 0) + 1

maximum = max(count.values())

for pattern in count:
    if count[pattern] == maximum:
        print(pattern, end=" ")