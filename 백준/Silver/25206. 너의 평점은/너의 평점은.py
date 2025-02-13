import sys
input = sys.stdin.readline
total_credit, total_grade = 0, 0
dic_grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for i in range(20):
    lecture, credit, grade = input().strip().split()
    if (grade == 'P'):
        continue
    total_credit += float(credit)
    total_grade += dic_grade.get(grade) * float(credit)
print(total_grade/total_credit)