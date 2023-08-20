def generate_strings(n, last_char, current_string):
    if n == 0:
        print(current_string)
        return
    for char in ['A', 'B', 'C', 'D', 'E']:
        if char != last_char:
            generate_strings(n-1, char, current_string + char)

n = int(input("Nhập độ dài của các chuỗi: "))
generate_strings(n, '', '')
