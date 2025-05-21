# judul


# fitur
* Dashboard
* Berita Emas
* Rata-Rata Pergerakan Emas

# Pengertian Moving Average
Moving Average (MA) atau rata-rata bergerak adalah metode statistik yang digunakan untuk menghaluskan data dalam suatu periode waktu tertentu, dengan cara menghitung rata-rata nilai data secara bertahap.

# Tujuan
Menggunakan Simple Moving Average (SMA) untuk melihat tren jangka pendek hingga menengah terhadap harga emas per jam, selama 3 hari (19–21 Mei 2025).

# Metode
Kita hitung rata-rata bergerak (moving average) dengan window (jendela) berikut:
SMA 3 jam: sangat sensitif, cepat tangkap perubahan.
SMA 6 jam: moderat, cocok untuk tren intraday.
SMA 12 jam: lebih halus, untuk tren umum harian.

# Hasil Analisis
1. Tren Umum
Hari 1 (19 Mei 2025):
Harga cenderung naik dari jam 00:00 ke puncak sekitar jam 10:00–13:00.
Setelah itu terjadi penurunan bertahap sampai akhir hari.
Hari 2 (20 Mei 2025):
Harga relatif stabil di pagi hingga siang, namun terjadi penurunan signifikan mulai sore hari (jam 15:00 ke bawah).
Harga menyentuh titik rendah baru dibanding hari sebelumnya.
Hari 3 (21 Mei 2025):
Harga tetap lemah dan fluktuatif, cenderung datar tapi sedikit membaik di malam hari.

2. Moving Average Insights
SMA 3 jam:
Menyentuh harga asli lebih sering → menunjukkan perubahan jangka pendek.
Sinyal beli/jual cepat tapi berpotensi false signal (karena terlalu sensitif).

SMA 6 jam:
Lebih mulus, tetap menangkap puncak di hari pertama dan penurunan bertahap berikutnya.
Cukup stabil sebagai panduan entry/exit intraday.

SMA 12 jam:
Lebih lambat bereaksi, namun tepat menunjukkan tren umum turun dari 19 ke 21 Mei.
Cocok untuk melihat bahwa tren harga emas sedang menurun perlahan dalam 3 hari terakhir.

# Penjelasan Fungsi Untuk Memuat Data
1. Fungsi Load Data
    Ini mendefinisikan fungsi bernama load_data, yang tidak menerima parameter. Fungsinya adalah untuk memuat dan menyiapkan data dari file CSV agar siap digunakan dalam analisis atau visualisasi.
2. Baris 2
    Fungsi pd.read_csv() dari pandas digunakan untuk membaca file CSV.
    'data_harga.csv' adalah nama file yang berisi data harga emas per jam.
    File ini harus berada di folder yang sama dengan script kamu (kecuali jika kamu tulis path lengkap).
    Hasilnya adalah DataFrame data dengan dua kolom: Tanggal dan Harga.
3. Baris 3
    Ini mengubah kolom 'Tanggal' dari teks/string menjadi tipe datetime.
    Ini penting supaya Python bisa mengerti bahwa itu adalah waktu → memungkinkan kamu:
    Melakukan sort berdasarkan waktu
    Membuat rolling window (moving average)
    Plot waktu secara otomatis
4. Baris 4
    Menjadikan kolom 'Tanggal' sebagai index DataFrame.
    Dengan menjadikan waktu sebagai index, kamu bisa:
    Lebih mudah menghitung moving average berdasarkan waktu
    Plot grafik waktu lebih rapi
    Melakukan filter berdasarkan tanggal
5. Baris 5
    Mengembalikan data yang sudah diproses (dengan index waktu) ke pemanggil fungsi.

# Penjelasan Fungsi Utama
1. Fungsi main(): Ini adalah fungsi utama yang mengatur tampilan dan interaksi pengguna di dashboard.
 -Pengaturan Halaman: Mengatur konfigurasi halaman dan memeriksa status sesi untuk menentukan halaman mana yang ditampilkan.

 -Navigasi: Menyediakan navigasi sidebar untuk memilih antara "Dashboard Utama" dan "Harga Emas".

2. Interaktivitas dengan Slider:
 -Menambahkan slider untuk memilih rentang tanggal yang memungkinkan pengguna untuk memfilter data berdasarkan tanggal yang diinginkan.
 -Menggunakan st.slider() untuk memilih rentang tanggal, yang kemudian digunakan untuk menyaring data.
3. Menampilkan Grafik dan Statistik: Menampilkan grafik harga emas, statistik deskriptif, dan berita terbaru.

4. Tombol Unduh: Menyediakan tombol untuk mengunduh data yang telah difilter dalam format CSV.