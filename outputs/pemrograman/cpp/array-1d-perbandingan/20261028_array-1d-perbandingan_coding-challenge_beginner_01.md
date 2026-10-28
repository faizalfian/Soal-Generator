---
id: "SOAL-20261028-005"
kategori: "pemrograman"
subjek: "cpp"
materi: "array-1d-perbandingan"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:08:00+07:00"
tags: ["cpp", "array-1d", "adjacent-comparison", "min-max", "sorted-check", "code-tracing", "debugging"]
---

# Bank Soal Latihan Mandiri di Rumah — Paket 04
**Topik:** Logika Array Menengah (Perbandingan Antar-Elemen Bersebelahan & Nilai Ekstremum)  
**Estimasi Waktu:** 25–30 Menit

---

## BAGIAN A: Tebak Output & Tabel Tracing (Tanpa Komputer)

### Soal 1: Melacak Perbandingan Dua Elemen Bersebelahan (`arr[i]` dan `arr[i + 1]`)
**Instruksi:**  
Kemampuan membandingkan elemen `arr[i]` dengan tetangga kanannya `arr[i + 1]` adalah dasar dari hampir semua algoritma pengurutan data. Perhatikan kode di bawah ini dan lengkapi tabel tracing-nya!

```cpp
#include <iostream>
using namespace std;

int main() {
    int skor[6] = {70, 85, 80, 90, 95, 88};
    int naik = 0;

    for (int i = 0; i < 5; i++) {
        if (skor[i + 1] > skor[i]) {
            naik++;
        }
    }

    cout << "Jumlah kenaikan: " << naik << endl;
    return 0;
}
```

**Tabel Tracing (Isilah titik-titik berikut):**

| Nilai `i` | Nilai `skor[i]` | Nilai `skor[i + 1]` | Apakah `skor[i + 1] > skor[i]`? | Nilai `naik` |
| :---: | :---: | :---: | :---: | :---: |
| `0` | `70` | `85` | Ya (`85 > 70`) | `1` |
| `1` | `85` | `80` | Tidak (`80 > 85` Salah) | `1` |
| `2` | `80` | ... | ... | ... |
| `3` | ... | ... | ... | ... |
| `4` | ... | ... | ... | ... |

**Tebakan Output Akhir:** `Jumlah kenaikan: ...`

---

### Soal 2: Melacak Variabel Pembanding Berantai
**Instruksi:**  
Perhatikan bagaimana variabel `rekor` berubah di sepanjang loop berikut, dan hitung berapa kali teks `"REKOR BARU!"` tercetak ke layar!

```cpp
#include <iostream>
using namespace std;

int main() {
    int lompatan[6] = {150, 145, 160, 158, 175, 175};
    int rekor = lompatan[0];

    for (int i = 1; i < 6; i++) {
        if (lompatan[i] > rekor) {
            rekor = lompatan[i];
            cout << "REKOR BARU: " << rekor << endl;
        }
    }

    return 0;
}
```

**Pertanyaan:**
1. Mengapa saat `i = 1` (`145`), tidak tercetak `"REKOR BARU"`?
2. Mengapa saat `i = 5` (`175`), tidak tercetak `"REKOR BARU"`?
3. Tuliskan output lengkap yang muncul di layar!

---

## BAGIAN B: Detektif Bug (Analisis & Perbaikan Kode)

### Soal 3: Jebakan Inisialisasi Nilai Terkecil (`min = 0`)
**Deskripsi Masalah:**  
Seorang siswa membuat program untuk mencari **angka terkecil (minimum)** di dalam array. Saat diuji dengan array `{-10, -5, -20, -2}`, program berjalan lancar dan mencetak `-20`.  
Namun ketika diuji dengan array berisi angka positif `{45, 20, 80, 35}`, programnya malah selalu menjawab **`0`** (padahal angka `0` tidak ada di dalam array)!

