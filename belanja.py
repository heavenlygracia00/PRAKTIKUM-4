
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

print("a. Hari pertama:", hari_pertama)
print("   Hari kedua:", hari_kedua)

hari_kedua.add("keju")
print("\nb. Setelah tambah keju di hari kedua:", hari_kedua)

sama = hari_pertama & hari_kedua
print("\nc. Barang yang sama:", sama)

hanya_hari1 = hari_pertama - hari_kedua
print("d. Hanya dibeli hari pertama:", hanya_hari1)

hari_pertama.remove("garam")
print("\ne. Hari pertama setelah hapus garam:", hari_pertama)

hanya_hari2 = hari_kedua - hari_pertama
print("f. Hanya dibeli hari kedua:", hanya_hari2)

tidak_sama = hari_pertama ^ hari_kedua
print("g. Barang yang tidak sama:", tidak_sama)

print("\nh. Semua keperluan hari pertama:")
for barang in hari_pertama:
    print("-", barang)

print("\ni. Semua keperluan hari kedua:")
for barang in hari_kedua:
    print("-", barang)