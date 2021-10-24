with open("personal_data.csv", "r") as personal_data_file:
    contents = personal_data_file.read().splitlines()
    print(contents)

    for row in contents:
        row_personal_data = row.split(",")
        print(f"{row_personal_data[0]} is {row_personal_data[1]} years old and {row_personal_data[2]}.")
