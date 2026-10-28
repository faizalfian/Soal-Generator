---
id: "SOAL-20261028-001"
kategori: "pemrograman"
subjek: "cpp"
materi: "array-1d-for-loop"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 11
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T09:31:00+07:00"
tags: ["cpp", "array-1d", "for-loop", "linear-search", "swapping", "bubble-sort-prep"]
---

# Modul Latihan Mandiri: Pemrograman Dasar C++ (Array 1 Dimensi & For Loop)

**Aturan Pengerjaan untuk Siswa:**
1. Kerjakan seluruh soal secara berurutan dari **Bagian 1** hingga **Bagian 4** menggunakan komputer masing-masing.
2. Seluruh kode cukup ditulis di dalam fungsi `int main()`.
3. Gunakan deklarasi *C-style array* (contoh: `int arr[100];` atau `int arr[n];`).
4. Perhatikan perbedaan antara **indeks elemen (`i`)** dan **nilai/isi elemen (`arr[i]`)**.

---

## BAGIAN 1: Pemanasan & Pemantapan Indeks vs Nilai

### Soal 1: Cetak Array secara Terbalik (Reverse Print)
**Deskripsi Masalah:**  
Buatlah program yang menerima sejumlah $N$ bilangan bulat ke dalam sebuah array, kemudian menampilkan kembali seluruh elemen array tersebut mulai dari **elemen paling belakang (indeks terakhir)** menuju **elemen paling depan (indeks ke-0)**.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (banyaknya elemen).
- Baris kedua berisi $N$ buah bilangan bulat yang dipisahkan spasi.
- Output berupa barisan angka yang dicetak terbalik, dipisahkan oleh spasi.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    10 20 30 40 50
    ```
  - Output:
    ```text
    50 40 30 20 10
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    7 3 9 1
    ```
  - Output:
    ```text
    1 9 3 7
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    99
    ```
  - Output:
    ```text
    99
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Ingat bahwa array dengan panjang $N$ memiliki indeks dari `0` sampai `N - 1`. Untuk mencetak mundur, mulailah perulangan `for` dari `i = n - 1`, dengan syarat berhenti `i >= 0`, dan lakukan pengurangan `i--` di setiap langkah.

---

### Soal 2: Filter Nilai Genap dan Ganjil (Nilai vs Indeks)
**Deskripsi Masalah:**  
Pada latihan sebelumnya kamu telah memisahkan elemen berdasarkan *indeks* genap dan ganjil. Kali ini, pisahkan elemen array berdasarkan **ISI/NILAI angkanya**! Tampilkan baris pertama berisi angka-angka yang **bernilai genap**, dan baris kedua berisi angka-angka yang **bernilai ganjil**.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ buah bilangan bulat positif.
- Output terdiri dari 2 baris: baris pertama untuk nilai genap, baris kedua untuk nilai ganjil.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $1 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    15 8 22 7 10 3
    ```
  - Output:
    ```text
    Nilai Genap: 8 22 10
    Nilai Ganjil: 15 7 3
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    1 3 5 7 9
    ```
  - Output:
    ```text
    Nilai Genap: 
    Nilai Ganjil: 1 3 5 7 9
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    2 4 6 8
    ```
  - Output:
    ```text
    Nilai Genap: 2 4 6 8
    Nilai Ganjil: 
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Jangan mengecek `i % 2 == 0` (itu mengecek nomor indeks). Ceklah isi kotaknya menggunakan `if (arr[i] % 2 == 0)`. Gunakan dua buah `for` loop terpisah: loop pertama untuk mencetak yang bernilai genap, dan loop kedua untuk mencetak yang bernilai ganjil.

---

### Soal 3: Penghitung Siswa yang Lulus KKM (Counting)
**Deskripsi Masalah:**  
Seorang guru memiliki daftar nilai ujian dari $N$ siswa. Kriteria Ketuntasan Minimal (KKM) adalah **75**. Buatlah program untuk menghitung **berapa banyak siswa** yang berhasil lulus (mendapat nilai $≥ 75$) dan berapa banyak siswa yang harus mengikuti remedial (nilai $< 75$).

