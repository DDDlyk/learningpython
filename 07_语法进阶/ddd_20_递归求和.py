def sum_numbers(num):

    # 1.出口
    if num == 1:
        return 1

    # 2. 数字的累加 num +（1....num - 1）
    # 假设 sum_numbers能够正确处理1....num-1
    temp = sum_numbers(num-1)

    return num + temp


result = sum_numbers(100)
print(result)
