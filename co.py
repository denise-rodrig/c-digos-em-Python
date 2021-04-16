reais=float(input('quanto reais vc tem na carteira?'))
dolar=reais*5.12
euro=reais*6.20
libra=reais*6.83

print('com {} Rs vc tem {:.2f} em dolares'.format(reais,dolar))
print('com {} vc tem {:.2f} em euro'.format(reais,euro))
print('com {} vc tem {:.2f} em libra'.format(reais,libra))
