---
id: "SOAL-20261028-004"
kategori: "pemrograman"
subjek: "cpp"
materi: "array-1d-for-loop"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:07:00+07:00"
tags: ["cpp", "array-1d", "for-loop", "index-vs-value", "code-tracing", "debugging"]
---

# Bank Soal Latihan Mandiri di Rumah — Paket 03
**Topik:** Dasar Array 1 Dimensi, Indeks vs Nilai, dan Kombinasi Loop  
**Estimasi Waktu:** 25–30 Menit

---

## BAGIAN A: Tebak Output & Tabel Tracing (Tanpa Komputer)

### Soal 1: Melacak Perubahan Isi Array
**Instruksi:**  
Perhatikan program C++ di bawah ini. Sebuah array `data` awalnya berisi `{4, 7, 2, 9, 6}`. Di dalam loop, nilai-nilai di dalam array tersebut dimodifikasi. Lacaklah perubahan isi array dan tuliskan hasil akhirnya!

```cpp
#include <iostream>
using namespace std;

int main() {
    int data[5] = {4, 7, 2, 9, 6};

    for (int i = 0; i < 5; i++) {
        if (i % 2 == 0) {
            data[i] = data[i] + 10;
        } else {
            data[i] = data[i] - 3;
        }
    }

    for (int i = 0; i < 5; i++) {
        cout << data[i] << " ";
    }
    return 0;
}
```

**Tabel Tracing (Isilah titik-titik berikut):**

| Indeks `i` | Nilai awal `data[i]` | Apakah `i % 2 == 0`? | Operasi yang Dijalankan | Nilai baru `data[i]` |
| :---: | :---: | :---: | :---: | :---: |
| `0` | `4` | Ya (Genap) | `4 + 10` | `14` |
| `1` | `7` | Tidak (Ganjil) | `7 - 3` | ... |
| `2` | `2` | ... | ... | ... |
| `3` | `9` | ... | ... | ... |
| `4` | `6` | ... | ... | ... |

**Tebakan Output Akhir:** `... ... ... ... ...`

---

### Soal 2: Akses Indeks dari Dua Arah
**Instruksi:**  
Perhatikan ekspresi di dalam kurung siku `arr[...]` pada kode berikut. Tentukan apa yang dicetak oleh program ini!

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    int arr[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 3; i++) {
        int jumlah = arr[i] + arr[n - 1 - i];
        cout << jumlah << " ";
    }

    return 0;
}
```

**Pertanyaan:**
1. Saat `i = 0`, elemen indeks berapa yang dijumlahkan dengan `arr[0]`? Berapa hasilnya?
2. Saat `i = 1`, elemen indeks berapa yang dijumlahkan dengan `arr[1]`? Berapa hasilnya?
3. Saat `i = 2`, elemen indeks berapa yang dijumlahkan dengan `arr[2]`? Berapa hasilnya?
4. Tuliskan output lengkapnya!

---

## BAGIAN B: Detektif Bug (Analisis & Perbaikan Kode)

### Soal 3: Dua Kesalahan Fatal Akses Array
**Deskripsi Masalah:**  
Seorang siswa ingin membuat program yang menerima 5 angka ke dalam array, lalu mencetak **hanya angka-angka yang lebih besar dari 50**. Namun kodenya memiliki **2 kesalahan logika**: batas loop yang keliru (*Off-by-One Error*) dan tertukarnya pengecekan indeks dengan isi elemen.

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {20, 80, 45, 90, 60};

    // KODE YANG BERMASALAH (BUGGY):
    for (int i = 0; i <= 5; i++) {       // Bug 1
        if (i > 50) {                    // Bug 2
            cout << arr[i] << " ";
        }
    }

    return 0;
}
```

**Tugasmu:**
1. Mengapa syarat `i <= 5` pada array berukuran 5 berbahaya di C++? Indeks berapa saja yang sah untuk `int arr[5]`?
2. Mengapa `if (i > 50)` tidak pernah bernilai benar di dalam program tersebut? Apa yang seharusnya diperiksa?
3. Tuliskan kembali perulangan `for` tersebut setelah diperbaiki!

---

## BAGIAN C: Tantangan Koding Kontekstual

### Soal 4: Analisis Suhu Udara Mingguan (Di Atas Rata-Rata)
**Deskripsi Masalah:**  
Badan meteorologi mencatat suhu udara siang hari selama $N$ hari berturut-turut ke dalam sebuah array. Buatlah program untuk:
1. Menghitung **rata-rata suhu** selama $N$ hari tersebut.
2. Menghitung **berapa hari** yang memiliki suhu **lebih tinggi dari rata-rata** tersebut!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah hari).
- Baris kedua berisi $N$ bilangan bulat (suhu harian dalam derajat Celcius).
- Baris pertama output menampilkan nilai rata-rata suhu, baris kedua menampilkan jumlah hari yang suhunya di atas rata-rata.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $15 ≤ suhu[i] ≤ 45$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    30 32 28 35 25
    ```
  - Output:
    ```text
    Rata-rata suhu: 30
    Hari di atas rata-rata: 2
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    28 30 32 34
    ```
  - Output:
    ```text
    Rata-rata suhu: 31
    Hari di atas rata-rata: 2
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    30 30 30
    ```
  - Output:
    ```text
    Rata-rata suhu: 30
    Hari di atas rata-rata: 0
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Kamu memerlukan **dua tahap loop** (tidak bisa diselesaikan hanya dalam 1 loop sekaligus):  
> - **Loop 1:** Hitung `total` seluruh suhu, lalu bagi dengan `n` untuk mendapatkan `double rataRata`.  
> - **Loop 2:** Telusuri kembali array dari indeks `0` sampai `n - 1`, periksa `if (suhu[i] > rataRata)`, lalu tambahkan penghitung `diAtasRata++`.

