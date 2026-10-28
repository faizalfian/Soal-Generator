---
id: "SOAL-20261028-007"
kategori: "pemrograman"
subjek: "cpp"
materi: "problem-solving-dekomposisi"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:25:00+07:00"
tags: ["cpp", "problem-solving", "decomposition", "algorithmic-thinking", "alternative-algorithms"]
---

# Paket 01: Latihan Analisis Masalah, Dekomposisi, & Eksplorasi Algoritma

## Aturan Emas Sebelum Menyentuh Keyboard ("10 Menit Tanpa Koding")
Pada paket ini, **tidak ada petunjuk sintaks** (`for`, `while`, `if`) dan **tidak ada judul topik** di setiap soal. Kamu dituntut berpikir layaknya seorang *programmer* profesional:
1. **Jangan langsung mengetik kode!** Ambil kertas coretan terlebih dahulu.
2. **Jawab Pertanyaan Analisis** di setiap soal untuk memecah masalah besar menjadi tahap-tahap kecil (*Dekomposisi*).
3. Setelah programmu berhasil, pikirkan: **"Bisakah soal ini diselesaikan dengan cara/algoritma yang berbeda?"**

---

### Kasus 1: Kebijakan Nilai Katrol (Subsidi Nilai)
**Skenario Masalah:**  
Seorang dosen merasa soal ujian kali ini terlalu sulit. Ia memutuskan untuk memberikan **"Nilai Katrol"** kepada seluruh $N$ mahasiswanya dengan aturan berikut:
1. Dosen mencari nilai ujian paling tinggi di kelas tersebut.
2. Selisih antara `100` dengan nilai tertinggi tersebut dijadikan sebagai **`poinBonus`** (sehingga mahasiswa pemilik nilai tertinggi akan pas menjadi `100`).
3. Seluruh mahasiswa di kelas tersebut mendapatkan tambahan nilai sebesar **`poinBonus`** yang sama.

Buatlah program yang menerima $N$ nilai awal mahasiswa, kemudian menampilkan daftar nilai akhir seluruh mahasiswa setelah dikatrol!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah mahasiswa).
- Baris kedua berisi $N$ bilangan bulat (nilai awal masing-masing mahasiswa).
- Output berupa $N$ bilangan bulat yang merupakan nilai akhir setelah ditambah `poinBonus`.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $0 ≤ nilaiAwal[i] ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    60 75 82 70 65
    ```
  - Output:
    ```text
    78 93 100 88 83
    ```
    *(Alasan: Nilai tertinggi di kelas adalah 82. Maka poin bonusnya adalah $100 - 82 = 18$. Semua siswa ditambah 18).*
- **Test Case 2:**
  - Input:
    ```text
    4
    50 40 60 30
    ```
  - Output:
    ```text
    90 80 100 70
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    100 85 90
    ```
  - Output:
    ```text
    100 85 90
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Analisis Masalah:** Bisakah kamu langsung menambahkan `poinBonus` ke nilai mahasiswa pada saat kamu baru mulai membaca input satu per satu? Mengapa bisa / mengapa tidak bisa?
2. **Pecah Tahapan (Dekomposisi):** Tuliskan 3 tahapan berurutan untuk menyelesaikan masalah ini!
   - *Tahap 1:* ........................................................................
   - *Tahap 2:* ........................................................................
   - *Tahap 3:* ........................................................................
3. **Eksplorasi Alternatif:** Bagaimana cara mendapatkan nilai tertinggi di Tahap 1? Apakah ada lebih dari 1 cara?

---

### Kasus 2: Pemeriksaan Barisan Parade Simetris
**Skenario Masalah:**  
Dalam sebuah upacara pembukaan, $N$ orang peserta berbaris memanjang dari kiri ke kanan. Panitia menginginkan formasi tinggi badan yang **simetris** (artinya urutan tinggi badan jika dilihat dari ujung kiri ke kanan sama persis dengan urutan jika dilihat dari ujung kanan ke kiri).  
Contoh barisan simetris: `160 168 175 168 160` atau `150 165 165 150`.  
Contoh barisan tidak simetris: `160 170 165 160`.

