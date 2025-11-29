# ULBMP – Représentation & Compression d’Images (Python + PySide6)

## Résumé du projet
Ce projet propose l’implémentation d’un nouveau format d’image personnalisé : **ULBMP (ULB-bitMaP)**, inspiré du format BMP.  
Il inclut :

- Un encodeur (version 1 et version 2 compressée)
- Un décodeur
- Une interface graphique PySide6 pour afficher et convertir les images
- Une classe Pixel, Image, Encoder, Decoder
- Une compression simple **RLE (Run-Length Encoding)** dans la version 2

Le projet permet de charger, visualiser, compresser et sauvegarder une image au format `.ulbmp`.

## Spécifications du format ULBMP

## 🔹 Version 1 — Représentation brute
- Stockage direct des pixels sous forme RGB (3 octets par pixel).
- Taille totale = `12 + (width × height × 3)`
- Aucune compression.

## 🔹 Version 2 — Compression RLE
Les pixels identiques consécutifs sont compressés.

