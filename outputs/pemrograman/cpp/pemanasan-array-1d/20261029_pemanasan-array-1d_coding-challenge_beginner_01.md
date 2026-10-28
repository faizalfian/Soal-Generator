---
id: "SOAL-20261029-001"
kategori: "pemrograman"
subjek: "cpp"
materi: "pemanasan-array-1d"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 10
model_ai: "gemini-3.8-flash"
prompt_version: "v1.0"
created_at: "2026-10-29T04:40:00+07:00"
tags: ["cpp", "array-1d", "pemanasan", "warmup", "isolated-topics", "beginner"]
---

# Paket Pemanasan Kilat: 10 Soal Isolasi Konsep Array 1D (C++)

**Panduan Sesi Pemanasan (JP 1–2):**
1. Setiap soal hanya menguji **satu keterampilan mikro** (topik terisolasi), tidak ada logika campuran atau jebakan rumit.
2. Kerjakan secara berurutan dari Soal 1 sampai Soal 10 untuk membangun *muscle memory* (kebiasaan mengetik dan memikirkan indeks).
3. Seluruh program cukup diselesaikan di dalam fungsi `int main()`.

---

## BAGIAN 1: Akses Indeks & Penelusuran Dasar

### Soal 1: Dua Ujung Array (Akses Indeks 0 dan N-1)
**Fokus Topik:** Mengakses elemen paling awal dan paling akhir tanpa loop.

**Deskripsi Masalah:**  
Diberikan sebuah array berisi $N$ buah bilangan bulat. Tampilkan nilai elemen **paling pertama** (indeks ke-0) dan elemen **paling terakhir** (indeks ke-(N-1)) yang dipisahkan oleh spasi!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat elemen array.
- Output berupa dua angka: elemen pertama dan elemen terakhir dipisahkan spasi.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- -1000 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    10 20 30 40 50
    ```
  - Output:
    ```text
    10 50
    ```
- **Test Case 2:**
  - Input:
    ```text
    3
    7 99 15
    ```
  - Output:
    ```text
    7 15
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    42
    ```
  - Output:
    ```text
    42 42
    ```

> **Petunjuk Fokus:**  
> Kamu tidak butuh loop untuk mencetak! Cukup gunakan `cout << arr[0] << " " << arr[n - 1] << endl;`.

---

### Soal 2: Cetak Barisan Horizontal (Loop Maju Dasar)
**Fokus Topik:** Menelusuri seluruh elemen array dari awal hingga akhir dengan `for` loop.

**Deskripsi Masalah:**  
Diberikan sebuah array berukuran $N$. Tampilkan kembali seluruh isi array tersebut dalam satu baris, di mana setiap angka dipisahkan oleh satu tanda spasi!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa $N$ bilangan bulat dalam satu baris dipisahkan spasi.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- -1000 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    4
    5 8 2 9
    ```
  - Output:
    ```text
    5 8 2 9
    ```
- **Test Case 2:**
  - Input:
    ```text
    3
    100 200 300
    ```
  - Output:
    ```text
    100 200 300
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    -10
    ```
  - Output:
    ```text
    -10
    ```

> **Petunjuk Fokus:**  
> Gunakan `for (int i = 0; i < n; i++)` dan cetak `arr[i] << " "`.

---

### Soal 3: Label Urutan Manusiawi (Indeks vs Nomor Urut)
**Fokus Topik:** Membedakan indeks array komputer (mulai dari 0) dengan nomor urut manusia (mulai dari 1).

**Deskripsi Masalah:**  
Diberikan $N$ nama kode nilai. Tampilkan setiap elemen array baris demi baris dengan format: `Data ke-<nomor>: <nilai>`, di mana `<nomor>` dimulai dari angka `1` hingga $N$.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output terdiri dari $N$ baris dengan format yang ditentukan.

**Batasan (Constraints):**
- 1 ≤ N ≤ 50
- 0 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    3
    85 90 78
    ```
  - Output:
    ```text
    Data ke-1: 85
    Data ke-2: 90
    Data ke-3: 78
    ```
- **Test Case 2:**
  - Input:
    ```text
    2
    10 20
    ```
  - Output:
    ```text
    Data ke-1: 10
    Data ke-2: 20
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    500
    ```
  - Output:
    ```text
    Data ke-1: 500
    ```

> **Petunjuk Fokus:**  
> Nilai elemen berada di `arr[i]`, sedangkan label nomor urut yang dicetak adalah `i + 1`.

---

### Soal 4: Menampilkan Mundur (Loop Terbalik)
**Fokus Topik:** Melatih perulangan `for` mundur dengan syarat `i >= 0` dan `i--`.

**Deskripsi Masalah:**  
Diberikan sebuah array berukuran $N$. Tampilkan isi array dari elemen paling belakang menuju elemen paling depan dalam satu baris dipisahkan spasi!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa barisan angka yang urutannya terbalik dari input.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- -1000 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    4
    1 2 3 4
    ```
  - Output:
    ```text
    4 3 2 1
    ```
