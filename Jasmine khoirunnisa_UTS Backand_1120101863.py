azarine = ["intense acne", "cwhit series", "easy white series", "herbal essential"]
scarlett = ["paket acne", "paket brightly", "body lotion", "body scrub"]
msglow = ["paket acne", "paket ultimate", "paket luminous", "paket whitening"]
skincare = "y"

print(20*"-")
print("BEAUTY MINE")

while skincare == "y":
    print(20*"=")
    print("List skincare")
    print(20*"=")
    print("1.| azarine")
    print("2.| scarlett")
    print("3.| msglow")
    print(20*"=")
    l_skincare = int(input("Pilih brand skincare: "))
    if l_skincare == 1:
        print(azarine[0])
        print(azarine[1])
        print(azarine[2])
        print(azarine[3])
    elif l_skincare == 2:
        print(scarlett[0])
        print(scarlett[1])
        print(scarlett[2])
        print(scarlett[3])
    elif l_skincare == 3:
        print(msglow[0])
        print(msglow[1])
        print(msglow[2])
        print(msglow[3])
    else:
        print("paket kosong")

    print(20*"=")
    pilihan = (input("Silahkan pilih nama paket skincare yang anda inginkan: "))
    paket = int(input("Berapa paket: "))
    print(20*"=")
    print("paket skincare yang anda pilih: ")
    print(20*"=")
    print(f"{pilihan} | {paket}")
    skincare = input("mau pilih lagi? : (Y/N) ")
    if skincare == "Y" or skincare == "y":
        continue
    else:
        print(20*"=")
        print("Terimakasih")