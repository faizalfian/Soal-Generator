---
id: "SOAL-20261028-008"
kategori: "pemrograman"
subjek: "cpp"
materi: "problem-solving-dekomposisi"
tingkat: "beginner"
tipe: "coding-challenge"
jumlah_soal: 5
model_ai: "gemini-4-argon"
prompt_version: "v1.0"
created_at: "2026-10-28T10:27:00+07:00"
tags: ["cpp", "problem-solving", "decomposition", "streak-counting", "two-sum", "mode-frequency"]
---

# Paket 02: Latihan Analisis Masalah, Dekomposisi, & Eksplorasi Algoritma (Lanjutan)

## Aturan Emas Sebelum Menyentuh Keyboard ("10 Menit Tanpa Koding")
Sama seperti Paket 01, paket ini melatih kemampuanmu **menganalisis masalah dari nol** tanpa bocoran sintaks:
1. **Pahami cerita masalahnya** dan uji dengan contoh kecil di kertas.
2. **Jawab pertanyaan di Lembar Analisis** untuk memecah masalah menjadi bagian-bagian kecil (*Dekomposisi*).
3. Diskusikan dengan teman atau gurumu: **"Mengapa caraku berbeda dengan caramu, dan mana yang lebih efisien?"**

---

### Kasus 1: Pemisahan Antrean Pasien Lansia & Reguler
**Skenario Masalah:**  
Di sebuah klinik kesehatan, terdapat $N$ pasien yang mendaftar secara berurutan. Setiap pasien dicatat **usianya**. Klinik menerapkan aturan antrean prioritas:
1. Seluruh pasien **Lansia (usia $≥ 60$ tahun)** harus dipanggil terlebih dahulu (sesuai urutan kedatangan mereka).
2. Setelah semua pasien Lansia selesai, barulah pasien **Reguler (usia $< 60$ tahun)** dipanggil (juga sesuai urutan kedatangan mereka).

Buatlah program yang menerima daftar usia $N$ pasien sesuai urutan datang, lalu menampilkan urutan usia pasien sesuai urutan pemanggilan klinik!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah pasien).
- Baris kedua berisi $N$ bilangan bulat (usia pasien sesuai urutan datang).
- Output berupa barisan usia pasien yang sudah dikelompokkan (Lansia di depan, Reguler di belakang).

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $1 ≤ usia[i] ≤ 120$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    6
    25 65 40 70 18 60
    ```
  - Output:
    ```text
    65 70 60 25 40 18
    ```
- **Test Case 2:**
  - Input:
    ```text
    4
    30 20 45 50
    ```
  - Output:
    ```text
    30 20 45 50
    ```
- **Test Case 3:**
  - Input:
    ```text
    4
    62 80 75 60
    ```
  - Output:
    ```text
    62 80 75 60
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Jangan Terburu-buru Pakai Sorting!** Apakah soal ini meminta usia diurutkan dari yang paling tua ke paling muda? Perhatikan Test Case 1: mengapa `65 70 60` urutannya seperti itu (bukan `70 65 60`)?
2. **Pecah Tahapan (Dekomposisi):** Bagaimana cara paling sederhana untuk menyelesaikan tugas ini dalam **2 tahap perjalanan** dari awal sampai akhir daftar?
   - *Perjalanan 1:* ........................................................................
   - *Perjalanan 2:* ........................................................................
3. **Eksplorasi Alternatif:** Bagaimana jika klinik meminta hasilnya disimpan ke dalam sebuah array baru bernama `antreanPrioritas[]` sebelum dicetak?

---

