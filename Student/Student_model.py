from statistics import mean

def listToStr(l, seperator):
	return seperator.join(l)

def grade(avg):
	if avg > 8 or avg == 8:
		return "Giỏi"
	if avg > 6.5 or avg == 6.5:
		return "Khá"
	if avg > 5 or avg == 5:
		return "Trung Bình"
	else:
		return "Ở lại lớp"

class Student:
	def __init__(self, full_name, age, habits, courses):
		self.full_name = full_name
		self.courses = courses
		self.age = age
		self.habits = habits

	def __repr__(self):
		habit = listToStr(self.habits, ", ")
		course = listToStr([c.course_name for c in self.courses], ", ")
		return f"{self.full_name} - {self.age} tuổi - {habit} - {course}"

	def student_info(self):
		with open("Student/Student_info.text", "w") as info:
			info.write(f"Học Viên {self.full_name}\n")
			info.write(f"1. Full Name: {self.full_name}\n")
			info.write(f"2. Tuổi: {self.age}\n")
			habit = listToStr(self.habits, ", ")
			info.write(f"3. Sở thích: {habit}\n")
			course = listToStr([c.course_name for c in self.courses], ", ")
			info.write(f"4. Khoá học đang tham gia: {course}\n")
			info.write(f"5. Điểm của học viên")

	def student_cls_change(self):
		with open("Student/Student_cls_change.text", "w") as HV_chitiet:
			HV_chitiet.write(f"Các khoá học viên {self.full_name} đang tham gia\n")
			for num in range(len(self.courses)):
				HV_chitiet.write(f"{num + 1}. {self.courses[num]}\n")
			HV_chitiet.write(f"{len(self.courses) + 1}. Lựa chọn tham gia thêm khoá học\n")
			
	def append_student_list(self):
		with open("Student/Student_list.text", "r+") as l:
			l.seek(0)
			ds = l.readlines()
			l.write(f"\n{len(ds)}. {self}")

class Stu_Course:
	def __init__(self, course_name, math = "0", literature = "0", eng = "0"):
		self.course_name = course_name
		self.math = math
		self.literature = literature
		self.eng = eng
		self.avg = round(mean([float(math),float(literature),float(eng)]), 1)
		self.grade = grade(self.avg)

	def __repr__(self):
		return f"{self.course_name}"

	def get_point(self):
		return f"{self.course_name} - Toán: {self.math}, Văn: {self.literature}, Anh: {self.eng} - {self.grade}"	
