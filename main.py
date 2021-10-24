"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 24 Oktober 2021, 07:24:02 WIB
    Magnitudo: 4.6
    Kedalaman: 10 km
    Lokasi: 2.74 LS - 122.20 BT
    Pusat Gempa: Pusat gempa berada di laut 10 Km Timur laut Kab. Morowali
    Dirasaan: Dirasakan (Skala MMI): III-IV Bahodopi
    """
    hasil = dict()
    hasil['tanggal'] = '24 Oktober 2021'
    hasil['waktu'] = '07:24:02 WIB'
    hasil['magnitudo'] = 4.0
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 2.74, 'bt': 122.20}
    hasil['pusat'] = 'Pusat gempa berada di laut 10 Km Timur laut Kab. Morowali'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III-IV Bahodopi'

    return hasil


# def: artinya definisi
# pass: artinya dilewatkan dulu
def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__': #ini adalah jika ini main, maka akan bisa dijalankan hanya lewat Terminal
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)
