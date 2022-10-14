nylon_quantity = int(input())
paint_quantity = int(input())
diluent_quantity = int(input())
workers_hours = int(input())
sum_bags = 0.4
sum_nylon = (nylon_quantity + 2) * 1.5
sum_paint = (paint_quantity + (paint_quantity * 10 / 100)) * 14.5
sum_diluent = diluent_quantity * 5

sum_materials = sum_nylon + sum_paint + sum_diluent + sum_bags
sum_workers = (0.3 * sum_materials) * workers_hours
expences = sum_materials + sum_workers
print(expences)
