def max_ranom_value(ranom_number):
    ranom_values = {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}
    max_value = float('-inf')
    for i in range(len(ranom_number)):
        for ranom_digit in ranom_values:
            new_ranom_number = ranom_number[:i] + ranom_digit + ranom_number[i+1:]
            value = 0
            for j in range(len(new_ranom_number)):
                if any(ranom_values[new_ranom_number[k]] > ranom_values[new_ranom_number[j]] for k in range(j+1, len(new_ranom_number))):
                    value -= ranom_values[new_ranom_number[j]]
                else:
                    value += ranom_values[new_ranom_number[j]]
            max_value = max(max_value, value)
    return max_value
n = int(input('Nhập số lượng cần tính: '))
values = []
for i in range(n):
    value = int(input(f'Nhập giá trị thứ {i+1}: '))
    values.append(value)


