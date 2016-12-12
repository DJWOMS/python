# -*- coding: utf-8 -*-
from grab import Grab
from pyquery import PyQuery
u_url = input("Адрес ")
g = Grab(log_file='out.html')
g.go(u_url)
#Название товара
print (g.doc.select('//h1[@class="product-name"]').text())

#Цена товара
price = g.doc.select('//span[@class="price-value"]').text()
price = float(price)
roz = price - (price * 0.08)
opt = price - (price * 0.11)
print(roz)
print(opt)

#Характеристики товара
print (g.doc.select('//p[@class="features__note"]').text())

print("<table style=\"border:black solid 1px\">\n")
for i, td in enumerate(g.doc.select('//ul[@class="features__list"]//dl')):
    for i2, td2 in enumerate(g.doc.select('//ul[@class="features__list"]//dd')):
        if i == i2:
            tt2 = '<tr><td style=\"border:black solid 1px\"> %s </td>\n<td style=\"border:black solid 1px\"> %s </td></tr>\n' % (td.text().lstrip(':'), td2.text().lstrip(':'))
            print(tt2)

#Парсинг изображений
i = 0
for elem in g.doc.select('//img[@class="js-gallery-small-img"]/@data-src'): 
    img_url = '%s' % elem.text().lstrip('.')
    g.go(img_url)
    g.response.save('%d.jpg' % i)
    print ('foto-%d' % i)
    #print(img_url)
    i += 1

