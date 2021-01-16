#apertura file in sola lettura e in modalita' byte
#in questo modo i dati non verranno decodificati come stringhe 
#ma come sequenze di byte semplificando le operazioni successive
file1 = open('./powpow.mp4', mode = 'rb')

#header, firma iniziale del file PNG 
png_header = bytearray(b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
#footer, firma finale del file PNG
png_footer = bytearray(b"\x49\x45\x4E\x44\xAE\x42\x60\x82")

#legge il contenuto del file ritornando un apposito oggetto file
dat = file1.read()

container = bytearray(b'') 

#calcola offset header
inizio_file =  dat.find(png_header)
#calcola offset footer
fine_file = dat.find(png_footer) + 7

#estrae le sequenze di caratteri esadecimali 
#comprese tra l'header e il footer
while inizio_file <= fine_file: 
    container.append(dat[inizio_file])
    inizio_file+=1

#apre il file in scrittura e in modalita' byte
#creandone uno nuovo che contiene i dati estratti
with open("png_estratto.png", mode = 'wb') as file2:
    file2.write(container)
