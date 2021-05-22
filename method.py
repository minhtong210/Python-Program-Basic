import time

def cross():
	print("------------------------------------")

def success(message):
	time.sleep(1)
	fail(message)

def fail(message):
	print(message)
	cross()
	time.sleep(2)

def not_allow():
	print("Rất tiếc, bạn không có quyền hạn để thực hiện điều này")
	cross()
	time.sleep(2)

def option_error():
	print("Vui lòng chỉ nhập những Option có trong danh sách hiển thị hoặc 'back' để quay về")
	time.sleep(2)

def listToStr(l, seperator):
	return seperator.join(l)

def str_range(max):
	return map(str, range(1,len(max)))

def str_range_inclue(max):
	a = list(range(1,len(max)))
	b = len(max)
	a.append(b)
	return map(str,a)

def atBeginning(file):
	with open(file) as file:
		file.seek(0)

def read(file):
	with open(file) as file:
		file.seek(0)
		print(file.read())

def input_condition(text, within_int = True, within_str = True):
	if not text:
		cross()
		print("Vui lòng không được để trống")
		return False
	if within_int:
		if within_str:
			if text.isnumeric():
				cross()
				print("Vui lòng chỉnh sửa thông tin bằng chữ (có thể có số hoặc ko)!")
				return False
			return True
		else:
			if not text.isnumeric():
				cross()
				print("Vui lòng chỉnh sửa thông tin bằng số và không có chữ!")
				return False
			return True

	else:
		if [l for l in text if l.isnumeric()]:
			cross()
			print("Vui lòng chỉnh sửa thông tin bằng chữ và không có số!")
			return False
		return True

def date_condition1(d = 0, m = 0, y = 0):
	def condition(kind, min_len = 0, max_len = 3, min_quantity = 0, max_quantity = 32):
		if kind.isnumeric():
			kind = int(kind)
			if len(str(kind)) > min_len and len(str(kind)) < max_len and kind < max_quantity and kind > min_quantity:
				return True
			return False
		return False

	if condition(d) and condition(m, 0, 3, 0, 13) and condition(y, 3, 5, 2020, 2100):
		return True
	return False

def date_condition2(d = 0, m = 0):
	d = int(d)
	m = int(m)
	if d == 29 and m == 2 or d == 30 and m == 2 or d == 31 and m == 2 or d == 31 and m == 4 or d == 31 and m == 6 or d == 31 and m == 9 or d == 31 and m == 11:   
		return False
	return True

def mark_condition(text, *m):
	if text.replace('.','',1).isdigit():
		x = [i for i in m if (float(i) > 0 or float(i) == 0) and (float(i) < 10 or float(i) == 10)]
		if len(x) == 3:
			return True
	return False