**Format Input & Output:**
- Baris pertama berisi jumlah siswa $N$.
- Baris kedua berisi $N$ nilai ujian siswa.
- Output menampilkan jumlah siswa lulus dan jumlah siswa remedial.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $0 ≤ nilai[i] ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    7
    80 65 75 90 50 74 100
    ```
  - Output:
    ```text
    Lulus: 4
    Remedial: 3
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    75 80 85 90
    ```
  - Output:
    ```text
    Lulus: 4
    Remedial: 0
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    40 50 60
    ```
  - Output:
    ```text
    Lulus: 0
    Remedial: 3
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Buat dua variabel penghitung sebelum loop dimulai, yaitu `int lulus = 0;` dan `int remedial = 0;`. Di dalam loop `for`, periksa setiap `nilai[i]`. Jika `nilai[i] >= 75`, tambahkan `lulus++`, jika tidak, tambahkan `remedial++`.

---

## BAGIAN 2: Akumulasi & Pencarian Nilai Ekstremum

### Soal 4: Total dan Rata-Rata Nilai Array
**Deskripsi Masalah:**  
Diberikan sebuah array berisi $N$ buah bilangan bulat. Hitunglah **jumlah total (sum)** dari seluruh elemen di dalam array tersebut beserta **nilai rata-ratanya (average)** dalam bentuk bilangan desimal (`float` / `double`).

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Baris pertama output adalah `Total: <hasil_total>`, baris kedua adalah `Rata-rata: <hasil_rata_rata>`.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $0 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    10 20 30 40 50
    ```
  - Output:
    ```text
    Total: 150
    Rata-rata: 30
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    10 15 20 22
    ```
  - Output:
    ```text
    Total: 67
    Rata-rata: 16.75
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    100 90 95
    ```
  - Output:
    ```text
    Total: 285
    Rata-rata: 95
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Siapkan variabel `int total = 0;` di luar loop. Di setiap putaran loop, tambahkan isi elemen ke dalam total: `total = total + arr[i];`. Setelah loop selesai, hitung rata-rata dengan `(double)total / n`.

---

### Soal 5: Mencari Nilai Tertinggi (Maximum)
**Deskripsi Masalah:**  
Diberikan sebuah array berisi $N$ bilangan bulat. Temukan dan tampilkan **angka terbesar (maksimum)** yang ada di dalam array tersebut!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa satu angka terbesar di dalam array.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    12 45 7 89 34 23
    ```
  - Output:
    ```text
    Nilai Terbesar: 89
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    -10 -5 -20 -2 -50
    ```
  - Output:
    ```text
    Nilai Terbesar: -2
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    50 50 50 50
    ```
  - Output:
    ```text
    Nilai Terbesar: 50
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Anggaplah elemen pertama sebagai nilai terbesar sementara: `int maks = arr[0];`. Kemudian buat loop dari `i = 1` hingga `n - 1`. Di dalam loop, bandingkan: jika `arr[i] > maks`, maka perbarui nilai `maks = arr[i];`.

---

### Soal 6: Nilai Terkecil Beserta Posisi Indeksnya
**Deskripsi Masalah:**  
Diberikan sebuah array berisi $N$ bilangan bulat yang semuanya berbeda. Carilah **nilai terkecil (minimum)** di dalam array tersebut, sekaligus tampilkan **pada indeks ke berapa** nilai terkecil itu berada!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output menampilkan nilai terkecil dan indeks lokasinya (indeks dimulai dari 0).

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    40 15 80 10 25
    ```
  - Output:
    ```text
    Nilai Terkecil: 10
    Berada di indeks: 3
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    5 12 19 20
    ```
  - Output:
    ```text
    Nilai Terkecil: 5
    Berada di indeks: 0
    ```
- **Test Case 3:**
  - Input:
    ```text
    6
    90 70 50 30 20 10
    ```
  - Output:
    ```text
    Nilai Terkecil: 10
    Berada di indeks: 5
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Selain menyimpan `int minVal = arr[0];`, buat juga variabel `int indeksMin = 0;`. Saat di dalam loop ditemukan `arr[i] < minVal`, perbarui kedua variabel tersebut: `minVal = arr[i];` dan `indeksMin = i;`.

