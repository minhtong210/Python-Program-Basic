import method, time, resources, datetime

def main_option(file_name, kind, option):
	with open(f"{file_name}") as danhsach:
		ds = danhsach.readlines()

	def option_case(func):
		while True:
			method.read(f"{file_name}")
			num_pick = input(f"Nhập vào {kind} muốn chọn: ")
			method.cross()
			# Quay lại
			if num_pick == "back": 
				break
			# Thông tin chi tiết
			if num_pick in method.str_range(ds):
			# FUNCTION CHI TIẾT
				func(int(num_pick))
			else:
				method.option_error()

	if option == 1: option_case(KH_chitiet)
	elif option == 2: option_case(HV_chitiet)
	else: option_case(GV_chitiet)
			
def KH_chitiet(num):
	while True:
		course = resources.courses[num - 1]
		course.chitietKH()
		method.read("KH_chitiet.text")

		num_pick = input(f"Nhập vào số thông tin muốn chỉnh sửa: ")
		method.cross()
		
		# Không thể chỉnh sửa số học viên
		if num_pick == "1":
			print("Bạn không thể chỉnh sửa mục số Học Viên")
		# Chỉnh sửa mô tả
		elif num_pick == "2":
			replace_text = input("Bạn muốn chỉnh sửa thành: ")
			method.input_condition(replace_text)
			course.description = replace_text
			method.success("Chỉnh sửa thành công")

		# Chỉnh sửa Giảng viên
		elif num_pick == "3":
			print("Bạn không thể chỉnh sửa mục giảng viên tại đây, vui lòng sang option 3 !")

		# Quay lại
		elif num_pick == "back": 
			break
		else: 
			method.option_error()
	

def HV_chitiet(num):
	while True:
		student = resources.students[num - 1]
		student.chitietHV()
		KH_total = len(student.courses)
		method.read("HV_chitiet.text")

		num_pick = input("Nhập vào khoá học muốn thoát / lựa chọn tham gia: ")
		method.cross()

		# Cho trường hợp học sinh không có khoá học nhưng bấm 0

		# Lựa chọn tham gia khoá học
		if num_pick == str(KH_total + 1):
			# Nếu có 3 khoá học
			if KH_total == 3:
				print("Học viên không thể tham gia quá 3 khoá học")
			# Ít hơn 3 khoá
			else:
				method.read("KH_ds.text")
				pick = input("Nhập vào khoá học bạn muốn tham gia: ")
				method.cross()

				if pick in method.str_range_inclue(resources.courses): #Có vấn đề
					course_pick = resources.courses[int(pick) - 1]
					# Trường hợp KH full
					if course_pick.quantity == 50:
						print("Khoá học đã full, không thể tham gia")
					# Trường hợp KH có thể tham gia
					elif course_pick.quantity < 50:
						# Trường hợp trùng KH
						if course_pick.course_name in student.courses:
							print("Khoá học này học viên đã tham gia, không thể tham gia trùng 1 lớp")
						# Trường hợp không trùng
						else:
							# Update học viên tham gia khoá học
							student.courses.insert(int(pick) - 1 ,course_pick.course_name)
							resources.update_HV()
							# Update khoá học
							course_pick.quantity += 1
							resources.update_KH()
							method.success("Đã tham gia thành công")

				elif pick == "back":
					pass
				else:
					method.option_error()		
						
		# Lựa chọn huỷ lớp
		elif num_pick in method.str_range_inclue(student.courses):
			course_pick = student.courses[int(num_pick) - 1]

			# Update khoá học
			for c in resources.courses:
				if c.course_name == course_pick:
					c.quantity -= 1
			resources.update_KH()

			# Update học viên huỷ khoá học
			student.courses.pop(int(num_pick) - 1)
			resources.update_HV()
			method.success("Đã huỷ thành công") 
			
		# Quay lại
		elif num_pick == "back": 
			break
		else:
			method.option_error()


