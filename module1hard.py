grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
num_of_std = len(students)
average_score = {students[0]:sum(grades[0])/len(grades[0])}
for i in range(1,num_of_std):
    average_score.update({students[i]:sum(grades[i])/len(grades[i])})
print(average_score)
