import sys

sys.path.append("Course/")
sys.path.append("Student/")
sys.path.append("Lecturer/")

import Course_model, Lecturer_model, Student_model

courses = []
students = []
lecturers = []

def start():
	update_course()
	update_student()
	update_lecturer()

def update_course():
	with open("Course/Course_list.text", "w") as ds:
		ds.seek(0)
		ds.write("Các Khoá Học  (Sử dụng 'back' để quay lại)")
	for course in courses:
		course.append_course_list()

def update_student():
	with open("Student/Student_list.text", "w") as ds:
		ds.seek(0)
		ds.write("Danh Sách Học Viên: (Sử dụng 'back' để quay lại)")
	for student in students:
		student.append_student_list()

def update_lecturer():
	with open("Lecturer/Lecturer_list.text", "w") as ds:
		ds.seek(0)
		ds.write("Danh Sách Giảng Viên: (Sử dụng 'back' để quay lại)")
	for lecturer in lecturers:
		lecturer.append_lecturer_list()

def update_student_pass(count = 0, n = ""):
	with open("Course/Course_pass_list.text", "w") as ds:
		ds.seek(0)
		ds.write("Các học viên đã pass qua khoá học:\n")
		for s in students:
			for c in s.courses:
				if c.course_name == n:
					if c.grade != "Ở lại lớp":
						ds.write(f"{count + 1}. {s.full_name} - Toán: {c.math}, Văn: {c.literature}, Anh: {c.eng} - {c.grade}\n")
						count += 1
	return count

def update_student_result(num):
	count = 1
	with open("Student/Student_info_results.text", "w") as ds:
		ds.seek(0)
		ds.write("Kết quả điểm của học viên qua các khoá học:\n")
		for c in students[num].courses:
			ds.write(f"{count}. {c.get_point()}\n")
			count += 1
