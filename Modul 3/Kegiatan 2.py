data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Membuat fungsi untuk memeriksa apakah suatu string adalah bilangan bulat
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Menggunakan filter untuk mengambil hanya nilai integer dari data
integer_values = list(filter(is_integer, ''.join(data).split()))

# Mencetak hasil
print(integer_values)
