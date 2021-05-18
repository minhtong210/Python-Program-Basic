def listToStr(l, seperator):
	return seperator.join(l)

class Lecturer:
	def __init__(self, full_name, courses, valid):
		self.full_name = full_name
		self.courses = courses
		self.valid = valid

	def __repr__(self):
		course = listToStr(self.courses, ", ")
		return f"{self.full_name} - {course} - {self.valid}"

	def lecturer_info(self):
		with open("Lecturer/Lecturer_info.text", "w") as info:
			info.write(f"Giảng Viên {self.full_name}\n")
			info.write(f"1. Full Name: {self.full_name}\n")
			course = listToStr(self.courses, ", ")
			info.write(f"2. Khoá học đang giảng dạy: {course}\n")
			info.write(f"3. Thời hạn hợp đồng: {self.valid}")

	def lecturer_course_info(self):
		with open("Lecturer/Lecturer_course_info.text", "w") as KH:
			KH.write(f"Các khoá học giảng viên đang giảng dạy:\n")
			for num in range(len(self.courses)):
				KH.write(f"{num + 1}. {self.courses[num]}\n")
			KH.write(f"{len(self.courses) + 1}. Lựa chọn tham gia giảng dạy khoá học còn trống\n")

	def append_lecturer_list(self):
		with open("Lecturer/Lecturer_list.text", "r+") as l:
			l.seek(0)
			ds = l.readlines()
			l.write(f"\n{len(ds)}. {self}")