- **Test Case 2:**
  - Input:
    ```text
    3
    10 50 30
    ```
  - Output:
    ```text
    30 50 10
    ```
- **Test Case 3:**
  - Input:
    ```text
    2
    99 88
    ```
  - Output:
    ```text
    88 99
    ```

> **Petunjuk Fokus:**  
> Loop dimulai dari `int i = n - 1;`, berjalan selama `i >= 0;`, dan di setiap iterasi kurangi nilai dengan `i--`.

---

## BAGIAN 2: Isolasi Manipulasi Indeks & Filter Kondisi

### Soal 5: Cetak Elemen pada Indeks Genap Saja
**Fokus Topik:** Mengisolasi operasi pada nomor **indeks (`i`)**, bukan pada nilai elemen.

**Deskripsi Masalah:**  
Diberikan sebuah array berukuran $N$. Tampilkan hanya elemen-elemen yang berada pada **nomor indeks genap** (indeks `0`, `2`, `4`, dst.) secara berurutan dipisahkan spasi!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa barisan elemen pada indeks genap.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- 0 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    10 20 30 40 50
    ```
  - Output:
    ```text
    10 30 50
    ```
    *(Penjelasan: arr[0]=10, arr[2]=30, arr[4]=50).*
- **Test Case 2:**
  - Input:
    ```text
    4
    7 14 21 28
    ```
  - Output:
    ```text
    7 21
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

> **Petunjuk Fokus:**  
> Kamu bisa menggunakan lompatan `for (int i = 0; i < n; i += 2)` atau menggunakan `if (i % 2 == 0)`. Ingat: yang dicek adalah `i`, BUKAN `arr[i]`.

---

### Soal 6: Filter Nilai Positif (Isolasi Nilai Elemen)
**Fokus Topik:** Mengisolasi operasi pada **nilai elemen (`arr[i]`)**, bukan pada nomor indeks.

**Deskripsi Masalah:**  
Diberikan sebuah array berisi $N$ bilangan bulat (yang mungkin mengandung angka positif, negatif, atau nol). Tampilkan **hanya angka-angka yang bernilai positif murni ($> 0$)** dipisahkan spasi! (Jika tidak ada angka positif, jangan cetak angka apa pun).

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa angka-angka positif dalam satu baris.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- -1000 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    12 -5 0 25 -8 7
    ```
  - Output:
    ```text
    12 25 7
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    -10 -20 -30 0
    ```
  - Output:
    ```text
    
    ```
    *(Output kosong karena tidak ada angka > 0)*
- **Test Case 3:**
  - Input:
    ```text
    3
    5 10 15
    ```
  - Output:
    ```text
    5 10 15
    ```

> **Petunjuk Fokus:**  
> Periksa isi kotaknya: `if (arr[i] > 0)` lalu cetak `arr[i] << " "`.

---

### Soal 7: Penghitung Kelipatan 5 (Variabel Counter Sederhana)
**Fokus Topik:** Menggunakan variabel pencatat/penghitung (*counter*) di luar loop.

**Deskripsi Masalah:**  
Diberikan array berukuran $N$. Hitunglah **ada berapa banyak bilangan** di dalam array tersebut yang merupakan **kelipatan 5** (habis dibagi 5)!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat positif.
- Output menampilkan jumlah angka kelipatan 5.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- 1 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    10 7 25 14 30 18
    ```
  - Output:
    ```text
    Banyak kelipatan 5: 3
    ```
    *(Penjelasan: Angka 10, 25, dan 30 adalah kelipatan 5).*
- **Test Case 2:**
  - Input:
    ```text
    4
    3 7 11 13
    ```
  - Output:
    ```text
    Banyak kelipatan 5: 0
    ```
- **Test Case 3:**
  - Input:
    ```text
    3
    5 50 500
    ```
  - Output:
    ```text
    Banyak kelipatan 5: 3
    ```

> **Petunjuk Fokus:**  
> Siapkan `int hitung = 0;` sebelum loop. Di dalam loop, jika `arr[i] % 5 == 0`, tambahkan `hitung++;`. Cetak `hitung` setelah loop selesai.

---

## BAGIAN 3: Operasi Aritmatika & Mutasi Data

### Soal 8: Cetak Nilai Berlipat Ganda
**Fokus Topik:** Melakukan operasi aritmatika pada saat menampilkan elemen tanpa merusak array aslinya.

