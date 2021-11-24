import csv


students_list = [["Roll no.", "Name"],
             [1, "Ram Khanal"],
             [2, "Hari Phuyal"],
             [3, "Arjun Shrestha"],
             [4, "Saurav Sharma"],
             [5, "Kushal Adhikari"],
             [6, "Bikash Shrestha"],
             [7, "Saugat Phuyal"],
             [8, "Rupesh Khanal"],
             [9, "Ujjwal Acharya"],
             [10, "Sushant Shrestha"],
             [11, "Dorna Kc"],
             [12, "Bishal Oli"],
             [13, "Aashish Shrestha"],
             [14, "Sunil Bhujel"],
             [15, "Sugam Baskota"]]
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students_list)


science_list = [["Roll no.", "Science"],
             [1, 44],
             [2, 55],
             [3, 87],
             [4, 41],
             [5, 67],
             [6, 55],
             [7, 64],
             [8, 71],
             [9, 70],
             [10, 64],
             [11, 43],
             [12, 67],
             [13, 57],
             [14, 79],
             [15, 81]]
with open('science.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(science_list)


math_list = [["Roll no.", "Math"],
             [1, 90],
             [2, 65],
             [3, 77],
             [4, 87],
             [5, 95],
             [6, 98],
             [7, 55],
             [8, 67],
             [9, 71],
             [10, 65],
             [11, 60],
             [12, 87],
             [13, 70],
             [14, 55],
             [15, 79]]
with open('math.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(math_list)


nepali_list = [["Roll no.", "Nepali"],
             [1, 79],
             [2, 55],
             [3, 70],
             [4, 55],
             [5, 60],
             [6, 65],
             [7, 71],
             [8, 59],
             [9, 38],
             [10, 44],
             [11, 75],
             [12, 69],
             [13, 57],
             [14, 75],
             [15, 71]]
with open('nepali.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(nepali_list)


english_list = [["Roll no.", "English"],
             [1, 44],
             [2, 57],
             [3, 35],
             [4, 53],
             [5, 66],
             [6, 72],
             [7, 35],
             [8, 58],
             [9, 47],
             [10, 47],
             [11, 53],
             [12, 69],
             [13, 71],
             [14, 69],
             [15, 83]]
with open('english.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(english_list)