first_names = set()

first_names.add("Jan")
first_names.add("Magdaleniusz")
first_names.add("Kacper")
first_names.add("Katarzyna")
first_names.add("Kacper")
first_names.add("Katarzyna")
first_names.add("Magdaleniusz")

print(first_names)

team_a = {"Jan", "Magdaleniusz", "Kacper", "Katarzyna", "Janina"}
team_b = {"Paweł", "Magdaleniusz", "Karol", "Katarzyna", "Janina", "Krzysztof", "Karolina"}

print('SUM', team_a | team_b)
print('DIFFERENCE A - B', team_a - team_b)
print('DIFFERENCE B - A', team_b - team_a)
print('INTERSECTION', team_a & team_b)
print('SYMMETRIC DIFFERENCE', team_a ^ team_b)