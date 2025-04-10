import functions as f
from datetime import datetime
from os import path, mkdir
from calendar import monthrange



def main() -> None:
    

    #тк ...
    m_y = datetime.now().strftime("%m_%y")
    file_name = "archive/" + f"finance_{m_y}.txt"

    

    if not path.exists(file_name):

        bal_1 = int(input("Начальная сумма >>> "))
        bal_2 = int(input("Прошлый остаток >>> "))

        print("=" * 40)
        
        mkdir("archive")

        f.make_file(file_name, bal_1, bal_2)

    
    
    day   = int(datetime.now().strftime("%d"))
    month = int(datetime.now().strftime("%m"))
    year  = int(datetime.now().strftime("%y"))

    last_day = int(f.l_day(file_name)) + 1



    with open(file_name, 'a') as file:
        
        while last_day <= day:
            wtf = f.write_to_file(file, last_day, day, month)
            sm = input(f"Sum for {wtf} >>> ")
            file.write(f"{wtf} - {sm}\n")

            last_day += 1



    summ  = f.add(file_name)
    start = f.init_amo(file_name)
    diff  = start - summ

    _, cnt_day = monthrange(year, month)


 
    if day == cnt_day:
        last_write(file_name, start, summ, diff)
        f.print_result(start, summ, diff)
    else:
        f.print_result(start, summ, diff)



if __name__ == "__main__":
    main()