Buatlah program untuk memeriksa apakah barisan $N$ peserta tersebut sudah simetris atau belum!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat (tinggi badan peserta).
- Output berupa `"SIMETRIS"` jika urutannya simetris, atau `"TIDAK SIMETRIS"` jika tidak.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $100 ≤ tinggi[i] ≤ 250$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    160 168 175 168 160
    ```
  - Output:
    ```text
    SIMETRIS
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    160 170 165 160
    ```
  - Output:
    ```text
    TIDAK SIMETRIS
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    150 165 165 150
    ```
  - Output:
    ```text
    SIMETRIS
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Simulasi Manual:** Jika ada 5 orang dengan indeks `0, 1, 2, 3, 4`:
   - Orang di indeks `0` harus sama tingginya dengan orang di indeks `...`
   - Orang di indeks `1` harus sama tingginya dengan orang di indeks `...`
2. **Rumus Hubungan:** Jika posisi kiri adalah `i` dan panjang barisan adalah `n`, maka rumus pasangan posisinya di sebelah kanan adalah `...`
3. **Eksplorasi Alternatif:**
   - *Cara A:* Bisakah kita membuat array kedua yang berisi kebalikan dari array pertama, lalu membandingkan kedua array tersebut?
   - *Cara B:* Bisakah kita langsung membandingkan ujung kiri dan ujung kanan tanpa membuat array baru?

---

### Kasus 3: Mencari Peraih Medali Perak (Juara Kedua)
**Skenario Masalah:**  
Dalam sebuah kompetisi memanah yang diikuti oleh $N$ peserta, setiap peserta menghasilkan skor akhir yang **semuanya berbeda (tidak ada skor seri)**. Panitia sudah tahu cara mencari peraih medali emas (skor tertinggi), namun sekarang panitia membutuhkan program untuk menemukan berapakah **skor peraih medali perak (skor tertinggi kedua)**!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah peserta).
- Baris kedua berisi $N$ bilangan bulat berbeda (skor masing-masing peserta).
- Output berupa satu angka yaitu skor tertinggi kedua.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $0 ≤ skor[i] ≤ 1000$
- Dijamin seluruh skor peserta berbeda satu sama lain.

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    70 95 80 60 88
    ```
  - Output:
    ```text
    Medali Perak: 88
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    100 50 75 90
    ```
  - Output:
    ```text
    Medali Perak: 90
    ```
- **Test Case 3:**
  - Input:
    ```text
    2
    40 85
    ```
  - Output:
    ```text
    Medali Perak: 40
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Simulasi Manual:** Jika kamu melihat kartu `[70, 95, 80, 60, 88]`, mengapa angka `88` yang menjadi juara kedua? Apa syarat sebuah angka disebut sebagai "terbesar kedua"?
2. **Eksplorasi Dua Jalan (Pikirkan 2 algoritma berbeda!):**
   - *Jalan 1 (Lewat Pengurutan):* Kalau datanya diurutkan dulu dari kecil ke besar, juara kedua pasti berada di posisi mana?
   - *Jalan 2 (Tanpa Pengurutan):* Kalau kita tidak mau mengurutkan array, melainkan mencari nilai tertinggi pertama (`emas`) dulu, bagaimana langkah selanjutnya untuk mencari nilai tertinggi kedua (`perak`)?

---

### Kasus 4: Audit Nomor Seri Barang Kembar di Gudang
**Skenario Masalah:**  
Manajer gudang mencurigai adanya kesalahan pencatatan label karena seharusnya setiap barang memiliki nomor seri yang **unik (berbeda semua)**. Diberikan daftar $N$ nomor seri barang di sebuah rak. Buatlah program untuk memeriksa apakah ada nomor seri yang **tercatat lebih dari satu kali (duplikat)**!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat (nomor seri barang).
- Output berupa `"ADA DUPLIKAT"` jika ditemukan minimal sepasang angka yang sama, atau `"SEMUA UNIK"` jika seluruh angka berbeda.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $1 ≤ seri[i] ≤ 10000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    102 305 410 208 305 501
    ```
  - Output:
    ```text
    ADA DUPLIKAT
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    11 22 33 44 55
    ```
  - Output:
    ```text
    SEMUA UNIK
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    99 12 45 99
    ```
  - Output:
    ```text
    ADA DUPLIKAT
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Simulasi Manual:** Saat kamu melihat daftar `102 305 410 208 305 501`:
   - Pertama kamu memegang angka `102`, lalu kamu bandingkan dengan angka mana saja di sebelah kanannya?
   - Berikutnya kamu memegang angka `305`, lalu kamu bandingkan dengan angka mana saja?
