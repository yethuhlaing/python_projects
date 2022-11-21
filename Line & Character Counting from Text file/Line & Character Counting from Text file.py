file_name = input("Enter the name of the file to be read:\n")
with open(file_name, 'r', encoding="UTF-8" ) as rf:
    line_count = 0
    character_count = 0
    for line in rf:
        if line != 0:
            line_count += 1
        character_count += len(line)
average_length = character_count // line_count

print("The file contained {} names and {} characters.".format(line_count, character_count))
print("The average name length was {} characters.".format(average_length))
