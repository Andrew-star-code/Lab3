import time
max_buffer_len = 100    
buffer_len = 1         

work_buffer = ""
try:
    start = time.time()
    with open("text.txt", "r", encoding="UTF-8") as file:
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)          
        if not buffer:                       
            print ("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:
            work_buffer += buffer
            if buffer.find(".") >= 0 or buffer.find("!") >= 0 or buffer.find("?") >= 0:
                a = work_buffer
                b = a.split()
                for j in reversed (b):
                    print(j, end = " ")
                    work_buffer = ""
            buffer = file.read(buffer_len)
            if len(work_buffer) >= max_buffer_len and buffer.find(".") < 0 and buffer.find("!") < 0 and buffer.find("?") < 0:
                print ("\nФайл text.txt не содержит знаков окончания предложения и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                work_buffer = ""
                break
        if len(work_buffer) > 0:
            print ("\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")

    finish = time.time()
    result = finish - start
    print("\nProgram time: " + str(result) + " seconds.")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.") 
    

