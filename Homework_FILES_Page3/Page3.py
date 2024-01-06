top = {}
def rate_files(cou_files: int):
    result = ""
    for i in range(1, cou_files + 1):
        file_name = f"{i}.txt"
        with open(file_name, 'r', encoding='utf-8') as f:
            file_strings = f.readlines()
        top[file_name] = [len(file_strings), "".join(file_strings)]

    sorted_top = sorted(top.items(), key=lambda x: x[1][0])

    for j in range(cou_files):
        result += f"\n{sorted_top[j][0]}\n{sorted_top[j][1][0]}\n{sorted_top[j][1][1]}".rstrip()

    return result.strip()

with open("result.txt", 'w', encoding='utf-8') as f:
    f.write(rate_files(3))
