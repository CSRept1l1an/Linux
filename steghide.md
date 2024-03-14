### Steghide Cheat Sheet

#### Basic Commands:
- **Embed Data into an Image:**
  ```bash
  steghide embed -cf <cover_file> -ef <embed_file> -sf <output_file>
   ```
  `-cf <cover_file>`: Path to the cover image file.

  `-ef <embed_file>`: Path to the file you want to hide.

  `-sf <output_file>`: Output stego-image file.
- **Extract Data from an Image**
  ```bash
  steghide extract -sf <stego_file>
  ```
  `-sf <stego_file>`: Path to the stego-image file.
  
#### Advanced Options: 
