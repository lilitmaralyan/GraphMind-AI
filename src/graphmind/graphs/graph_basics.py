VERSION = 0

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': [],
    'E': []
}

question_1 = input("Which key do you want to see the cites for? ")
if question_1 in graph.keys():
    print(f"{question_1} cites to {graph[question_1]}")
else:
    print("Key not found")

question_2 = input("Which key do you want to see who cites it? ")
keys_list = []
for keys in graph.keys():
    if question_2 in graph[keys]:
        keys_list.append(keys)
print(f"{question_2} is cited by {keys_list}")

question_3 = input("Which key do you want to count the outgoing and incoming cites for? ")
print(f"{question_3} has {len(graph[question_3])} outgoing cites")
count = 0
for i in graph.values():
    if question_3 in i:
        count += 1
print(f"{question_3} has {count} incoming cites")

print("Which paper is cited the most? ")
count = 0
max_count = 0
for i in graph.keys():
    for j in graph.values():
        if i in j:
            count += 1
    if count > max_count:
        max_count = count
        max_count_key = i
        count = 0
    else:
        count = 0
print(f"{max_count_key} has {max_count} cites")

