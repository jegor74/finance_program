import functions as f
from datetime import datetime
from os import path, mkdir
from calendar import monthrange



def main() -> None:
    

    
    m_y = datetime.now().strftime("%m_%y")                       #every file names as finance_<month>_<year>
    file_name = "archive/" + f"finance_{m_y}.txt"                #and they are in "archive" directory

    

    if not path.exists("archive"):                               #block for making directory for all files
            mkdir("archive")
        
    if not path.exists(file_name):                               #block for making new files when new moth started

        bal_1 = int(input("Start sum >>> "))
        bal_2 = int(input("Bal for last month >>> "))

        print("=" * 40)                          

        f.make_file(file_name, bal_1, bal_2)

    
    
    day   = int(datetime.now().strftime("%d"))                   #data about day, month and year  
    month = int(datetime.now().strftime("%m"))
    year  = int(datetime.now().strftime("%y"))

    last_day = int(f.l_day(file_name)) + 1                       #the number of the next day after the last writing to the file



    with open(file_name, 'a') as file:                           #writing sums from last_day to today 
        
        while last_day <= day:                                   
            wtf = f.write_to_file(file, last_day, day, month)
            sm = input(f"Sum for {wtf} >>> ")
            file.write(f"{wtf} - {sm}\n")

            last_day += 1



    summ  = f.add(file_name)                                     #sum of all spendings
    start = f.init_amo(file_name)                                #start sum from top of the file
    diff  = start - summ                                         #the difference between start sum and sum of all spendings

    _, cnt_day = monthrange(year, month)


 
    if day == cnt_day:                                          
        last_write(file_name, start, summ, diff)                 #writing final results to the end of file
        f.print_result(start, summ, diff)                        #print of the results for today
    else:
        f.print_result(start, summ, diff)                        #same thing



if __name__ == "__main__":
    main()
