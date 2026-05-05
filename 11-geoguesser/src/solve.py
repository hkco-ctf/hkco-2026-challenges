
def main():
    enc = input("Enter the encrypted flag: ")
    # The input is from digits 1-8, make them 0-7
    enc = ''.join(str(int(c) - 1) for c in enc)
    # Convert the base-8 string to an integer
    num = int(enc, 8)
    # Convert the integer to bytes
    flag_bytes = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    # Decode the bytes to get the flag
    flag = 'hkco2026{' + flag_bytes.decode() + '}'
    print(flag)

if __name__ == "__main__":
    main()