### Kasus 2: Mencocokkan Dua Barang dengan Nominal Voucher Belanja
**Skenario Masalah:**  
Andi memenangkan voucher belanja senilai `V` rupiah. Syarat penggunaan voucher tersebut sangat unik: Andi harus membeli **tepat 2 barang berbeda** di etalase toko yang jika dijumlahkan harganya **sama persis** dengan `V` rupiah (tidak boleh kurang dan tidak boleh lebih).  
Diberikan daftar harga $N$ barang di etalase dan nilai voucher `V`. Periksalah apakah Andi **BISA** menemukan 2 barang yang total harganya pas sama dengan `V`!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (banyaknya barang).
- Baris kedua berisi $N$ bilangan bulat (harga masing-masing barang).
- Baris ketiga berisi satu bilangan bulat `V` (nominal voucher).
- Output berupa `"BISA"` jika ada dua barang berbeda yang jumlah harganya sama dengan `V`, atau `"TIDAK BISA"` jika tidak ada.

**Batasan (Constraints):**
- $2 ≤ N ≤ 100$
- $1000 ≤ harga[i], V ≤ 1000000$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    5
    15000 40000 25000 10000 35000
    50000
    ```
  - Output:
    ```text
    BISA
    ```
    *(Alasan: Ada barang seharga 15000 dan 35000 yang jika dijumlahkan = 50000, atau 40000 + 10000 = 50000).*
- **Test Case 2:**
  - Input:
    ```text
    4
    25000 10000 15000 30000
    50000
    ```
  - Output:
    ```text
    TIDAK BISA
    ```
    *(Catatan: Meskipun $25000 + 25000 = 50000$, barang seharga 25000 hanya ada satu, tidak boleh membeli barang yang sama dua kali!)*
- **Test Case 3:**
  - Input:
    ```text
    3
    25000 25000 10000
    50000
    ```
  - Output:
    ```text
    BISA
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Simulasi Manual:** Pada Test Case 2 (`25000, 10000, 15000, 30000`), tuliskan semua pasangan 2 barang yang mungkin dibeli Andi:
   - Barang ke-0 (`25000`) dipasangkan dengan: indeks `1`, indeks `2`, indeks `3`.
   - Barang ke-1 (`10000`) dipasangkan dengan: indeks `...`, indeks `...`
   - Barang ke-2 (`15000`) dipasangkan dengan: indeks `...`
2. **Peringatan Penting:** Mengapa barang ke-0 **tidak boleh** dipasangkan dengan barang ke-0 sendiri?

---

### Kasus 3: Rekor Hari Cerah Berturut-Turut Terpanjang (*Longest Streak*)
**Skenario Masalah:**  
Seorang petani mencatat kondisi cuaca selama $N$ hari menggunakan kode angka:
- Angka **`0`** berarti cuaca **CERAH**.
- Angka **`1`** berarti turun **HUJAN**.

Petani ingin mengetahui berapakah **rekor jumlah hari CERAH (`0`) berturut-turut paling panjang** tanpa terputus oleh hujan!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah hari pengamatan).
- Baris kedua berisi $N$ angka (hanya bernilai `0` atau `1`).
- Output berupa satu angka yaitu panjang rentetan angka `0` terpanjang.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- Elemen array hanya bernilai `0` atau `1`.

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    10
    0 0 1 0 0 0 0 1 0 0
    ```
  - Output:
    ```text
    Rekor cerah terpanjang: 4
    ```
- **Test Case 2:**
  - Input:
    ```text
    5
    1 1 1 1 1
    ```
  - Output:
    ```text
    Rekor cerah terpanjang: 0
    ```
- **Test Case 3:**
  - Input:
    ```text
    6
    1 0 0 0 0 0
    ```
  - Output:
    ```text
    Rekor cerah terpanjang: 5
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Simulasi Otak Manusia:** Bayangkan kamu membaca deretan `0 0 1 0 0 0 0 1 0 0` satu per satu dari kiri ke kanan.
   - Kamu butuh **dua catatan di kepalamu**: `cerahSekarang` (berapa hari cerah yang sedang berlangsung saat ini) dan `rekorTerbaik` (rekor tertinggi yang pernah dicapai sejauh ini).
   - Apa yang kamu lakukan pada `cerahSekarang` setiap kali melihat angka `0`?
   - Apa yang kamu lakukan pada `cerahSekarang` begitu tiba-tiba melihat angka `1` (Hujan)?
   - Kapan `rekorTerbaik` diperbarui?

