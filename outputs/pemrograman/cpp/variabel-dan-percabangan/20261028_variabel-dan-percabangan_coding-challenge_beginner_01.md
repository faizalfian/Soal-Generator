---
id: "SOAL-20261028-002"
kategori: "pemrograman"
subjek: "cpp"
materi: "variabel-dan-percabangan"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:05:00+07:00"
tags: ["cpp", "variabel", "tipe-data", "operator-modulus", "if-else", "code-tracing", "debugging"]
---

# Bank Soal Latihan Mandiri di Rumah — Paket 01
**Topik:** Variabel, Operator Aritmatika (`/`, `%`), dan Logika Percabangan (`if-else`)  
**Estimasi Waktu:** 20–30 Menit

---

## BAGIAN A: Tebak Output & Tabel Tracing (Tanpa Komputer)

### Soal 1: Melacak Perubahan Nilai Variabel (Variable Mutation)
**Instruksi:**  
Perhatikan potongan kode C++ di bawah ini. Lacaklah perubahan nilai variabel `a`, `b`, dan `c` baris demi baris dengan mengisi tabel di bawahnya, lalu tuliskan apa output yang muncul di layar!

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 12;
    int b = 5;
    int c = a / b;       // Baris 1
    int d = a % b;       // Baris 2
    a = b + c;           // Baris 3
    b = a - d;           // Baris 4
    c = a * d;           // Baris 5

    cout << a << " " << b << " " << c << " " << d << endl;
    return 0;
}
```

**Tabel Tracing (Isilah titik-titik berikut):**

| Langkah | nilai `a` | nilai `b` | nilai `c` | nilai `d` |
| :--- | :---: | :---: | :---: | :---: |
| Awal | `12` | `5` | `?` | `?` |
| Setelah Baris 1 (`c = a / b`) | `12` | `5` | ... | `?` |
| Setelah Baris 2 (`d = a % b`) | `12` | `5` | ... | ... |
| Setelah Baris 3 (`a = b + c`) | ... | `5` | ... | ... |
| Setelah Baris 4 (`b = a - d`) | ... | ... | ... | ... |
| Setelah Baris 5 (`c = a * d`) | ... | ... | ... | ... |

**Tebakan Output Akhir:** `... ... ... ...`

---

### Soal 2: Menebak Jalur Logika Majemuk (`&&` dan `||`)
**Instruksi:**  
Perhatikan program di bawah ini. Tentukan **output** yang dicetak ke layar untuk **3 skenario input** yang berbeda!

```cpp
#include <iostream>
using namespace std;

int main() {
    int nilai, kehadiran;
    cin >> nilai >> kehadiran;

    if (nilai >= 80 && kehadiran >= 90) {
        cout << "LULUS ISTIMEWA" << endl;
    } else if (nilai >= 75 || kehadiran == 100) {
        if (nilai < 60) {
            cout << "UJIAN ULANG" << endl;
        } else {
            cout << "LULUS BERSYARAT" << endl;
        }
    } else {
        cout << "TIDAK LULUS" << endl;
    }

    return 0;
}
```

**Pertanyaan:**
1. Jika input adalah `85 85`, apa outputnya? Mengapa tidak masuk ke `"LULUS ISTIMEWA"`?
2. Jika input adalah `55 100`, apa outputnya?
3. Jika input adalah `70 80`, apa outputnya?

---

## BAGIAN B: Detektif Bug (Analisis & Perbaikan Kode)

### Soal 3: Bug Penentuan Predikat Nilai Ujian
**Deskripsi Masalah:**  
Seorang siswa membuat program untuk mengubah nilai angka (0–100) menjadi nilai huruf dengan aturan:
- Nilai $≥ 85$: Grade `A`
- Nilai $≥ 70$ s/d $84$: Grade `B`
- Nilai $≥ 55$ s/d $69$: Grade `C`
- Nilai $< 55$: Grade `D`

Namun, ketika diuji dengan nilai `90`, programnya malah mencetak **`C`**! Berikut kode yang dibuat siswa tersebut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int skor;
    cin >> skor;

    // KODE YANG BERMASALAH (BUGGY):
    if (skor >= 55) {
        cout << "C" << endl;
    } else if (skor >= 70) {
        cout << "B" << endl;
    } else if (skor >= 85) {
        cout << "A" << endl;
    } else {
        cout << "D" << endl;
    }

    return 0;
}
```

