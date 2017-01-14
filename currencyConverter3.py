#Script-type currency converter
#Author: JAIME ENRIQUEZ

# / ___|   _ _ __ _ __ ___ _ __   ___ _   _
#| |  | | | | '__| '__/ _ \ '_ \ / __| | | |
#| |__| |_| | |  | | |  __/ | | | (__| |_| |
# \____\__,_|_|  |_|  \___|_| |_|\___|\__, |
#                                     |___/
# ____                          _
#/ ___|___  _ ____   _____ _ __| |_ ___ _ __
#| |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
#| |__| (_) | | | \ V /  __/ |  | ||  __/ |
 #\____\___/|_| |_|\_/ \___|_|   \__\___|_|

#FIGLET BANNER

import sys
from datetime import datetime #imports required modules
import requests

from bs4 import BeautifulSoup



url="http://www.x-rates.com/table/?from=EUR&amount=1"
r=requests.get(url)             #scraps url from x-rates.com
soup=BeautifulSoup(r.text,"lxml")


countries=[]           #creates the lists which will be needed for convert_to() function
rates=[]
inicials=[]


for table_rows in soup.select(".tablesorter tr"):        #loops table rows from table belonging to the tablesorter class
    table_cells=table_rows.findAll("td")            #finds all td in table rows
    if len(table_cells)>=2:
        country=table_cells[0].text
        countries.append(country)   #appends country to country list
        to_euros=table_cells[1].find("a").text.strip()
        rates.append(float(to_euros))   #appends value of (currency value)/euro from country previously appended to country list, to rates list

def createInicials():
    if len(inicials)!=0:
        for inicial in inicials:
            inicials.remove(inicial)
    else:
        pass
    for country in countries:
        output=''
        for upperCases in country.upper().split():  #creates inicials by looping over upper cases from the countries strings
            output +=upperCases[0]                  #and adding them together

        for countryy in inicials:       #if inicials are already taken, add * at the end
            if countryy==output:
                output= output +"*"
            else:
			    pass
        inicials.append(output)

def newCurrency(name,value):
    countries.append(name)
    rates.append(value)
    createInicials()

newCurrency("European U R", 1)     #add new currencies if wanted



currenciesToEuros={}        #create FUNCTION
countriesAndInicials={}

ilist1=range(0,len(countries))  #list which will be used to loop, and so create dicitonaries.
for i in ilist1:

    currenciesToEuros[inicials[i]]=rates[i]
    countriesAndInicials[inicials[i]]=countries[i]      #creates two dictionaries with inicials as keys and, rates and countries as values, repectively




def convert_to():  #MAIN FUNCTION
    amount=float(sys.argv[1])   #first argument entered: AMOUNT
    currency_from=sys.argv[2]   #what currency does the amount entered belonng to: CURRENCY BELONGING
    currency_to=sys.argv[3]  #second argument entered: WHAT CURRENCY TO GET
    per_euro1=currenciesToEuros[currency_from] #amount of first entered currency per euro
    per_euro2=currenciesToEuros[currency_to] #amount of second entered currency per euro

    interm_amount_euros=amount / per_euro1 #creation of an intermediate variable so that it is easier to calculate the final amount
    final_amount=per_euro2 * interm_amount_euros #final amount

    return str(final_amount)    #returns final value


def showResult():
    print( sys.argv[1]+ " "+ sys.argv[2]+", "+countriesAndInicials[sys.argv[2]]+"s"+" = "+ convert_to() +" "+ sys.argv[3]+ ", "+ countriesAndInicials[sys.argv[3]]+"s")   #prints final value


def helpMenu():

    print("\n\nHELP MENU : \n\n Enter as FIRST parameter amount you want converted\n Enter as SECOND parameter what currency this amount is\n Enter as THIRD parameter what currency to convert")
    print("\n\nCall \"list\" as first parameter when you want a full list of currencie's rates")
    print("\n\nEXAMPLE CONVERT:     python currency_converter.py 200 UD BP")
    print("EXAMPLE LIST:     python currency_converter.py list")
    print("\nLIST OF CURRENCIES:")
    print("\n\nCURRENCY -- VALUE per EURO -- INICIALS TO USE\n(currencies in alphabetical order)\n\n%s\n\n" % (datetime.today()))
    ilist2=range(0,len(countries))  #creates list ranging from 0 to the length of ccountries list, to loop over their different components
    for i in ilist2:
        print (countries[i]+ " -- "+ str(rates[i])+ " -- "+ inicials[i])


def isOK():     #creates a function to check if all parameters are ok

    if type(sys.argv[1])==int or type(sys.argv[1])==float:
        return True
    elif sys.argv[2] in inicials and sys.argv[3] in inicials:
        return True
    elif sys.argv[1]=="h" or sys.argv[1]:
        pass

def isnotOK():      #creates a function to check if any of the parameters are not OK

    if type(sys.argv[1])!=int or type(sys.argv[1])!=float:
        return True
    elif sys.argv[2] not in inicials or sys.argv[3] not in inicials:
        return True



def situation():
    if len(sys.argv)<=1:
        print("\n\n")
        print(" / ___|   ")
        print("| |  | | | | '__| '__/ _ \ '_ \ / __| | | |")
        print("| |__| |_| | |  | | |  __/ | | | (__| |_| |")
        print(" \____\__,_|_|  |_|  \___|_| |_|\___|\__, |")
        print("                                     |___/ ")
        print("\n / ___|___  _ ____   _____ _ __| |_ ___ _ __ ")
        print("| |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|")
        print("| |__| (_) | | | \ V /  __/ |  | ||  __/ |   ")
        print(" \____\___/|_| |_|\_/ \___|_|   \__\___|_|   ")
        print("\n by Jaime Enriquez")
        print("\n[*]This is a currency converter which can exchange between more than 30 currrencies.")
        print("[*]It is written in python in a script-type of way.")
        print ("\n\n\n\"python currencyConverter.py h / help\" -----> HELP MENU\n\n")

    elif sys.argv[1]=="h" or sys.argv[1]=="help": #help menu appears when first parameter is h or help
	   return(helpMenu())

    elif sys.argv[1]=="list":
       print("\n")
       for inicial in inicials:
           print("1 EUR ----> %f %s" %(currenciesToEuros[inicial], inicial))

    elif sys.argv[1]=="get":
        if sys.argv[2] in inicials:
            print(str(datetime.today())+"\n")
            print("1 EUR ----> %f %s" %(currenciesToEuros[sys.argv[2]],sys.argv[2]))
            inverse_rate=1/currenciesToEuros[sys.argv[2]]
            print("1 %s ----> %f EUR" %(sys.argv[2], inverse_rate))

        else:
            print("Missing second parameter: CURRENCY")

    else:       #calls isOk()
        if isOK():
            return(showResult())

        elif isnotOK():
            print("\n\nINCORRECT NOTATION\n\n")
            print("FULL LIST OF CURRENCIES:\n\n")
            print("On %s:\n" % (datetime.today()))
            for countries in countriesAndInicials.keys():
                print("%s -- %s" %(countries, countriesAndInicials[countries]))
        else:
            pass

if __name__=="__main__":
    situation()



'''elif sys.argv[1]=="addcurrency":

    newCurrencyName=raw_input("Name (add at leats one upper-case):  ")
    newCurrencyRates=raw_input("1 EUR =  ")

    f = open("currency_converter3.py", "r")
    contents = f.readlines()
    f.close()

    stringNewCurrency="newCurrency(\""+newCurrencyName+"\","+newCurrencyRates+")"

    contents.insert(66, stringNewCurrency)

    f = open("currency_converter3.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()''' #en prueba