---

## BAGIAN 3: Penerapan Pencarian Mandiri (Linear Search)

### Soal 7: Pencarian Angka Target (Linear Search Dasar)
**Deskripsi Masalah:**  
Diberikan sebuah array dengan $N$ elemen dan sebuah angka target $X$ yang ingin dicari. Periksalah satu per satu elemen array dari awal hingga akhir. Jika angka $X$ ditemukan, tampilkan indeks pertama tempat angka tersebut ditemukan. Jika sampai akhir array angka $X$ tidak ditemukan, tampilkan `"TIDAK DITEMUKAN"`.

**Format Input & Output:**
- Baris pertama berisi jumlah elemen $N$.
- Baris kedua berisi $N$ bilangan bulat elemen array.
- Baris ketiga berisi satu bilangan bulat $X$ (angka yang dicari).
- Output berupa indeks ditemukannya $X$, atau pesan `"TIDAK DITEMUKAN"`.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $-1000 ≤ arr[i], X ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    14 28 9 35 42 19
    35
    ```
  - Output:
    ```text
    Ditemukan pada indeks: 3
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    10 20 30 40 50
    99
    ```
  - Output:
    ```text
    TIDAK DITEMUKAN
    ```
- **Test Case 3:**
  - Input:
    ```text
    5
    7 12 7 19 7
    7
    ```
  - Output:
    ```text
    Ditemukan pada indeks: 0
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Buat variabel penanda `int posisi = -1;` sebelum loop. Telusuri array dengan `for`. Jika `arr[i] == x`, simpan `posisi = i;` lalu hentikan loop dengan perintah `break;`. Setelah loop selesai, cek apakah `posisi != -1`.

---

### Soal 8: Menghitung Frekuensi Kemunculan Angka
**Deskripsi Masalah:**  
Terkadang sebuah angka muncul lebih dari satu kali di dalam array. Buatlah program untuk menghitung **berapa kali** angka target $X$ muncul di dalam array berukuran $N$.

**Format Input & Output:**
- Baris pertama berisi jumlah elemen $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Baris ketiga berisi bilangan bulat $X$ yang ingin dihitung kemunculannya.
- Output berupa jumlah kemunculan angka $X$.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $0 ≤ arr[i], X ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    8
    5 2 8 5 9 5 1 5
    5
    ```
  - Output:
    ```text
    Angka 5 muncul sebanyak 4 kali
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    1 2 3 4 5
    9
    ```
  - Output:
    ```text
    Angka 9 muncul sebanyak 0 kali
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    7 7 7 7
    7
    ```
  - Output:
    ```text
    Angka 7 muncul sebanyak 4 kali
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Sama seperti Linear Search, tetapi jangan gunakan `break`. Buat variabel `int frekuensi = 0;`. Setiap kali `arr[i] == x` bernilai benar, tambahkan `frekuensi++`.

---

## BAGIAN 4: Jembatan Menuju Bubble Sort (Swapping & Perbandingan)

### Soal 9: Menukar Isi Dua Variabel (Konsep Dasar Swap)
**Deskripsi Masalah:**  
Sebelum mengurutkan array, kita harus mahir menukar isi dua buah wadah/variabel. Buatlah program yang menerima dua bilangan bulat `A` dan `B`, menukar isi variabel `A` dan `B` menggunakan variabel bantuan `temp`, lalu mencetak nilai `A` dan `B` setelah ditukar!

