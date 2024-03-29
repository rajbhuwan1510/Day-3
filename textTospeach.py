#!/usr/bin/env python
# coding: utf-8

# In[4]:


from deep_translator import GoogleTranslator
def translate_text(text,lan):
    print(text)
    for i in lan:
        print(i)
        translateText=GoogleTranslator(source='auto',target=i).translate(text)
        print(translateText)

text=input()
lan=['en','german']
translate_text(text,lan)





from gtts import gTTS
import os
def texttospeach(text,language='hi'):
    tts=gTTS(text=text,lang=language,slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")
text="आप कैसे हैं"
texttospeach(text)




