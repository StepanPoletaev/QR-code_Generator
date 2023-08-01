import qrcode


def get_qrcode(url: str, name: str) -> str:
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR-code was created. Open the {name}.png'


def main():
    get_qrcode(url='', name='')


if __name__ == '__main__':
    main()


