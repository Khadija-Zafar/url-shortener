import string
import random

url_db = {}
def generate_short_code(length=6):
    """Generate a random short code for the URL."""
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if short_code not in url_db:
            break
    return short_code


def shorten_url(long_url):
    """Create a short URL for a given long URL."""
    if long_url in url_db.values():
        for code, url in url_db.items():
            if url == long_url:
                return f"http://short.url/{code}"

    short_code = generate_short_code()
    url_db[short_code] = long_url
    return f"http://short.url/{short_code}"


def retrieve_long_url(short_url):
    """Retrieve the original long URL from the short URL."""
    short_code = short_url.split("/")[-1]
    long_url = url_db.get(short_code, "Short URL not found!")
    return long_url


def main():
    while True:
        print("Select option:")
        print("1. Shorten a URL")
        print("2. Retrieve the original URL")

        choice = input("Enter your choice (or type 'exit' to quit): ")

        if choice == '1':
            long_url = input("Enter the URL to be shortened: ")
            short_url = shorten_url(long_url)
            print(f"Short URL: {short_url}\n")

        elif choice == '2':
            short_url = input("Enter the short URL to retrieve the original URL: ")
            long_url = retrieve_long_url(short_url)
            print(f"Original URL: {long_url}\n")

        elif choice.lower() == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter '1', '2', or 'exit'.")


if __name__ == "__main__":
    main()