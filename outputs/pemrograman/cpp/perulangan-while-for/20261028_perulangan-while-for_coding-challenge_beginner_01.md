---
id: "SOAL-20261028-003"
kategori: "pemrograman"
subjek: "cpp"
materi: "perulangan-while-for"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:06:00+07:00"
tags: ["cpp", "while-loop", "for-loop", "accumulator", "counter", "code-tracing", "debugging"]
---

# Bank Soal Latihan Mandiri di Rumah — Paket 02
**Topik:** Logika Perulangan `while` dan `for` (Tanpa Array)  
**Estimasi Waktu:** 20–30 Menit

---

## BAGIAN A: Tebak Output & Tabel Tracing (Tanpa Komputer)

### Soal 1: Melacak Putaran `while` Loop
**Instruksi:**  
Perhatikan kode C++ di bawah ini. Lacaklah perubahan nilai variabel `n` dan `langkah` pada setiap putaran `while` dengan melengkapi tabel di bawahnya, lalu tentukan output akhirnya!

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 50;
    int langkah = 0;

    while (n > 3) {
        n = n / 2;
        langkah = langkah + 1;
    }

    cout << "Sisa n: " << n << endl;
    cout << "Total langkah: " << langkah << endl;
    return 0;
}
```

**Tabel Tracing (Isilah titik-titik berikut):**

| Putaran Ke- | Cek Syarat `n > 3` | Nilai `n` setelah `n = n / 2` | Nilai `langkah` |
| :---: | :---: | :---: | :---: |
| Kondisi Awal | - | `50` | `0` |
| Putaran 1 | `50 > 3` (Benar) | `25` | `1` |
| Putaran 2 | `25 > 3` (Benar) | ... | ... |
| Putaran 3 | ... | ... | ... |
| Putaran 4 | ... | ... | ... |
| Setelah Putaran 4 | ... (Salah -> Berhenti) | - | - |

**Tebakan Output Akhir:**
- `Sisa n: ...`
- `Total langkah: ...`

---

### Soal 2: Menebak Output `for` Loop dengan Lompatan dan `if`
**Instruksi:**  
Telusuri perulangan `for` di bawah ini dengan cermat. Perhatikan bahwa kenaikan variabel `i` adalah **`i += 2`** (bertambah 2 setiap langkah), bukan `i++`!

```cpp
#include <iostream>
using namespace std;

int main() {
    int hasil = 0;

    for (int i = 1; i <= 9; i += 2) {
        if (i % 3 == 0) {
            hasil = hasil + (i * 2);
        } else {
            hasil = hasil + i;
        }
        cout << hasil << " ";
    }

    return 0;
}
```

**Pertanyaan:**
1. Sebutkan angka `i` berapa saja yang akan masuk ke dalam perulangan tersebut!
2. Pada saat `i` bernilai berapa saja kondisi `if (i % 3 == 0)` bernilai BENAR?
3. Tuliskan deretan angka yang tercetak di layar!

---

## BAGIAN B: Detektif Bug (Analisis & Perbaikan Kode)

### Soal 3: Dua Kesalahan Klasik di Dalam Loop
**Deskripsi Masalah:**  
Seorang siswa ingin membuat program untuk menghitung **jumlah total bilangan dari 1 sampai `N`** (misal jika `N = 4`, maka $1 + 2 + 3 + 4 = 10$). Namun kode yang ia tulis memiliki **2 bug fatal**: variabel `total` tidak pernah bertambah dengan benar, dan jika menggunakan `while` sebelumnya ia sempat mengalami *infinite loop*.

Perhatikan kode `for` yang ia tulis di bawah ini:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 4;

    // KODE YANG BERMASALAH (BUGGY):
    for (int i = 1; i <= n; i++) {
        int total = 0;          // Bug 1
        total = total + i;
        cout << total << endl;  // Bug 2 (Inginnya hanya cetak 1 kali di akhir)
    }

    return 0;
}
```

