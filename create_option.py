import method, resources, model

def student():
	while True:
		choice = input("Bạn có chắc tạo học viên mới (y/n)? ")
		method.cross()
		if choice == "n":
			break
		elif choice == "y":
			print("Vui lòng nhập thông tin đăng ký theo thứ tự tên, tuổi và sở thích")
			method.cross()
			while True:		
				print("Tên của học viên phải có đầy đủ họ và tên và không chứa số !")
				name = input("Họ và tên của học viên: ")
				method.cross()
				print("Tuổi của học viên phải là số !")
				age = input("Tuổi hiện tại của học viên: ")
				method.cross()
				print("Sở thích của học viên ngăn cách nhau giữa giấu phẩy và không chứa số !")
				print("Lưu ý: Nếu chỉ có 1 sở thích, vui lòng điền sở thích có dấu phẩy cuối cùng VD: '(sở thích), '")
				habits = input("Sở thích của học viên: ")
				method.cross()

				# Check đủ điều kiện
				if method.input_condition(name, False, True) and method.input_condition(age, True, False) and method.input_condition(habits, False, True) and [l for l in habits if l == ","]:
					habit = habits.split(",")
					# Tạo học viên mới
					new_student = model.Student(name, int(age), habit, [])
					# Cập nhật học viên
					resources.students.append(new_student)
					resources.update_HV()
					method.success("Bạn đã thêm học viên thành công")
					break
				else:
					print("Vui lòng nhập lại tất cả thông tin đúng theo yêu cầu đã nói trên")
					method.cross()
			break

		else:
			print("Vui lòng chọn 'y' hoặc 'n'")
			method.cross()

def lecturer():
	while True:
		choice = input("Bạn có chắc tạo giảng viên mới (y/n)? ")
		method.cross()
		if choice == "n":
			break
		elif choice == "y":
			print("Vui lòng nhập thông tin đăng ký theo thứ tự họ tên và thời hạn hợp đồng")
			method.cross()
			while True:		
				print("Tên của giảng viên phải có đầy đủ họ và tên và không chứa số !")
				name = input("Họ và tên của giảng viên: ")
				method.cross()
				print("Vui lòng nhập ngày tháng năm thời hạn hợp đồng theo thứ tự !")
				day = input("Ngày (2 chữ số): ")
				month = input("Tháng (2 chữ số): ")
				year = input("Năm (4 chữ số và 2020 < năm < 2100): ")
				method.cross()

				d = int(day)
				m = int(month)
			
				valid_date = method.listToStr([day,month,year], "")
				# Check đủ điều kiện
				if method.input_condition(name, False, True) and method.date_condition1(day, month, year) and method.date_condition2(d, m) and method.input_condition(valid_date , True, False):
					valid_date = method.listToStr([day,month,year], "/")
					# Tạo giảng viên mới
					new_lecturer = model.Lecturer(name, [], valid_date)
					# Cập nhật giảng viên
					resources.lecturers.append(new_lecturer)
					resources.update_GV()
					method.success("Bạn đã thêm giảng viên thành công")
					break
				else:
					print("Vui lòng nhập lại tất cả thông tin đúng theo yêu cầu đã nói trên")
					method.cross()
			break

		else:
			print("Vui lòng chọn 'y' hoặc 'n'")
			method.cross()