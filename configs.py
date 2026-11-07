


scr_timeout = 10

messages = {
    "welcome": "Welcome to the price tracker bot.",
    "add_start": "Send the product link:",
    "add_name": "Send the product name:",
    "add_success": "Product added.",
    "track_start": "Fetching price...",
    "track_error": "Error fetching price.",
}


def get_message(key):
    return messages.get(key, "")


if __name__ == "__main__":
    print("Config OK.")