---

### Soal 5: Sensor Pembersih Data Negatif (Modifikasi Array)
**Deskripsi Masalah:**  
Sebuah alat sensor kadang mengalami gangguan sehingga menghasilkan angka negatif. Buatlah program yang membaca $N$ data angka ke dalam array, kemudian **mengubah semua elemen yang bernilai negatif ($< 0$) di dalam array tersebut menjadi `0`**, sementara angka positif atau nol dibiarkan tetap. Setelah diubah, tampilkan isi array yang sudah bersih!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat (bisa positif, nol, atau negatif).
- Output berupa isi array setelah semua nilai negatif diubah menjadi `0`.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    15 -4 20 -12 0 8
    ```
  - Output:
    ```text
    15 0 20 0 0 8
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    -1 -5 -9 -2
    ```
  - Output:
    ```text
    0 0 0 0
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    10 20 30
    ```
  - Output:
    ```text
    10 20 30
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Di dalam loop, periksa `if (arr[i] < 0)`. Jika benar, timpa isi kotaknya dengan `arr[i] = 0;`. Setelah itu cetak seluruh elemen array.

---
---

# Kunci Jawaban & Pembahasan (Paket 03)

### Pembahasan Soal 1 (Tracing Modifikasi Array)
Perhatikan bahwa `if (i % 2 == 0)` mengecek apakah **nomor indeksnya** genap (`0, 2, 4`), bukan isi angkanya.

| Indeks `i` | Nilai awal `data[i]` | Apakah `i % 2 == 0`? | Operasi yang Dijalankan | Nilai baru `data[i]` |
| :---: | :---: | :---: | :---: | :---: |
| `0` | `4` | Ya (Genap) | `4 + 10` | `14` |
| `1` | `7` | Tidak (Ganjil) | `7 - 3` | `4` |
| `2` | `2` | Ya (Genap) | `2 + 10` | `12` |
| `3` | `9` | Tidak (Ganjil) | `9 - 3` | `6` |
| `4` | `6` | Ya (Genap) | `6 + 10` | `16` |

**Output Akhir:** `14 4 12 6 16 `

---

### Pembahasan Soal 2 (Akses Indeks Dua Arah)
1. Saat `i = 0`: `arr[0] + arr[5 - 1 - 0]` = `arr[0] + arr[4]` = `10 + 50` = **`60`**.
2. Saat `i = 1`: `arr[1] + arr[5 - 1 - 1]` = `arr[1] + arr[3]` = `20 + 40` = **`60`**.
3. Saat `i = 2`: `arr[2] + arr[5 - 1 - 2]` = `arr[2] + arr[2]` = `30 + 30` = **`60`**.
4. **Output lengkap:** `60 60 60 `

---

### Pembahasan Soal 3 (Detektif Bug)
1. **Bug 1 (`i <= 5`):** Array berukuran 5 hanya memiliki indeks **`0, 1, 2, 3, 4`**. Ketika `i` mencapai `5`, program mengakses `arr[5]` yang berada di luar memori sah (*Out-of-Bounds*), sehingga bisa memunculkan angka sampah (*garbage value*) atau membuat program *crash*.
2. **Bug 2 (`if (i > 50)`):** Variabel `i` adalah nomor indeks (0 s/d 4), sehingga tidak mungkin lebih dari 50. Seharusnya yang diperiksa adalah isi kotaknya, yaitu `if (arr[i] > 50)`.
3. **Kode Perbaikan:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {20, 80, 45, 90, 60};

    for (int i = 0; i < 5; i++) {
        if (arr[i] > 50) {
            cout << arr[i] << " ";
        }
    }

    return 0;
}
```

---

### Pembahasan Soal 4 (Analisis Suhu Udara Mingguan)
**Penjelasan Langkah demi Langkah:**
1. Baca semua data suhu ke dalam array `suhu[100]` sembari menjumlahkannya ke variabel `total`.
2. Hitung `double rataRata = (double)total / n;`.
3. Lakukan perulangan kedua untuk membandingkan setiap `suhu[i]` dengan `rataRata`. Inilah alasan utama mengapa kita butuh menyimpan data di **array**: karena kita harus membaca ulang data suhu tersebut setelah nilai rata-ratanya diketahui!

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int suhu[100];
    int total = 0;

    for (int i = 0; i < n; i++) {
        cin >> suhu[i];
        total = total + suhu[i];
    }

    double rataRata = (double)total / n;

    int diAtasRata = 0;
    for (int i = 0; i < n; i++) {
        if (suhu[i] > rataRata) {
            diAtasRata++;
        }
    }

    cout << "Rata-rata suhu: " << rataRata << endl;
    cout << "Hari di atas rata-rata: " << diAtasRata << endl;

    return 0;
}
```

---

### Pembahasan Soal 5 (Sensor Pembersih Data Negatif)
**Penjelasan Langkah demi Langkah:**
1. Simpan input ke dalam array `arr`.
2. Gunakan loop `for` untuk memeriksa setiap elemen. Jika `arr[i] < 0`, ubah nilainya menjadi `0`.
3. Tampilkan isi array yang telah diperbarui.

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

    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            arr[i] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```
