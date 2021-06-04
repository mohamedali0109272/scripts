

head -n 1000   مصر\ -\ الجزء\ الأول.txt |awk -F,  '{var7 = $7 ;var4 = $4;print "BEGIN:VCARD\nVERSION:2.1\nN:;"$7 ";;;\nFN:" $7 "\nTEL;CELL:"  $4 "\nEND:VCARD" } '
