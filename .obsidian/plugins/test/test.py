import googletrans as gt
from googletrans.client import Translator
print(gt.LANGUAGES)
Translator.detect(text='hello')