

with open('game_stat.txt') as file:
    lines = []
    for line in file:
        lines.append(line.rstrip().split("/n"))
    for i in lines:


print(lines)
