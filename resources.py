import model

course1 = model.Course("Beginner 1", 48, "Lớp dành cho học viên mới bắt đầu", "Lê Phương")
course2 = model.Course("Beginner 2", 35, "Lớp dành cho học viên mới bắt đầu", "Cẩm Tú")
course3 = model.Course("Inter 1", 40, "Lớp dành cho học viên có trình độ", "Nguyễn My")
course4 = model.Course("Inter 2", 50, "Lớp dành cho học viên có trình độ", "Unknown")
course5 = model.Course("Advance 1", 48, "Lớp dành cho học viên đi làm", "")
course6 = model.Course("Advance 2", 30, "Lớp dành cho học viên đi làm", "Vi")
course7 = model.Course("Advance 3", 35, "Lớp dành cho học viên đi làm", "")

courses = [course1, course2, course3, course4, course5, course6, course7]

student1 = model.Student("Ngô Minh Tông", 23, ["Đá bóng", "Game", "Gái"], ["Beginner 1", "Inter 2"])
student2 = model.Student("Phan Hữu Toàn", 24, ["Cầu lông", "Gym", "Game", "Gái"], ["Beginner 1", "Inter 1", "Advance 1"])
student3 = model.Student("Lê Quang Đạo", 24, ["Hành Quân", "Gym", "Game", "Gái"], ["Beginner 1", "Inter 2", "Advance 1"])
student4 = model.Student("Nguyễn Đình Nam", 24, ["Check", "Khịa", "Gái"], ["Beginner 1", "Inter 1", "Advance 1"])
student5 = model.Student("Nguyễn Đình Phương", 24, ["Design", "Cafe", "Gái"], ["Beginner 1", "Inter 2", "Advance 2"])
student6 = model.Student("Nguyễn Hữu Thắng", 24, ["Running", "Khịa", "Gái"], ["Beginner 2", "Inter 1", "Advance 1"])

students = [student1, student2, student3, student4, student5, student6]

lecturer1 = model.Lecturer("Lê Phương", ["Beginner 1"], "23/10/2022")
lecturer2 = model.Lecturer("Cẩm Tú", ["Beginner 2"], "13/3/2021")
lecturer3 = model.Lecturer("Nguyễn My", ["Inter 1"], "12/3/2021")
lecturer4 = model.Lecturer("Unknown", ["Inter 2", "Advance 1"], "8/8/2021")
lecturer5 = model.Lecturer("Nhật Vy", ["Advance 2"], "30/10/2021")

lecturers = [lecturer1, lecturer2, lecturer3, lecturer4, lecturer5]

def start():
	update_KH()
	update_HV()
	update_GV()

def update_KH():
	with open("KH_ds.text", "w") as ds:
		ds.seek(0)
		ds.write("Các Khoá Học  (Sử dụng 'back' để quay lại)")
	for course in courses:
		course.append_listKH()

def update_HV():
	with open("HV_ds.text", "w") as ds:
		ds.seek(0)
		ds.write("Danh Sách Học Viên: (Sử dụng 'back' để quay lại)")
	for student in students:
		student.append_listHV()

def update_GV():
	with open("GV_ds.text", "w") as ds:
		ds.seek(0)
		ds.write("Danh Sách Giảng Viên: (Sử dụng 'back' để quay lại)")
	for lecturer in lecturers:
		lecturer.append_listGV()
