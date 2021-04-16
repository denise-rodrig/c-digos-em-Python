largura=float(input('largura'))
altura=float(input('altura'))
area=largura*altura
print('a parede {:.2f} x {:.2f} tem area {:.2f}m²'.format(largura,altura,area))
tinta=area/2
print('vc usara {} litros de tinta pra essa parede'.format(tinta))
