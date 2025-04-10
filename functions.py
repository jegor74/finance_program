def l_day(fname: str) -> str:

    with open(fname, 'r') as file:
        for s in file:
            ld = s[:2]

    return ld




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

    with open(fname, 'w') as file:
        file.write(f"Имеется - {b1:_}\n")
        #there should be mod function
        file.write(f"Остаток с прошлого месяца - {b2:_}\n")
        file.write(f"========================================\n")
        file.write(f"00.00 - 0 (шаблон)\n")




def add(fname: str) -> int:

    with open(fname) as file:
        s = [int(x[8:]) for x in file.read().splitlines() if x[8:].isdigit()]
    
    cnt = sum(s)

    return cnt




def write_to_file(fname: str, lday: int, d: int, m: int) -> str:
    
    if lday <= 9 and m <= 9:
        return f"0{lday}.0{m}"

    elif lday > 9:
        return f"{lday}.0{m}"

    return f"{lday}.{m}"
    



def last_write(fname: str, b1: int, sm: int, df: int) -> None:

    with open(fname, 'a') as file:
        file.write(f"========================================\n")
        file.write(f"Итого потрачено: {sm:_}\n")
        file.write(f"Остаток: {b1:_} - {sm:_} = {df:_}\n")




def init_amo(fname: str) -> int:
    
    with open(fname) as file:
        s = file.readline()
        n = int(s[10:])

    return n




def print_result(st: int, s: int, d: int) -> None:
    print("========================================")
    print(f"Потрачено на данный момент: {s:_}")
    print(f"Остаток на данный момент: {st:_} - {s:_} = {d:_}")
