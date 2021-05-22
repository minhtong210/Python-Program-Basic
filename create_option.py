import method, resources, os, sys

sys.path.append("Student/")
sys.path.append("Lecturer/")
import Lecturer_model as l, Student_model as s, Course_model as c

def create_option(account_check):
	while True:
		os.system("clear")
		print("Các mục có thể tạo mới:")
		print("1. Học Viên")
		print("2. Giảng viên")
		print("3. Khoá học")
		choice = input("Nhập vào số mục mà bạn muốn tạo mới: ")
		method.cross()

		if choice == "1": student(account_check)
		elif choice == "2": lecturer(account_check)
		elif choice == "3": course(account_check)
		elif choice == "back": break
		else: method.option_error()


def student(a_check):
	if "HIEUTRUONG" in a_check:
		while True:
			os.system("clear")
			choice = input("Bạn có chắc tạo học viên mới (y/n)? ")
			method.cross()
			if choice == "n":
				break
			elif choice == "y":
				method.fail("Vui lòng nhập thông tin đăng ký theo thứ tự tên, tuổi và sở thích")
				while True:
					#Điền thông tin học viên mới
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
						if not method.input_condition(name, False, True):
							method.fail("Bạn đã nhập HỌ TÊN không đúng yêu cầu")
						if not method.input_condition(age, True, False):
							method.fail("Bạn đã nhập TUỔI không đúng yêu cầu")
						if not method.input_condition(habits, False, True):
							method.fail("Bạn đã nhập SỞ THÍCH không đúng yêu cầu")
						input("Nhấn Enter để thử lại")
				break
			else:
				method.fail("Vui lòng chọn 'y' hoặc 'n'")
	else:
		method.not_allow()

def lecturer(a_check):
	if "HIEUTRUONG" in a_check:
		while True:
			os.system("clear")
			choice = input("Bạn có chắc tạo giảng viên mới (y/n)? ")
			method.cross()
			if choice == "n":
				break
			elif choice == "y":
				method.fail("Vui lòng nhập thông tin đăng ký theo thứ tự họ tên và thời hạn hợp đồng")
				while True:
					#Điền thông tin giảng viên mới
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
						if not method.date_condition1(day, month, year):
							print("Bạn đã nhập THỜI HẠN không đúng theo yêu cầu")
						if not method.date_condition2(day, month):
							print("Bạn đã nhập THỜI HẠN không tồn tại")
						input("Nhấn Enter để thử lại")
				break

			else:
				method.fail("Vui lòng chọn 'y' hoặc 'n'")
	else:
		method.not_allow()

def course(a_check):
	if "HIEUTRUONG" in a_check:
		while True:
			os.system("clear")
			choice = input("Bạn có chắc tạo khoá học mới (y/n)? ")
			method.cross()
			if choice == "n":
				break
			elif choice == "y":
				method.fail("Vui lòng nhập thông tin tạo theo thứ tự Tên Khoá, mô tả, giới hạn học sinh và giáo viên giảng dạy")
				while True:
					#Điền thông tin khoá học mới
					os.system("clear")
					method.read("Course/Course_list.text")
					method.cross()
					print("Lưu ý: Tên của khoá học không được trùng cái đã có!")
					name = input("Tên của khoá học: ")
					method.cross()
					description = input("Mô tả của khoá học: ")
					method.cross()
					method.read("Lecturer/Lecturer_list.text")
					num_lecturer = input("Vui lòng chọn số giáo viên trong danh sách: ")
					method.cross()
					max_quantity = input("Nhập số lượng học viên tối đa của khoá học (số dương): ")

					if not name in [c.course_name for c in resources.courses] and num_lecturer in method.str_range_inclue(resources.lecturers) and max_quantity.isdigit():
						lect = resources.lecturers[int(num_lecturer) - 1]
						# Tạo khoá học mới
						new_course = c.Course(name, 0, description, lect.full_name, int(max_quantity))
						# Update list khoá học 
						resources.courses.append(new_course)
						resources.update_course()
						# Update giảng viên 
						lect.courses.insert(len(lect.courses) - 1, name)
						resources.update_lecturer()

						method.success("Bạn đã thêm khóa học thành công")
						break

					else:	
						if name in [c.course_name for c in resources.courses]:
							print("Bạn đã nhập TÊN KHOÁ HỌC trùng với khoá học đã có")
						if num_lecturer in method.str_range_inclue(resources.lecturers):
							print("Bạn đã nhập SỐ GIÁO VIÊN không có trong danh sách")
						if not max_quantity.isdigit():
							print("Bạn đã nhập SỐ LƯỢNG HỌC VIÊN TỐI ĐA không đúng yêu cầu")
						input("Nhấn Enter để thử lại")
				break
						
			else:
				method.fail("Vui lòng chọn 'y' hoặc 'n'")
	else:
		method.not_allow()