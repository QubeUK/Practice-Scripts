import qrcode


def main():
    url, filename = get_inputs()
    gen_qr_code(url, filename)


def get_inputs():
    url = input("Enter full URL: https://").strip()
    url = f"https://{url}"
    filename = input("Enter filename to save QR code: ").strip()
    return url, filename


def gen_qr_code(link: str, file: str):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{file}.png")
    print(f"{file}.png has been created with a link to {link}")


if __name__ == "__main__":
    main()