Berikut kode siswa tersebut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[4] = {45, 20, 80, 35};

    // KODE YANG BERMASALAH (BUGGY):
    int terkecil = 0; 
    for (int i = 0; i < 4; i++) {
        if (arr[i] < terkecil) {
            terkecil = arr[i];
        }
    }

    cout << "Nilai terkecil: " << terkecil << endl;
    return 0;
}
```

**Tugasmu:**
1. Jelaskan mengapa menginisialisasi `int terkecil = 0;` menyebabkan hasil akhir tetap `0` ketika semua isi array bernilai positif!
2. Bagaimana cara menginisialisasi variabel `terkecil` yang benar agar selalu akurat untuk angka berapa pun? Tuliskan kode perbaikannya!

---

## BAGIAN C: Tantangan Koding Kontekstual

### Soal 4: Pemeriksa Apakah Array Sudah Terurut Naik (*Sorted Check*)
**Deskripsi Masalah:**  
Sebelum kita mengurutkan array atau menjalankan *Binary Search*, kita sering perlu memeriksa apakah sebuah array **sudah terurut dari kecil ke besar (non-decreasing)** atau belum.  
Sebuah array dikatakan terurut naik jika untuk setiap elemen berlaku `arr[i] <= arr[i + 1]`. Buatlah program untuk memeriksa apakah array berukuran $N$ sudah terurut naik! Jika sudah, cetak `"TERURUT"`, jika ada satu saja pasangan bersebelahan yang salah urutan (`arr[i] > arr[i + 1]`), cetak `"BELUM TERURUT"`.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa `"TERURUT"` atau `"BELUM TERURUT"`.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $-1000 ≤ arr[i] ≤ 1000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    10 20 25 40 50
    ```
  - Output:
    ```text
    TERURUT
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    10 30 25 40 50
    ```
  - Output:
    ```text
    BELUM TERURUT
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    5 5 8 10
    ```
  - Output:
    ```text
    TERURUT
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Buat variabel penanda `bool urut = true;` (atau `int urut = 1;`). Jalankan loop dari `i = 0` sampai `i < n - 1`. Di dalam loop, cek apakah ada pelanggaran urutan: `if (arr[i] > arr[i + 1])`. Jika ditemukan, ubah `urut = false;` dan `break;`.

---

### Soal 5: Lonjakan Suhu Terbesar Antar-Hari Berurutan
**Deskripsi Masalah:**  
Diberikan data suhu udara selama $N$ hari berurutan. Hitunglah **selisih perubahan suhu terbesar** antara dua hari yang bersebelahan! (Selisih dihitung sebagai nilai mutlak/positif antara `arr[i]` dan `arr[i + 1]`).

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output menampilkan selisih terbesar antara dua elemen yang bersebelahan.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $0 ≤ arr[i] ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    28 30 25 34 31
    ```
  - Output:
    ```text
    Lonjakan terbesar: 9
    ```
    *(Penjelasan: Selisih bersebelahan berturut-turut adalah $|28-30|=2$, $|30-25|=5$, $|25-34|=9$, $|34-31|=3$. Yang terbesar adalah 9).*
- **Test Case 2:**
  - Input:
    ```text
    4
    20 20 20 20
    ```
  - Output:
    ```text
    Lonjakan terbesar: 0
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    40 25 30
    ```
  - Output:
    ```text
    Lonjakan terbesar: 15
    ```

> **Petunjuk Alur Berpikir (Clue):**  
> Untuk menghitung selisih positif antara `arr[i]` dan `arr[i + 1]` tanpa fungsi tambahan:  
> Jika `arr[i] > arr[i + 1]`, maka `selisih = arr[i] - arr[i + 1]`, selain itu `selisih = arr[i + 1] - arr[i]`.  
> Bandingkan `selisih` di setiap langkah dengan variabel `lonjakanMaks`.

---
---

# Kunci Jawaban & Pembahasan (Paket 04)

### Pembahasan Soal 1 (Tracing Perbandingan Bersebelahan)