2. **Eksplorasi Alternatif:** Bagaimana jika daftar nomor seri tersebut **diurutkan terlebih dahulu**? Di mana posisi angka yang kembar jika datanya sudah terurut?

---

### Kasus 5: Rotasi Giliran Jaga (Geser Kiri 1 Langkah)
**Skenario Masalah:**  
Terdapat $N$ petugas keamanan yang dijadwalkan dalam sebuah daftar antrean. Setiap pergantian hari, petugas yang berada di posisi paling depan (indeks ke-0) pindah ke posisi **paling belakang (indeks ke-(N-1))**, dan seluruh petugas lainnya maju satu posisi ke kiri.  
Buatlah program yang membaca daftar ID petugas hari ini, lalu menampilkan susunan daftar ID petugas untuk besok!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat (ID petugas).
- Output berupa susunan ID petugas setelah bergeser ke kiri 1 langkah.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $1 ≤ id[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    10 20 30 40 50
    ```
  - Output:
    ```text
    20 30 40 50 10
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    7 8 9 1
    ```
  - Output:
    ```text
    8 9 1 7
    ```
- **Test Case 3:**
  - Input:
    ```text
    2
    100 200
    ```
  - Output:
    ```text
    200 100
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Analisis Perubahan Data:** Jika kamu langsung menimpa `arr[0] = arr[1]`, apa yang terjadi dengan nilai asli `arr[0]`? Apa yang harus kamu lakukan sebelum menggeser elemen-elemen lainnya?
2. **Eksplorasi Alternatif:** Bandingkan antara **benar-benar menggeser isi array di memori** vs **hanya mengatur urutan pencetakan `cout`**. Apa untung dan ruginya masing-masing?

---
---

# Panduan Pengajar: Dekomposisi & Perbandingan Alternatif Algoritma (Paket 01)

> **Catatan Pedagogis untuk Guru:**  
> Saat membahas soal-soal ini di kelas, jangan hanya menampilkan satu kunci jawaban. Tanyakan kepada siswa bagaimana mereka memecah masalahnya, lalu tampilkan **Pendekatan A** dan **Pendekatan B** di bawah ini untuk memicu diskusi kritis!

---

## Pembahasan Kasus 1: Kebijakan Nilai Katrol

### Dekomposisi Masalah:
Banyak siswa pemula terjebak ingin menyelesaikan semuanya dalam 1 loop. Padahal kita **tidak mungkin** mengetahui berapa `poinBonus` sebelum seluruh nilai mahasiswa selesai diperiksa! Maka masalah wajib dipecah menjadi 3 tahap:
1. **Tahap 1:** Cari nilai tertinggi (`maks`) dari seluruh elemen array.
2. **Tahap 2:** Hitung `poinBonus = 100 - maks`.
3. **Tahap 3:** Tambahkan `poinBonus` ke setiap elemen array dan tampilkan.

### Pendekatan A: Pencarian Maksimum Langsung (2 Loop Terpisah)
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

    // Tahap 1: Cari nilai tertinggi
    int maks = nilai[0];
    for (int i = 1; i < n; i++) {
        if (nilai[i] > maks) {
            maks = nilai[i];
        }
    }

    // Tahap 2: Hitung bonus
    int poinBonus = 100 - maks;

    // Tahap 3: Tambahkan bonus dan cetak
    for (int i = 0; i < n; i++) {
        nilai[i] = nilai[i] + poinBonus;
        cout << nilai[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### Pendekatan B: Cari Maksimum Sekaligus Saat Input (Lebih Ringkas)
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int nilai[100];
    int maks = -1; // Karena nilai minimal 0

    // Tahap 1 digabung saat membaca input
    for (int i = 0; i < n; i++) {
        cin >> nilai[i];
        if (nilai[i] > maks) {
            maks = nilai[i];
        }
    }

    int poinBonus = 100 - maks;

    for (int i = 0; i < n; i++) {
        cout << nilai[i] + poinBonus << " ";
    }
    cout << endl;

    return 0;
}
```
* **Bahan Diskusi Kelas:** *"Mengapa kita tidak bisa menggabungkan Tahap 3 ke dalam loop pertama juga? Karena `maks` yang sesungguhnya baru ketahuan setelah angka terakhir dimasukkan!"*

---

## Pembahasan Kasus 2: Pemeriksaan Barisan Parade Simetris

### Pendekatan A: Buat Array Kebalikan Lalu Bandingkan (Intuitif bagi Pemula)
Siswa yang belum lancar rumus indeks biasanya lebih mudah membayangkan: *"Balik saja barisannya ke array kedua, lalu cek apakah sama persis!"*

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int tinggi[100], kebalikan[100];
    for (int i = 0; i < n; i++) {
        cin >> tinggi[i];
    }

    // Tahap 1: Isi array kebalikan
    for (int i = 0; i < n; i++) {
        kebalikan[i] = tinggi[n - 1 - i];
    }

    // Tahap 2: Bandingkan kedua array
    bool simetris = true;
    for (int i = 0; i < n; i++) {
        if (tinggi[i] != kebalikan[i]) {
            simetris = false;
            break;
        }
    }

    if (simetris) cout << "SIMETRIS" << endl;
    else cout << "TIDAK SIMETRIS" << endl;

    return 0;
}
```

### Pendekatan B: Perbandingan Dua Ujung Langsung (Hemat Memori & Cepat)
Kita tidak perlu membuat array kedua dan hanya perlu memeriksa sampai **setengah barisan (`n / 2`)**.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int tinggi[100];
    for (int i = 0; i < n; i++) {
        cin >> tinggi[i];
    }

    bool simetris = true;
    for (int i = 0; i < n / 2; i++) {
        if (tinggi[i] != tinggi[n - 1 - i]) {
            simetris = false;
            break;
        }
    }

    if (simetris) cout << "SIMETRIS" << endl;
    else cout << "TIDAK SIMETRIS" << endl;

    return 0;
}
```
* **Bahan Diskusi Kelas:** *"Pendekatan A butuh 2 array dan memeriksa $N$ kali. Pendekatan B hanya butuh 1 array dan cukup memeriksa $N/2$ kali. Mengapa cukup sampai tengah (`n / 2`)?"*

---

## Pembahasan Kasus 3: Mencari Peraih Medali Perak (Juara Kedua)

### Pendekatan A: Dua Tahap Pencarian Maksimum (Dekomposisi Bertahap)
1. **Tahap 1:** Cari skor tertinggi pertama (`emas`).
2. **Tahap 2:** Cari skor tertinggi di antara semua elemen yang **bukan `emas`** (`skor[i] != emas`).

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int skor[100];
    for (int i = 0; i < n; i++) {
        cin >> skor[i];
    }

    // Tahap 1: Cari peraih medali emas (terbesar pertama)
    int emas = skor[0];
    for (int i = 1; i < n; i++) {
        if (skor[i] > emas) {
            emas = skor[i];
        }
    }

    // Tahap 2: Cari nilai terbesar yang tidak sama dengan emas
    int perak = -1;
    for (int i = 0; i < n; i++) {
        if (skor[i] != emas) {
            if (skor[i] > perak) {
                perak = skor[i];
            }
        }
    }

    cout << "Medali Perak: " << perak << endl;
    return 0;
}
```

### Pendekatan B: Urutkan dengan Bubble Sort Lalu Ambil `skor[n - 2]`
Karena siswa baru belajar *Bubble Sort*, mereka bisa memanfaatkannya: urutkan saja dari kecil ke besar, maka juara 1 pasti di `skor[n - 1]` dan juara 2 pasti di `skor[n - 2]`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int skor[100];
    for (int i = 0; i < n; i++) {
        cin >> skor[i];
    }

    // Urutkan dari kecil ke besar dengan Bubble Sort
    for (int tahap = 0; tahap < n - 1; tahap++) {
        for (int i = 0; i < n - 1 - tahap; i++) {
            if (skor[i] > skor[i + 1]) {
                int temp = skor[i];
                skor[i] = skor[i + 1];
                skor[i + 1] = temp;
            }
        }
    }

    cout << "Medali Perak: " << skor[n - 2] << endl;
    return 0;
}
```
* **Bahan Diskusi Kelas:** *"Jika datanya ada 1.000 peserta dan kita hanya butuh Juara 2, Pendekatan A jauh lebih cepat karena hanya butuh 2 kali loop. Tapi kalau panitia minta daftar Juara 1 sampai Juara 10, Pendekatan B (Sorting) jauh lebih praktis!"*

---

## Pembahasan Kasus 4: Audit Nomor Seri Barang Kembar

### Pendekatan A: Bandingkan Setiap Pasangan Elemen (Nested Loop)
Ambil elemen `i`, lalu bandingkan dengan semua elemen di sebelah kanannya (`j = i + 1` sampai `n - 1`).

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int seri[100];
    for (int i = 0; i < n; i++) {
        cin >> seri[i];
    }

    bool adaDuplikat = false;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (seri[i] == seri[j]) {
                adaDuplikat = true;
                break;
            }
        }
    }

    if (adaDuplikat) cout << "ADA DUPLIKAT" << endl;
    else cout << "SEMUA UNIK" << endl;

    return 0;
}
```