---

### Kasus 4: Pemilihan Ketua Kelas (Mencari Suara Terbanyak / Modus)
**Skenario Masalah:**  
Pemilihan ketua kelas dilakukan secara tertutup. Terdapat $N$ lembar surat suara yang masuk. Setiap surat suara berisi **satu nomor urut kandidat** yang dipilih (misalnya kandidat nomor `1`, `2`, `3`, atau nomor lainnya).  
Buatlah program untuk menghitung hasil pemungutan suara dan menentukan **kandidat nomor berapa yang memperoleh suara terbanyak**, beserta **jumlah suaranya**! *(Dijamin tidak ada dua kandidat dengan jumlah suara tertinggi yang seri)*.

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah surat suara).
- Baris kedua berisi $N$ bilangan bulat (nomor kandidat pada tiap surat suara).
- Output menampilkan nomor kandidat pemenang dan total suara yang didapatnya.

**Batasan (Constraints):**
- $1 ≤ N ≤ 100$
- $1 ≤ pilihan[i] ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    8
    2 5 2 8 5 2 5 2
    ```
  - Output:
    ```text
    Pemenang: Kandidat 2
    Jumlah Suara: 4
    ```
- **Test Case 2:**
  - Input:
    ```text
    6
    10 20 10 30 20 20
    ```
  - Output:
    ```text
    Pemenang: Kandidat 20
    Jumlah Suara: 3
    ```
- **Test Case 3:**
  - Input:
    ```text
    5
    7 7 7 7 7
    ```
  - Output:
    ```text
    Pemenang: Kandidat 7
    Jumlah Suara: 5
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Pecah Masalah:** Kamu sudah pernah membuat program untuk menghitung berapa kali sebuah angka $X$ muncul di dalam array (Paket 05 Soal 4 / Paket Kelas Soal 8).
   - Sekarang, bagaimana jika angka yang ingin dihitung kemunculannya adalah **setiap elemen `pilihan[i]`** di dalam array itu sendiri?
2. **Eksplorasi Alternatif:**
   - *Cara A:* Untuk setiap elemen di indeks `i`, hitung berapa kali angka tersebut muncul di seluruh array, lalu bandingkan dengan `suaraTerbanyak`.
   - *Cara B:* Bagaimana jika kertas suaranya **diurutkan dulu** (`2 2 2 2 5 5 5 8`)? Apakah menghitungnya jadi lebih mudah?

---

### Kasus 5: Menggabungkan Dua Kelas ke Satu Daftar Urut
**Skenario Masalah:**  
Sekolah ingin menggabungkan data nilai dari **Kelas A** (berisi $N$ siswa) dan **Kelas B** (berisi $M$ siswa) menjadi satu daftar gabungan berukuran $N + M$ siswa, kemudian menampilkannya dalam keadaan **terurut dari nilai terkecil hingga nilai terbesar**!

**Format Input & Output:**
- Baris pertama berisi bilangan bulat $N$ (jumlah siswa Kelas A).
- Baris kedua berisi $N$ bilangan bulat (nilai siswa Kelas A).
- Baris ketiga berisi bilangan bulat $M$ (jumlah siswa Kelas B).
- Baris keempat berisi $M$ bilangan bulat (nilai siswa Kelas B).
- Output berupa $N + M$ nilai gabungan yang sudah terurut naik.

**Batasan (Constraints):**
- $1 ≤ N, M ≤ 50$ (sehingga total gabungan maksimal 100)
- $0 ≤ nilai ≤ 100$

**Contoh Test Case:**
- **Test Case 1:**
  - Input:
    ```text
    3
    80 60 90
    4
    75 85 50 70
    ```
  - Output:
    ```text
    50 60 70 75 80 85 90
    ```
- **Test Case 2:**
  - Input:
    ```text
    2
    100 50
    2
    90 60
    ```
  - Output:
    ```text
    50 60 90 100
    ```