**Tugasmu:**
1. Mengapa menaruh `int total = 0;` di **dalam** kurung kurawal `{ ... }` milik `for` loop menyebabkan hasil penjumlahan selalu ter-reset?
2. Perbaiki kode di atas agar hanya mencetak satu baris hasil akhir (yaitu `10` saat `n = 4`)!

---

## BAGIAN C: Tantangan Koding Kontekstual

### Soal 4: Simulasi Menabung di Celengan (`while` Loop)
**Deskripsi Masalah:**  
Budi ingin membeli sepatu seharga `target` rupiah. Saat ini tabungan awal Budi adalah `0` rupiah. Setiap hari, Budi menabung sebesar `setoranHarian` rupiah secara rutin. Buatlah program menggunakan **`while` loop** untuk menghitung **berapa hari** yang dibutuhkan Budi sampai total tabungannya **minimal mencapai atau melebihi** harga sepatu tersebut!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat `target` (harga sepatu) dan `setoranHarian`.
- Output menampilkan jumlah hari yang dibutuhkan dan total uang yang terkumpul pada hari terakhir tersebut.

**Batasan (Constraints):**
- $1000 ≤ target ≤ 10000000$
- $500 ≤ setoranHarian ≤ 1000000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input: `100000 15000`
  - Output:
    ```text
    Hari yang dibutuhkan: 7
    Total tabungan terkumpul: 105000
    ```
- **Test Case 2:**
  - Input: `50000 10000`
  - Output:
    ```text
    Hari yang dibutuhkan: 5
    Total tabungan terkumpul: 50000
    ```
- **Test Case 3:**
  - Input: `25000 30000`
  - Output:
    ```text
    Hari yang dibutuhkan: 1
    Total tabungan terkumpul: 30000
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Karena kita belum tahu pasti berapa putaran harinya, gunakan `while (tabungan < target)`. Di dalam loop, tambahkan `tabungan = tabungan + setoranHarian;` dan tambahkan penghitung `hari++`.

---

### Soal 5: Permainan "Tepuk Tiga-Lima" (`for` Loop & `if-else`)
**Deskripsi Masalah:**  
Dalam sebuah permainan berhitung dari angka `1` sampai `N`, setiap siswa harus menyebutkan angka secara berurutan, KECUALI:
- Jika angkanya **habis dibagi 3 DAN habis dibagi 5** (kelipatan 15), cetak `"TEPUK-GANDA"`.
- Jika angkanya hanya **habis dibagi 3**, cetak `"TEPUK-TIGA"`.
- Jika angkanya hanya **habis dibagi 5**, cetak `"TEPUK-LIMA"`.
- Selain itu, cetak angka tersebut seperti biasa.

**Format Input & Output:**
- Input berupa satu bilangan bulat positif $N$.
- Output berupa barisan kata/angka dari $1$ sampai $N$ yang dipisahkan oleh spasi.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input: `6`
  - Output: `1 2 TEPUK-TIGA 4 TEPUK-LIMA TEPUK-TIGA`
- **Test Case 2:**
  - Input: `15`
  - Output: `1 2 TEPUK-TIGA 4 TEPUK-LIMA TEPUK-TIGA 7 8 TEPUK-TIGA TEPUK-LIMA 11 TEPUK-TIGA 13 14 TEPUK-GANDA`
- **Test Case 3:**
  - Input: `2`
  - Output: `1 2`

> **Petunjuk Alur Berpikir (Clue):**  
> Gunakan `for (int i = 1; i <= n; i++)`. Ingat pelajaran Paket 01: periksa syarat yang paling ketat/spesifik terlebih dahulu, yaitu `if (i % 3 == 0 && i % 5 == 0)` di urutan paling atas!

---
---

# Kunci Jawaban & Pembahasan (Paket 02)

### Pembahasan Soal 1 (Tracing `while` Loop)

| Putaran Ke- | Cek Syarat `n > 3` | Nilai `n` setelah `n = n / 2` | Nilai `langkah` |
| :---: | :---: | :---: | :---: |
| Kondisi Awal | - | `50` | `0` |
| Putaran 1 | `50 > 3` (Benar) | `25` | `1` |
| Putaran 2 | `25 > 3` (Benar) | `12` (`25 / 2` bulat) | `2` |
| Putaran 3 | `12 > 3` (Benar) | `6` | `3` |
| Putaran 4 | `6 > 3` (Benar) | `3` | `4` |
| Setelah Putaran 4 | `3 > 3` (Salah -> Berhenti) | - | - |

**Output Akhir:**
- `Sisa n: 3`
- `Total langkah: 4`

---

### Pembahasan Soal 2 (Tracing `for` Loop)
1. Nilai `i` yang masuk ke dalam loop adalah bilangan ganjil: **`1, 3, 5, 7, 9`**.
2. Kondisi `i % 3 == 0` bernilai BENAR saat **`i = 3`** dan **`i = 9`**.
3. Jejak perhitungan `hasil`:
   - `i = 1`: `1 % 3 != 0` $→$ `hasil = 0 + 1 = 1` (cetak `1`)
   - `i = 3`: `3 % 3 == 0` $→$ `hasil = 1 + (3 * 2) = 7` (cetak `7`)
   - `i = 5`: `5 % 3 != 0` $→$ `hasil = 7 + 5 = 12` (cetak `12`)
   - `i = 7`: `7 % 3 != 0` $→$ `hasil = 12 + 7 = 19` (cetak `19`)
   - `i = 9`: `9 % 3 == 0` $→$ `hasil = 19 + (9 * 2) = 37` (cetak `37`)
   - **Output di layar:** `1 7 12 19 37 `

---

### Pembahasan Soal 3 (Detektif Bug)
1. **Penyebab Bug:** Mendeklarasikan `int total = 0;` di dalam badan loop membuat komputer mengulang pembuatan variabel `total` dari `0` pada setiap putaran baru. Akibatnya, hasil penjumlahan dari putaran sebelumnya selalu hilang. Selain itu, `cout` di dalam loop membuat program mencetak di setiap putaran, bukan di akhir saja.
2. **Kode Perbaikan:**

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 4;
    int total = 0; // Deklarasikan di LUAR sebelum loop

    for (int i = 1; i <= n; i++) {
        total = total + i;
    }

    // Cetak satu kali saja setelah loop selesai
    cout << total << endl;

    return 0;
}
```

