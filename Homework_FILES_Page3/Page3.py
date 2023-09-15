top = {}

for i in range(1, 4):
    file_name = f"{i}.txt"
    with open(file_name, 'r', encoding='utf-8') as f:
        file_strings = f.readlines()
    top[file_name] = [len(file_strings), "".join(file_strings)]

sorted_top = sorted(top.items(), key=lambda x: x[1][0])

result = f"{sorted_top[0][0]}\n{sorted_top[0][1][0]}\n{sorted_top[0][1][1]}" \
         f"{sorted_top[1][0]}\n{sorted_top[1][1][0]}\n{sorted_top[1][1][1]}\n" \
         f"{sorted_top[2][0]}\n{sorted_top[2][1][0]}\n{sorted_top[2][1][1]}"

with open("result.txt", 'w', encoding='utf-8') as f:
    f.write(result)