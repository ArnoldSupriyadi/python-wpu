# ============================================
# Penggunaan "from ... import ..." di Python
# Modul yang dipakai: modular.py (satu folder)
# ============================================

# 1. Mengambil SATU fungsi dari modul
from modular import get_profile

get_profile()   # dipanggil langsung, tanpa "modular."

print("-" * 30)


# 2. Mengambil BEBERAPA nama sekaligus, dipisah koma
from modular import name, age, is_student

print("Nama   :", name)
print("Umur   :", age)
print("Pelajar:", is_student)

print("-" * 30)


# 3. Mengambil nama lalu diberi ALIAS dengan "as"
from modular import get_profile as tampilkan_profil

tampilkan_profil()   # fungsi yang sama, hanya beda nama panggilan

print("-" * 30)


# 4. Nama hasil "from import" bisa dipakai seperti variabel biasa
tahun_depan = age + 1
print(f"{name} tahun depan berumur {tahun_depan} tahun")


# CATATAN:
# - "from modular import get_profile" TIDAK membuat nama "modular" tersedia.
#   Jadi memanggil modular.get_profile() di file ini akan NameError.
# - Titik hanya boleh di sisi KIRI kata "import":
#       from intro.modular import get_profile   -> valid (bentuk paket)
#       from modular import modular.get_profile -> SyntaxError
# - Hindari "from modular import *" karena menarik semua nama sekaligus
#   sehingga tidak jelas nama mana berasal dari modul mana.
