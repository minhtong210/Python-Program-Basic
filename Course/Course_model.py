class Course:
	def __init__(self, course_name, quantity, description, lecturer, max_quantity = 10):
		self.course_name = course_name
		self.quantity = quantity
		self.description = description
		self.lecturer = lecturer
		self.max_quantity = max_quantity
		self.rate = 0
		self.pass_list = []


		
	def __repr__(self):
		return f"{self.course_name}		<{self.quantity}/{self.max_quantity}>"

	def course_info(self):
		with open("Course/Course_info.text", "w") as info:
			info.write(f"Khoá học {self.course_name}\n")
			info.write(f"1. Số học viên: {self.quantity}/{self.max_quantity}\n")
			info.write(f"2. Mô tả: {self.description}\n")
			info.write(f"3. Giảng viên đứng lớp: {self.lecturer}\n")
			try: 
				percent = int(self.rate * 100 / self.quantity)
			except ZeroDivisionError:
				percent = 0
			info.write(f"4. Danh sách học viên qua môn ({percent}% qua môn)")
	def append_course_list(self):
		with open("Course/Course_list.text", "r+") as KH_ds:
			KH_ds.seek(0)
			ds = KH_ds.readlines()
			if self.quantity < self.max_quantity:
				KH_ds.write(f"\n{len(ds)}. {self} <Còn trống>")
			else:
				KH_ds.write(f"\n{len(ds)}. {self} <Đã full>")
