INPUT_FILE = r"C:\Users\PC\Notebooks (Py)\text_files_lesson\StudentsPerformance.csv"
data_list = []
for line in open(INPUT_FILE).readlines():
    data_list.append(line[1:-2].split('\",\"'))
for line in data_list[1:]:
    line[-3] = int(line[-3])
    line[-2] = int(line[-2])
    line[-1] = int(line[-1])
data_dict = {}
for i in range(len(data_list[0])):
    data_dict[data_list[0][i]] = [r[i] for r in data_list[1:]]