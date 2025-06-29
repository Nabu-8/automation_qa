import requests
import json

# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером
# “Curiosity” на Марсi. Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових
# запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно зробити
# використовуючи модуль requests

response = requests.get(url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
                        params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'})

if response.status_code == 200:
    data = response.json()
else:
    print("Error. Status code:", response.status_code)
    exit()
# print(json.dumps(data, indent=4))

my_photos = data.get('photos', [])

photos_list = []
for item in my_photos:
    url_to_download = item.get("img_src")
    photos_list.append(url_to_download)
# print(photos_list)

if not photos_list:
    print("There is no photo with those parameters.")
    exit()

for index, photo_url in enumerate(photos_list):
    image_response = requests.get(photo_url)
    filename = f'mars_photo{index + 1}.jpg'
    if image_response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(image_response.content)
    else:
        print(f'{photo_url} is not downloaded, Status code: {image_response.status_code}')