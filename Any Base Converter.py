digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def UpdateBase(number, base):
    for digit in number:
        if digit not in digits[:base]:
            if digit in digits:
                print(f"The number you input contains a character ({digit}) that isn't included in the base specified ({base})")
                base = int(input(f"Input new base (>{digits.index(digit)}): "))
            else:
                print(f"The number you input contain an unrecognised character ({digit})")
                number = input("Input new number: ")
    return number, base

def DecToOther(number, base):
    result = ""
    if base < 1 or base > len(digits) or type(number) != int:
        return "0"
    if base == 1:
        return digits[0]*(number+1)
    while number != 0:
        result = digits[number%base] + result
        number = number // base
    return result

def AnyToDec(number, base):
    result = 0
    number, base = UpdateBase(number, base)
    if base < 1 or base > len(digits) or type(number) != str:
        return 0
    if base == 1:
        return len(number)-1
    for digit in range(len(number)):
        result += digits.index(number[::-1][digit])*base**digit
    return result

def AnyConvert(number, origbase, finalbase):
    return DecToOther(AnyToDec(str(number.upper()), int(origbase)), int(finalbase))

while True:
    number = input("Input number: ")
    origbase = input("Input original base: ")
    finalbase = input("Input final base: ")
    print("Result:", AnyConvert(number, origbase, finalbase), "\n")
