# expense_tracker

## 1. Judul/Tema Aplikasi

**expense_tracker**

---

## 2. Stakeholder/User

Orang yang ingin melakukan manajemen keuangan pribadi dengan rapi.

---

## 3. Deskripsi Aplikasi

**expense_tracker** adalah aplikasi manajemen pengeluaran harian yang ditulis menggunakan bahasa pemrograman **Python** dan dapat dijalankan melalui **terminal**.

Aplikasi ini dibuat untuk memenuhi **Capstone Project Module 1** pada program **Data Science Purwadhika**.

---

## 4. Tujuan Pembuatan Aplikasi

Aplikasi ini dibuat untuk membantu pengguna melakukan **tracking** dan **kontrol** terhadap pengeluarannya.

---

## 5. Penjelasan Fitur

Fitur yang tersedia dalam aplikasi ini adalah:

1. Menampilkan semua data pengeluaran.
2. Menampilkan data pengeluaran berdasarkan filter tanggal dan kategori.
3. Menambah data pengeluaran.
4. Mengedit data pengeluaran.
5. Memberikan warning ketika pengeluaran di suatu hari melebihi budget yang ditetapkan.
6. Menghapus data pengeluaran tertentu.
7. Menampilkan ringkasan total pengeluaran berdasarkan hari.
8. Menampilkan ringkasan total pengeluaran berdasarkan bulan.
9. Menampilkan kategori pengeluaran terbesar.
10. Melakukan pengaturan atau mengubah budget harian.
11. Beberapa validasi input untuk menjaga data tetap rapi dan meng-handle error

---

## 6. Flow Chart

Flow chart aplikasi dapat dilihat melalui link berikut:

[Flow Chart expense_tracker](https://drive.google.com/file/d/1asmsALSbTvFfGqp86PoJ9y0kESX8xeKy/view?usp=sharing)

---

## 7.Minimum Requirement

- Python ver 3.14.4
- VS Code
- datetime library

---

## 8. Limitasi Aplikasi

Aplikasi **expense_tracker** masih memiliki beberapa keterbatasan, yaitu:

1. **Data belum tersimpan permanen**  
   Data pengeluaran hanya tersimpan selama program berjalan. Jika program ditutup, data baru yang ditambahkan akan hilang karena belum menggunakan file eksternal atau database.

2. **Aplikasi masih berbasis terminal**  
   Aplikasi hanya dapat dijalankan melalui terminal/command line dan belum memiliki tampilan antarmuka grafis atau GUI.

3. **Belum ada sistem login pengguna**  
   Aplikasi belum mendukung multi-user, sehingga semua data dianggap milik satu pengguna saja.

4. **Belum ada kategori tetap**  
   User masih bisa memasukkan kategori secara bebas. Hal ini dapat menyebabkan kategori yang mirip tetapi berbeda penulisan, misalnya `Makan`, `Makanan`, atau `Food`.

5. **Belum tersedia fitur ekspor data**  
   Aplikasi belum bisa mengekspor data pengeluaran ke format lain seperti `.csv`, `.xlsx`, atau `.pdf`.

6. **Belum tersedia visualisasi data**  
   Ringkasan pengeluaran masih ditampilkan dalam bentuk teks, belum dalam bentuk grafik atau chart.

7. **Budget hanya berlaku harian**  
   Fitur budget saat ini hanya digunakan untuk mengecek pengeluaran harian, belum mendukung budget mingguan, bulanan, atau per kategori.

8. **Nomor pengeluaran belum menggunakan ID permanen**  
   Nomor pengeluaran ditampilkan berdasarkan urutan data dalam list. Jika data dihapus, nomor urut dapat berubah.

9. **Belum ada fitur pencarian berdasarkan nama pengeluaran**  
   Filter data saat ini hanya tersedia berdasarkan tanggal dan kategori.

10. **Format tanggal masih manual**  
    User harus memasukkan tanggal dengan format `DD-MM-YYYY`. Jika format salah, aplikasi akan meminta user mengulang input.

---

## 9. Pengembangan Berikutnya

Selanjutnya, aplikasi ini bisa dikembangkan untuk menjawab limitasi yang ada di atas.

---

## 10. Credit

This project is created by Mitra Surya Darojat, for educational purposes.
