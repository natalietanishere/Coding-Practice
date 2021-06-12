import datetime
x=(datetime.datetime.now)
winter=["December","January","February"]
#print("Winter:"+', '.join(winter))
spring=["March","April","May"]
#print("Spring:"+', '.join(spring))
summer=["June","July","August"]
#print("Summer:" +', '.join(summer))
fall=["September","October","November"]
#print("Fall:"+', '.join(fall))
x=input("What is your favorite month?")
if x in winter:
 print("Months you might like:"+','.join(winter) )
elif x in fall:
 print("Months you might like:"+','.join(fall) )
elif x in spring:
  print("Months you might like:"+','.join(spring))
elif x in summer:
   print("Months you might like:"+','.join(summer))
else:
  print("not a month")
