import resources, method, os

def del_option(account_check):
	while True:
		os.system("clear")
		print("Các mục có thể xoá:")
		print("1. Học Viên")
		print("2. Giảng viên")
		print("3. Khoá học")
		choice = input("Nhập vào số mục mà bạn muốn xoá: ")
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
			stu_list = resources.students
			resources.update_course()
			resources.update_student()

			method.read("Student/Student_list.text")
			num_pick = input("Nhập vào số của học viên mà bạn muốn xoá: ")
			method.cross()

			if num_pick in method.str_range_inclue(stu_list):
				del_student = stu_list[int(num_pick) - 1]

				# Update số lượng học viên trong danh sách khoá học
				for c in resources.courses:
					for stu_c in del_student.courses:
						if c.course_name == stu_c.course_name:
							c.quantity -= 1

				# Update danh sách học viên
				stu_list.pop(int(num_pick) - 1)

				method.success("Đã xoá thành công") 

			elif num_pick == "back": 
				break
			else: 
				method.option_error()
	else:
		method.not_allow()

def lecturer(a_check):
	if "HIEUTRUONG" in a_check:
		while True:
			os.system("clear")
			lect_list = resources.lecturers
			resources.update_course()
			resources.update_lecturer()
			
			method.read("Lecturer/Lecturer_list.text")
			num_pick = input("Nhập vào số của giảng viên mà bạn muốn xoá: ")
			method.cross()

			if num_pick in method.str_range_inclue(lect_list):
				del_lecturer = lect_list[int(num_pick) - 1]

				# Update giáo viên đứng lớp trong danh sách khoá học
				for c in resources.courses:
					for lect_c in del_lecturer.courses:
						if c.course_name == lect_c:
							c.lecturer = ""

				# Update danh sách giảng viên
				lect_list.pop(int(num_pick) - 1)

				method.success("Đã xoá thành công") 

			elif num_pick == "back": 
				break
			else: 
				method.option_error()
	else:
		method.not_allow()

def course(a_check):
	if "HIEUTRUONG" in a_check:
		while True:
			os.system("clear")
			course_list = resources.courses
			resources.update_course()
			resources.update_lecturer()
			resources.update_student()
			
			method.read("Course/Course_list.text")
			num_pick = input("Nhập vào số của khoá học mà bạn muốn xoá: ")
			method.cross()

			if num_pick in method.str_range_inclue(course_list):
				del_course = course_list[int(num_pick) - 1]

				# Update khoá học tham gia của học viên
				for s in resources.students:
					for c in s.courses:
						if c.course_name == del_course.course_name:
							s.courses.remove(c)

				# Update khoá học giảng dạy của giảng viên
				for l in resources.lecturers:
					for c in l.courses:
						if c == del_course.course_name:
							l.courses.remove(c)

				# Update khoá học
				course_list.pop(int(num_pick) - 1)

				method.success("Đã xoá thành công")

			elif num_pick == "back": 
				break
			else: 
				method.option_error()
	else:	
		method.not_allow()
		