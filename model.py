import method

class Person:
	def __init__(self, full_name, courses):
		self.full_name = full_name
		self.courses = courses

class Lecturer(Person):
	def __init__(self, full_name, courses, valid):
		super().__init__(full_name, courses)
		self.valid = valid

	def __repr__(self):
		course = method.listToStr(self.courses, ", ")
		return f"{self.full_name} - {course} - {self.valid}"

	def chitietGV(self):
		with open("GV_chitiet.text", "w") as GV_chitiet:
			GV_chitiet.write(f"Giảng Viên {self.full_name}\n")
			GV_chitiet.write(f"1. Full Name: {self.full_name}\n")
			course = method.listToStr(self.courses, ", ")
			GV_chitiet.write(f"2. Khoá học đang giảng dạy: {course}\n")
			GV_chitiet.write(f"3. Thời hạn hợp đồng: {self.valid}")

	def chitietGV_KH(self):
		with open("GV_chitiet_KH.text", "w") as KH:
			KH.write(f"Các khoá học giảng viên đang giảng dạy:\n")
			for num in range(len(self.courses)):
				KH.write(f"{num + 1}. {self.courses[num]}\n")
			KH.write(f"{len(self.courses) + 1}. Lựa chọn tham gia giảng dạy khoá học còn trống\n")

	def append_listGV(self):
		with open("GV_ds.text", "r+") as GV_ds:
			GV_ds.seek(0)
			ds = GV_ds.readlines()
			GV_ds.write(f"\n{len(ds)}. {self}")

class Student(Person):
	def __init__(self, full_name, age, habits, courses):
		super().__init__(full_name, courses)
		self.age = age
		self.habits = habits

	def __repr__(self):
		habit = method.listToStr(self.habits, ", ")
		course = method.listToStr(self.courses, ", ")
		return f"{self.full_name} - {self.age} tuổi - {habit} - {course}"

	def chitietHV(self):
		with open("HV_chitiet.text", "w") as HV_chitiet:
			HV_chitiet.write(f"Các khoá học viên {self.full_name} đang tham gia\n")
			for num in range(len(self.courses)):
				HV_chitiet.write(f"{num + 1}. {self.courses[num]}\n")
			HV_chitiet.write(f"{len(self.courses) + 1}. Lựa chọn tham gia thêm khoá học\n")
			
	def append_listHV(self):
		with open("HV_ds.text", "r+") as HV_ds:
			HV_ds.seek(0)
			ds = HV_ds.readlines()
			HV_ds.write(f"\n{len(ds)}. {self}")

class Course:
	def __init__(self, course_name, quantity, description, lecturer):
		self.course_name = course_name
		self.quantity = quantity
		self.description = description
		self.lecturer = lecturer
		
	def __repr__(self):
		return f"{self.course_name}		<{self.quantity}/50>"

	def chitietKH(self):
		with open("KH_chitiet.text", "w") as KH_chitiet:
			KH_chitiet.write(f"Khoá học {self.course_name}\n")
			KH_chitiet.write(f"1. Số học viên: {self.quantity}/50\n")
			KH_chitiet.write(f"2. Mô tả: {self.description}\n")
			KH_chitiet.write(f"3. Giảng viên đứng lớp: {self.lecturer}")

	def append_listKH(self):
		with open("KH_ds.text", "r+") as KH_ds:
			KH_ds.seek(0)
			ds = KH_ds.readlines()
			if self.quantity < 50:
				KH_ds.write(f"\n{len(ds)}. {self} <Còn trống>")
			else:
				KH_ds.write(f"\n{len(ds)}. {self} <Đã full>")

	def update_listKH(self):
		with open("KH_ds.text", "w") as KH_ds:
			KH_ds.write("")
		append_listKH()