---
id: "SOAL-20261028-006"
kategori: "pemrograman"
subjek: "cpp"
materi: "searching-dan-sorting"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:09:00+07:00"
tags: ["cpp", "linear-search", "binary-search", "bubble-sort", "code-tracing", "debugging"]
---

# Bank Soal Latihan Mandiri di Rumah — Paket 05
**Topik:** Logika Pencarian (*Linear Search* & *Binary Search*) dan Pengurutan (*Bubble Sort*)  
**Estimasi Waktu:** 30–35 Menit

---

## BAGIAN A: Tebak Output & Tabel Tracing (Tanpa Komputer)

### Soal 1: Simulasi Langkah *Binary Search* di Atas Kertas
**Instruksi:**  
*Binary Search* bekerja pada array yang **sudah terurut** dengan cara membelah dua area pencarian menggunakan indeks `kiri`, `kanan`, dan `tengah = (kiri + kanan) / 2`.  
Diberikan sebuah array terurut berukuran 7 dan angka target yang dicari adalah **`x = 42`**:

| Indeks | `0` | `1` | `2` | `3` | `4` | `5` | `6` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Isi `arr`** | `10` | `18` | `25` | `30` | `42` | `55` | `70` |

Perhatikan kode *Binary Search* berikut:
```cpp
int kiri = 0, kanan = 6;
while (kiri <= kanan) {
    int tengah = (kiri + kanan) / 2;
    if (arr[tengah] == x) {
        cout << "Ketemu di indeks " << tengah << endl;
        break;
    } else if (arr[tengah] < x) {
        kiri = tengah + 1;
    } else {
        kanan = tengah - 1;
    }
}
```

**Tabel Tracing (Isilah titik-titik berikut sampai angka `42` ditemukan):**

| Putaran | Nilai `kiri` | Nilai `kanan` | `tengah = (kiri + kanan) / 2` | Nilai `arr[tengah]` | Perbandingan dgn `x = 42` | Perubahan Batas |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | `0` | `6` | `(0 + 6) / 2 = 3` | `30` | `30 < 42` (Kurang kecil) | `kiri = 3 + 1 = 4` |
| **2** | `4` | `6` | ... | ... | ... | ... |
| **3** | ... | ... | ... | ... | ... | ... |

**Pertanyaan:** Pada putaran ke berapa angka `42` ditemukan, dan berapa nilai `tengah` saat itu?

---

### Soal 2: Simulasi Tahapan Gelembung (*Bubble Sort*)
**Instruksi:**  
Diberikan array awal berukuran 4 elemen: **`{ 40, 20, 30, 10 }`**.  
Kita ingin mengurutkannya dari **kecil ke besar** menggunakan algoritma *Bubble Sort*:

```cpp
for (int tahap = 0; tahap < 3; tahap++) {
    for (int i = 0; i < 3 - tahap; i++) {
        if (arr[i] > arr[i + 1]) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }
}
```

**Tugasmu:**  
Tuliskan susunan isi array setelah setiap langkah perbandingan di **Tahap 0** (`tahap = 0`), serta hasil akhir setelah **Tahap 1** dan **Tahap 2** selesai!

- **Kondisi Awal:** `{ 40, 20, 30, 10 }`
- **Tahap 0 (`tahap = 0`):**
  - Saat `i = 0` (Bandingkan indeks 0 dan 1): `{ 20, 40, 30, 10 }` *(karena $40 > 20$, ditukar)*
  - Saat `i = 1` (Bandingkan indeks 1 dan 2): `{ ..., ..., ..., ... }`
  - Saat `i = 2` (Bandingkan indeks 2 dan 3): `{ ..., ..., ..., ... }`
- **Akhir Tahap 1 (`tahap = 1` selesai):** `{ ..., ..., ..., ... }`
- **Akhir Tahap 2 (`tahap = 2` selesai):** `{ ..., ..., ..., ... }`

---

## BAGIAN B: Detektif Bug (Analisis & Perbaikan Kode)

### Soal 3: Dua Kesalahan Fatal pada Swap dan Bubble Sort
**Deskripsi Masalah:**  
Seorang siswa mencoba menulis kode *Bubble Sort* untuk mengurutkan 5 angka. Namun setelah dijalankan, sebagian angka di dalam array malah **hilang/terduplikasi**, dan program juga mengakses indeks di luar batas!