**Format Input & Output:**
- Input terdiri dari dua bilangan bulat `A` dan `B`.
- Output menampilkan nilai `A` dan `B` sebelum dan sesudah ditukar.

**Batasan (Constraints):**
- $-1000 ≤ A, B ≤ 1000$
- Wajib menukar isi variabel di memori menggunakan variabel ke-3 (`temp`), bukan sekadar membalik urutan `cout`.

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    10 25
    ```
  - Output:
    ```text
    Sebelum: A = 10, B = 25
    Sesudah: A = 25, B = 10
    ```
- **Test Case 2:**
  - Input:
    ```text
    99 1
    ```
  - Output:
    ```text
    Sebelum: A = 99, B = 1
    Sesudah: A = 1, B = 99
    ```
- **Test Case 3:**
  - Input:
    ```text
    -5 5
    ```
  - Output:
    ```text
    Sebelum: A = -5, B = 5
    Sesudah: A = 5, B = -5
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Bayangkan menukar air di gelas A dan gelas B. Kamu butuh gelas kosong C (`temp`):  
> 1. Tuang A ke temp (`int temp = a;`)  
> 2. Tuang B ke A (`a = b;`)  
> 3. Tuang temp ke B (`b = temp;`)

---

### Soal 10: Menukar Elemen Pertama dan Terakhir Array
**Deskripsi Masalah:**  
Diberikan sebuah array berukuran $N$. Tukarlah isi elemen paling depan (**indeks ke-0**) dengan elemen paling belakang (**indeks ke-(N-1)**), kemudian cetak seluruh isi array setelah proses penukaran tersebut!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa isi array setelah elemen pertama dan terakhirnya ditukar.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    90 20 30 40 10
    ```
  - Output:
    ```text
    10 20 30 40 90
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    1 2 3 4
    ```
  - Output:
    ```text
    4 2 3 1
    ```
- **Test Case 3:**
  - Input:
    ```text
    2
    55 77
    ```
  - Output:
    ```text
    77 55
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Terapkan rumus swap dengan variabel `temp` pada `arr[0]` dan `arr[n - 1]`. Setelah ditukar, gunakan loop `for` dari `0` sampai `n - 1` untuk mencetak seluruh array.

---

### Soal 11: Satu Putaran Gelembung (1-Pass Bubble)
**Deskripsi Masalah:**  
Ini adalah langkah inti dari algoritma **Bubble Sort**! Diberikan sebuah array berukuran $N$. Lakukan **satu kali perjalanan loop** dari indeks `0` sampai `N - 2`. Pada setiap langkah `i`, bandingkan elemen `arr[i]` dengan elemen di sebelah kanannya yaitu `arr[i + 1]`.  
Jika `arr[i] > arr[i + 1]` (angka kiri lebih besar dari angka kanan), **tukar posisi keduanya (swap)**! Setelah satu kali loop selesai, cetak seluruh isi array dan amati di mana posisi angka terbesarnya sekarang.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa isi array setelah melalui 1 putaran penggeseran gelembung.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    50 10 40 20 30
    ```
  - Output:
    ```text
    10 40 20 30 50
    ```
- **Test Case 2:**
  - Input:
    ```text
    6
    8 3 9 2 5 1
    ```
  - Output:
    ```text
    3 8 2 5 1 9
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    10 20 30 40
    ```
  - Output:
    ```text
    10 20 30 40
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Mengapa batas loop hanya `i < n - 1` (sampai indeks `n - 2`)? Karena di dalam loop kita mengakses `arr[i + 1]`. Jika `i` sampai `n - 1`, maka `arr[i + 1]` akan mengakses luar batas array (*out of bounds*).  
> Di dalam loop:
> ```cpp
> if (arr[i] > arr[i + 1]) {
>     int temp = arr[i];
>     arr[i] = arr[i + 1];
>     arr[i + 1] = temp;
> }
> ```
> Perhatikan bahwa setelah loop ini selesai, angka paling besar dijamin telah "mengapung" ke indeks paling ujung kanan (`arr[n - 1]`)!

