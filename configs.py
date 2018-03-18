settings = dict(
    telegram_api_key="YOUR_API_KEY",
    mercury_api_key="YOUR_API_kEY",
    #api key for web parser
    #https://mercury.postlight.com/web-parser/
    yandex_api_key="YOUR_API_KEY",
    #documentation https://tech.yandex.ru/speechkit/jsapi/doc/dg/concepts/tts-docpage/
    #get key https://tech.yandex.ru/maps/keys/get/
    start_mess="""Вас приветствует бот Voice News преобразующий 
ссылки на сайт в звуковые дорожки
Для получения более подробной информации введите команду /help
                                    """,
    help_mess="""Для работы с ботом необхдимо ввести ссылку на нужную
вам статью.  Пример:  https://geektimes.ru/post/299139/
Бот был протестирован на сайтах geektime.ru, habrhabr.ru 
            """,
    err_mess="""Похоже текст по вашей ссылке не может быть получен
        попробуйте другой сайт"""
)