Perhatikan kode siswa tersebut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    int arr[5] = {50, 20, 40, 10, 30};

    // KODE YANG BERMASALAH (BUGGY):
    for (int tahap = 0; tahap < n; tahap++) {
        for (int i = 0; i < n; i++) {          // Bug 1: Batas loop dalam
            if (arr[i] > arr[i + 1]) {
                arr[i] = arr[i + 1];           // Bug 2: Cara menukar (Swap)
                arr[i + 1] = arr[i];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
```

**Tugasmu:**
1. Mengapa syarat `i < n` pada loop bagian dalam menyebabkan error saat membandingkan `arr[i] > arr[i + 1]`? Seharusnya apa batasnya?
2. Mengapa baris `arr[i] = arr[i + 1];` yang langsung diikuti `arr[i + 1] = arr[i];` membuat kedua elemen bernilai sama?
3. Tuliskan kode perbaikan lengkapnya!

---

## BAGIAN C: Tantangan Koding Kontekstual

### Soal 4: Pencarian Semua Lokasi Indeks (*Multiple Linear Search*)
**Deskripsi Masalah:**  
Pada *Linear Search* biasa, pencarian langsung berhenti (`break`) saat menemukan angka target pertama kali. Kali ini, buatlah program yang mencari angka target $X$ di dalam array berukuran $N$, lalu **menampilkan SEMUA nomor indeks** tempat angka $X$ tersebut berada! Jika angka $X$ sama sekali tidak ada di dalam array, tampilkan `"TIDAK ADA"`.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Baris ketiga berisi angka target $X$.
- Output berupa daftar nomor indeks (dipisahkan spasi) tempat $X$ ditemukan, atau `"TIDAK ADA"` jika tidak pernah muncul.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $-1000 ≤ arr[i], X ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    7
    10 25 10 40 50 10 30
    10
    ```
  - Output:
    ```text
    0 2 5
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    12 15 18 21 24
    99
    ```
  - Output:
    ```text
    TIDAK ADA
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    8 8 8 8
    8
    ```
  - Output:
    ```text
    0 1 2 3
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Buat variabel penghitung `int ketemu = 0;`. Telusuri array dari `i = 0` sampai `n - 1`. Setiap kali `arr[i] == x`, cetak nilai `i` (`cout << i << " ";`) dan tambahkan `ketemu++`. Di luar loop, periksa `if (ketemu == 0)` untuk mencetak `"TIDAK ADA"`.

---

### Soal 5: Mengurutkan Nilai Ujian Siswa (*Full Bubble Sort*)
**Deskripsi Masalah:**  
Diberikan daftar nilai ujian dari $N$ siswa yang masih acak. Gunakan algoritma **Bubble Sort** untuk mengurutkan nilai-nilai tersebut dari **nilai terkecil hingga nilai terbesar (Ascending)**, lalu tampilkan hasilnya!

**Format Input & Output:**
- Baris pertama berisi jumlah siswa $N$.
- Baris kedua berisi $N$ bilangan bulat nilai siswa.
- Output berupa barisan nilai siswa yang sudah terurut dari terkecil ke terbesar.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $0 ≤ nilai[i] ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    85 60 90 75 50 95
    ```
  - Output:
    ```text
    50 60 75 85 90 95
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    100 80 60 40 20
    ```
  - Output:
    ```text
    20 40 60 80 100
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    70 75 70 80
    ```
  - Output:
    ```text
    70 70 75 80
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Ingat latihan **1-Pass Bubble** di kelas! Satu putaran loop `for (int i = 0; i < n - 1; i++)` akan mendorong 1 angka terbesar ke ujung kanan. Agar seluruh $N$ angka terurut sempurna, bungkus loop tersebut di dalam loop luar `for (int tahap = 0; tahap < n - 1; tahap++)`.

---
---

# Kunci Jawaban & Pembahasan (Paket 05)

### Pembahasan Soal 1 (Tracing *Binary Search*)

| Putaran | Nilai `kiri` | Nilai `kanan` | `tengah = (kiri + kanan) / 2` | Nilai `arr[tengah]` | Perbandingan dgn `x = 42` | Perubahan Batas |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | `0` | `6` | `(0 + 6) / 2 = 3` | `30` | `30 < 42` (Kurang kecil) | `kiri = 3 + 1 = 4` |
| **2** | `4` | `6` | `(4 + 6) / 2 = 5` | `55` | `55 > 42` (Kelebihan) | `kanan = 5 - 1 = 4` |
| **3** | `4` | `4` | `(4 + 4) / 2 = 4` | `42` | `42 == 42` (**KETEMU!**) | Loop berhenti (`break`) |

**Jawaban:** Angka `42` ditemukan pada **Putaran ke-3** saat indeks **`tengah = 4`**.

---

### Pembahasan Soal 2 (Tracing Tahapan *Bubble Sort*)
- **Kondisi Awal:** `{ 40, 20, 30, 10 }`
- **Tahap 0 (`tahap = 0`):**
  - Saat `i = 0` (Bandingkan `40` dan `20`): `{ 20, 40, 30, 10 }`
  - Saat `i = 1` (Bandingkan `40` dan `30`): **`{ 20, 30, 40, 10 }`** *(karena $40 > 30$, ditukar)*
  - Saat `i = 2` (Bandingkan `40` dan `10`): **`{ 20, 30, 10, 40 }`** *(karena $40 > 10$, ditukar — angka terbesar `40` sudah sampai di ujung kanan)*
- **Akhir Tahap 1 (`tahap = 1` selesai):** **`{ 20, 10, 30, 40 }`** *(angka `30` terdorong ke posisi kedua dari kanan)*
- **Akhir Tahap 2 (`tahap = 2` selesai):** **`{ 10, 20, 30, 40 }`** *(angka `20` dan `10` bertukar, seluruh array kini terurut sempurna)*

---

### Pembahasan Soal 3 (Detektif Bug)
1. **Bug 1 (`i < n`):** Saat `i` bernilai `n - 1` (indeks terakhir, yaitu `4`), kode mengakses `arr[i + 1]` yaitu `arr[5]` yang berada di luar batas array. Batas loop dalam haruslah `i < n - 1` (atau lebih optimal `i < n - 1 - tahap`).
2. **Bug 2 (Tanpa `temp`):** Baris `arr[i] = arr[i + 1];` menimpa nilai asli `arr[i]` tanpa menyimpannya lebih dulu. Akibatnya, baris kedua `arr[i + 1] = arr[i];` hanya menyalin nilai yang sama kembali. Wajib menggunakan variabel bantuan `int temp`.
3. **Kode Perbaikan:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    int arr[5] = {50, 20, 40, 10, 30};

    for (int tahap = 0; tahap < n - 1; tahap++) {
        for (int i = 0; i < n - 1 - tahap; i++) {
            if (arr[i] > arr[i + 1]) {
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}
```

---

### Pembahasan Soal 4 (Pencarian Semua Lokasi Indeks)
**Penjelasan Langkah demi Langkah:**
1. Baca array `arr` dan target `x`.
2. Gunakan variabel `ketemu = 0` untuk menghitung berapa kali `x` ditemukan.
3. Telusuri seluruh array dengan `for`. Setiap kali `arr[i] == x`, cetak indeks `i` dan tambahkan `ketemu++`.
4. Jika selesai loop ternyata `ketemu == 0`, cetak `"TIDAK ADA"`.

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

    int ketemu = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            cout << i << " ";
            ketemu++;
        }
    }

    if (ketemu == 0) {
        cout << "TIDAK ADA";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 5 (Mengurutkan Nilai Ujian dengan *Bubble Sort*)
**Penjelasan Langkah demi Langkah:**
1. Baca `n` dan elemen-elemen array `nilai`.
2. Gunakan loop luar `tahap` sebanyak `n - 1` kali.
3. Gunakan loop dalam `i` dari `0` sampai `n - 1 - tahap` untuk membandingkan `nilai[i]` dan `nilai[i + 1]`. Jika `nilai[i] > nilai[i + 1]`, tukar posisinya menggunakan variabel `temp`.
4. Cetak array setelah proses pengurutan selesai.

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

    // Algoritma Bubble Sort Ascending (Kecil ke Besar)
    for (int tahap = 0; tahap < n - 1; tahap++) {
        for (int i = 0; i < n - 1 - tahap; i++) {
            if (nilai[i] > nilai[i + 1]) {
                int temp = nilai[i];
                nilai[i] = nilai[i + 1];
                nilai[i + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << nilai[i] << " ";
    }
    cout << endl;

    return 0;
}
```
