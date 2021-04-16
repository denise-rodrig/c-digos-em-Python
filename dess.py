valor=float(input('valor:'))
desc=int(input('desconto:'))
calc=valor*desc/100
novo=valor-calc

print('o valor {:.2f} tem descomto  de {:.2f} reais '.format(valor,calc))
print('novo valor é {}'.format(novo))
