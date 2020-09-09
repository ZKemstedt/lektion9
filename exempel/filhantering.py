try:
    with open("a_lost_file", "r") as f:
        print(f)
except FileNotFoundError:
    print("File not found")


persons = ["kalle", "lisa", "stina", "olle"]
with open("a_new_file", "w+") as w:
    for person in persons:
        w.write(f'{person}\n')
