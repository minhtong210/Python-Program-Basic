import sys

sys.path.append("Course/")
sys.path.append("Student/")
sys.path.append("Lecturer/")

import Course_model as c, Lecturer_model as l, Student_model as s

course1 = c.Course("Beginner 1", 48, "Lớp dành cho học viên mới bắt đầu", "Lê Phương")
course2 = c.Course("Beginner 2", 35, "Lớp dành cho học viên mới bắt đầu", "Cẩm Tú")
course3 = c.Course("Inter 1", 40, "Lớp dành cho học viên có trình độ", "Nguyễn My")
course4 = c.Course("Inter 2", 50, "Lớp dành cho học viên có trình độ", "Unknown")
course5 = c.Course("Advance 1", 48, "Lớp dành cho học viên đi làm", "")
course6 = c.Course("Advance 2", 30, "Lớp dành cho học viên đi làm", "Vi")
course7 = c.Course("Advance 3", 35, "Lớp dành cho học viên đi làm", "")

courses = [course1, course2, course3, course4, course5, course6, course7]

student1 = s.Student("Ngô Minh Tông", 23, ["Đá bóng", "Game", "Gái"], ["Beginner 1", "Inter 2"])
student2 = s.Student("Phan Hữu Toàn", 24, ["Cầu lông", "Gym", "Game", "Gái"], ["Beginner 1", "Inter 1", "Advance 1"])
student3 = s.Student("Lê Quang Đạo", 24, ["Hành Quân", "Gym", "Game", "Gái"], ["Beginner 1", "Inter 2", "Advance 1"])
student4 = s.Student("Nguyễn Đình Nam", 24, ["Check", "Khịa", "Gái"], ["Beginner 1", "Inter 1", "Advance 1"])
student5 = s.Student("Nguyễn Đình Phương", 24, ["Design", "Cafe", "Gái"], ["Beginner 1", "Inter 2", "Advance 2"])
student6 = s.Student("Nguyễn Hữu Thắng", 24, ["Running", "Khịa", "Gái"], ["Beginner 2", "Inter 1", "Advance 1"])

students = [student1, student2, student3, student4, student5, student6]

lecturer1 = l.Lecturer("Lê Phương", ["Beginner 1"], "23/10/2022")
lecturer2 = l.Lecturer("Cẩm Tú", ["Beginner 2"], "13/3/2021")
lecturer3 = l.Lecturer("Nguyễn My", ["Inter 1"], "12/3/2021")
lecturer4 = l.Lecturer("Unknown", ["Inter 2", "Advance 1"], "8/8/2021")
lecturer5 = l.Lecturer("Nhật Vy", ["Advance 2"], "30/10/2021")

lecturers = [lecturer1, lecturer2, lecturer3, lecturer4, lecturer5]

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
