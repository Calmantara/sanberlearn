# Soal 1
print("\nSoal 1")
string_var = "sanber learn"
print(string_var == "sanber learn")
bool_var = False
bool2_var = True
print(bool_var != bool2_var)
int_var = 10
print(int_var > 100)

# Soal 2
print("\nSoal 2")
# and logic
int_var = 102
abc = "Logic is true" if int_var > 100 and int_var < 105 else "Logic is false"
print(abc)

# or logic with not
str_var = "You are so beautiful"
abc = str_var if str_var is not None or str_var is not "" else "String is empty"
print(abc)

# Soal 3
print("\nSoal 3")
ruangan = "Kamar"
size = 20

if ruangan.lower() == "kamar" and size > 12:
    print("Besar")
elif ruangan.lower() == "kamar" and (size > 6 and size <= 12):
    print("Sedang")
elif ruangan.lower() == "kamar" and size <= 6:
    print("Sedang")
else:
    print("Undefined")

# Soal 4
print("\nSoal 4")


def funct_comp(num: int) -> str:
    """Function that will return some criteria depends on input condition"""
    if num % 2 == 1 or (num >= 6 and num <= 20):
        return "Aneh"
    elif (num % 2 == 0 and (num >= 2 and num <= 5)) or (num % 2 == 0 and (num > 20)):
        return "Tidak Aneh"
    return "Aneh"


# function testing
for i in range(0, 25):
    print(i, funct_comp(num=i))

# Soal 5
print("\nSoal 5")

print(
    "The for statement iterates through a collection or iterable object or generator function."
)
print("The while statement simply loops until a condition is False.")

# example
for i in range(0, 10):
    # will looping with range between 0 until before 10
    print("for: ", i)

i = 0
while i < 10:
    # will looping with increment 2 until value less than 10
    print("while: ", i)
    i += 2

# Soal 6
print("\nSoal 6")
a = 10


def fungsi_while(num: int) -> None:
    """Checking the num until 0"""
    _state = True
    _num = num
    while _state:
        if _num > 0:
            print(_num)
            _num -= 1
        else:
            _num += 1
            _state = False


fungsi_while(a)

# Soal 7
print("\nSoal 7")
obj_list = [1, 16, 11, 10, 5]

for idx, elm in enumerate(obj_list):
    print(idx * elm)