---
---

# Kunci Jawaban & Pembahasan (Pegangan Pengajar)

### Pembahasan Soal 1: Cetak Array secara Terbalik
**Penjelasan Langkah demi Langkah:**
1. Baca ukuran array `n`, lalu baca tiap elemen dengan loop maju (`0` s/d `n - 1`).
2. Gunakan loop kedua yang berjalan mundur dari indeks terakhir (`n - 1`) turun hingga indeks pertama (`0`).

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Loop mundur dari indeks terakhir (n - 1) ke 0
    for (int i = n - 1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 2: Filter Nilai Genap dan Ganjil
**Penjelasan Langkah demi Langkah:**
1. Simpan seluruh input ke dalam `arr`.
2. Untuk memfilter berdasarkan **nilai**, kita memeriksa sisa bagi elemen terhadap 2: `arr[i] % 2 == 0`.
3. Lakukan loop pertama khusus mencetak yang genap, lalu loop kedua khusus mencetak yang ganjil.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Nilai Genap: ";
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            cout << arr[i] << " ";
        }
    }
    cout << endl;

    cout << "Nilai Ganjil: ";
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0) {
            cout << arr[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 3: Penghitung Siswa yang Lulus KKM
**Penjelasan Langkah demi Langkah:**
1. Inisialisasi variabel `lulus = 0` dan `remedial = 0` sebelum perulangan dimulai.
2. Telusuri setiap elemen array, gunakan percabangan `if-else` dengan batas nilai `75`.
3. Cetak hasil penghitungan setelah loop berakhir.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int nilai[100];
    for (int i = 0; i < n; i++) {
        cin >> nilai[i];
    }

    int lulus = 0;
    int remedial = 0;

    for (int i = 0; i < n; i++) {
        if (nilai[i] >= 75) {
            lulus++;
        } else {
            remedial++;
        }
    }

    cout << "Lulus: " << lulus << endl;
    cout << "Remedial: " << remedial << endl;

    return 0;
}
```

---

### Pembahasan Soal 4: Total dan Rata-Rata Nilai Array
**Penjelasan Langkah demi Langkah:**
1. Gunakan variabel akumulator `total = 0`.
2. Tambahkan setiap elemen `arr[i]` ke variabel `total` di dalam loop.
3. Lakukan *type casting* `(double)total / n` agar pembagian menghasilkan angka desimal yang akurat, bukan pembagian bilangan bulat.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int total = 0;
    for (int i = 0; i < n; i++) {
        total = total + arr[i];
    }

    double rataRata = (double)total / n;

    cout << "Total: " << total << endl;
    cout << "Rata-rata: " << rataRata << endl;

    return 0;
}
```

---

### Pembahasan Soal 5: Mencari Nilai Tertinggi (Maximum)
**Penjelasan Langkah demi Langkah:**
1. Jangan menginisialisasi `maks = 0` karena jika semua isi array bernilai negatif, hasilnya akan salah. Inisialisasikan dengan elemen pertama: `int maks = arr[0];`.
2. Bandingkan `maks` dengan elemen mulai dari indeks `1` hingga `n - 1`. Jika ditemukan elemen yang lebih besar, perbarui nilai `maks`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int maks = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > maks) {
            maks = arr[i];
        }
    }

    cout << "Nilai Terbesar: " << maks << endl;

    return 0;
}
```

---

### Pembahasan Soal 6: Nilai Terkecil Beserta Posisi Indeksnya
**Penjelasan Langkah demi Langkah:**
1. Simpan nilai awal `minVal = arr[0]` dan posisinya `indeksMin = 0`.
2. Setiap kali kondisi `arr[i] < minVal` terpenuhi, kita mencatat nilai barunya sekaligus menyimpan nomor indeks `i` saat itu.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int minVal = arr[0];
    int indeksMin = 0;

    for (int i = 1; i < n; i++) {
        if (arr[i] < minVal) {
            minVal = arr[i];
            indeksMin = i;
        }
    }

    cout << "Nilai Terkecil: " << minVal << endl;
    cout << "Berada di indeks: " << indeksMin << endl;

    return 0;
}
```

