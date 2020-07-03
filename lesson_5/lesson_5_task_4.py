with open('file_4_input.txt', 'r', encoding="utf-8") as f:
    input_array = f.readlines()
output_array = []
for i in input_array:
    line_array = i.split()
    if line_array[0] == 'One':
        line_array[0] = 'Один'
    elif line_array[0] == 'Two':
        line_array[0] = 'Два'
    elif line_array[0] == 'Three':
        line_array[0] = 'Три'
    elif line_array[0] == 'Four':
        line_array[0] = 'Четыре'
    output_array.append(' '.join(line_array) + '\n')
with open('file_4_output.txt', 'w') as f:
    f.writelines(output_array)
