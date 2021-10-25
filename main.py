"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""

import gempaterkini

if __name__ == '__main__': #ini adalah jika ini main, maka akan bisa dijalankan hanya lewat Terminal
    print(f'Deskripsi package {gempaterkini.descriptions}')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
