def l_day(fname: str) -> str:
    """
    function for counting
    last writed day in the file.

    input  - file name: str
    output - number: str
    """
    
    with open(fname) as file:
        ld = file.readlines()[-1]        #list of lines [l1, l2, l3, ... , ln] -> ln -> first 2 symbols in ln

    return ld[:2]




##function in alpha ver
#def mod(fname: str) -> int:
#    
#    reg = "=\s\d+"
#    pat = re.compile(reg)
#
#    with open(fname) as file:
#        if pat.find(file):
#            return 




def make_file(fname: str, b1: int, b2: int) -> None:
    """
    function for making file 
    with information about
    finance in this month.

    input:
    file name: str
    start balance - b1: int
    last month balance - b2: int

    output - None
    """
    
    with open(fname, 'w') as file:
        file.write(f"Start balance - {b1:_}\n")
        #there should be mod function
        file.write(f"Balance from last month: {b2:_}\n")
        file.write("========================================\n")
        file.write(f"00.00 - 0 (filler)\n")




def add(fname: str) -> int:
    """
    function that sums all spendings.

    input  - file name: str
    output - summ: int
    """
    
    with open(fname) as file:
        s = [int(x[8:]) for x in file.read().splitlines() if x[8:].isdigit()]
    
    cnt = sum(s)

    return cnt




def write_to_file(fname: str, lday: int, d: int, m: int) -> str:
    """
    function for naming
    of every writing

    input:
    file name: str
    last day - lday: int
    day - d: int
    month - m: int

    output - name of line: str
    """
    
    if lday <= 9 and m <= 9: 
        return f"0{lday}.0{m}"            #format: 0x.0x

    elif lday > 9:
        return f"{lday}.0{m}"             #format: xx.0x

    return f"{lday}.{m}"                  #format: xx.xx
    



def last_write(fname: str, b1: int, sm: int, df: int) -> None:
    """
    function for writing the final information

    input:
    file name: str
    start balance - b1: int
    spending - sm: int
    final balance - df: int

    output - None
    """
    
    with open(fname, 'a') as file:
        file.write("========================================\n")
        file.write(f"Total spent: {sm:_}\n")
        file.write(f"Balance: {b1:_} - {sm:_} = {df:_}\n")




def init_amo(fname: str) -> int:
    """
    function for returning
    start balance

    input  - file name: str
    output - balance: int
    """
    with open(fname) as file:
        s = file.readline()        #first line in file
        n = int(s[10:])            

    return n




def print_result(st: int, s: int, d: int) -> None:
    """
    function for printing results

    input:
    start balance - st: int
    sum - s: int
    balance - d: int

    output - None
    """
    
    print(40 * "=")
    print(f"Spends at the moment: {s:_}")
    print(f"Remaining balance: {st:_} - {s:_} = {d:_}")
