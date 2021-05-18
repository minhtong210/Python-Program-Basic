import method, resources, datetime, os
import Student_model as s
from statistics import mean

def main_option(file_name, kind, option, account_check):

	def option_case(func):
		while True:
			os.system("clear")
			with open(f"{file_name}") as danhsach:
				ds = danhsach.readlines()
				danhsach.seek(0)
				print(danhsach.read())

			num_pick = input(f"Nhập vào {kind} muốn chọn: ")
			method.cross()
			
			# Quay lại
			if num_pick == "back": 
				break
			# Thông tin chi tiết
			if num_pick in method.str_range(ds):
			
			# FUNCTION CHI TIẾT
				func(int(num_pick), account_check)
			else:
				method.option_error()

	if option == 1: option_case(course_option)
	elif option == 2: option_case(student_option)
	else: option_case(lecturer_option)
			
def course_option(num, a_check):
	while True:
		os.system("clear")
		course = resources.courses[num - 1]
		
		# Kiểm tra số lượng học viên qua môn
		course.rate = resources.update_student_pass(0, course.course_name)
		
		# Show thông tin
		course.course_info()
		method.read("Course/Course_info.text")

		num_pick = input(f"Nhập vào số thông tin muốn chỉnh sửa hoặc xem danh sách học viên qua môn: ")
		method.cross()
		
		# Không thể chỉnh sửa số học viên
		if num_pick == "1":
			if "HIEUTRUONG" in a_check:
				method.fail("Bạn không thể chỉnh sửa mục số Học Viên")
			else:
				method.not_allow()

		# Chỉnh sửa mô tả
		elif num_pick == "2":
			if "HIEUTRUONG" in a_check:
				replace_text = input("Bạn muốn chỉnh sửa thành: ")
				method.input_condition(replace_text)
				course.description = replace_text
				method.success("Chỉnh sửa thành công")
			else:
				method.not_allow()
		
		# Không thể chỉnh sửa Giảng viên
		elif num_pick == "3":
			if "HIEUTRUONG" in a_check:
				method.fail("Bạn không thể chỉnh sửa mục giảng viên tại đây, vui lòng sang option 3 !")
			else:
				method.not_allow()

		# Show danh sách học viên qua môn
		elif num_pick == "4":
			os.system("clear")
			method.read("Course/Course_pass_list.text")
			input("Nhấn Enter để quay lại ")
		
		# Quay lại
		elif num_pick == "back": 
			break
		else: 
			method.option_error()
	
def student_option(num, a_check):
	while True:
		os.system("clear")
		student = resources.students[num - 1]
		student.student_info()
		resources.update_student()
		resources.update_student_result(num - 1)
		method.read("Student/Student_info.text")
		info_pick = input("Nhập vào số của thông tin muốn chỉnh sửa hoặc xem điểm: ")
		method.cross()

		# Chỉnh sửa tên học viên
		if info_pick == "1":
			if not "GIAOVIEN" in a_check:
				replace_text = input("Bạn muốn chỉnh sửa thành: ")
				if method.input_condition(replace_text, False):
					student.full_name = replace_text
					method.success("Chỉnh sửa thành công")
			else:
				method.not_allow()

		# Chỉnh sửa tuổi học viên
		elif info_pick == "2":
			if not "GIAOVIEN" in a_check:
				replace_text = input("Bạn muốn chỉnh sửa thành: ")
				if method.input_condition(replace_text, True, False):
					student.age = int(replace_text)
					method.success("Chỉnh sửa thành công")
			else:
				method.not_allow()

		# Chỉnh sửa sở thích học viên
		elif info_pick == "3":
			if not "GIAOVIEN" in a_check:
				replace_text = input("Bạn muốn chỉnh sửa thành: ")
				if method.input_condition(replace_text, False, True):
					habits = replace_text.split(", ")
					student.habits = habits
					method.success("Chỉnh sửa thành công")
			else:
				method.not_allow()

		# Chỉnh sửa khoá học học viên tham gia
		elif info_pick == "4":
			if not "GIAOVIEN" in a_check:
				while True:
					os.system("clear")
					student.student_cls_change()
					method.read("Student/Student_cls_change.text")
					print("Lưu ý: Nếu bạn thoát khoá học, điểm của khoá học đó sẽ mất.")
					num_pick = input("Nhập vào khoá học muốn thoát / lựa chọn tham gia: ")
					method.cross()

					# Lựa chọn tham gia khoá học
					if num_pick == str(len(student.courses) + 1):
						
						# Nếu có 3 khoá học
						if len(student.courses) == 3:
							method.fail("Học viên không thể tham gia quá 3 khoá học")
						
						# Ít hơn 3 khoá
						else:
							method.read("Course/Course_list.text")
							pick = input("Nhập vào khoá học bạn muốn tham gia: ")
							method.cross()

							if pick in method.str_range_inclue(resources.courses):
								course_pick = resources.courses[int(pick) - 1]
								
								# Trường hợp KH full
								if course_pick.quantity == course_pick.max_quantity:
									method.fail("Khoá học đã full, không thể tham gia")
								
								# Trường hợp KH có thể tham gia
								elif course_pick.quantity < course_pick.max_quantity:
									
									# Trường hợp trùng KH
									if course_pick.course_name in [c.course_name for c in student.courses]:
										method.fail("Khoá học này học viên đã tham gia, không thể tham gia trùng 1 lớp")
									
									# Trường hợp không trùng
									else:
										# Update học viên tham gia khoá học
										student.courses.insert(int(pick) - 1 ,s.Stu_Course(course_pick.course_name))
										resources.update_student()
										
										# Update khoá học
										course_pick.quantity += 1
										resources.update_course()
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
							if c.course_name == course_pick.course_name:
								c.quantity -= 1
						resources.update_course()

						# Update học viên huỷ khoá học
						student.courses.pop(int(num_pick) - 1)
						resources.update_student()
						method.success("Đã huỷ thành công") 
						
					# Quay lại
					elif num_pick == "back": 
						break
					else:
						method.option_error()
			else:
				method.not_allow()

		# Xem / Chỉnh sửa điểm		
		elif info_pick == "5":
			if "GIAOVIEN" in a_check:
				while True:
					os.system("clear")
					resources.update_student_result(num - 1)
					method.read("Student/Student_info_results.text")

					pick = input("Nhập vào khoá học bạn muốn chỉnh sửa điểm: ")
					method.cross()

					# Chỉnh sửa điểm
					if pick in method.str_range_inclue(student.courses):
						print("Vui lòng nhập điểm theo thứ tự Toán Văn Anh! (Yêu cầu: 10 > điểm > 0)")
						math = input("Toán: ")
						liter = input("Văn: ")
						eng = input("Anh: ")
						
						text = math + liter + eng

						# Check điểm chỉnh sửa
						if method.mark_condition(text, math, liter, eng):
							stu_point = student.courses[int(pick) - 1]
							stu_point.math = math
							stu_point.literature = liter
							stu_point.eng = eng
							stu_point.avg = round(mean([float(math),float(liter),float(eng)]), 1)
							stu_point.grade = s.grade(stu_point.avg)
							method.success("Đã chỉnh sửa thành công")
						else:
							method.fail("Vui lòng điền lại số theo yêu cầu và không có chữ!")				

					# Quay lại
					elif pick == "back":
						break
					else:
						method.option_error()

			#Chỉ xem điểm
			else:
				os.system("clear")
				method.read("Student/Student_info_results.text")
				input("Bạn không có quyền hạn để chỉnh sửa điểm. Nhấn 'Enter' de quay lai")
		
		# Quay lại		
		elif info_pick == "back": 
			break
		else:
			method.option_error()

