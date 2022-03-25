import os
import time
max_buffer_len = 100    
buffer_len = 1         

work_buffer = ""        
engl_flag = False      
try:
    start = time.time()
    with open("text.txt", "r") as file:        
        print("\n-----Результат работы программы-----\n")
        buffer = file.read(buffer_len)          
        if not buffer:                       
            print ("\nФайл text.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:                                
            if buffer>='a' and buffer<='z':     
                engl_flag = True
                work_buffer += buffer
            else:
                work_buffer += buffer
                if buffer>='A' and buffer<='Z':
                    engl_flag = True
            if buffer.find(".") >= 0 or buffer.find("!") >= 0 or buffer.find("?") >= 0:   
                if engl_flag:
                    a = work_buffer;
                    b = a.split();
                    for j in reversed (b):
                        print(j, end = " ")
                engl_flag = False
                work_buffer = ""
            buffer = file.read(buffer_len)
            if len(work_buffer) >= max_buffer_len and buffer.find(".") < 0 and buffer.find("!") < 0 and buffer.find("?") < 0:
                print ("\nФайл text.txt не содержит знаков окончания предложения и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")     
        if len(work_buffer) > 0:
            print ("\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")

        finish = time.time()
        result = finish - start
        print("\nProgram time: " + str(result) + " seconds.")         
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.") 
    
