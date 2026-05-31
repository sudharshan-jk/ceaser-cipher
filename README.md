# caesar-cipher

A command line tool to encrypt, decrypt, brute force, and crack Caesar cipher messages using frequency analysis.

No external libraries needed — pure Python.

---

## usage

```cmd
python cipher.py encrypt "hello world" --shift 3
python cipher.py decrypt "khoor zruog" --shift 3
python cipher.py bruteforce "khoor zruog"
python cipher.py analyse "khoor zruog"
```

---

## commands

| command | what it does |
|---------|--------------|
| encrypt | encrypts plaintext with a given shift |
| decrypt | decrypts ciphertext with a given shift |
| bruteforce | tries all 25 possible shifts |
| analyse | uses letter frequency to guess the shift |

---

## example output

```
caesar cipher tool
------------------------------
  plaintext:  hello world
  shift:      3
  ciphertext: khoor zruog

-- brute force all 25 shifts ----------------------------

  shift  1:  jgnnq yqtnf
  shift  2:  ifmmp xpsme
  shift  3:  hello world   <-- this is the one
  ...

-- frequency analysis ------------------------------------

  k  ####################  5 (33.3%)
  h  ########             2 (13.3%)
  ...

  most common letter: 'k'
  likely shift: 6
  likely plaintext: ebiil tloia
```

---

## how frequency analysis works

in english, the letter E appears most often. if we find the most common letter in the ciphertext and assume it maps to E, we can calculate the shift and decode the message without knowing the key.
