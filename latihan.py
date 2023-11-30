pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    Prabowo-Gibran Coffe
    List Menu Minuman Kopi 
 
    ==============================
    A. ES Kopi Susu : Rp 21.000
    B. ES Kopi Coklat : Rp 18.000
    C. ES Kopi Hitam : Rp 15.000
    D. Sosis  : Rp 17.000
    ==============================
    """)
    pesan=str(input("masukkan menu pilihan anda ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    nomermeja=(input("masukan omer meja"))
    if pesan == "A":
        listnama= "ES Kopi Susu"
        harga=(21000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "B":
        listnama= "ES Kopi Coklat"
        harga = (18000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "C":
        listnama= "ES Kopi Hitam"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "D":
        listnama= "Sosis"
        harga=int(17000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("Ananda Coffe")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")