**Tugasmu:**
1. Jelaskan mengapa saat diberi input `90`, program langsung mencetak `"C"` dan mengabaikan kondisi di bawahnya!
2. Tuliskan ulang bagian blok `if - else if - else` tersebut agar berjalan dengan benar!

---

## BAGIAN C: Tantangan Koding Kontekstual

### Soal 4: Konversi Detik ke Jam, Menit, dan Detik
**Deskripsi Masalah:**  
Sebuah stopwatch mencatat durasi lari maraton dalam satuan **total detik** (misalnya `3665` detik). Buatlah program yang menerima satu bilangan bulat berupa total detik, lalu mengubahnya menjadi format **Jam, Menit, dan Sisa Detik**!

**Format Input & Output:**
- Input berupa satu bilangan bulat `totalDetik`.
- Output berupa format `<jam> jam <menit> menit <detik> detik`.

**Batasan (Constraints):**
- $0 ≤ totalDetik ≤ 86400$
- 1 Jam = 3600 Detik, 1 Menit = 60 Detik.

**Contoh Test Case:**
- **Test Case 1:**
  - Input: `3665`
  - Output: `1 jam 1 menit 5 detik`
- **Test Case 2:**
  - Input: `7320`
  - Output: `2 jam 2 menit 0 detik`
- **Test Case 3:**
  - Input: `45`
  - Output: `0 jam 0 menit 45 detik`

> **Petunjuk Alur Berpikir (Clue):**  
> - Gunakan pembagian bulat `/` untuk mendapatkan jumlah jam: `jam = totalDetik / 3600;`  
> - Gunakan operator sisa bagi `%` untuk mendapatkan sisa detik yang belum jadi jam: `sisa = totalDetik % 3600;`  
> - Dari `sisa` tersebut, bagi dengan `60` untuk mendapat menit, dan `% 60` untuk mendapat detik akhirnya!

---

### Soal 5: Kasir Toko Buku & Diskon Bertingkat
**Deskripsi Masalah:**  
Sebuah toko buku mengadakan promo diskon berdasarkan total belanja pembeli:
- Jika total belanja **minimal Rp 200.000**, mendapat potongan diskon **Rp 30.000**.
- Jika total belanja **minimal Rp 100.000** (tapi di bawah Rp 200.000), mendapat potongan diskon **Rp 10.000**.
- Jika di bawah Rp 100.000, tidak mendapat diskon (**Rp 0**).

Buatlah program yang menerima nominal total belanja, kemudian menampilkan **Besar Diskon** dan **Total yang Harus Dibayar**!

**Format Input & Output:**
- Input berupa satu bilangan bulat `belanja`.
- Output terdiri dari 2 baris: baris pertama nominal diskon, baris kedua nominal akhir yang harus dibayar.

**Batasan (Constraints):**
- $1000 ≤ belanja ≤ 10000000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input: `250000`
  - Output:
    ```text
    Diskon: 30000
    Total Bayar: 220000
    ```
- **Test Case 2:**
  - Input: `120000`
  - Output:
    ```text
    Diskon: 10000
    Total Bayar: 110000
    ```
