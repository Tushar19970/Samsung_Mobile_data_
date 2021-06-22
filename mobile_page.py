import requests, json
from bs4 import BeautifulSoup
from pprint import pprint

def scrape_multiple_pages():
    user = int(input("How many pages you want to scrape :"))
    for i in range (1, int(user)+1):
        url = "https://www.flipkart.com/search?q=samsung+and+nokia+smart+phone+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page"+str(i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        details = soup.find_all("div", class_="fMghEO")
        Mobile_name = soup.find_all("div", class_="_4rR01T")
        Mobile_price = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        Name, Price = [], []
        for name in Mobile_name:
            Name.append(name.text)
        for price in Mobile_price:
            Price.append(price.text)

        dict2={}
        mobile_details = []
        for item, price in zip (details, Price) :
            dict2["Price"] = price
            ram_rom_expondable = item.find_all("li", class_="rgWa7D")
            dict2['ram_rom_expondable'] = ram_rom_expondable[0].text
            dict2["Size"] = ram_rom_expondable[1].text
            dict2["Camera_details"] = ram_rom_expondable[2].text
            dict2["Battery_details"] = ram_rom_expondable[3].text
            dict2["Processer"] = ram_rom_expondable[4].text
            mobile_details.append(dict2.copy())
            
        dict3 = {}
        for j, k in zip (Name, mobile_details):
            dict3[j] = k
            

            json_files = open("mobiles1_data.json", "a")
            json.dump(dict3, json_files, indent = 4 )
            json_files.close()

            pprint(dict3)

scrape_multiple_pages()

