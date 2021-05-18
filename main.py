import resources, time, method, main_option, create_option, os


resources.start()

while True:
	os.system("clear")
	method.read("introduction.text")

	pick = input("Nhập vào Option bạn muốn chọn: ")
	method.cross()

	if pick == "1": main_option.main_option("Course/Course_list.text", "khoá", 1)
	elif pick == "2": main_option.main_option("Student/Student_list.text", "học viên", 2)
	elif pick == "3": main_option.main_option("Lecturer/Lecturer_list.text", "giảng viên", 3)
	elif pick == "4": create_option.student()
	elif pick == "5": create_option.lecturer()
	elif pick == "quit":
		print("TẠM BIỆT")
		time.sleep(3)
		quit()
	else:
		print("Vui lòng chỉ nhập những Option có trong danh sách hiển thị hoặc 'quit' để thoát")
		time.sleep(2)