### Pendekatan B: Urutkan Dulu, Lalu Cek Tetangga Sebelahnya
Jika array diurutkan lebih dulu, maka angka-angka yang kembar **pasti akan berkumpul bersebelahan**!

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int seri[100];
    for (int i = 0; i < n; i++) {
        cin >> seri[i];
    }

    // Tahap 1: Urutkan array dengan Bubble Sort
    for (int tahap = 0; tahap < n - 1; tahap++) {
        for (int i = 0; i < n - 1 - tahap; i++) {
            if (seri[i] > seri[i + 1]) {
                int temp = seri[i];
                seri[i] = seri[i + 1];
                seri[i + 1] = temp;
            }
        }
    }

    // Tahap 2: Cek apakah ada dua elemen bersebelahan yang sama
    bool adaDuplikat = false;
    for (int i = 0; i < n - 1; i++) {
        if (seri[i] == seri[i + 1]) {
            adaDuplikat = true;
            break;
        }
    }

    if (adaDuplikat) cout << "ADA DUPLIKAT" << endl;
    else cout << "SEMUA UNIK" << endl;

    return 0;
}
```

---

## Pembahasan Kasus 5: Rotasi Giliran Jaga (Geser Kiri 1 Langkah)

### Pendekatan A: Menggeser Isi Array di Memori (Mutasi Data)
1. Simpan `pertama = id[0]` ke variabel sementara.
2. Geser semua elemen dari indeks `1..n-1` ke kiri satu langkah (`id[i] = id[i + 1]`).
3. Masukkan `pertama` ke indeks terakhir `id[n - 1]`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int id[100];
    for (int i = 0; i < n; i++) {
        cin >> id[i];
    }

    int pertama = id[0];
    for (int i = 0; i < n - 1; i++) {
        id[i] = id[i + 1];
    }
    id[n - 1] = pertama;

    for (int i = 0; i < n; i++) {
        cout << id[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### Pendekatan B: Trik Urutan Cetak Tanpa Menggeser Isi Array
Jika kita hanya diminta menampilkan urutan barunya ke layar, kita bisa mencetak mulai dari indeks `1` sampai `n - 1`, lalu terakhir mencetak `id[0]`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int id[100];
    for (int i = 0; i < n; i++) {
        cin >> id[i];
    }

    // Cetak dari indeks 1 sampai n-1
    for (int i = 1; i < n; i++) {
        cout << id[i] << " ";
    }
    // Terakhir cetak elemen pertama
    cout << id[0] << endl;

    return 0;
}
```
* **Bahan Diskusi Kelas:** *"Pendekatan B sangat cerdik dan singkat jika kita hanya butuh mencetak. TAPI jika setelah ini program masih harus mengolah antrean hari ke-2, hari ke-3, dan seterusnya, mengapa kita WAJIB menggunakan Pendekatan A?"*
