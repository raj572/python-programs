def main():
  student_number = 5
  exam_number = 4
  for i in range(student_number):
    student_name = input(f"Enter the name of student{i+1}: ")
    total_mark = 0
    for j in range(exam_number):
      mark = float(input(f"Enter exam mark {j+1} for {student_name}: "))
      total_mark += mark
    average_mark = total_mark / exam_number
    print(f"The average mark for {student_name} is {average_mark:.1f}")

main()