- **Test Case 3:**
  - Input:
    ```text
    1
    75
    2
    80 70
    ```
  - Output:
    ```text
    70 75 80
    ```

#### Lembar Analisis & Dekomposisi (Isi Sebelum Ngoding!)
1. **Pecah Masalah Menjadi Tahap Kecil:** Jangan bingung melihat 2 array input! Pecah menjadi:
   - *Tahap 1:* Bagaimana cara memasukkan semua isi Kelas A dan Kelas B ke dalam satu array besar `gabungan[100]`?
   - *Tahap 2:* Jika `gabungan[]` sudah berisi seluruh $N + M$ angka, algoritma apa yang kamu gunakan untuk mengurutkannya?

---
---

# Panduan Pengajar: Dekomposisi & Perbandingan Alternatif Algoritma (Paket 02)

## Pembahasan Kasus 1: Pemisahan Antrean Pasien Lansia & Reguler

### Dekomposisi Masalah:
Masalah ini menguji apakah siswa mampu membedakan antara **Pengelompokan (*Filtering/Partitioning*)** dengan **Pengurutan (*Sorting*)**. Karena urutan kedatangan di dalam masing-masing kelompok tidak boleh berubah, kita tidak boleh menggunakan *Bubble Sort* biasa.

### Pendekatan A: Dua Kali Perjalanan Loop Cetak (Sangat Sederhana)
1. **Loop Pertama:** Telusuri dari awal sampai akhir, cetak hanya yang berusia $≥ 60$.
2. **Loop Kedua:** Telusuri lagi dari awal sampai akhir, cetak hanya yang berusia $< 60$.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int usia[100];
    for (int i = 0; i < n; i++) {
        cin >> usia[i];
    }

    // Tahap 1: Panggil semua Lansia (>= 60) sesuai urutan datang
    for (int i = 0; i < n; i++) {
        if (usia[i] >= 60) {
            cout << usia[i] << " ";
        }
    }

    // Tahap 2: Panggil semua Reguler (< 60) sesuai urutan datang
    for (int i = 0; i < n; i++) {
        if (usia[i] < 60) {
            cout << usia[i] << " ";
        }
    }
    cout << endl;

    return 0;
}
```

### Pendekatan B: Menyusun ke Array Baru (`hasil[]`) dengan Penunjuk Posisi
Jika datanya harus disimpan ke dalam sebuah array baru untuk diolah lebih lanjut:

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int usia[100], hasil[100];
    for (int i = 0; i < n; i++) {
        cin >> usia[i];
    }

    int pos = 0; // Penunjuk indeks pengisian untuk array hasil[]

    // Masukkan lansia dulu
    for (int i = 0; i < n; i++) {
        if (usia[i] >= 60) {
            hasil[pos] = usia[i];
            pos++;
        }
    }

    // Lanjutkan masukkan reguler
    for (int i = 0; i < n; i++) {
        if (usia[i] < 60) {
            hasil[pos] = usia[i];
            pos++;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << hasil[i] << " ";
    }
    cout << endl;

    return 0;
}
```

---

## Pembahasan Kasus 2: Mencocokkan Dua Barang dengan Nominal Voucher