def GV_chitiet(num):
	while True:
		lecturer = resources.lecturers[num - 1]
		lecturer.chitietGV()
		lecturer.chitietGV_KH()
		resources.update_GV()
		method.read("GV_chitiet.text")

		num_pick = input("Nhập vào thông tin giảng viên muốn chỉnh sửa: ")
		method.cross()

		# Chỉnh sửa tên giảng viên
		if num_pick == "1":
			replace_text = input("Bạn muốn chỉnh sửa thành: ")
			if method.input_condition(replace_text, False):
				for c in resources.courses:
					if c.lecturer == lecturer.full_name:
						c.lecturer = replace_text
				lecturer.full_name = replace_text
				resources.update_KH()
				method.success("Chỉnh sửa thành công")
		
		# Chỉnh sửa khoá học đang giảng dạy
		elif num_pick == "2":
			while True:
				# List ra các khoá học
				lecturer.chitietGV_KH()
				method.read("GV_chitiet_KH.text")
				pick = input("Nhập vào khoá học muốn huỷ dạy / lựa chọn tham gia: ")
				method.cross()

				# Lựa chọn tham gia khoá học còn trống
				if pick == str(len(lecturer.courses) + 1):
					
					# Xét điều kiện đăng ký với thời hạn hợp đồng
					valid_date = datetime.datetime.strptime(lecturer.valid, '%d/%m/%Y')
					today = datetime.datetime.today()
					if valid_date > today:
						method.read("KH_ds.text")
						pick_KH = input("Nhập vào khoá học bạn muốn tham gia giảng dạy: ")

						# Nếu đủ điều kiện
						if pick_KH in method.str_range_inclue(resources.courses):
							course_pick = resources.courses[int(pick_KH) - 1]
							method.cross()
							
							# Nếu lớp còn trống
							if course_pick.lecturer == "":
								course_pick.lecturer = lecturer.full_name
								lecturer.courses.insert(int(pick_KH) - 1, course_pick.course_name)
								method.success("Đã tham gia thành công")
								
							# Nếu lớp đã có giảng viên
							else:
								print("Bạn không thể giảng dạy khoá học đã có giảng viên, vui lòng xem khoá học tại option 1")
						
						# Quay lại
						elif num_pick == "back": 
							break
						else:						
							method.option_error()
					else:
						print("Bạn không thể giảng dạy khoá học vì đã hết thời hạn hợp đồng")

				# Lựa chọn huỷ dạy khoá học
				elif pick in method.str_range_inclue(lecturer.courses):
					course_pick = lecturer.courses[int(pick) - 1]

					# Update khoá học
					for c in resources.courses:
						if c.course_name == course_pick:
							c.lecturer = ""
					resources.update_KH()

					# Update giảng viên dạy khoá học
					lecturer.courses.pop(int(pick) - 1)
					lecturer.chitietGV_KH()
					resources.update_GV()

					method.success("Đã huỷ thành công")

				# Quay lại
				elif pick == "back": 
					break
				else:
					method.option_error()
		
		# Chỉnh sửa thời hạn hợp đồng
		elif num_pick == "3":
			print("Vui lòng nhập ngày tháng năm theo thứ tự !")
			day = input("Ngày (2 chữ số): ")
			month = input("Tháng (2 chữ số): ")
			year = input("Năm (4 chữ số và 2020 < năm < 2100): ")
			method.cross()
			
			d = int(day)
			m = int(month)
			
			l = method.listToStr([day,month,year], "")

			# Check ngày tháng năm
			if method.date_condition1(day, month, year) and method.date_condition2(d, m) and method.input_condition(l , True, False):
				# Cập nhật thời hạn hợp đồng
				l = method.listToStr([day,month,year], "/")
				lecturer.valid = l
				resources.update_GV()
				method.success("Chỉnh sửa thành công")
			else:
				print("Vui lòng nhập lại ngày tháng năm đúng theo lịch và chỉ có số")

		# Quay lại		
		elif num_pick == "back": 
			break
		else:
			method.option_error()

