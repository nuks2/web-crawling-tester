student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),]

sorted = sorted(student_tuples, key=lambda student: student[2], reverse=True)
print(sorted)
# dic = dict(sorted)

student_tuples_2 = [
    ('john', 'A'),
    ('jane', 'B'),
    ('dave', 'B'),]

dic = dict(student_tuples_2)
print(dic)