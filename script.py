import json
import requests
from datetime import datetime
import mysql.connector
import time
while True:
    try:
        f = requests.get('http://dataservice.accuweather.com/currentconditions/v1/330088?apikey=4N1tv8aMvQOyCSuF6GN24PL8bpkmeKQC&details=true')
        response = f.json()
        LODT = response[0]['LocalObservationDateTime']
        WT = response[0]['WeatherText']
        Temp = response[0]['Temperature']['Metric']['Value']
        RFT = response[0]['RealFeelTemperature']['Metric']['Value']
        RFTS = response[0]['RealFeelTemperatureShade']['Metric']['Value']
        RH = response[0]['RelativeHumidity']
        IRH = response[0]['IndoorRelativeHumidity']
        DP = response[0]['DewPoint']['Metric']['Value']
        WDD = response[0]['Wind']['Direction']['Degrees']
        WDL = response[0]['Wind']['Direction']['Localized']
        WS = response[0]['Wind']['Speed']['Metric']['Value']
        WG = response[0]['WindGust']['Speed']['Metric']['Value']
        UV = response[0]['UVIndexText']
        Vis = response[0]['Visibility']['Metric']['Value']
        OTV = response[0]['ObstructionsToVisibility']
        CC = response[0]['CloudCover']
        Ceil = response[0]['Ceiling']['Metric']['Value']
        Pr = response[0]['Pressure']['Metric']['Value']
        PT = response[0]['PressureTendency']['LocalizedText']
        PTemp = response[0]['Past24HourTemperatureDeparture']['Metric']['Value']
        AT = response[0]['ApparentTemperature']['Metric']['Value']
        WCT = response[0]['WindChillTemperature']['Metric']['Value']
        WBT = response[0]['WetBulbTemperature']['Metric']['Value']
        p1hr = response[0]['Precip1hr']['Metric']['Value']
        now = datetime.now()
        insert = "INSERT INTO accuweather (DateTime,EpochTime,WeatherText,Temperature,RealFeelTemperature,RealFeelTemperatureShade,RelativeHumidity,IndoorRelativeHumidity,DewPoint,Wind_angle,Wind_direction,Wind_speed,Wind_Gust,UVIndex,Visibility, ObstructionsVisibility,Cloudcover,Ceiling,Pressure, Pressure_Tendency, Past24HourTemperatureDeparture, Apparent_temp, WindChill_Temp, WetBulb_Temp, Precip1hr) VALUES ('"+ str(now) + "','" + LODT + "','" + WT + "'," + str(Temp) + "," + str(RFT) + "," + str(RFTS) + "," + str(RH) + "," + str(IRH) + "," + str(DP) + "," + str(WDD) + ",'" + WDL + "'," + str(WS) + "," + str(WG) + ",'" + UV + "'," + str(Vis) + ",'" + OTV + "'," + str(CC) + "," + str(Ceil) + "," + str(Pr) + ",'" + PT + "'," + str(PTemp) + "," + str(AT) + "," + str(WCT) + "," + str(WBT) + "," + str(p1hr) +  ");"
        #print (insert)
        mydb = mysql.connector.connect(host="www.db4free.net",user="testertester193",
                                       passwd="Tester@1234",auth_plugin='mysql_native_password',
                                       database='accuweather')
        print(mydb)
        
        cursor = mydb.cursor()
        #cursor.execute("use AccuWeather")
        cursor.execute(insert)
        mydb.commit()
        mydb.close()
        print ("Process Successful")
        time.sleep(1800)
        
    except:
        print ("Error")
        time.sleep(100)