**Deskripsi Masalah:**  
Diberikan array berukuran $N$. Tampilkan setiap elemen array yang nilainya telah **dikalikan dengan 2** ($arr[i] × 2$) dalam satu baris dipisahkan spasi!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa nilai-nilai elemen setelah dikalikan 2.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- -500 ≤ arr[i] ≤ 500

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    4
    3 7 10 15
    ```
  - Output:
    ```text
    6 14 20 30
    ```
- **Test Case 2:**
  - Input:
    ```text
    3
    -4 0 8
    ```
  - Output:
    ```text
    -8 0 16
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    25
    ```
  - Output:
    ```text
    50
    ```

> **Petunjuk Fokus:**  
> Di dalam loop cukup cetak `cout << arr[i] * 2 << " ";`.

---

### Soal 9: Akumulator Penjumlahan Sederhana (Sum)
**Fokus Topik:** Menggunakan variabel penampung (*accumulator*) untuk menghitung total seluruh elemen.

**Deskripsi Masalah:**  
Diberikan sebuah array berukuran $N$. Hitung dan tampilkan **jumlah total (sum)** dari seluruh angka yang ada di dalam array tersebut!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa satu angka hasil penjumlahan total seluruh elemen.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- 0 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    4
    10 20 30 40
    ```
  - Output:
    ```text
    Total: 100
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    5 5 5 5 5
    ```
  - Output:
    ```text
    Total: 25
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    99
    ```
  - Output:
    ```text
    Total: 99
    ```

> **Petunjuk Fokus:**  
> Siapkan `int total = 0;` di LUAR sebelum loop. Di setiap putaran loop, lakukan `total = total + arr[i];`. Cetak `total` setelah loop selesai.

---

### Soal 10: Penggantian Angka Nol Menjadi -1 (Mutasi Nilai di Memori)
**Fokus Topik:** Mengubah isi kotak array di memori (*in-place update*) sebelum dicetak.

**Deskripsi Masalah:**  
Diberikan array berukuran $N$. Lakukan pemeriksaan pada seluruh elemen: jika ada elemen yang bernilai **`0`**, ubahlah nilai elemen tersebut menjadi **`-1`** di dalam array! Setelah semua elemen diperiksa dan diubah, tampilkan seluruh isi array yang sudah diperbarui.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$.
- Baris kedua berisi $N$ bilangan bulat.
- Output berupa barisan elemen array setelah nilai `0` diganti menjadi `-1`.

**Batasan (Constraints):**
- 1 ≤ N ≤ 100
- -1000 ≤ arr[i] ≤ 1000

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    4 0 8 0 12
    ```
  - Output:
    ```text
    4 -1 8 -1 12
    ```
- **Test Case 2:**
  - Input:
    ```text
    3
    0 0 0
    ```
  - Output:
    ```text
    -1 -1 -1
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

> **Petunjuk Fokus:**  
> Gunakan `if (arr[i] == 0) { arr[i] = -1; }` untuk menimpa nilai lama di dalam array. Setelah itu, buat loop untuk mencetak array yang baru.

---
---

# Panduan Pengajar: Kunci Jawaban Lengkap (Paket Pemanasan)

### Pembahasan Soal 1 (Dua Ujung Array)
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

    // Elemen pertama di indeks 0, elemen terakhir di indeks n - 1
    cout << arr[0] << " " << arr[n - 1] << endl;

    return 0;
}
```

---

### Pembahasan Soal 2 (Cetak Barisan Horizontal)
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

    // Loop maju dari indeks 0 sampai n - 1
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 3 (Label Urutan Manusiawi)
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

    // Indeks komputer i, nomor urut manusia i + 1
    for (int i = 0; i < n; i++) {
        cout << "Data ke-" << (i + 1) << ": " << arr[i] << endl;
    }

    return 0;
}
```

---

### Pembahasan Soal 4 (Menampilkan Mundur)
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

    // Loop mundur dari n - 1 turun ke 0
    for (int i = n - 1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 5 (Cetak Indeks Genap Saja)
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

    // Melompat 2 langkah (indeks 0, 2, 4, ...)
    for (int i = 0; i < n; i += 2) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 6 (Filter Nilai Positif)
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
        if (arr[i] > 0) {
            cout << arr[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 7 (Penghitung Kelipatan 5)
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

    int hitung = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 5 == 0) {
            hitung++;
        }
    }

    cout << "Banyak kelipatan 5: " << hitung << endl;

    return 0;
}
```

---

### Pembahasan Soal 8 (Cetak Nilai Berlipat Ganda)
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
        cout << (arr[i] * 2) << " ";
    }
    cout << endl;

    return 0;
}
```

---

### Pembahasan Soal 9 (Akumulator Penjumlahan Sederhana)
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

    cout << "Total: " << total << endl;

    return 0;
}
```

---

### Pembahasan Soal 10 (Penggantian Angka Nol Menjadi -1)
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

    // Tahap 1: Mutasi / timpa nilai di memori
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            arr[i] = -1;
        }
    }

    // Tahap 2: Cetak hasil akhir
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```
