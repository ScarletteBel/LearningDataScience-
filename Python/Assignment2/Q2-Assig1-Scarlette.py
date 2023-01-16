#Scarlette Bello Barron     0860234
#Q2

#secretMessage is the message as input for discover the hidden message...
secretMessage = "dfP, Prned:Hicbti;veadnd pred,scriHH;ptGiVEda teaan ajg?nal:: ytiscs"

#For discovering the hidden frase, it was deviden in words and also, a few words were devided in parts (w#p#)...
w1p1 = secretMessage[5:10]
w1p1_1 = w1p1.replace("n","")
w1p2 = secretMessage[12:16] + secretMessage[16] + secretMessage[18:20]
w1p2_1 = w1p2.replace("b","")
word1 = w1p1_1 + w1p2_1

word2 = secretMessage[20] + secretMessage[22:24]

w3p3 = secretMessage[37:43]
w3p3 = w3p3.replace("G","")
word3 = secretMessage[25:28] + secretMessage[30:34] + w3p3.lower()

w4p1 = secretMessage[44:49:2]
word4 = secretMessage[43] + w4p1

word5 = secretMessage[52] + secretMessage[56:59] + secretMessage[62:65] + secretMessage[66:68+1]

discoveredMessage = word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5

print(discoveredMessage)















