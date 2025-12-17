Simple Example: Sort [5, 2, 8, 1, 9]
Compare and swap adjacent pairs from left to right
[5, 2, 8, 1, 9]
 ↓ ↓
[2, 5, 8, 1, 9]  (5 > 2, swap)
    ↓ ↓
[2, 5, 8, 1, 9]  (5 < 8, no swap)
       ↓ ↓
[2, 5, 1, 8, 9]  (8 > 1, swap)
          ↓ ↓
[2, 5, 1, 8, 9]  (8 < 9, no swap)

Result after Pass 1: [2, 5, 1, 8, 9]  ← 9 bubbled to end
