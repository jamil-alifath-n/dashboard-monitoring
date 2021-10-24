import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 24 Oktober 2021, 07:24:02 WIB
    Magnitudo: 4.6
    Kedalaman: 10 km
    Lokasi: 2.74 LS - 122.20 BT
    Pusat Gempa: Pusat gempa berada di laut 10 Km Timur laut Kab. Morowali
    Dirasaan: Dirasakan (Skala MMI): III-IV Bahodopi
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil

    else:
        return None

# def: artinya definisi
# pass: artinya dilewatkan dulu
def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menampilkan data gempat terkini")
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Dirasakan: {result['dirasakan']}")
