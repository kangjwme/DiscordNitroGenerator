import random, string
import webbrowser
import time
import requests
import os


deleteopt = input("刪除原有NitroCodes.txt？1=要 2=不要：")
if deleteopt == "1":
   if os.path.exists("NitroCodes.txt"):
      os.remove("NitroCodes.txt")
      print("刪除完畢")

num=input('產生多少Nitro禮物連結(暴力破解次數): ')
print("事先聲明，這些都是亂數產生，個人覺得機率很低！如果都不可用請不要怪程式！")
time.sleep(2)
txtwriter=open("NitroCodes.txt","w", encoding='utf-8')

print("暴力破解亂打牆中，等我一下")
      
for n in range(int(num)):
   #尾數亂數生成
   possiblecode = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   #連結組合
   txtwriter.write('https://discord.gift/')
   txtwriter.write(possiblecode)
   txtwriter.write("\n")

txtwriter.close()


#驗證連結可用性
with open("NitroCodes.txt") as txtwriter:
    for line in txtwriter:
        
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(r.status_code," 可用 | {} ".format(line.strip("\n")))
            canuse=open("NitroCanUseCodes.txt","w", encoding='utf-8')
            canuse.write('https://discord.gift/')
            canuse.write(possiblecode)
            canuse.write("\n")
            canuse.close()
        elif r.status_code == 429:
            print(r.status_code," 請求過多，將於600秒後重試"))
            time.sleep(600)
        else:
        	print(r.status_code," 不可用 | {} ".format(line.strip("\n")))
        	time.sleep(30)
            
   
        	
input("點擊Enter退出程式")
