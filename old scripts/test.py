# x = str('string') # set variable name, type, and value
# for i in range(3): # scan multiple times to show the address stays the same per execution
#     print(f'memory address: {id(x)}') # print scanned memory location address
# print(f'type: {type(x)}')
# print(f'length: {len(x)}')
# # memory address is same each scan,
# # but different each program execution

import googletrans

translator = googletrans.Translator()
detected = translator.detect('King shi')
print(detected)
lang = detected.lang
for i, l in enumerate(lang):
    lang[i] = str(l).lower()
    print(l)
print(lang)
# translation = translator.translate("测试")
# print(translation.extra_data)