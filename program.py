#1: V

#2:
try:
    with open('mt_text.txt', 'w') as file:
        file.writelines(["Hello world", "It’s the first exercise in I/O", "That mean it is number 1", "Not 2", "Not three", "It is exciting", "And i am all 4 it"])
except IOError as ex:
    print("Error performing I/O operations on the file: ", ex)

#3:
