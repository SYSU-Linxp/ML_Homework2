import numpy as np
from scipy import sparse

file = open("train_data.txt")
train_y = []
train_x_data = []
train_row_ind = []
train_col_ind = []
cnt = 0
for line in file:
    data_line = str(line).split()
    train_y.append(int(data_line[0]))
    for i in range(1,len(data_line)):
        key_value = data_line[i].split(":")
        key = int(key_value[0])
        value = float(key_value[1])
        if (key <= 132):
            train_row_ind.append(cnt)
            train_col_ind.append(key)
            train_x_data.append(value)
    cnt += 1
train_x =  sparse.csr_matrix((train_x_data,(train_row_ind,train_col_ind)))
train_y = np.array(train_y)

file = open("test_data.txt")
test_id = []
test_y = []
test_x_data = []
test_row_ind = []
test_col_ind = []
cnt = 0

for line in file:
    data_line = str(line).split()
    test_id.append(int(data_line[0]))
    for i in range(1,len(data_line)):
        key_value = data_line[i].split(":")
        key = int(key_value[0])
        value = float(key_value[1])
        test_row_ind.append(cnt)
        test_col_ind.append(key)
        test_x_data.append(value)
    cnt += 1
test_x =  sparse.csr_matrix((test_x_data,(test_row_ind,test_col_ind)))