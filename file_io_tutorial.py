# Задача: записать в выходной файл данные из входного файла.
fin = open ( 'input.txt', 'r' )
fout = open ( 'output.txt', 'w' )

fout.write(fin.read())
# fin.readline() - считывает строку
# fin.read(n) - считывает ровно n символов
# Перенос строки ('\n') также является символом

fin.close()
fout.close()

with open("input.txt", "r") as fin:# with..as освобождает указатель fin сразу после использования
    a = fin.read()

with open("output.txt", "w") as fout:
    fout.write(a)
    
# for line in f:
#     print(line)