### Pendekatan A: Periksa Semua Pasangan Barang dengan Nested Loop
Pasangkan setiap barang di indeks `i` dengan setiap barang lain di indeks `j` (di mana `j` mulai dari `i + 1` agar tidak memasangkan barang yang sama dua kali).

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, v;
    cin >> n;

    int harga[100];
    for (int i = 0; i < n; i++) {
        cin >> harga[i];
    }
    cin >> v;

    bool bisa = false;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (harga[i] + harga[j] == v) {
                bisa = true;
                break;
            }
        }
    }

    if (bisa) cout << "BISA" << endl;
    else cout << "TIDAK BISA" << endl;

    return 0;
}
```

### Pendekatan B: Urutkan Dulu, Lalu Gunakan Dua Penunjuk (*Two Pointers*)
Jika harga barang diurutkan dari termurah ke termahal, kita bisa menaruh penunjuk `kiri = 0` (termurah) dan `kanan = n - 1` (termahal):
- Jika `harga[kiri] + harga[kanan] == v` $→$ Ketemu!
- Jika jumlahnya terlalu kecil ($< v$) $→$ Geser `kiri++` (cari yang lebih mahal).
- Jika jumlahnya terlalu besar ($> v$) $→$ Geser `kanan--` (cari yang lebih murah).

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, v;
    cin >> n;

    int harga[100];
    for (int i = 0; i < n; i++) {
        cin >> harga[i];
    }
    cin >> v;

    // Tahap 1: Urutkan harga dengan Bubble Sort
    for (int tahap = 0; tahap < n - 1; tahap++) {
        for (int i = 0; i < n - 1 - tahap; i++) {
            if (harga[i] > harga[i + 1]) {
                int temp = harga[i];
                harga[i] = harga[i + 1];
                harga[i + 1] = temp;
            }
        }
    }

    // Tahap 2: Pencarian Dua Ujung (Two Pointers)
    int kiri = 0, kanan = n - 1;
    bool bisa = false;
    while (kiri < kanan) {
        int jumlah = harga[kiri] + harga[kanan];
        if (jumlah == v) {
            bisa = true;
            break;
        } else if (jumlah < v) {
            kiri++;
        } else {
            kanan--;
        }
    }

    if (bisa) cout << "BISA" << endl;
    else cout << "TIDAK BISA" << endl;

    return 0;
}
```

---

## Pembahasan Kasus 3: Rekor Hari Cerah Berturut-Turut Terpanjang

### Pendekatan A: Pelacakan State dalam 1 Loop (`cerahSekarang` & `rekorMaks`)
Pendekatan paling elegan: gunakan variabel `cerahSekarang` yang bertambah saat melihat `0`, dan langsung ter-reset menjadi `0` saat melihat `1`.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int cuaca[100];
    for (int i = 0; i < n; i++) {
        cin >> cuaca[i];
    }

    int cerahSekarang = 0;
    int rekorMaks = 0;

    for (int i = 0; i < n; i++) {
        if (cuaca[i] == 0) {
            cerahSekarang++;
            if (cerahSekarang > rekorMaks) {
                rekorMaks = cerahSekarang;
            }
        } else {
            cerahSekarang = 0; // Terputus oleh hujan, reset kembali ke 0
        }
    }

    cout << "Rekor cerah terpanjang: " << rekorMaks << endl;
    return 0;
}
```

### Pendekatan B: Hitung Rentetan Maju dari Setiap Posisi `i` (Nested Loop)
Sebagian siswa lebih mudah berpikir: *"Dari setiap hari ke-`i`, hitung ada berapa angka `0` berurutan mulai dari hari `i` tersebut sampai ketemu angka `1`."*

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int cuaca[100];
    for (int i = 0; i < n; i++) {
        cin >> cuaca[i];
    }

    int rekorMaks = 0;
    for (int i = 0; i < n; i++) {
        int hitung = 0;
        for (int j = i; j < n; j++) {
            if (cuaca[j] == 0) {
                hitung++;
            } else {
                break; // Berhenti menghitung karena ketemu hujan
            }
        }
        if (hitung > rekorMaks) {
            rekorMaks = hitung;
        }
    }

    cout << "Rekor cerah terpanjang: " << rekorMaks << endl;
    return 0;
}
```

---

## Pembahasan Kasus 4: Pemilihan Ketua Kelas (Modus / Suara Terbanyak)

