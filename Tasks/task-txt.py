with open('students.txt', 'r', encoding='utf-8') as f, \
        open('without_scholarship.txt', 'w', encoding='utf-8') as f1, \
        open('up_scholarship.txt', 'w', encoding='utf-8') as f2:
    for line in f:
        parts = line.split(' ')
        mark = int(parts[-1])
        if mark <= 3:
            f1.write(f"{parts[0]} {parts[1]}\n")
        elif mark == 5:
            f2.write(f"{parts[0]} {parts[1]}\n")
