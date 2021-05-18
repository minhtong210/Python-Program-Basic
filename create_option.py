import method, resources, time, os, sys

sys.path.append("Student/")
sys.path.append("Lecturer/")
import Lecturer_model as l, Student_model as s

def student():
	while True:
		os.system("clear")
		choice = input("Bạn có chắc tạo học viên mới (y/n)? ")
		method.cross()
		if choice == "n":
			break
		elif choice == "y":
			print("Vui lòng nhập thông tin đăng ký theo thứ tự tên, tuổi và sở thích")
			method.cross()
			time.sleep(2)
			while True:
				os.system("clear")
				print("Tên của học viên phải có đầy đủ họ và tên và không chứa số !")
				name = input("Họ và tên của học viên: ")
				method.cross()
				print("Tuổi của học viên phải là số !")
				age = input("Tuổi hiện tại của học viên: ")
				method.cross()
				print("Sở thích của học viên ngăn cách nhau giữa giấu phẩy và không chứa số !")
				habits = input("Sở thích của học viên: ")
				method.cross()

				# Check đủ điều kiện
				if method.input_condition(name, False, True) and method.input_condition(age, True, False) and method.input_condition(habits, False, True):
					habit = habits.split(", ")
					# Tạo học viên mới
					new_student = s.Student(name, int(age), habit, [])
					# Cập nhật học viên
					resources.students.append(new_student)
					resources.update_student()
					method.success("Bạn đã thêm học viên thành công")
					break
				else:
					method.cross()
					print("Vui lòng nhập lại tất cả thông tin đúng theo yêu cầu đã nói trên")
					time.sleep(2)
			break

		else:
			print("Vui lòng chọn 'y' hoặc 'n'")
			method.cross()
			time.sleep(2)

def lecturer():
	while True:
		os.system("clear")
		choice = input("Bạn có chắc tạo giảng viên mới (y/n)? ")
		method.cross()
		if choice == "n":
			break
		elif choice == "y":
			print("Vui lòng nhập thông tin đăng ký theo thứ tự họ tên và thời hạn hợp đồng")
			method.cross()
			time.sleep(2)
			while True:
				os.system("clear")	
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
				if method.input_condition(name, False, True) and method.date_condition1(day, month, year) and method.date_condition2(day, month) and method.input_condition(valid_date , True, False):
					valid_date = method.listToStr([day,month,year], "/")
					# Tạo giảng viên mới
					new_lecturer = l.Lecturer(name, [], valid_date)
					# Cập nhật giảng viên
					resources.lecturers.append(new_lecturer)
					resources.update_lecturer()
					method.success("Bạn đã thêm giảng viên thành công")
					break
				else:
					if not method.input_condition(name, False, True):
						print("Bạn đã nhập TÊN không đúng theo yêu cầu")
					elif not method.date_condition1(day, month, year):
						print("Bạn đã nhập THỜI HẠN không đúng theo yêu cầu")
					elif not method.date_condition2(day, month):
						print("Bạn đã nhập THỜI HẠN không tồn tại")

					method.cross()
					print("Vui lòng nhập lại tất cả thông tin đúng theo yêu cầu đã nói trên")
					time.sleep(2)
			break

		else:
			print("Vui lòng chọn 'y' hoặc 'n'")
			method.cross()
			time.sleep(2)