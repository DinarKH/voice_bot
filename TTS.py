import requests

# based on https://github.com/art1415926535/yandex_speech
class TTS:
    TTS_URL = "https://tts.voicetech.yandex.net/generate"

    def __init__(self, key, lang="ru-RU",speaker="oksana",audio_format="mp3"):

        self.__params = {
            "speaker": speaker,
            "format": audio_format,
            "key": key,
            "lang": lang,
        }
        self._data = None

    def generate(self, text):
        """Try to get the generated file.

        Args:
            text: The text that you want to generate.
        """
        self.__params['text']=text
        self._data = requests.get(self.TTS_URL, params=self.__params,
                                  stream=False).iter_content()

    def save(self, path="Speech/Speech.mp3"):

        if self._data is None:
            raise Exception("There's nothing to save")

        with open(path, "ab") as f:
            for d in self._data:
                f.write(d)

