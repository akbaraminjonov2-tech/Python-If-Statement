a = int(input("Tomon01: "))
b = int(input("Tomon02: "))
c = int(input("Tomon03: "))

if a == b and b == c:
    print("Teng tomonli")
elif a == b or a == c or b == c:
    print("Teng yonli")
else:
    print("Turli tomonli")