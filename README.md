# **Finance Program** 

## **About project** 
This is my first pet-project using Python for automatization of the countig money spent for every day. There is only two Python files, because of
the ease of project. 
I was made it for practice working with files, directories and strigns. There is no benefits to use this program. 

## **Versions**

**Ver 1.0**\
-program has 2 files: *main.py* and *functions.py*\
-some phrases were written in russian, but the interface is still clear (maybe)\
-some functions can be non-optimized\
-it’s impossible to done writing for previous month if there is already another\

**Ver 2.0**\
-all phrases now in english\
-optimized some functions\
-added many comments in code\
-added descriptions in functions\

## **Quick start** 

### Download 
To start use this program, you only need to clone repository and run the program. For example, in terminal in linux: 
```
$python3 main.py
```
Programm has no interface or app, so it will work only in terminal. 

### Using 
After running this program, it will ask you to write the start ammount, and after this - to write the remaining ammount for the previos month *(if
you dont have - write 0 or smth, thats not making sense now in ver 1.0)*.

**There is example of working:** 

```
$python3 main.py

Start ammount >>> 300
remaining ammount >>> 140
========================================
Sum for 01.01 >>> 5
Sum for 01.02 >>> 7
========================================
Total sum at the moment: 12
Remaining: 300 - 12 = 288
```

The results are written to a file *finance_{month}_{year}*, that is in directory archive. The directory is in the same way, as *main.py* and *functions.py*. The last two lines will always print in terminal, but not in file if the day isn’t last in month. Otherwise, the two lines will print in terminal and will write in file. 

**Big problem:**
If there was no time to write the spending until the last day of month 23:59:59, it will impossible to work with this file, because the
new file will make. 

## **Сriticism and suggestions** 
I always will happy to see constructive criticism and any suggestions.