### Pendekatan A: Hitung Frekuensi Tiap Elemen dengan Nested Loop
Untuk setiap elemen `pilihan[i]`, kita jalankan loop dalam untuk menghitung berapa kali kandidat tersebut muncul di seluruh array.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int pilihan[100];
    for (int i = 0; i < n; i++) {
        cin >> pilihan[i];
    }

    int pemenang = pilihan[0];
    int suaraTerbanyak = 0;

    for (int i = 0; i < n; i++) {
        int hitungSuara = 0;
        for (int j = 0; j < n; j++) {
            if (pilihan[j] == pilihan[i]) {
                hitungSuara++;
            }
        }

        if (hitungSuara > suaraTerbanyak) {
            suaraTerbanyak = hitungSuara;
            pemenang = pilihan[i];
        }
    }

    cout << "Pemenang: Kandidat " << pemenang << endl;
    cout << "Jumlah Suara: " << suaraTerbanyak << endl;

    return 0;
}
```

### Pendekatan B: Urutkan Surat Suara, Lalu Hitung Rentetan yang Sama
Jika surat suara diurutkan dulu (misal `2 5 2 8 5 2 5 2` menjadi `2 2 2 2 5 5 5 8`), maka nomor kandidat yang sama akan berdempetan dan bisa dihitung persis seperti menghitung *streak* pada Kasus 3!

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int pilihan[100];
    for (int i = 0; i < n; i++) {
        cin >> pilihan[i];
    }

    // Tahap 1: Urutkan surat suara dengan Bubble Sort
    for (int tahap = 0; tahap < n - 1; tahap++) {
        for (int i = 0; i < n - 1 - tahap; i++) {
            if (pilihan[i] > pilihan[i + 1]) {
                int temp = pilihan[i];
                pilihan[i] = pilihan[i + 1];
                pilihan[i + 1] = temp;
            }
        }
    }

    // Tahap 2: Hitung rentetan angka yang sama bersebelahan
    int pemenang = pilihan[0];
    int suaraTerbanyak = 1;
    int suaraSaatIni = 1;

    for (int i = 1; i < n; i++) {
        if (pilihan[i] == pilihan[i - 1]) {
            suaraSaatIni++;
        } else {
            suaraSaatIni = 1;
        }

        if (suaraSaatIni > suaraTerbanyak) {
            suaraTerbanyak = suaraSaatIni;
            pemenang = pilihan[i];
        }
    }

    cout << "Pemenang: Kandidat " << pemenang << endl;
    cout << "Jumlah Suara: " << suaraTerbanyak << endl;

    return 0;
}
```

---

## Pembahasan Kasus 5: Menggabungkan Dua Kelas ke Satu Daftar Urut

### Dekomposisi Masalah:
1. **Tahap 1:** Baca $N$ elemen Kelas A dan masukkan ke indeks `0` s/d `N - 1` pada array `gabungan[]`.
2. **Tahap 2:** Baca $M$ elemen Kelas B dan masukkan ke indeks `N` s/d `N + M - 1` pada array `gabungan[]`.
3. **Tahap 3:** Jalankan *Bubble Sort* pada array `gabungan[]` sepanjang `total = N + M`.

### Kode Solusi Acuan:
```cpp
#include <iostream>
using namespace std;

int main() {
    int n, m;
    int gabungan[100];

    // Tahap 1: Masukkan data Kelas A ke dalam array gabungan
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> gabungan[i];
    }

    // Tahap 2: Masukkan data Kelas B melanjutkan posisi setelah Kelas A
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> gabungan[n + i];
    }

    int totalSiswa = n + m;

    // Tahap 3: Urutkan array gabungan menggunakan Bubble Sort
    for (int tahap = 0; tahap < totalSiswa - 1; tahap++) {
        for (int i = 0; i < totalSiswa - 1 - tahap; i++) {
            if (gabungan[i] > gabungan[i + 1]) {
                int temp = gabungan[i];
                gabungan[i] = gabungan[i + 1];
                gabungan[i + 1] = temp;
            }
        }
    }

    // Tahap 4: Tampilkan hasil akhir
    for (int i = 0; i < totalSiswa; i++) {
        cout << gabungan[i] << " ";
    }
    cout << endl;

    return 0;
}
```
