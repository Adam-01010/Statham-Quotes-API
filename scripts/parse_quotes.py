import requests
from bs4 import BeautifulSoup

# URL-адрес веб-сайта
url = 'https://citaty.info/selection/citaty-stethema'  # Замените на нужный URL

# Получаем страницу
response = requests.get(url)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Парсим HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все теги blockquote
    quotes = soup.find_all('blockquote')
    f = open('quotes.txt', 'w', encoding='utf-8')
    a = 0
    # Извлекаем текст из каждого тега blockquote
    for quote in quotes:
        if a == 10:
            break 
        a += 1
        print(quote.get_text(strip=True))
        f.write(quote.get_text(strip=True) + '\n')
    f.close()
else:
    print(f'Ошибка: {response.status_code}')