| Nilai `i` | Nilai `skor[i]` | Nilai `skor[i + 1]` | Apakah `skor[i + 1] > skor[i]`? | Nilai `naik` |
| :---: | :---: | :---: | :---: | :---: |
| `0` | `70` | `85` | Ya (`85 > 70`) | `1` |
| `1` | `85` | `80` | Tidak (`80 > 85` Salah) | `1` |
| `2` | `80` | `90` | Ya (`90 > 80`) | `2` |
| `3` | `90` | `95` | Ya (`95 > 90`) | `3` |
| `4` | `95` | `88` | Tidak (`88 > 95` Salah) | `3` |

**Output Akhir:** `Jumlah kenaikan: 3`

---

### Pembahasan Soal 2 (Tracing Variabel Pembanding Berantai)
1. Saat `i = 1`, `lompatan[1]` adalah `145`, yang lebih kecil dari `rekor` awal (`150`), sehingga syarat `lompatan[i] > rekor` tidak terpenuhi.
2. Saat `i = 5`, `lompatan[5]` adalah `175`, sedangkan `rekor` sudah bernilai `175` dari langkah `i = 4`. Karena syaratnya menggunakan tanda `>` (lebih besar murni, bukan `>=`), maka `175 > 175` bernilai salah.
3. **Output lengkap:**
   ```text
   REKOR BARU: 160
   REKOR BARU: 175
   ```

---

### Pembahasan Soal 3 (Detektif Bug)
1. **Penyebab Bug:** Karena `terkecil` diisi awal dengan `0`, sedangkan seluruh isi array `{45, 20, 80, 35}` bernilai lebih besar dari `0`, maka kondisi `if (arr[i] < terkecil)` tidak pernah terpenuhi sekalipun.
2. **Kode Perbaikan:** Selalu inisialisasikan nilai minimum/maksimum dengan **elemen pertama array (`arr[0]`)**:

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[4] = {45, 20, 80, 35};

    int terkecil = arr[0]; // Gunakan elemen pertama sebagai patokan awal
    for (int i = 1; i < 4; i++) {
        if (arr[i] < terkecil) {
            terkecil = arr[i];
        }
    }

    cout << "Nilai terkecil: " << terkecil << endl;
    return 0;
}
```

---

### Pembahasan Soal 4 (Pemeriksa Array Terurut Naik)
**Penjelasan Langkah demi Langkah:**
1. Anggap di awal bahwa array sudah terurut (`bool urut = true;`).
2. Periksa setiap pasangan bersebelahan `arr[i]` dan `arr[i + 1]` untuk `i = 0` hingga `n - 2`.
3. Jika ditemukan satu saja kondisi `arr[i] > arr[i + 1]`, berarti urutannya rusak: ubah `urut = false;` dan hentikan loop dengan `break`.

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

    bool urut = true;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            urut = false;
            break;
        }
    }

    if (urut) {
        cout << "TERURUT" << endl;
    } else {
        cout << "BELUM TERURUT" << endl;
    }

    return 0;
}
```

---

### Pembahasan Soal 5 (Lonjakan Suhu Terbesar)
**Penjelasan Langkah demi Langkah:**
1. Buat variabel `lonjakanMaks = 0`.
2. Telusuri setiap pasangan bersebelahan dari `i = 0` hingga `n - 2`.
3. Hitung selisih positif antara `arr[i]` dan `arr[i + 1]`. Jika `selisih > lonjakanMaks`, perbarui `lonjakanMaks = selisih`.

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

    int lonjakanMaks = 0;
    for (int i = 0; i < n - 1; i++) {
        int selisih;
        if (arr[i] > arr[i + 1]) {
            selisih = arr[i] - arr[i + 1];
        } else {
            selisih = arr[i + 1] - arr[i];
        }

        if (selisih > lonjakanMaks) {
            lonjakanMaks = selisih;
        }
    }

    cout << "Lonjakan terbesar: " << lonjakanMaks << endl;

    return 0;
}
```
