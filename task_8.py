#Задача
#Поменять местами значение двух переменных.

#В Python множественное присвоение можно использовать,
#если вы хотите поменять значения двух переменных местами.

first_value, second_value = "first_value", "second_value"
print(first_value, second_value)

print("Меняем местами переменные...")
first_value, second_value = second_value, first_value

print(first_value, second_value)