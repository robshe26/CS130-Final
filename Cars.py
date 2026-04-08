import csv

total_city_mpg = 0
total_cars = 0

with open('cars (1).csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  


    for row in reader:
        city_mpg_str = row[8]
        
        city_mpg = float(city_mpg_str)

        total_city_mpg += city_mpg
        total_cars += 1

    average_city_mpg = total_city_mpg / total_cars

    print("Average City MPG:", round(average_city_mpg, 2))
  
