line_num = int(input())

num_array = list(range(1, (line_num * 4)+1))

for l in range(0, line_num):
    nums = str(num_array[0:3]).strip('[]').replace(',', '')
    print(nums, "PUM")
    del num_array[0:4]
