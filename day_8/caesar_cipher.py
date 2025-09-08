"""
Interactive Caesar cipher tool that can encode and decode text.

- Prompts user to choose Encode, Decode, or Exit
- Accepts a shift value (integer). Positive shifts move forward in the alphabet
  while decoding applies the inverse shift automatically.
- Preserves letter case and leaves non-letters unchanged.
"""


def caesar(text: str, shift: int) -> str:
    """Return text shifted by `shift` using the Caesar cipher.

    Letters preserve case; non-letters are not changed.
    Shift wraps within A-Z/a-z.
    """
    result_chars = []
    normalized_shift = shift % 26

    for ch in text:
        if "A" <= ch <= "Z":
            base = ord("A")
            offset = ord(ch) - base
            new_ch = chr(base + (offset + normalized_shift) % 26)
            result_chars.append(new_ch)
        elif "a" <= ch <= "z":
            base = ord("a")
            offset = ord(ch) - base
            new_ch = chr(base + (offset + normalized_shift) % 26)
            result_chars.append(new_ch)
        else:
            result_chars.append(ch)

    return "".join(result_chars)


def prompt_int(prompt: str) -> int:
    """Prompt the user until they enter a valid integer; returns the integer."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer (e.g., 3 or -5).")


def run_cli() -> None:
    print("Caesar Cipher - Encode/Decode")
    print("--------------------------------")

    while True:
        print("\nChoose an option:")
        print("  [E] Encode")
        print("  [D] Decode")
        print("  [X] Exit")
        choice = input("> ").strip().lower()

        if choice == "x":
            print("Goodbye!")
            break

        if choice not in {"e", "d"}:
            print("Invalid choice. Please enter E, D, or X.")
            continue

        text = input("Enter text: ")
        shift = prompt_int("Enter shift (integer, e.g., 3): ")

        # For decoding, invert the shift
        effective_shift = shift if choice == "e" else -shift
        transformed = caesar(text, effective_shift)

        action = "Encoded" if choice == "e" else "Decoded"
        print(f"{action} text: {transformed}")

        # After an encode operation, explicitly offer decode-or-exit as requested
        if choice == "e":
            follow = input(
                "\nWould you like to [D]ecode something else or [X] Exit? ").strip().lower()
            if follow == "x":
                print("Goodbye!")
                break
            elif follow == "d":
                # Fall through to a quick decode flow
                text = input("Enter text to decode: ")
                shift = prompt_int("Enter shift used to encode (integer): ")
                print(f"Decoded text: {caesar(text, -shift)}")
            # Otherwise, loop back to main menu


if __name__ == "__main__":
    run_cli()

#
