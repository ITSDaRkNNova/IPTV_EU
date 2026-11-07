import requests

# Список ваших посилань для перевірки
urls = ["http://example.com"]

for url in urls:
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ Працює: {url}")
        else:
            print(f"❌ Помилка {response.status_code}: {url}")
    except requests.RequestException:
        print(f"💀 Мертвий лінк: {url}")
      
