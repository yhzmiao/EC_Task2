import csv
output_csv = open("sa_all.csv", "w", newline="")
writer = csv.writer(output_csv)
writer.writerow(["experiment_id", "gen_id","gen_fit_max", "gen_gain_max", "overall_fit_max", "overall_gain_max", "fit_mean", "fit_var", "fit_std", "gain_mean", "gain_var", "gain_std"])

for e_id in range(1, 11):
	filename = str(e_id) + "/task2_sa_all/output.txt"
	fp = open(filename, "r")
	input_buffer = fp.readlines()

	for i in range(0, 90, 3):
		str1 = input_buffer[i].split(' ')
		str2 = input_buffer[i + 1].split(' ')
		str3 = input_buffer[i + 2].split(' ')
		gen_id = i // 3 + 1
		print(str1)
		print(str2)
		print(str3)
		writer.writerow([str(e_id), str(gen_id), str1[5][:-1], str1[7][:-1], str1[12][:-1], str1[14][:-1], str2[5][:-1], str2[8][:-1], str2[11][:-1], str3[5][:-1], str3[8][:-1], str3[11][:-1]])
	
	fp.close()
output_csv.close()

output_csv = open("sa_13.csv", "w", newline="")
writer = csv.writer(output_csv)
writer.writerow(["experiment_id", "gen_id","gen_fit_max", "gen_gain_max", "overall_fit_max", "overall_gain_max", "fit_mean", "fit_var", "fit_std", "gain_mean", "gain_var", "gain_std"])

for e_id in range(1, 11):
	filename = str(e_id) + "/task2_sa_13/output.txt"
	fp = open(filename, "r")
	input_buffer = fp.readlines()

	for i in range(0, 90, 3):
		str1 = input_buffer[i].split(' ')
		str2 = input_buffer[i + 1].split(' ')
		str3 = input_buffer[i + 2].split(' ')
		gen_id = i // 3 + 1
		print(str1)
		print(str2)
		print(str3)
		writer.writerow([str(e_id), str(gen_id), str1[5][:-1], str1[7][:-1], str1[12][:-1], str1[14][:-1], str2[5][:-1], str2[8][:-1], str2[11][:-1], str3[5][:-1], str3[8][:-1], str3[11][:-1]])
	
	fp.close()
output_csv.close()

output_csv = open("sa_4678.csv", "w", newline="")
writer = csv.writer(output_csv)
writer.writerow(["experiment_id", "gen_id","gen_fit_max", "gen_gain_max", "overall_fit_max", "overall_gain_max", "fit_mean", "fit_var", "fit_std", "gain_mean", "gain_var", "gain_std"])

for e_id in range(1, 11):
	filename = str(e_id) + "/task2_sa_4678/output.txt"
	fp = open(filename, "r")
	input_buffer = fp.readlines()

	for i in range(0, 90, 3):
		str1 = input_buffer[i].split(' ')
		str2 = input_buffer[i + 1].split(' ')
		str3 = input_buffer[i + 2].split(' ')
		gen_id = i // 3 + 1
		print(str1)
		print(str2)
		print(str3)
		writer.writerow([str(e_id), str(gen_id), str1[5][:-1], str1[7][:-1], str1[12][:-1], str1[14][:-1], str2[5][:-1], str2[8][:-1], str2[11][:-1], str3[5][:-1], str3[8][:-1], str3[11][:-1]])
	
	fp.close()
output_csv.close()

output_csv = open("self_adaptive_13.csv", "w", newline="")
writer = csv.writer(output_csv)
writer.writerow(["experiment_id", "gen_id","gen_fit_max", "gen_gain_max", "overall_fit_max", "overall_gain_max", "fit_mean", "fit_var", "fit_std", "gain_mean", "gain_var", "gain_std"])

for e_id in range(1, 11):
	filename = str(e_id) + "/task2_self_13/output.txt"
	fp = open(filename, "r")
	input_buffer = fp.readlines()

	for i in range(0, 90, 3):
		str1 = input_buffer[i].split(' ')
		str2 = input_buffer[i + 1].split(' ')
		str3 = input_buffer[i + 2].split(' ')
		gen_id = i // 3 + 1
		print(str1)
		print(str2)
		print(str3)
		writer.writerow([str(e_id), str(gen_id), str1[5][:-1], str1[7][:-1], str1[12][:-1], str1[14][:-1], str2[5][:-1], str2[8][:-1], str2[11][:-1], str3[5][:-1], str3[8][:-1], str3[11][:-1]])
	
	fp.close()
output_csv.close()

output_csv = open("self_adaptive_4678.csv", "w", newline="")
writer = csv.writer(output_csv)
writer.writerow(["experiment_id", "gen_id","gen_fit_max", "gen_gain_max", "overall_fit_max", "overall_gain_max", "fit_mean", "fit_var", "fit_std", "gain_mean", "gain_var", "gain_std"])

for e_id in range(1, 11):
	filename = str(e_id) + "/task2_self_4678/output.txt"
	fp = open(filename, "r")
	input_buffer = fp.readlines()

	for i in range(90, 180, 3):
		str1 = input_buffer[i].split(' ')
		str2 = input_buffer[i + 1].split(' ')
		str3 = input_buffer[i + 2].split(' ')
		gen_id = i // 3 + 1
		print(str1)
		print(str2)
		print(str3)
		writer.writerow([str(e_id), str(gen_id), str1[5][:-1], str1[7][:-1], str1[12][:-1], str1[14][:-1], str2[5][:-1], str2[8][:-1], str2[11][:-1], str3[5][:-1], str3[8][:-1], str3[11][:-1]])
	
	fp.close()
output_csv.close()

output_csv = open("sa_all_100.csv", "w", newline="")
writer = csv.writer(output_csv)
writer.writerow(["experiment_id", "gen_id","gen_fit_max", "gen_gain_max", "overall_fit_max", "overall_gain_max", "fit_mean", "fit_var", "fit_std", "gain_mean", "gain_var", "gain_std"])

for e_id in range(1, 11):
	filename = str(e_id) + "/task2_sa_all_100/output.txt"
	fp = open(filename, "r")
	input_buffer = fp.readlines()

	for i in range(0, 300, 3):
		str1 = input_buffer[i].split(' ')
		str2 = input_buffer[i + 1].split(' ')
		str3 = input_buffer[i + 2].split(' ')
		gen_id = i // 3 + 1
		print(str1)
		print(str2)
		print(str3)
		writer.writerow([str(e_id), str(gen_id), str1[5][:-1], str1[7][:-1], str1[12][:-1], str1[14][:-1], str2[5][:-1], str2[8][:-1], str2[11][:-1], str3[5][:-1], str3[8][:-1], str3[11][:-1]])
	
	fp.close()
output_csv.close()