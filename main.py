import requests
import random

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'garticio=s%3A55dcac36-bbe7-452b-b578-2861e967eaad.hay4iytBBkoB0CbDI36tNYdOsZ7KLYiYAfXqG%2F70EOo; _gid=GA1.2.1549165846.1700834495; _pbjs_userid_consent_data=3524755945110770; _sharedid=0e241ab3-370e-41ec-b2b2-e60ab4d3d74a; _ga=GA1.1.589929221.1700834495; _ga_VR1WBQ9P5N=GS1.1.1700834494.1.1.1700835907.32.0.0',
    'Origin': 'https://gartic.io',
    'Referer': 'https://gartic.io/create',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# İstek sayısı
num_requests = 313313

# İstek yapacak fonksiyon
def send_post_request(url, data):
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error: {response.status_code}, {response.text}'

# Belirli bir URL'ye 10 farklı istek gönder
for _ in range(num_requests):
    # "players" için rastgele sayı oluştur
    random_numbers_250 = random.randint(1, 250)

    # "points" için 5 farklı rakam oluştur
    unique_digits = random.sample(range(10), 4)
    five_digit_number = ''.join(map(str, unique_digits))

    # İstek verilerini oluştur
    data = {
        "players": random_numbers_250,
        "points": int(five_digit_number),
        "language": 23,
        "subject": 7,
        "created": False
    }

    # İstek gönder ve yanıtı yazdır
    response = send_post_request('https://gartic.io/req/createRoom', data)
    print(response)
