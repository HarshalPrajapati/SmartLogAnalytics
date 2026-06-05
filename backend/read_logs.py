def analyze_logs():

	info_count = 0
	warning_count = 0
	error_count = 0
	payment_count = 0
	login_count = 0
	database_count = 0
	with open("../logs/server.log","r") as file:
		for line in file:
			if "INFO" in line:
				info_count += 1
			elif "WARNING" in line:
				warning_count += 1
			elif "ERROR" in line:
				error_count += 1
			if "Payment" in line:
				payment_count += 1
			if "Login" in line:
				login_count += 1
			if "Database" in line:
				database_count += 1
	print("Info Log:",info_count)	
	print("Warning Log:",warning_count)
	print("Error Log:",error_count)
	print("Payment Log:",payment_count)
	print("Login Log:",login_count)
	print("Database Log:",database_count)

analyze_logs()
