# == Program Manajemen Pengeluaran Harian ==
# Tujuan: Membantu user mencatat pengeluaran sehari-hari, melihat total pengeluaran, dan mengontrol pengeluaran

print("\n=== Selamat Datang di Program Manajemen Pengeluaran Harian ===")

# Data awal disimpan dalam bentuk list of dictionary.
# Setiap dictionary mewakili satu transaksi pengeluaran.
data_pengeluaran = [
    {
    'tanggal' : '01-01-2026',
    'kategori' : 'Makan',
    'nama_pengeluaran' : 'Bakso',
    'nominal' : 25000,
    'metode_pembayaran' : 'E-Wallet',
    'catatan' : 'Makan Siang'
    },
    {
    'tanggal' : '02-01-2026',
    'kategori' : 'Minum',
    'nama_pengeluaran' : 'Air Minum Galon',
    'nominal' : 105000,
    'metode_pembayaran' : 'Cash',
    'catatan' : 'Beli di Indomaret'
    },
    {
    'tanggal' : '01-02-2026',
    'kategori' : 'Makan',
    'nama_pengeluaran' : 'Beli beras',
    'nominal' : 80000,
    'metode_pembayaran' : 'Cash',
    'catatan' : 'Belanja stok mingguan'
    }
]

# Fungsi untuk menampilkan data pengeluaran dalam format tabel
def printTable(data):
    print(f"\nDaftar Pengeluaran\n\n{"Nomor":<5} | {"Tanggal":<12} | {"Kategori":<10} | {"Nama Pengeluaran":<18} | {"Nominal":<8} | {"Metode Pembayaran":<18} | {"Catatan":<20}")
    for indeks, i in enumerate(data, start=1):
        print(f"{indeks:<5} | {i['tanggal']:<12} | {i['kategori']:<10} | {i['nama_pengeluaran']:<18} | {i['nominal']:<8} | {i['metode_pembayaran']:<18} | {i['catatan']:<20}")

def filterTanggal(data, tgl):
    hasilFilter = []
    for i in data:
        if i['tanggal'] == tgl:
            hasilFilter.append(i)
    if len(hasilFilter) > 0:
        printTable(hasilFilter)
    else:
        print('Data tidak ditemukan.')

def filterKategori(data, ktg):
    hasilFilter = []
    for i in data:
        if i['kategori'].lower() == ktg:
            hasilFilter.append(i)
    if len(hasilFilter) > 0:
        printTable(hasilFilter)
    else:
        print('Data tidak ditemukan')

def tambahData(tgl, ktg, namaPgl, nom, payment, note):
    data_pengeluaran.append({
        'tanggal' : tgl,
        'kategori' : ktg,
        'nama_pengeluaran' : namaPgl,
        'nominal' : nom,
        'metode_pembayaran' : payment,
        'catatan' : note
    })
    print("\nData berhasil ditambahkan.")

def ringkasanHarian(data, tgl):
    totalPengeluaran = 0
    for i in data:
        if i['tanggal'] == tgl:
            totalPengeluaran += i['nominal']
    if totalPengeluaran == 0:
        print("Tidak ada pengeluaran pada tanggal tersebut.")
    else:
        print(f"Total pengeluaran pada tanggal {tgl} adalah {totalPengeluaran}.")

def ringkasanBulanan(data, bln):
    totalPengeluaran = 0
    for i in data:
        # Mengambil bagian bulan dan tahun dari format DD-MM-YYYY.
        # Contoh: "01-02-2026"[3:] menghasilkan "02-2026".
        if i['tanggal'][3:] == bln:
            totalPengeluaran += i['nominal']
    if totalPengeluaran == 0:
        print("Tidak ada pengeluaran pada bulan tersebut.")
    else:
        print(f"Total pengeluaran pada bulan {bln} adalah {totalPengeluaran}.")

def pengeluaranTerbesar(data):
    # Dictionary ini menyimpan total pengeluaran untuk setiap kategori.
    # Contoh: {"Makan": 105000, "Minum": 105000}
    listKategori = {}
    for i in data:
        if i['kategori'] in listKategori:
            listKategori[i['kategori']] += i['nominal']
        else:
            listKategori[i['kategori']] = i['nominal']
    
    nominalTerbesar = 0
    for i in listKategori:
        if listKategori[i] > nominalTerbesar:
            nominalTerbesar = listKategori[i]

    listKategoriTerbesar = []       
    for i in listKategori:
        if listKategori[i] == nominalTerbesar:
            listKategoriTerbesar.append(i)
    
    print("\nKategori pengeluaran terbesar adalah sebagai berikut:")
    for i in listKategoriTerbesar:
        print(f"{i} dengan total {nominalTerbesar}")
            
