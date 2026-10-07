"""
One-Time Pad (OTP) with TRNG
----------------------------
Menu:
  1 -> Encrypt : input plaintext, TRNG auto-generates key, output ciphertext + key
  2 -> Decrypt : input ciphertext + key, output plaintext
"""

import os
import base64


# ---------- TRNG (true random bytes from hardware/OS entropy) ----------
def trng(n: int) -> bytes:
    return os.urandom(n)


# ---------- Encrypt ----------
def encrypt(plaintext: str):
    msg = plaintext.encode("utf-8")
    key = trng(len(msg))                        # auto TRNG key, same length
    cipher = bytes(m ^ k for m, k in zip(msg, key))
    return key, cipher


# ---------- Decrypt ----------
def decrypt(cipher: bytes, key: bytes) -> str:
    if len(cipher) != len(key):
        raise ValueError("Key length must equal ciphertext length.")
    msg = bytes(c ^ k for c, k in zip(cipher, key))
    return msg.decode("utf-8")


# ---------- Main menu ----------
def main():
    print("=" * 55)
    print("   ONE-TIME PAD (TRNG) — ENCRYPT / DECRYPT")
    print("=" * 55)

    while True:
        print("\nChoose an option:")
        print("  1) Encrypt")
        print("  2) Decrypt")
        print("  3) Quit")

        choice = input("Enter 1 / 2 / 3: ").strip()

        # -------- ENCRYPT --------
        if choice == "1":
            plaintext = input("\nEnter plaintext: ")
            key, cipher = encrypt(plaintext)

            print("\n--- ENCRYPTION OUTPUT ---")
            print("Key (hex)       :", key.hex())
            print("Key (base64)    :", base64.b64encode(key).decode())
            print("Ciphertext (hex):", cipher.hex())
            print("Ciphertext(b64) :", base64.b64encode(cipher).decode())
            print("\n⚠ Save BOTH the key and ciphertext. Never reuse the key.")

        # -------- DECRYPT --------
        elif choice == "2":
            print("\nPaste ciphertext (hex or base64):")
            c_in = input("Ciphertext: ").strip()

            print("Paste key (hex or base64):")
            k_in = input("Key       : ").strip()

            try:
                # Try hex first, then base64
                def parse(s):
                    try:
                        return bytes.fromhex(s)
                    except ValueError:
                        return base64.b64decode(s)

                cipher = parse(c_in)
                key = parse(k_in)

                plaintext = decrypt(cipher, key)
                print("\n--- DECRYPTION OUTPUT ---")
                print("Plaintext:", plaintext)

            except Exception as e:
                print("\n❌ Decryption failed:", e)

        # -------- QUIT --------
        elif choice == "3":
            print("\nBye.")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
