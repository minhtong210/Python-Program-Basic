import resources, time, method, main_option, create_option, del_option, os

while True:
	os.system("clear")
	resources.start()

	account = input("Nhập mã đăng nhập: ")
	account_list = ["HOCSINH001", "GIAOVIEN001", "HIEUTRUONG001"]

	if account in account_list:
		method.cross()
		if "HOCSINH" in account:
			method.success("Xin chào Học Sinh")
		if "GIAOVIEN" in account:
			method.success("Xin chào Giảng Viên")
		if "HIEUTRUONG" in account:
			method.success("Xin chào Hiệu Trưởng")

		while True:
			os.system("clear")
			method.read("introduction.text")

			pick = input("Nhập vào Option bạn muốn chọn: ")
			method.cross()

			if pick == "1": main_option.main_option("Course/Course_list.text", "khoá", 1, account)
			elif pick == "2": main_option.main_option("Student/Student_list.text", "học viên", 2, account)
			elif pick == "3": main_option.main_option("Lecturer/Lecturer_list.text", "giảng viên", 3, account)
			elif pick == "4": create_option.create_option(account)
			elif pick == "5": del_option.del_option(account)
			elif pick == "6": break
			elif pick == "quit":
				print("TẠM BIỆT")
				time.sleep(3)
				quit()
			else:
				method.fail("Vui lòng chỉ nhập những Option có trong danh sách hiển thị hoặc 'quit' để thoát")
	
	elif account == "quit":
		quit()
	else:
		method.fail("Vui lòng nhập đúng mã đăng nhập để có thể sử dụng chương trình hoặc 'quit' để thoát")
