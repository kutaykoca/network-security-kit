import functions as func

func.secim()

islem = input("\nİşlem Seçiniz: ")

while True:

    if islem == "1":
        func.getMac()
        break

    elif islem == "2":
        func.infoinfo()
        break

    elif islem == "3":
        func.nmapscan()
        break


    elif islem == "4":
        func.searchsploit()
        break


    elif islem == "5":
        func.niktoscan()
        break

    elif islem == "6":
        func.exiftool()
        break

    elif islem == "7":
        func.wordpress()
        break

    elif islem == "8":
        func.wordlist()
        break

    else:
        print("Hatalı Seçim Yaptınız. Tekar Deneyiniz.")