import argparse


def decrypt_message(message):
    words = message.split()
    first_letters = list(word[0] for word in words)
    decrypted_message = "".join(first_letters)
    return decrypted_message


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="display decrypted message", type=str)
    args = parser.parse_args()
    print(decrypt_message(args.message))
