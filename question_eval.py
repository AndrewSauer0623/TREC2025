import unicodedata

# Specify the path to the text file
file_path = 'Desktop/2024-question-assessment.txt'



with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split("\t")
        if (line[5] == "4"):
            with open('Desktop/filtered_questions.txt', 'a', encoding='utf-8') as out_file:
                out_file.write("Clueweb Tag: " + line[1] + " Rating: " + line[5] + " Question: " + line[7] + "\n")



