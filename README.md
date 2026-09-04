
# Visualisasi Vektor: Resultan Jajar Genjang & Sudut Antar Vektor

Skrip Python sederhana untuk menghitung dan memvisualisasikan operasi vektor 2D, termasuk resultan (metode jajar genjang), dot product, dan sudut antara dua vektor.

## Fitur

- Menghitung **dot product** antara vektor A dan B
- Menghitung **vektor resultan** (A + B) beserta panjangnya (magnitude)
- Menghitung **sudut** antara vektor A dan B menggunakan rumus cosinus
- Visualisasi grafis:
  - Vektor A, B, dan Resultan digambar dengan panah (quiver)
  - Garis putus-putus jajar genjang
  - Busur sudut (θ) antara A dan B lengkap dengan label derajat
  - Label kuadran pada bidang kartesius

## Contoh Output

```
Vektor A = [30 50]
Vektor B = [-10   2]
Dot product A·B = -200
Resultan (A + B) = [20 52]
Panjang Resultan |R| = 55.71
Sudut antara A dan B = 102.71 derajat
```

Beserta grafik jajar genjang vektor dengan sudut θ ditandai pada bidang XY.

## Instalasi

Pastikan Python 3 sudah terpasang, lalu instal dependensi berikut:

```bash
pip install numpy matplotlib
```

## Cara Menjalankan

```bash
python vektor_resultan.py
```

Skrip akan mencetak hasil perhitungan di terminal dan menampilkan jendela grafik berisi visualisasi vektor.

## Struktur Perhitungan

| Variabel | Keterangan |
|---|---|
| `A`, `B` | Vektor input dalam bentuk `[x, y]` |
| `dot_AB` | Hasil dot product A · B |
| `R` | Vektor resultan (A + B) |
| `magnitude_R` | Panjang (norma) vektor resultan |
| `theta_deg` | Sudut antara A dan B dalam derajat |

## Kustomisasi

Untuk mencoba vektor lain, cukup ubah nilai `A` dan `B` di bagian atas skrip:

```python
A = np.array([30, 50])
B = np.array([-10, 2])
```

Batas sumbu (`xlim`, `ylim`) mungkin perlu disesuaikan jika menggunakan vektor dengan skala yang jauh berbeda.

## Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan pembelajaran.
