from operator import itemgetter


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted_list = sorted(student_tuples, key=lambda student: student[2], reverse=True)
print(sorted_list)
# dic = dict(sorted_list)

print(sorted(student_tuples, key=itemgetter(0)))

student_tuples_2 = [
    ('john', 'A'),
    ('jane', 'B'),
    ('dave', 'B'),]

dic = dict(student_tuples_2)
print(dic)