---

### Pembahasan Soal 7: Pencarian Angka Target (Linear Search Dasar)
**Penjelasan Langkah demi Langkah:**
1. Gunakan variabel `posisi = -1` sebagai penanda awal bahwa angka belum ditemukan (karena indeks array tidak mungkin bernilai `-1`).
2. Telusuri array dari indeks `0` sampai `n - 1`. Jika `arr[i] == x`, catat `posisi = i` dan keluar dari loop menggunakan `break`.
3. Di luar loop, periksa apakah `posisi` masih `-1` atau sudah berubah.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, x;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cin >> x;

    int posisi = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            posisi = i;
            break; // Hentikan pencarian karena sudah ketemu pertama kali
        }
    }

    if (posisi != -1) {
        cout << "Ditemukan pada indeks: " << posisi << endl;
    } else {
        cout << "TIDAK DITEMUKAN" << endl;
    }

    return 0;
}
```

---

### Pembahasan Soal 8: Menghitung Frekuensi Kemunculan Angka
**Penjelasan Langkah demi Langkah:**
1. Buat variabel penghitung `frekuensi = 0`.
2. Telusuri seluruh elemen array dari awal hingga akhir tanpa `break` agar semua kemunculan angka `x` terhitung.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, x;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cin >> x;

    int frekuensi = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            frekuensi++;
        }
    }

    cout << "Angka " << x << " muncul sebanyak " << frekuensi << " kali" << endl;

    return 0;
}
```

---

### Pembahasan Soal 9: Menukar Isi Dua Variabel (Konsep Dasar Swap)
**Penjelasan Langkah demi Langkah:**
1. Jika kita langsung menulis `a = b;`, maka nilai asli `a` akan tertimpa dan hilang.
2. Oleh sebab itu, amankan nilai `a` terlebih dahulu ke dalam variabel `temp`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << "Sebelum: A = " << a << ", B = " << b << endl;

    int temp = a;
    a = b;
    b = temp;

    cout << "Sesudah: A = " << a << ", B = " << b << endl;

    return 0;
}
```

---

### Pembahasan Soal 10: Menukar Elemen Pertama dan Terakhir Array
**Penjelasan Langkah demi Langkah:**
1. Elemen pertama selalu berada di `arr[0]` dan elemen terakhir berada di `arr[n - 1]`.
2. Gunakan teknik `temp` untuk menukar kedua elemen tersebut, lalu tampilkan isi array dengan loop.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Menukar elemen indeks ke-0 dengan indeks ke-(n-1)
    int temp = arr[0];
    arr[0] = arr[n - 1];
    arr[n - 1] = temp;

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 11: Satu Putaran Gelembung (1-Pass Bubble)
**Penjelasan Langkah demi Langkah:**
1. Loop berjalan dari `i = 0` hingga `i < n - 1` (berhenti satu langkah sebelum elemen terakhir agar `arr[i + 1]` tetap valid).
2. Di setiap langkah, kita membandingkan dua elemen bersebelahan: `arr[i]` dan `arr[i + 1]`.
3. Jika elemen kiri lebih besar dari elemen kanan, kita lakukan pertukaran (*swap*). Hasilnya, angka paling besar akan terdorong terus ke kanan hingga menempati posisi terakhir (`arr[n - 1]`).
4. *Catatan Pengajar untuk Pertemuan Berikutnya:* Ketika siswa sudah berhasil mengerjakan soal ini, tunjukkan bahwa **Bubble Sort** hanyalah membungkus loop ini di dalam satu loop `for` lagi sebanyak `n - 1` kali!

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 1-Pass Bubble: menggeser nilai terbesar ke posisi paling ujung kanan
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```
