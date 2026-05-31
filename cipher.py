import sys
import argparse


def encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(text):
    print()
    print("-- brute force all 25 shifts " + "-" * 28)
    print()
    for shift in range(1, 26):
        result = decrypt(text, shift)
        print(f"  shift {str(shift).rjust(2)}:  {result}")
    print()


def analyse_frequency(text):
    """
    simple frequency analysis — most common letter is likely E
    returns the most likely shift
    """
    letters = [c.lower() for c in text if c.isalpha()]
    if not letters:
        return None

    freq = {}
    for c in letters:
        freq[c] = freq.get(c, 0) + 1

    most_common = max(freq, key=freq.get)
    # E is the most common letter in english (index 4)
    likely_shift = (ord(most_common) - ord('e')) % 26
    return likely_shift, most_common, freq


def print_freq(text):
    result = analyse_frequency(text)
    if not result:
        print("[!] no letters found in input")
        return

    shift, most_common, freq = result
    total = sum(freq.values())

    print()
    print("-- frequency analysis " + "-" * 35)
    print()
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_freq[:8]:
        bar = "#" * count
        pct = round((count / total) * 100, 1)
        print(f"  {char}  {bar:<20}  {count} ({pct}%)")

    print()
    print(f"  most common letter: '{most_common}'")
    print(f"  likely shift: {shift}  (assuming most common = 'e')")
    print(f"  likely plaintext: {decrypt(text, shift)}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="caesar cipher tool - encrypt, decrypt, and crack messages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python cipher.py encrypt "hello world" --shift 3
  python cipher.py decrypt "khoor zruog" --shift 3
  python cipher.py bruteforce "khoor zruog"
  python cipher.py analyse "khoor zruog"
        """
    )

    subparsers = parser.add_subparsers(dest="command")

    enc = subparsers.add_parser("encrypt", help="encrypt a message")
    enc.add_argument("text", help="text to encrypt")
    enc.add_argument("--shift", type=int, required=True, help="shift value (1-25)")

    dec = subparsers.add_parser("decrypt", help="decrypt a message")
    dec.add_argument("text", help="text to decrypt")
    dec.add_argument("--shift", type=int, required=True, help="shift value (1-25)")

    bf = subparsers.add_parser("bruteforce", help="try all 25 shifts")
    bf.add_argument("text", help="ciphertext to brute force")

    an = subparsers.add_parser("analyse", help="frequency analysis to guess the shift")
    an.add_argument("text", help="ciphertext to analyse")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    print()
    print("caesar cipher tool")
    print("-" * 30)

    if args.command == "encrypt":
        shift = args.shift % 26
        result = encrypt(args.text, shift)
        print(f"  plaintext:  {args.text}")
        print(f"  shift:      {shift}")
        print(f"  ciphertext: {result}")
        print()

    elif args.command == "decrypt":
        shift = args.shift % 26
        result = decrypt(args.text, shift)
        print(f"  ciphertext: {args.text}")
        print(f"  shift:      {shift}")
        print(f"  plaintext:  {result}")
        print()

    elif args.command == "bruteforce":
        print(f"  input: {args.text}")
        brute_force(args.text)

    elif args.command == "analyse":
        print(f"  input: {args.text}")
        print_freq(args.text)


if __name__ == "__main__":
    main()
