store = [
    ['Sabun', 5000, 'test'],
    ['Shampo', 5000, 'test'],
    ['Sabun', 5000, 'test'],
]

clear = False
def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row
    return -1

while(clear == False):
    print('============== STORE ==============')
    print('Menu')
    print('1. Daftar Produk')
    print('2. Detail Produk')
    print('3. Tambah Produk')
    print('4. Edit Produk')
    print('5. Hapus Produk')
    answer = input('Masukkan menu ')

    if (answer == '1' or answer == 1):
        print ("{:<8}".format('Nama Produk'))
        for i in range(len(store)):
            for j in range(1):
                print ("{:<8}".format(store[i][0]))
    elif(answer == '2' or answer == 2):
        namaproduk = input('Masukkan Nama Produk ')
        produks = find(store, namaproduk)
        if (produks < 0):
            print('Nama Produk Tidak Ada')
        else:    
            print ("{:<8} {:<15} {:<10}".format('Nama', 'Harga', 'Detail'))
            print ("{:<8} {:<15} {:<10}".format(store[produks][0], store[produks][1], store[produks][2]))
    elif(answer == '3' or answer == 3):
        namaproduk = input('Masukkan Nama Produk Baru ')
        produks = find(store, namaproduk)
        if(produks < 0):
            hargaproduk = input('Masukkan Harga Produk Baru ')
            detailproduk = input('Masukkan Detail Produk Baru ')
            newproduk = [namaproduk, hargaproduk, detailproduk]
            store.append(newproduk)
            print('Produk Berhasil Ditambahkan')
        else:
              print('Nama Produk sama ')
        
            
    elif(answer == '4' or answer == 4):
        userinput = input('Masukkan Nama Produk ')
        produks = find(store, userinput)
        if(produks < 0):
            print('Nama Produk Tidak Ada ')
        else:
            hargaproduk = input('Masukkan Harga Produk Baru ')
            detailproduk = input('Masukkan Detail Produk Baru ')
            store[produks][1] = hargaproduk
            store[produks][2] = detailproduk
            print('Produk Berhasil Diupdate')
    elif(answer == 5 or answer == '5'):
        userinput = input('Masukkan Nama Produk ')
        produks = find(store, userinput)
        if(produks < 0):
            print('Nama Produk Tidak Ada ')
        else:
            store.pop(produks)
            print('Produk Berhasil Dihapus')
    elif(answer == 6 or answer == '6'):
        clear = True
    
    

