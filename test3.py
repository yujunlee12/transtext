from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont("malgun","malgun.ttf"))


import os
import a
import spacy
f2=open("test.txt","w")
f=open("lesson1.txt","r")
nlp = spacy.load("en_core_web_sm")
f1=f.readlines()
p = []

for i in range(len(f1)):
    if f1[i] == "\n":
        continue
    t=a.translate(f1[i],"en","ko")
    doc=nlp(t)
    p.append(doc)
for j in range(len(p)):
    f2.write(str(f1[j]))
    f2.write(str(t[j])+"\n")

c=canvas.Canvas("font.pdf")
c.setFont("malgun",24)
c.drawString(10,50,"hellow")
c.drawString(10,50,"world")
c.drawString(300,50,"1")
r=0
for y in range(len(f1)):
    
    y=y+2
    c.showPage()
    c.drawString(300,50,str(y))
    c.setFont("malgun",16)
    c.drawString(50,600,str(f1[r]))
    c.drawString(50,500,str(p[r]))
    y=0
    r=r+1
c.save()
os.startfile("font.pdf")

