# nasihatpersonal

Kendime her gün kısa nasihat gönderen küçük bir Telegram botu. MongoDB'deki
nasihat koleksiyonundan rastgele birini seçip Telegram'a yollar. GitHub Actions
ile zamanlanmış olarak çalışır.

## Nasıl çalışır

1. `main.py`, MongoDB'deki `telegram` veritabanının `advices-personal`
   koleksiyonundan `$sample` ile rastgele bir nasihat çeker.
2. Seçilen nasihatı Telegram bot API üzerinden kişisel sohbete gönderir.
3. GitHub Actions (`.github/workflows/actions.yml`) bunu Türkiye saatiyle
   10:00–21:00 arası her saat başı otomatik tetikler.

## Kurulum

```bash
pip install -r requirements.txt
```

Ardından bir `.env` dosyası oluştur:

```env
BOT_TOKEN=telegram_bot_token
CHAT_ID=hedef_chat_id
URI=mongodb_baglanti_adresi
```

## Çalıştırma

```bash
python main.py
```

## Ortam Değişkenleri

| Değişken    | Açıklama                                  |
|-------------|-------------------------------------------|
| `BOT_TOKEN` | Telegram bot token'ı (BotFather'dan)      |
| `CHAT_ID`   | Mesajın gideceği sohbet ID'si             |
| `URI`       | MongoDB bağlantı adresi                   |

> Otomatik çalışma için bu değerler GitHub deposunda **Settings → Secrets and
> variables → Actions** altında tanımlıdır.
