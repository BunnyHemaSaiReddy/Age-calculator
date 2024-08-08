import streamlit as s
import time
import calendar
#import cv2
#img=cv2.imread(r"C:\Users\user\OneDrive\Pictures\Screenshots\FB_IMG_1693589854767.png")
#cv2.show("frame",img)
def agecalculator():
    s.title("Age Calculator")
    t=time.localtime()
    s.header("Enter your date of birth :")
    day=s.slider("choose the date",1,31,value=t.tm_mday)
    month=s.slider("chose the month",1,12,value=t.tm_mon)
    year=s.number_input("Enter year :",t.tm_year-100,t.tm_year,value=t.tm_year)
    s.markdown("## Choice your format :")
    radio=s.radio("--",("present date","custum date"))
    if radio=="present date":
        p_day=str(t.tm_mday)+"-"+str(t.tm_mon)+"-"+str(t.tm_year)
    elif radio=="custum date":
        p_day=s.date_input("enter Custom date")
        p_day=str(p_day).split("-")
        p_day=str(p_day[2])+"-"+str(p_day[1])+"-"+str(p_day[0])
    if(s.button("Find the Age")):
        with s.spinner("wait"):
           time.sleep(5)
        s.error("Your Date of birth is : \t{} - {} - {} ".format(day,month,year))
        s.warning("Present date is: \t"+p_day)
        p_day=(p_day).split("-")
        x=month
        y1=day
        if x==1:
            z=365-y1
        if x==2:
            z=365-31-y1
        if x==3:
            z=365-31-28-y1
        if x==4:
            z=365-31*2-28-y1
        if x==5:
            z=365-31*2-28-30*1-y1
        if x==6:
            z=365-31*3-28-30*1-y1
        if x==7:
            z=365-31*3-28-30*2-y1
        if x==8:
            z=365-31*4-28-30*2-y1
        if x==9:
            z=365-31*5-28-30*2-y1
        if x==10:
            z=365-31*5-28-30*3-y1
        if x==11:
            z=365-31*6-28-30*3-y1
        if x==12:
            z=365-31*6-28-30*4-y1
        leap=calendar.leapdays(year,int(p_day[2]))
        td=z+365*(int(p_day[2])-year-1)+int(t.tm_yday)+leap-1
        t_yx=td%365
        s.error("Your age:    "+str(td//365)+"    years   "+str(t_yx//30)+"   months   "+str(t_yx%30)+"   days")
        s.info("no of days.          "+str(td))
        s.success('no of month.        '+str(td//12))
        s.warning('total years.           '+str(td//365))
        h=td*24-24+t.tm_hour
        s.error('no of hours.         '+str(h))
        s.success('no of minutes.     '+str(h*60+t.tm_min))
        s.info('no of seconds.     '+str(h*3600+t.tm_sec))
        s.balloons()
s.image(r"C:\Users\user\OneDrive\Pictures\Screenshots\FB_IMG_1693589854767.png")
button_css = """
    <style>
        .stButton {
            background-color: white; 
            color: blue; 
            border-radius: 5px; 
        }
    </style>
"""
s.markdown(button_css, unsafe_allow_html=True)
s.title("*****BUNNY*****")
agecalculator()