- **Test Case 3:**
  - Input: `75000`
  - Output:
    ```text
    Diskon: 0
    Total Bayar: 75000
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Buat variabel `int diskon = 0;`. Periksa mulai dari syarat nominal paling tinggi (`belanja >= 200000`), baru turun ke `else if (belanja >= 100000)`. Setelah blok `if` selesai, hitung `bayar = belanja - diskon`.

---
---

# Kunci Jawaban & Pembahasan (Paket 01)

### Pembahasan Soal 1 (Tracing Variabel)
1. **Baris 1 (`c = a / b`):** Karena `a` dan `b` bertipe `int`, pembagian `12 / 5` menghasilkan bilangan bulat `2` (desimalnya dibuang).
2. **Baris 2 (`d = a % b`):** Sisa bagi `12` dibagi `5` adalah `2` (karena $5 × 2 = 10$, sisanya $12 - 10 = 2$).
3. **Baris 3 (`a = b + c`):** Nilai `a` ditimpa menjadi `5 + 2 = 7`.
4. **Baris 4 (`b = a - d`):** Gunakan nilai `a` yang **terbaru** (`7`), sehingga `b = 7 - 2 = 5`.
5. **Baris 5 (`c = a * d`):** `c = 7 * 2 = 14`.

| Langkah | nilai `a` | nilai `b` | nilai `c` | nilai `d` |
| :--- | :---: | :---: | :---: | :---: |
| Awal | `12` | `5` | `?` | `?` |
| Setelah Baris 1 | `12` | `5` | `2` | `?` |
| Setelah Baris 2 | `12` | `5` | `2` | `2` |
| Setelah Baris 3 | `7` | `5` | `2` | `2` |
| Setelah Baris 4 | `7` | `5` | `2` | `2` |
| Setelah Baris 5 | `7` | `5` | `14` | `2` |

**Output Akhir:** `7 5 14 2`

---

### Pembahasan Soal 2 (Tracing Logika `&&` dan `||`)
1. **Input `85 85`:** Outputnya adalah **`LULUS BERSYARAT`**.  
   *Penjelasan:* Kondisi pertama `nilai >= 80 && kehadiran >= 90` bernilai **SALAH (False)** karena operator `&&` (DAN) mewajibkan kedua syarat terpenuhi, sedangkan kehadiran hanya `85` ($< 90$). Program lanjut ke `else if (nilai >= 75 || kehadiran == 100)` yang bernilai **BENAR** karena `85 >= 75`. Karena nilai tidak kurang dari 60, tercetak `"LULUS BERSYARAT"`.
2. **Input `55 100`:** Outputnya adalah **`UJIAN ULANG`**.  
   *Penjelasan:* Kondisi pertama gagal. Kondisi `else if` terpenuhi karena `kehadiran == 100` (operator `||` / ATAU cukup salah satu benar). Namun di dalamnya terdapat pengecekan `if (nilai < 60)` yang bernilai benar (`55 < 60`), sehingga mencetak `"UJIAN ULANG"`.
3. **Input `70 80`:** Outputnya adalah **`TIDAK LULUS`**.  
   *Penjelasan:* Kedua kondisi `if` dan `else if` gagal, sehingga jatuh ke blok `else`.

---

### Pembahasan Soal 3 (Detektif Bug)
1. **Penyebab Bug:** Rangkaian `if - else if` dieksekusi dari **atas ke bawah** dan akan langsung berhenti pada cabang pertama yang bernilai benar. Karena `skor >= 55` ditaruh paling atas, angka `90` jelas lebih besar dari `55`, sehingga cabang pertama langsung dijalankan dan cabang di bawahnya (`>= 70`, `>= 85`) tidak pernah diperiksa.
2. **Kode Perbaikan:** Urutkan pengecekan dari batas paling tinggi ke paling rendah:

```cpp
#include <iostream>
using namespace std;

int main() {
    int skor;
    cin >> skor;

    if (skor >= 85) {
        cout << "A" << endl;
    } else if (skor >= 70) {
        cout << "B" << endl;
    } else if (skor >= 55) {
        cout << "C" << endl;
    } else {
        cout << "D" << endl;
    }

    return 0;
}
```

---

### Pembahasan Soal 4 (Konversi Detik)
**Penjelasan Langkah demi Langkah:**
1. Bagi `totalDetik` dengan `3600` untuk mendapatkan jumlah jam utuh.
2. Ambil sisa detiknya dengan `totalDetik % 3600`.
3. Bagi sisa detik tersebut dengan `60` untuk mendapatkan menit, dan ambil sisanya terhadap `60` untuk mendapatkan detik terakhir.

```cpp
#include <iostream>
using namespace std;

int main() {
    int totalDetik;
    cin >> totalDetik;

    int jam = totalDetik / 3600;
    int sisaDetik = totalDetik % 3600;
    int menit = sisaDetik / 60;
    int detik = sisaDetik % 60;

    cout << jam << " jam " << menit << " menit " << detik << " detik" << endl;

    return 0;
}
```

---

### Pembahasan Soal 5 (Kasir Toko Buku)
**Penjelasan Langkah demi Langkah:**
1. Siapkan variabel `diskon = 0`.
2. Gunakan `if (belanja >= 200000)` terlebih dahulu agar belanja di atas Rp 200.000 mendapatkan diskon tertinggi.
3. Kurangi `belanja` dengan `diskon` dan tampilkan hasilnya.

```cpp
#include <iostream>
using namespace std;

int main() {
    int belanja;
    cin >> belanja;

    int diskon = 0;
    if (belanja >= 200000) {
        diskon = 30000;
    } else if (belanja >= 100000) {
        diskon = 10000;
    } else {
        diskon = 0;
    }

    int totalBayar = belanja - diskon;

    cout << "Diskon: " << diskon << endl;
    cout << "Total Bayar: " << totalBayar << endl;

    return 0;
}
```
