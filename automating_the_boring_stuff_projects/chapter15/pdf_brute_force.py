import PyPDF2

def encrypt_file():
    with open('meetingminutes.pdf', 'wb') as pdfFileObj:
        pdfWriter = PyPDF2.PdfFileWriter()

        pdfWriter.encrypt('rockyou')
        pdfWriter.write(pdfFileObj)

    with open('meetingminutes.pdf', 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        if pdfReader.isEncrypted:
            print('PDF File is encrypted.')

def brute_force():
    with open('meetingminutes.pdf', 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)

        with open('rockyou.txt', 'r') as password_file:
            passwords = password_file.readlines(1000)

            for password in passwords:
                pdfReader.decrypt(password)
                print('Trying ' + password)
                if not pdfReader.isEncrypted:
                    print('PDF File is decrypted.')
                    print(pdfReader.getPage(0))
                    break

def main():
    encrypt_file()
    brute_force()

if __name__ == '__main__':
    main()
