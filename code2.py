#Write this code in ur IDLE SHELL to display message 
import os 
os.chdir('')#Add ur directory name where u stored lcd.py
import lcd 
lcd.lcd_init()
#Ignore any red warnings
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("Raspberry pi", 2)#We use 2 here to center the word in the display 
lcd.lcd_string("")#Add any message u want LCD to display 
