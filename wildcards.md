# Wildcards in Linux

Wildcards are characters used for pattern matching in the Linux command line. They are powerful tools for selecting and manipulating files. Here's a quick reference for commonly used wildcards:

## Asterisk (*)

- **Description:** Matches any sequence of characters (including none).
- **Example:** 
  - `*.txt`: Matches all files with the `.txt` extension.
  - `file*`: Matches all files starting with "file".

## Question Mark (?)

- **Description:** Matches any single character.
- **Example:**
  - `file?.txt`: Matches files like `file1.txt`, `fileA.txt`, etc.

## Square Brackets ([])

- **Description:** Matches any one of the characters within the brackets.
- **Example:**
  - `[aeiou]`: Matches any single vowel.
  - `[0-9]`: Matches any single digit.

## Curly Braces ({})

- **Description:** Matches any of the comma-separated patterns enclosed in curly braces.
- **Example:**
  - `{file1,file2}.txt`: Matches `file1.txt` and `file2.txt`.

## Tilde (~)

- **Description:** Represents the user's home directory.
- **Example:**
  - `~/documents/*.txt`: Matches all `.txt` files in the user's "documents" directory.

## Examples:

- `*.pdf`: Matches all PDF files in the current directory.
- `image[1-3].jpg`: Matches `image1.jpg`, `image2.jpg`, and `image3.jpg`.
- `file[!0-9].txt`: Matches files like `fileA.txt`, but not `file1.txt`.
