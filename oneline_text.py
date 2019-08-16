text=""
for izirig in open("c:/tal/kabyle.txt",encoding='utf-8'):
     izirig=izirig.replace("\n"," ")
     text=text+" "+ izirig.strip()
#print(text)
h= open("c:/tal/original_text.txt","w+",encoding='utf-8')
h.write(text.strip())
h.close()