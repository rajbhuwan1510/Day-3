#!/usr/bin/env python
# coding: utf-8

# In[4]:


class vehicle:
    def __init__(self,name,colour,kind,value):
        self.name1=name
        self.colour1=colour
        self.kind1=kind
        self.value=value
    def description(self):
        print(f'Vehicle Parent company={self.name1}')
    def engine(self):
        if self.value>60000:
            print("BS6")
        elif self.value>=10000 and self.value<40000:
            print("BS5")
        elif self.value<10000:
            print("BS4")
name=input()
colour=input()
kind=input()
value=input()
obj1=vehicle(name,colour,kind,value)
obj1.description()


# In[5]:


class vehicle:
    
    def __init__(self,name,kind,color,value):
        self.name1=name
        self.kind1=kind
        self.color1=color
        self.value1=value
        
    def description(self):
        print("name: ",self.name1)
        print("kind: ",self.kind1)
        print("color: ",self.color1)
        
    def engine(self):
        if self.value1> 60000:
            return 'BS6'
        elif self.value1>10000 and self.value1<40000:
            return 'BS5'
        elif self.value1<10000:
            return 'BS4'
        
    def vehicle_parent_company(self):
        comp=self.name1.split()[0]
        return comp


# In[6]:


obj1=vehicle("nam33 1","colour","kind",10000)
obj1.vehicle_parent_company()


# In[10]:


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


# In[1]:


print(j)


# In[1]:


from gtts import gTTS
import os
def texttospeach(text,language='hi'):
    tts=gTTS(text=text,lang=language,slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")
text="आप कैसे हैं"
texttospeach(text)


# In[ ]:


Homework:
Task:
Fetch COVID-19 Data for Indian States

Description:
Create a Python script to fetch the latest COVID-19 data for Indian states from the provided API URL: https://data.covid19india.org/v4/min/timeseries.min.json. This script print the Response of the json data.
        

