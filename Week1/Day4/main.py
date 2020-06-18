# Soal 1
print("\n Soal 1")
print("Every data type in python can store in list")

# Soal 2
print("\n Soal 2")
a = ["1", "13b", "aa1", 1.32, 22.1, 2.34]
# slicing list with bracket on output
print(a[:5])
# without bracket on output
print("{}".format(a[:5]).replace("[", "").replace("]", ""))

# Soal 3
print("\n Soal 3")
a = [1.32, 22.1, 2.34]
b = ["1", "13b", "aa1"]
c = [3, 40, 100]
# combine list if the output is one dimention
print("{}".format(a + c + b))
# if the output is two dimentions
print("{}".format([a, c, b]))

# Soal 4
print("\n Soal 4")
a = [[5, 9, 8], [0, 0, 6]]
# subsetting with bracket
print(a[1][1:3])
# without brackets
print("{}, {}".format(*a[1][1:3]))

# Soal 5
print("\n Soal 5")
p = [0, 5, 2, 10, 4, 9]
# ordered list with bracket
print(sorted(p, reverse=False))
# ordered list without brackets
print("{}".format(sorted(p, reverse=False)).replace("[", "").replace("]", ""))
# get max value of list
print(max(p))

# Soal 6
print("\n Soal 6")
a = [1, 3, 5]
b = [5, 1, 3]
# combine list
print(b + a)

# without brackets
print("{}".format(b + a).replace("[", "").replace("]", ""))

# Soal 7
print("\n Soal 7")
a = [[5, 9, 8], [0, 0, 6]]
# change list value
a[0][2] = 10
# change list value
a[1][0] = 11
print("{}".format(a[0] + a[1]))

# if the output is two dimentions
print("{}".format(a))

# Soal 8
print("\n Soal 8")
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

# Soal 9
print("\n Soal 9")
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [s for s in S if s % 2 == 0]
print(T)

# Soal 10
print("\n Soal 10")
europe = {"spain": "madrid", "france": "paris", "germany": "berlin", "norway": "oslo"}

# print semua key yang ada di objek europe
print(europe.keys())
# print nilai dari key france
print(europe["france"])

# Soal 11
print("\n Soal 11")
europe = {"spain": "madrid", "france": "paris", "germany": "berlin", "norway": "oslo"}

# tambahkan key itali ke objek dictionary dengan value roma
europe["itali"] = "roma"
# cek apakah itali ada di dalam objek dictionary
print(True if "itali" in europe else False)

# Soal 12
print("\n Soal 12")
europe = {
    "spain": "madrid",
    "france": "paris",
    "germany": "bonn",
    "norway": "oslo",
    "italy": "rome",
    "poland": "warsaw",
    "australia": "vienna",
}

# update nilai ibukota german ke berlin
europe.update({"germany": "berlin"})

# remove australia dari europa
europe.pop("australia", None)

print(europe)

# Soal 13
print("\n Soal 13")
country = {
    "spain": {"capital": "madrid", "population": 46.77},
    "france": {"capital": "paris", "population": 66.03},
    "germany": {"capital": "berlin", "population": 80.62},
    "norway": {"capital": "oslo", "population": 5.084},
}

# berapa populasi dari kota german?
print(country["germany"]["population"])

# update data baru, yaitu negara indonesia dengan capital jakarta dan poulasi 250
data_update = {"indonesia": {"capital": "jakarta", "population": 250.0}}
country.update(data_update)
print(country)

# Soal 14
print("\n Soal 14")
country = {
    "spain": {"capital": "madrid", "population": 46.77},
    "france": {"capital": "paris", "population": 66.03},
    "germany": {"capital": "berlin", "population": 80.62},
    "norway": {"capital": "oslo", "population": 5.084},
    "indonesia": {"capital": "jakarta", "population": 250},
}

for key, val in country.items():
    print("Ibukota {} adalah {}\n".format(key, val["capital"]))

# TAMBAHAN
print("\n TAMBAHAN : REMOVE DUPLICATE LIST")
# solusi tanpa menggunakan set
def remove_duplicate(obj_list: list) -> list:
    """
    Remove duplicate list function
    """
    new_list = obj_list.copy()
    for idx, val in enumerate(new_list):
        if new_list.count(val) > 1:
            new_list.pop(idx)
    new_list.sort()
    return new_list


# solusi dengan menggunakan set
def remove_duplicate_with_set(obj_list: list) -> list:
    """
    code Here
    """
    return list(set(obj_list))


obj_list = [1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6]
print(remove_duplicate(obj_list))
print(remove_duplicate_with_set(obj_list))

# TAMBAHAN
print("\n TAMBAHAN : CHAT BOT")

# import library
from datetime import datetime
import random

# ganti dengan sebuah nama
nama = "Sanber Learn"
# variabel tanggal
tanggal = datetime.now().day
# default variabel untuk pertanyaan tidak diketahui
default = "maaf, aku tidak tahu jawaban dari pertanyaanmu"

# Membuat objek dictionary berisi berbagai opsi jawaban

# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
    "nama saya  {0}".format(nama),
    "orang-orang memanggil saya {0}".format(nama),
    "panggil saja saya {0}".format(nama),
]

# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
    "hari ini tanggal {0}".format(tanggal),
    "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal),
]

# opsi pertanyaan yang bisa dijawab
pertanyaan = {
    "nama kamu siapa?": jawaban_nama,
    "kamu siapa?": jawaban_nama,
    "tanggal berapa hari ini?": jawaban_tanggal,
    "hari ini tanggal berapa?": jawaban_tanggal,
    "default": default,
}

# list jawaban untuk sebuah argument selain pertanyaan
statement = [
    "ceritakan lebih banyak!",
    "kenapa kamu berpikir begitu?",
    "sudah berapa lama kamu merasa seperti ini?",
    "Itu sangat menarik!",
    "oh wow!",
    ":)",
]

# respon keseluruhan
responses = {"pertanyaan": pertanyaan, "statement": statement}


# ayo buat chatbotmu
def chatbot(message: str) -> str:
    """
    Function that will return string of the aswer
    whether the message is statement or question
    """
    # check is this statement or not
    if message.find("?") >= 0:
        if message in responses["pertanyaan"]:
            return responses["pertanyaan"][message][
                int(random.uniform(0, len(responses["pertanyaan"][message])))
            ]
        else:
            return responses["pertanyaan"]["default"]
    else:
        return responses["statement"][
            int(random.uniform(0, len(responses["statement"])))
        ]


print(chatbot("Selamat Pagi"))
print(chatbot("Mau bermain bersamaku?"))
print(chatbot("nama kamu siapa?"))
print(chatbot("hari ini tanggal berapa?"))

