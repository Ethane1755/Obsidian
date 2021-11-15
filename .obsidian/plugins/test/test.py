from googletrans import Translator

translator = Translator(service_urls=['translate.googleapis.com'])
print(translator.translate('測試').text)