def listToStr(l, seperator):
	return seperator.join(l)

class Student:
	def __init__(self, full_name, age, habits, courses):
		self.full_name = full_name
		self.courses = courses
		self.age = age
		self.habits = habits

	def __repr__(self):
		habit = listToStr(self.habits, ", ")
		course = listToStr(self.courses, ", ")
		return f"{self.full_name} - {self.age} tuổi - {habit} - {course}"

	def student_info(self):
		with open("Student/Student_info.text", "w") as HV_chitiet:
			HV_chitiet.write(f"Các khoá học viên {self.full_name} đang tham gia\n")
			for num in range(len(self.courses)):
				HV_chitiet.write(f"{num + 1}. {self.courses[num]}\n")
			HV_chitiet.write(f"{len(self.courses) + 1}. Lựa chọn tham gia thêm khoá học\n")
			
	def append_student_list(self):
		with open("Student/Student_list.text", "r+") as l:
			l.seek(0)
			ds = l.readlines()
			l.write(f"\n{len(ds)}. {self}")