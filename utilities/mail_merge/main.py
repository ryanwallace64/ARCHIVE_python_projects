with open("./Names/invited_names.txt") as names:
    names_list = names.readlines()
    for name in names_list:
        name = name.strip()
        with open("Input/Letters/starting_letter.txt") as input_letter:
            input_text = input_letter.read()
            output_letter = input_text.replace("[name]", name)
            print(output_letter)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output:
                output.write(output_letter)
