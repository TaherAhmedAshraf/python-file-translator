from translate import Translator

lang = "ja"
translator = Translator(to_lang=lang)

try:
    with open('./file.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        open(f'translated-{lang}.txt', mode='w').write(translation)
except FileNotFoundError as e:
    print('check your file path')
    pass
