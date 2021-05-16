import resources, time, method, main_option, create_option

resources.start()

while True:
	method.read("introduction.text")

	pick = input("Nhập vào Option bạn muốn chọn: ")
	method.cross()

	if pick == "1": main_option.main_option("KH_ds.text", "khoá", 1)
	elif pick == "2": main_option.main_option("HV_ds.text", "học viên", 2)
	elif pick == "3": main_option.main_option("GV_ds.text", "giảng viên", 3)
	elif pick == "4": create_option.student()
	elif pick == "5": create_option.lecturer()
	elif pick == "quit":
		print("TẠM BIỆT")
		time.sleep(3)
		quit()
	else:
		print("Vui lòng chỉ nhập những Option có trong danh sách hiển thị hoặc 'quit' để thoát")