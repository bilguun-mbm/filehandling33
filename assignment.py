# You can remove 'pass' if you written code in the function
# Exercise 1
def read_line(filename, line_number):
    if line_number<=0:
        return ""

    file = open(filename, "r")
    target_line=""

    for current in range(1, line_number + 1):
        line=file.readline()
        if line=="":
            target_line = ""
            break
        if current==line_number:
            target_line = line.rstrip("\n")

    file.close()
    return target_line


# Exercise 2
def reverse_lines(source, destination):
    src_file=open(source, "r")
    lines=[]
    for line in src_file:
        lines.append(line.strip())
    src_file.close()

    dest_file=open(destination, "w")
    count = 0
    for line in reversed(lines):
        dest_file.write(line + "\n")
        count+=1
    dest_file.close()

    return count


# Exercise 3
def merge_files(first, second, destination):
    dest_file=open(destination, "w")
    total_written=0

    file_1 = open(first, "r")
    for line in file_1:
        dest_file.write(line.strip() + "\n")
        total_written += 1
    file_1.close()

    file_2 = open(second, "r")
    for line in file_2:
        dest_file.write(line.strip() + "\n")
        total_written += 1
    file_2.close()

    dest_file.close()
    return total_written


# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")
    score=-1

    for line in file:
        parts = line.strip().split(",")
        if len(parts)==2 and parts[0] == name:
            score=int(parts[1])
            break

    file.close()
    return score


# Exercise 5
def update_score(filename, name, new_score):
    file=open(filename, "r")
    lines=file.readlines()
    file.close()

    found=False
    updated_lines=[]

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[0]==name:
            updated_lines.append(f"{name},{new_score}\n")
            found = True
        else:
            updated_lines.append(line.strip() + "\n")

    if found:
        file = open(filename, "w")
        for line in updated_lines:
            file.write(line)
        file.close()
        return True

    return False