def lecturer_option(num, a_check):
	while True:
		os.system("clear")
		lecturer = resources.lecturers[num - 1]
		lecturer.lecturer_info()
		lecturer.lecturer_course_info()
		resources.update_lecturer()
		method.read("Lecturer/Lecturer_info.text")
		if "HIEUTRUONG" in a_check:

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
					resources.update_course()
					method.success("Chỉnh sửa thành công")
			
			# Chỉnh sửa khoá học đang giảng dạy
			elif num_pick == "2":
				while True:
					os.system("clear")
					# List ra các khoá học
					lecturer.lecturer_course_info()
					method.read("Lecturer/Lecturer_course_info.text")
					pick = input("Nhập vào khoá học muốn huỷ dạy / lựa chọn tham gia: ")
					method.cross()

					# Lựa chọn tham gia khoá học còn trống
					if pick == str(len(lecturer.courses) + 1):
						
						# Xét điều kiện đăng ký với thời hạn hợp đồng
						valid_date = datetime.datetime.strptime(lecturer.valid, '%d/%m/%Y')
						today = datetime.datetime.today()
						if valid_date > today or valid_date == today:
							method.read("Course/Course_list.text")
							pick_course = input("Nhập vào khoá học bạn muốn tham gia giảng dạy: ")

							# Nếu đủ điều kiện
							if pick_course in method.str_range_inclue(resources.courses):
								course_pick = resources.courses[int(pick_course) - 1]
								method.cross()
								
								# Nếu lớp còn trống
								if course_pick.lecturer == "":
									course_pick.lecturer = lecturer.full_name
									lecturer.courses.insert(int(pick_course) - 1, course_pick.course_name)
									method.success("Đã tham gia thành công")
								
								# Nếu lớp đã có giảng viên
								else:
									method.fail("Bạn không thể giảng dạy khoá học đã có giảng viên, vui lòng xem khoá học tại option 1")
							
							# Quay lại
							elif num_pick == "back": 
								break
							else:						
								method.option_error()
						else:
							method.fail("Bạn không thể giảng dạy khoá học vì đã hết thời hạn hợp đồng")

					# Lựa chọn huỷ dạy khoá học
					elif pick in method.str_range_inclue(lecturer.courses):
						course_pick = lecturer.courses[int(pick) - 1]

						# Update khoá học
						for c in resources.courses:
							if c.course_name == course_pick:
								c.lecturer = ""
						resources.update_course()

						# Update giảng viên dạy khoá học
						lecturer.courses.pop(int(pick) - 1)
						lecturer.lecturer_course_info()
						resources.update_lecturer()

						method.success("Đã huỷ thành công")

					# Quay lại
					elif pick == "back": 
						break
					else:
						method.option_error()
			
			# Chỉnh sửa thời hạn hợp đồng
			elif num_pick == "3":
				os.system("clear")
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
					resources.update_lecturer()
					method.success("Chỉnh sửa thành công")
				else:
					method.fail("Vui lòng nhập lại ngày tháng năm đúng theo lịch và chỉ có số")

			# Quay lại		
			elif num_pick == "back": 
				break
			else:
				method.option_error()
		else:
			input("Bạn không có quyền hạn để chỉnh sửa thông tin giảng viên. Nhấn 'Enter' de quay lai")
