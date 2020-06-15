# soal 1
print("\nsoal 1:")
print(
    "List bisa berisi tipe data apapun dan tidak harus semua data berisi tipe data yang sama"
)

# soal 2
print("\nsoal 2:")
a = ["1", "13b", "aa1", 1.32, 22.1, 2.34]
# slicing list
# quotes will dissapear
# so i added the singel quotes manually (because list function or looping is not already trained)
print("'{}', '{}', {}, {}".format(*a[1:-1]))

# if allowed to use replace method
print("{}".format(a[1:-1]).replace("]", "").replace("[", ""))

# soal 3
print("\nsoal 3:")
a = [1.32, 22.1, 2.34]
b = ["1", "13b", "aa1"]
c = [3, 40, 100]
# combine list
print("{}".format(a + c + b))

# soal 4
print("\nsoal 4:")
a = [[5, 9, 8], [0, 0, 6]]
# subsetting
print(a[1][1:3])

# without brackets
print("{}, {}".format(*a[1][1:3]))

# soal 5
print("\nsoal 5:")
p = [0, 5, 2, 10, 4, 9]
# ordered list
print(sorted(p, reverse=False))
# ordered list without brackets
print("{}".format(sorted(p, reverse=False)).replace("[", "").replace("]", ""))
# get max value of list
print(max(p))

# soal 6
print("\nsoal 6:")
a = [1, 3, 5]
b = [5, 1, 3]
# combine list
print(b + a)

# without brackets
print("{}".format(b + a).replace("[", "").replace("]", ""))


# soal 7
print("\nsoal 7:")
a = [[5, 9, 8], [0, 0, 6]]
# change list value
a[0][2] = 10
# change list value
a[1][0] = 11
print("{}".format(a[0] + a[1]))

# soal 8
print("\nsoal 8:")
areas = [
    "hallway",
    11.25,
    "kitchen",
    18.0,
    "chill zone",
    20.0,
    "bedroom",
    10.75,
    "bathroom",
    10.50,
    "poolhouse",
    24.5,
    "garage",
    15.45,
]

# Hilangkan elemen yang bernilai "bathroom" dan 10.50 dalam satu statement code
del areas[areas.index("bathroom")]
del areas[areas.index(10.5)]
print(areas)
