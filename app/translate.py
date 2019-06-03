from googletrans import Translator


def translate(trans, src_lan, dest_lan):
    translator = Translator(service_urls=['translate.google.cn'])
    text = translator.translate(trans, src=src_lan, dest=dest_lan).text
    return text
