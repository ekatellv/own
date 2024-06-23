with open('17.txt', 'r', encoding='utf-8') as o:
    line_str = o.readlines()
    line_int = [int(line.strip()) for line in line_str]
    count = 0
    sum = []
    for i in range(len(line_str) - 1):
        for j in range(i + 1, len(line_str)):
            if (line_int[i] + line_int[j]) % 2 != 0 and (line_int[i] * line_int[j]) % 3 == 0:
                count += 1
                sum.append(line_int[i] + line_int[j])
    print(count, max(sum))
