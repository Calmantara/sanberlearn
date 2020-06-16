# Soal 1
print("\n Soal 1")
help(len)

# Soal 2
print("\n Soal 2")
print(
    "Function that has already defined in python as Object.",
    "So we can call it whenever we need without any external module/library",
)
arr = [1, 2, 3, 4]
# len
print("(len) array length: ", len(arr))
# max
print("(max) max element of array: ", max(arr))
# map
print("(map) array element plus 2: ", list(map(lambda x: x + 2, arr)))

# Soal 3
print("\n Soal 3")
print(
    "Method is function that object' have.",
    "For example, String object has its own method such as upper, split, join, etc.",
    "List object has its own method such as append, clear, remove, etc. \n",
    "A function is a block of code which only runs when it is called.",
    "We can pass data, known as parameters, into a function. ",
    "A function can return data as a result.",
)

# Soal 4
print("\nSoal 4")
kalimat = "Corona cepat selesai"

# gunakan method untuk mengubah nilai kalimat menjadi uppercase semua kemudian tampilkan hasilnya
print("Uppercase: {}".format(kalimat.upper()))

# gunakan method untuk menghitung berapa huruf e di dalam kalimat
print("Amount of e char: {}".format(kalimat.count("e")))

# Soal 5
print("\nSoal 5")
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# gunakan suatu method dari object list untuk menampilkan index dari nilai 20
print("Index of element 20 is {}".format(areas.index(20)))

# gunakan suatu method dari object list untuk menambahkan nilai 15.5 kedalam list ke index terakhirnya
areas.append(15.5)
print(areas)

# Soal 6
print("\nSoal 6")
obj_list = [11.25, 18.0, 20.0, 10.75, 9.50]


def mean_list(inp_list: list) -> float:
    return sum(inp_list) / len(inp_list)


print(mean_list(obj_list))

# Soal 7
print("\nSoal 7")
obj_list = [2, 4, 5, 6]
obj_pengali = [1, 2, 3]


def kali_list(in_list: list, times_list: list) -> list:
    return in_list + times_list


print(kali_list(obj_list, obj_pengali))
