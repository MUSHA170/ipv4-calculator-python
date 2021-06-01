import math

ip = input('Informe o ip(192.168.1.1) ===')

mascara = int(input('Informe a mascara (/25) ==='))

""" ip = '192.168.1.1'
mascara = int(24)"""


    #mascara "25"
# mascara para binario '1111111111111111111111111'
masc_bit = ''
for x in range(mascara):
    masc_bit = masc_bit + '1'

#add zeros '11111111111111111111111110000000'
dif = int(32 - mascara)
for x in range(dif):
    masc_bit = masc_bit + '0'

""" print('mascara =  /',mascara)
print('quant de ultimo bits 0 da mascara = ',dif)
print('mascar em bit = ',masc_bit)
print('tamanho mascara = ',len(masc_bit)) """

#dividindo em octetos
masc_bit_oct1 = masc_bit[0:8]#1111 1111
masc_bit_oct2 = masc_bit[8:16]#1111 1111
masc_bit_oct3 = masc_bit[16:24]#1111 1111
masc_bit_oct4 = masc_bit[24:32]#1000 0000

mas_dec1 = int(masc_bit_oct1, 2)
mas_dec2 = int(masc_bit_oct2, 2)
mas_dec3 = int(masc_bit_oct3, 2)
mas_dec4 = int(masc_bit_oct4, 2)


# lista = [mas_dec1,mas_dec2,mas_dec3,mas_dec4]   #[255, 255, 255, 128]
mascara_decimal = str(mas_dec1) + '.' + str(mas_dec2) + '.' + str(mas_dec3) + '.' +str(mas_dec4)
print("mascara ==",mascara_decimal) #255.255.255.0


    #ip host e octetos para binario
#separando o ip   
ip_separado = ip.split('.') #['192', '168', '1', '1']

#separando os octetos
octeto1 = int(ip_separado[0]) #192
octeto2 = int(ip_separado[1]) #168
octeto3 = int(ip_separado[2]) #1
octeto4 = int(ip_separado[3]) #1

#transformando em binario
octeto1_bit = int(bin(octeto1)[2:]) #11000000
octeto2_bit = bin(octeto2)[2:] #10101000
octeto3_bit = bin(octeto3)[2:] #1
octeto4_bit = bin(octeto4)[2:] #1


    #ip rede
rede_oct1 = octeto1 & mas_dec1
rede_oct2 = octeto2 & mas_dec2
rede_oct3 = octeto3 & mas_dec3
rede_oct4 = octeto4 & mas_dec4
print('ip rede ==',rede_oct1,rede_oct2,rede_oct3,rede_oct4, sep='.')

    #ip broadcast
broadcast = (2 ** dif)-1
ip_broadcast = str(rede_oct1) + '.' + str(rede_oct2) + '.' + str(rede_oct3) + '.' +str(broadcast)
print('ip broadcast == ',ip_broadcast)

#hosts
print('numero de hosts == ',broadcast -2)
ip_h_ultimo = str(rede_oct1) + '.' + str(rede_oct2) + '.' + str(rede_oct3) + '.' +str(broadcast - 1)
print('ultimo host == ',ip_h_ultimo)

ip_h_primeiro = str(rede_oct1) + '.' + str(rede_oct2) + '.' + str(rede_oct3) + '.' +str(rede_oct4 + 1)
print('primeiro host == ',ip_h_primeiro)
