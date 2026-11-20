#Задача
# Сколько полных дней и часов в 5000 часах?
hours_in_day = 24
total_hours = 5000

days = total_hours // hours_in_day
hours = total_hours % hours_in_day

print("количество полных дней =", days)
print("количество частов =", hours)