# from googletrans import Translator
import json
import requests


# use youdao translate API instead of googletrans
def translate(trans, src_lan, dest_lan):
    # translator = Translator(service_urls=['translate.google.cn'])
    # text = translator.translate(trans, src=src_lan, dest=dest_lan).text
    # return text
    language = src_lan + '2' + dest_lan
    text = requests.get('http://fanyi.youdao.com/translate?&doctype=json&type={}&i={}'.format(language, trans))
    return json.dumps(text.json()['translateResult'][0][0]['tgt'], ensure_ascii=False)
