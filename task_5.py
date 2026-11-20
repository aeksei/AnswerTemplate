#Задача. Раздеделить список учеников на две половины.
list_players = ["Alex", "Maria", "Kate", "William", "Ivan"]
middle_index = len(list_players) // 2

left_team = list_players[:middle_index]
right_team = list_players[middle_index:]

print(left_team)
print(right_team)