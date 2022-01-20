##IMPORTANT THIS IS A JOKE PROGRAM TO MESS WITH PEOPLE NOT AN ACTUAL THREAT TO ANY SYSTEM
## this is purely to be used for the entertainment purposes of messing with gullible people
import time
C = 1
per = 0
cent = 0
B=0.008
while True:
   
    if per < 45:
        time.sleep(B)
        print('EXTRACTING FILES',per,'%')
        per=per+1
        B = B +0.0001
    elif per < 101:
        B= B +0.00001
        time.sleep (B)
        print('EXTRACTING FILES',per,'%')
        per=per+1
    else:
        time.sleep(0.021)
        if cent < 45:
            time.sleep(0.023)
            print('UPLOADING...',cent,'GB(s) to the Dark Web')
            cent=cent+0.03451
        elif cent < 101:
            B= B +0.0023
            time.sleep(B)
            print('UPLOADING...',cent,'GB(s) to the Dark Web')
            cent = cent+0.000671
        else:
            print('UPLOADED TO THE DARK WEB')
            time.sleep(0.4)
            break
                