---

### Pembahasan Soal 4 (Simulasi Menabung dengan `while`)
**Penjelasan Langkah demi Langkah:**
1. Buat variabel `tabungan = 0` dan `hari = 0`.
2. Selama `tabungan < target`, tambahkan `setoranHarian` ke `tabungan` dan tambahkan `hari` sebanyak 1.
3. Begitu `tabungan >= target`, kondisi `while` menjadi salah dan perulangan otomatis berhenti.

```cpp
#include <iostream>
using namespace std;

int main() {
    int target, setoranHarian;
    cin >> target >> setoranHarian;

    int tabungan = 0;
    int hari = 0;

    while (tabungan < target) {
        tabungan = tabungan + setoranHarian;
        hari++;
    }

    cout << "Hari yang dibutuhkan: " << hari << endl;
    cout << "Total tabungan terkumpul: " << tabungan << endl;

    return 0;
}
```

---

### Pembahasan Soal 5 (Permainan Tepuk Tiga-Lima)
**Penjelasan Langkah demi Langkah:**
1. Gunakan perulangan `for` dari `i = 1` hingga `n`.
2. Cek syarat habis dibagi 3 dan 5 (`i % 3 == 0 && i % 5 == 0`) pada cabang `if` pertama.
3. Lanjutkan dengan `else if (i % 3 == 0)`, `else if (i % 5 == 0)`, dan `else`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "TEPUK-GANDA ";
        } else if (i % 3 == 0) {
            cout << "TEPUK-TIGA ";
        } else if (i % 5 == 0) {
            cout << "TEPUK-LIMA ";
        } else {
            cout << i << " ";
        }
    }
    cout << endl;

    return 0;
}
```