budgetHarian = 100000

# Mengecek apakah total pengeluaran harian sudah melebihi budget harian
def cekBudget(data, tgl):
    totalHarian = 0

    for i in data:
        if i['tanggal'] == tgl:
            totalHarian += i['nominal']

    if totalHarian > budgetHarian:
        print(f"Peringatan! Total pengeluaran tanggal {tgl} sudah melebihi budget harian.")
        print(f"Budget: {budgetHarian}")
        print(f"Total pengeluaran: {totalHarian}")
        print(f"Kelebihan: {totalHarian - budgetHarian}")
    else:
        print(f"Sisa budget harian kamu untuk tanggal {tgl} adalah {budgetHarian - totalHarian}.")


from datetime import datetime

def validasiTanggal(tanggal):
    try:
        datetime.strptime(tanggal, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validasiBulan(bulan):
    try:
        datetime.strptime(bulan, "%m-%Y")
        return True
    except ValueError:
        return False

while True:
    print('''\n--- Menu Utama ---
1. Lihat Pengeluaran
2. Tambah Pengeluaran
3. Edit Pengeluaran
4. Hapus Pengeluaran
5. Ringkasan & Pengaturan Budget
6. Keluar''')

    menuDipilih = input('Masukkan nomor menu yang ingin dijalankan (1-6) : ')

# MENU 1: LIHAT PENGELUARAN  
    if menuDipilih == '1':
        if len(data_pengeluaran) == 0:
            print("\nData pengeluaran masih kosong.")
            continue
        while True:
            print('''\n-- Sub Menu Lihat Pengeluaran --
1. Lihat Semua Data
2. Filter Tanggal/Kategori
3. Kembali ke Menu Utama''')

            subMenuDipilih = input('Masukkan nomor sub menu yang ingin dijalankan (1-3) : ')

            if subMenuDipilih == '1':
                printTable(data_pengeluaran)
            
            elif subMenuDipilih == '2':
                while True:
                    jenisFilter = input('\nKetik \"T\" untuk Tanggal atau \"K\" untuk Kategori : ').upper()
                    if jenisFilter == 'T':
                        tanggal = input('Masukkan tanggal dengan format DD-MM-YYYY: ')
                        if not validasiTanggal(tanggal):
                            print("Format tanggal harus DD-MM-YYYY.")
                            continue
                        filterTanggal(data_pengeluaran, tanggal)
                        break
                    elif jenisFilter == 'K':
                        kategori = input('Masukkan kategori : ').lower()
                        filterKategori(data_pengeluaran, kategori)
                        break
                    else:
                        print('\nMasukkan huruf \"T\" atau \"K\" saja. Silakan ulangi.')
                        continue
            elif subMenuDipilih == '3':
                break
            else:
                print('\nMasukkan angka 1-3 saja. Silakan ulangi.\n')
                continue

# MENU 2: TAMBAH PENGELUARAN
    elif menuDipilih == '2':
        while True:
            print('''\n-- Sub Menu Tambah Pengeluaran --
1. Tambah Data Baru
2. Kembali ke Menu Utama''')
            
            subMenuDipilih = input('Masukkan nomor sub menu yang ingin dijalankan (1 atau 2) : ')
            
            if subMenuDipilih == '1':
                while True:
                    print('\nMasukkan data berikut')
                    tanggal = input('Tanggal : ')
                    if not validasiTanggal(tanggal):
                        print("Format tanggal harus DD-MM-YYYY.")
                        continue
                    
                    while True:
                        kategori = input('Kategori : ').strip().capitalize()
                        if kategori == "":
                            print("Kategori tidak boleh kosong.")
                            continue
                        else:
                            break
                    while True:
                        namaPengeluaran = input('Nama Pengeluaran : ').strip()
                        if namaPengeluaran == "":
                            print("Nama pengeluaran tidak boleh kosong.")
                            continue
                        else:
                            break

                    while True:
                        try:
                            nominal = int(input('Nominal : '))

                            if nominal <= 0:
                                print("Nominal harus lebih dari 0. Silakan ulangi.")
                                continue

                            break
                        except ValueError:
                            print("Nominal tidak boleh kosong dan harus angka bulat.")
                            continue
                    
                    while True:
                        metodePembayaran = input('Metode Pembayaran : ').strip()
                        if metodePembayaran == "":
                            print("Metode pembayaran tidak boleh kosong.")
                            continue
                        else:
                            break

                    catatan = input('Catatan : ').strip()
                    if catatan == "":
                        catatan = "-"
                    
                    tambahData(tanggal, kategori, namaPengeluaran, nominal, metodePembayaran, catatan)
                    cekBudget(data_pengeluaran, tanggal)

                    break
            
            elif subMenuDipilih == '2':
                break
            else:
                print('\nMasukkan angka 1 atau 2 saja. Silakan ulangi.\n')
                continue

# MENU 3: EDIT PENGELUARAN
    elif menuDipilih == '3':
        if len(data_pengeluaran) == 0:
            print('\nData pengeluaran masih kosong. Belum ada yang bisa diedit.')
            continue

        while True:
            print('''\n-- Sub Menu Edit Pengeluaran --
1. Edit Berdasarkan Nomor Pengeluaran
2. Kembali ke Menu Utama''')
            
            subMenuDipilih = input('Masukkan nomor sub menu yang ingin dijalankan (1 atau 2) : ')

            if subMenuDipilih == '1':
                printTable(data_pengeluaran)
                while True:
                    try:
                        nomor = int(input('\nMasukkan nomor pengeluaran : '))
                        if nomor < 1 or nomor > len(data_pengeluaran):
                            print('Nomor yang kamu masukkan tidak ada dalam data. Silakan ulangi.')
                            continue
                        else:
                            break
                    except ValueError:
                        print("Masukkan angka bulat saja. Silakan ulangi.\n")
                        continue
                
                while True:
                    print('''\nData apa yang ingin kamu ubah?
1. Tanggal
2. Kategori
3. Nama Pengeluaran
4. Nominal
5. Metode Pembayaran
6. Catatan''')
                    pilihanData = input('Ketik dan enter salah satu angka pilihan di atas : ')
                    if pilihanData == '1':
                        while True:
                            tanggalBaru = input('Masukkan tanggal baru dengan format DD-MM-YYYY : ')
                            if not validasiTanggal(tanggalBaru):
                                print("Format tanggal harus DD-MM-YYYY.")
                                continue
                            else:
                                break
                        data_pengeluaran[nomor-1]['tanggal'] = tanggalBaru
                        cekBudget(data_pengeluaran, data_pengeluaran[nomor-1]['tanggal'])
                        break
                    elif pilihanData == '2':
                        while True:
                            kategoriBaru = input('Masukkan kategori baru : ').strip().capitalize()
                            if kategoriBaru == "":
                                print("Kategori tidak boleh kosong.")
                                continue
                            else:
                                break
                        data_pengeluaran[nomor-1]['kategori'] = kategoriBaru
                        break
                    elif pilihanData == '3':
                        while True:
                            namaBaru = input('Masukkan nama pengeluaran baru : ').strip()
                            if namaBaru == "":
                                print("Nama pengeluaran tidak boleh kosong.")
                                continue
                            else:
                                break
                        data_pengeluaran[nomor-1]['nama_pengeluaran'] = namaBaru
                        break
                    elif pilihanData == '4':
                        while True:
                            try:
                                nominalBaru = int(input('Masukkan nominal pengeluaran baru : '))

                                if nominalBaru <= 0:
                                    print("Nominal harus lebih dari 0. Silakan ulangi.")
                                    continue

                                data_pengeluaran[nomor-1]['nominal'] = nominalBaru
                                cekBudget(data_pengeluaran, data_pengeluaran[nomor-1]['tanggal'])
                                break
                            except ValueError:
                                print('Input hanya bisa berupa angka bulat. Silakan ulangi.')
                                continue
                        break
                    elif pilihanData == '5':
                        while True:
                            metodeBaru = input('Masukkan metode pengeluaran baru : ').strip()
                            if metodeBaru == "":
                                print("Metode pembayaran tidak boleh kosong.")
                                continue
                            else:
                                break
                        data_pengeluaran[nomor-1]['metode_pembayaran'] = metodeBaru
                        break
                    elif pilihanData == '6':
                        catatanBaru = input('Masukkan catatan baru : ').strip()
                        if catatanBaru == "":
                            catatanBaru = "-"
                        data_pengeluaran[nomor-1]['catatan'] = catatanBaru
                        break
                    else:
                        print('\nKetik dan enter salah satu dari angka pilihan di atas saja. Silakan ulangi.\n')
                        continue
                print('\nEdit data berhasil.')

            elif subMenuDipilih == '2':
                break
            else:
                print('\nMasukkan angka 1 atau 2 saja. Silakan ulangi.\n')
                continue

# MENU 4: HAPUS PENGELUARAN
    elif menuDipilih == '4':
        if len(data_pengeluaran) == 0:
            print('\nData pengeluaran masih kosong. Belum ada yang bisa dihapus.')
            continue

        while True:
            print('''\n-- Sub Menu Hapus Pengeluaran --
1. Hapus Berdasarkan Nomor Pengeluaran
2. Kembali ke Menu Utama''')
            
            subMenuDipilih = input('Masukkan nomor sub menu yang ingin dijalankan (1 atau 2) : ')

            if subMenuDipilih == '1':
                printTable(data_pengeluaran)
                while True:
                    try:
                        nomor = int(input('\nMasukkan nomor pengeluaran : '))
                        if nomor < 1 or nomor > len(data_pengeluaran):
                            print('Nomor yang kamu masukkan tidak ada dalam data. Silakan ulangi.')
                            continue
                        else:
                            prosesAtauTidak = False
                            while True:
                                yakin = input("Apakah kamu yakin ingin menghapus data tersebut?(Ya/Tidak) : ").lower()
                                if yakin == "ya":
                                    prosesAtauTidak = True
                                    break
                                elif yakin == "tidak":
                                    break
                                else:
                                    print("Ketik dan enter \"Ya\" atau \"Tidak\" saja. Silakan ulangi.")
                            if prosesAtauTidak == True:
                                del data_pengeluaran[nomor-1]
                                print("\nData yang dipilih berhasil dihapus.")
                            break
                    except ValueError:
                        print("Masukkan angka bulat saja. Silakan ulangi.\n")
                        continue
            elif subMenuDipilih == '2':
                break
            else:
                print('\nMasukkan angka 1 atau 2 saja. Silakan ulangi.\n')
                continue

#MENU 5: RINGKASAN & PENGATURAN BUDGET
    elif menuDipilih == '5':
        
        while True:
            print('''\n-- Sub Menu Ringkasan & Pengaturan Budget --
1. Total Pengeluaran Harian
2. Total Pengeluaran Bulanan
3. Kategori Pengeluaran Terbesar
4. Atur Budget Harian
5. Kembali ke Menu Utama''')
            
            subMenuDipilih = input('Masukkan nomor sub menu yang ingin dijalankan (1-5) : ')
            if subMenuDipilih == '1':
                if len(data_pengeluaran) == 0:
                    print('\nData pengeluaran masih kosong. Belum ada ringkasan yang bisa ditampilkan.')
                    continue
                else:
                    tanggal = input("\nMasukkan tanggal dengan format DD-MM-YYYY : ")
                    if not validasiTanggal(tanggal):
                        print("Format tanggal harus DD-MM-YYYY.")
                        continue
                    ringkasanHarian(data_pengeluaran, tanggal)
                    continue
            elif subMenuDipilih == '2':
                if len(data_pengeluaran) == 0:
                    print('\nData pengeluaran masih kosong. Belum ada ringkasan yang bisa ditampilkan.')
                    continue
                else:
                    while True:
                        bulan = input("\nMasukkan bulan dan tahun dengan format MM-YYYY : ")
                        if not validasiBulan(bulan):
                            print("Format bulan harus MM-YYYY.")
                            continue
                        ringkasanBulanan(data_pengeluaran, bulan)
                        break
                    continue
            elif subMenuDipilih == '3':
                if len(data_pengeluaran) == 0:
                    print('\nData pengeluaran masih kosong. Belum ada ringkasan yang bisa ditampilkan.')
                    continue
                else:
                    pengeluaranTerbesar(data_pengeluaran)
                    continue
            elif subMenuDipilih == '4':
                print(f"\nBudget harian kamu saat ini adalah {budgetHarian}")
                while True:
                    ubahBudget = input("Apakah kamu ingin mengubah budget harian?(Ya/Tidak) : ").lower()
                    if ubahBudget == 'ya':
                        while True:
                            try:
                                budgetBaru = int(input("Silakan masukkan budget harian kamu : "))

                                if budgetBaru <= 0:
                                    print("Budget harus lebih dari 0. Silakan ulangi.")
                                    continue

                                budgetHarian = budgetBaru
                                print(f"Budget harian berhasil disimpan. Budget harian kamu sekarang adalah {budgetHarian}.")

                                break
                            except ValueError:
                                print("Masukkan angka bulat saja. Silakan ulangi.")
                                continue
                        break
        
                    elif ubahBudget == 'tidak':
                        break
                    else:
                        print("Ketik dan enter \"Ya\" atau \"Tidak\" saja. Silakan ulangi.")
                        continue
            elif subMenuDipilih == '5':
                break
            else:
                print('\nMasukkan angka 1-5 saja. Silakan ulangi.\n')
                continue

# MENU 6: KELUAR
    elif menuDipilih == '6':
        break
    else:
        print('\nMasukkan angka 1-6 saja. Silakan ulangi.\n')
        continue