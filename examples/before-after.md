# Contoh Before → After

**Folder sebelum:**
photo1.jpg
photo2.jpg
photo3.jpg
vacation_video.mp4

**Command:**
```bash
python src/renamer.py "./photos" --prefix "Bali-2025-" --number --pad 2 --ext jpg

Hasil setelah:
Bali-2025-01.jpg
Bali-2025-02.jpg
Bali-2025-03.jpg
vacation_video.mp4   ← tidak berubah karena bukan .jpg
