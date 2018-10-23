from easygui import*
import sys

while 1:
    msgbox("E-mall!")

    msg ="what do you wish to buy??"
    title = "Domains"
    choices = ["Electronics","Clothing", "Home Decor"]
    choice = choicebox(msg, title, choices)
    
    if choice=='Electronics':
     msg1="choose your category"
     title1="Electronics"
     choises1=["Computers","Mobiles","Home Appliences"]
     choice1= choicebox(msg1,title1,choises1)
     if choice1=='Computers':
      msg11="Choose your product"
      title11="Computers"
      choices11=["Lenovo-1500$","Dell-1650$","HP-1675$","Apple-2000$"]
      choice11=choicebox(msg11,title11,choices11)
     elif choice1=='Mobiles':
     msg11="Choose your product"
      title11="Mobiles"
      choices11=["Vivo-199$""Samsung-499$""Moto-350$""Apple-999$"]
      elif choice1=='Mobiles':
     msg11="Choose your product"
      title11="Home Appliances"
      choices11=["Oven-125$""TV-3499$""Washing Machine-300$"]
    elif choice=='Clothing':
     title3="Clothing"
     msg3="choose your category"
     choises3=["Shirts and Tops""Sweaters and Sweatshirts""Footwear""Ethinic Wear""Jeans and shorts""Gym Wear"]
     choice3=choicebox(msg3,title3,choises3)    
    elif choice=='Home Decor':
     msg4="choose your category"
     title4="Home Decor"
     choises4=["Beds""Dining tables""Curtains,Bedsheets and Pillow Covers""Wardrobes and cupboards""Sofa sets""Chairs""Lamps"]
     choice4=choicebox(msg4,title4,choises4)
     
    
     	
	 
     
