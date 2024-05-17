print('PROGRAM INVENTORY MANAGEMENT')

print('----------------')
print('Menu')
print('----------------')

print('1. Input Data' )
print('2. Menampilkan Data' )

class Item:
    def __init__ (self, nama, kategori, harga):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
    
class Cart:
    def __init__ (self):
        self.capacity = 5
        self.list_item = []

    def addItem(self, item):
        self.list_item.append(item)
        


# input = []

def input_perintah(input):
    
    
    while input != exit:
        if input == 1:
            print(data[1])
            return