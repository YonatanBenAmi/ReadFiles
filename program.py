#1: V

#2:
# try:
#     with open('mt_text.txt', 'w') as file:
#         file.write("Hello world\n")
#         file.write("It's the first exercise in I/O\n")
#         file.write("That mean it is number 1\n")
#         file.write("Not 2\n")
#         file.write("Not three\n")
#         file.write("It is exciting\n")
#         file.write("And i am all 4 it")
# except IOError as ex:
#     print("Error performing I/O operations on the file: ", ex)

#3:
# try:
#     with open('mt_text.txt', 'r', encoding="utf-8") as file:
#         contact = file.read().split("\n")
#         for line in contact:
#             if any(char.isdigit() for char in line):
#                 print(line)
# except IOError as ex:
#     print("Error performing I/O operations on the file: ", ex)

#4:

try:
    with open('mt_text.txt', 'r', encoding="utf-8") as file:
        text = file.read()
        contact = text.split("\n")
        index_line = 0
        count_words_without_num = 0
        for line in contact:
            if len(line.split()) % 2 == 0:
                print(f"Index line: {index_line}, Count words: {len(line.split())}")
            index_line += 1
            count_words_without_num += sum(1 for word in line.split() if not word.isdigit())
        print(f"Count words(without numbers): {count_words_without_num}")
        print(f"Count chars in text(without spaces): {sum(1 for character in text if character.isalnum())}")
except IOError as ex:
    print("Error performing I/O operations on the file: ", ex)
