import appuifw, telephone, e32, random, messaging, key_codes,globalui,sysinfo,graphics,codecs,thread
from time import ctime
from graphics import *
import os, string, codecs, inbox
from appuifw import *
from graphics import *
app_lock = e32.Ao_lock()
appuifw.app.screen='full'
# defining the exit handler
def quit():
    app_lock.signal()
    appuifw.app.exit_key_handler=quit
 
 
 
#define image resolution
img=graphics.Image.new(sysinfo.display_pixels())
img.rectangle(((30,sysinfo.display_pixels()[1]/2-20),(sysinfo.display_pixels()[0]-20,sysinfo.display_pixels()

 
[1]/2+20)), outline=(0,0,0))
def hr(rect):canvas.blit(img)
canvas=appuifw.Canvas(redraw_callback=hr)
appuifw.app.body=canvas
 
p=0
img=Image.open("c:\\Data\\X-SMS\\5.jpg")
 
#Increment the progress bar by 10% every second.
for i in range(5):
   img.rectangle(((p,sysinfo.display_pixels()[1]/2-20),(p+(sysinfo.display_pixels()[0]-
 
40)/10,sysinfo.display_pixels()[1]/2+20)), fill=0)
   canvas=appuifw.Canvas(redraw_callback=hr)
   p+=(sysinfo.display_pixels()[0]-40)/10
   e32.ao_sleep(1)
 
app_lock = e32.Ao_lock()

app_lock = e32.Ao_lock()
appuifw.app.screen='full'
img=Image.new((240,320))
img=Image.open("c:\\Data\\X-SMS\\1.jpg")

def quit():
    global running
    running=0
    appuifw.app.set_exit()


def handle_redraw(rect):
    canvas.blit(img)

running=1

canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
appuifw.app.body=canvas

e32.ao_sleep(3)

appuifw.query(u"Siraj's X-SMS v1.5 is developed by ~Siraj~ [Symbian Freak]", "query")
def draw():
    app_lock = e32.Ao_lock()
    appuifw.app.screen='full'
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")

    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas

img.clear()
draw()

dymzdir=u"e:\\Siraj\\"

try:
    if not os.path.exists(dymzdir):  
        os.makedirs(dymzdir)
    else:
        pass
except:
    appuifw.note(u"Couldn't create the directory!", "error")
Backdir=u"e:\\Back\\"

try:
    if not os.path.exists(Backdir):  
        os.makedirs(Backdir)
    else:
        pass
except:
    appuifw.note(u"Couldn't create the directory!", "error")


def texty():
    app_lock = e32.Ao_lock()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")

    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
       
    appuifw.note(u"Please wait...Backups are being created!", "info")

    f = codecs.open('E:/Siraj/SMS-backup.txt', 'w', 'utf8')
    box = inbox.Inbox()
   
    msg = box.sms_messages()

    for i in msg:
       f.write('From: ' +box.address(i))
       f.write('\n')
       f.write('Time: ' +ctime(box.time(i))) 
       f.write('\n')       
       f.write('Message: ' +box.content(i))
       f.write('\n')
       f.write('\n')
       f.write('* * * * * *')
       f.write('\n')
       f.write('\n')
       f.write('\n')
    f.close()
    appuifw.note(u"Backups have  been  created successfully!", "info")

    print ""
    img.clear()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")

    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    e32.ao_sleep(3)
    img.clear()
    draw()
def htmlydymz():
    dymzdir=u"e:\\Siraj\\"

    try:
        if not os.path.exists(dymzdir):  
            os.makedirs(dymzdir)
        else:
            pass
    except:
        appuifw.note(u"Couldn't create the directory!", "error")

    app_lock = e32.Ao_lock()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")
    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    appuifw.note(u"Please wait...Backups are being created!", "info")
    f = codecs.open('E:/Siraj/SMS-backup.html', 'w', 'utf8')
    f.write('<p align="center">')
    f.write('<title>DyMZ</title>')
    f.write('<body bgcolor="black" link="lime" text="white" vlink="purple">')
    f.write('\n')
    f.write('<h2><p align="center"><font color="red"><b><u>SMS backup</u></b></font><br></p></h2>')
    f.write('\n')
    f.write('<br>')
    f.write('\n')
    f.write('<br>')
    f.write('\n')

    box = inbox.Inbox()
    msg = box.sms_messages()

    for i in msg:
       f.write('<font color="red"><b><u>FROM: </u></b></font>')
       f.write(box.address(i) +'<br>')
       f.write('\n')
       f.write('<font color="red">Time</font>') 
       f.write('\n')       
       f.write(ctime(box.time(i)) +'<br>') 
       f.write('\n')       
       f.write('<font color="red"><b><u>MESSAGE: </u></b></font>')
       f.write(box.content(i) +'<br>')
       f.write('\n')
       f.write('<br>')
       f.write('$ $ $ $ $ $   <br>')
       f.write('\n')
       f.write('<br>')
    f.write('<br>')
    f.write('\n')
    f.write('<font color="yellow">Brought to you by: @Siraj@</font><br>')
    f.write('\n')
    f.write('<br>')
    f.write('\n')
    f.write('</p></body></html>')
    f.close()
    appuifw.note(u"Backups have  been  created successfully!", "info")
    img.clear()
    app_lock = e32.Ao_lock()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")
    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    e32.ao_sleep(3)
    img.clear()
    draw()
def docy():
    app_lock = e32.Ao_lock()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")

    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    appuifw.note(u"Please wait...Backups are being created!", "info")
    f = codecs.open('e:\\Siraj\SMS-backup.doc', 'w', 'utf8')
    box = inbox.Inbox()
    msg = box.sms_messages()

    for i in msg:
       f.write('From: ' +box.address(i))
       f.write('\n')
       f.write('Time:  ' +ctime(box.time(i))) 
       f.write('\n')
       f.write('Message: ' +box.content(i))
       f.write('\n')
       f.write('\n')
       f.write('! ! ! ! ! !')
       f.write('\n')
       f.write('\n')
       f.write('\n')
    f.close()
    appuifw.note(u"Backups have  been  created successfully!", "info")
    print ""
    img.clear()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")

    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    e32.ao_sleep(3)
    img.clear()

def show():
    appuifw.note(u"Create an HTML backup first!","info")
    tempfile = "e:\\Siraj\SMS-backup.html"
    lock=e32.Ao_lock()
    content_handler = appuifw.Content_handler(lock.signal)
    content_handler.open(tempfile)
    lock.wait()
def pdfy():
    app_lock = e32.Ao_lock()
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\1.jpg")

    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    appuifw.note(u"Testing on progress will be in next version!:-)", "info")

def show1():
  
    appuifw.note(u"If Backups have  been  created successfully before  it will appear now if not create html backup!", "info")
    tempfile = "e:\\Siraj\SMS-backup.html"
    lock=e32.Ao_lock()
    content_handler = appuifw.Content_handler(lock.signal)
    content_handler.open(tempfile)
    lock.wait()

def back():
 
   folder = "E:\\Siraj\\" 
   files = os.listdir(folder) 
    
   
   target = 'E:\\Back\\'
 
   count = len(files) 
   for i in range(count):
 
    t_file = folder + "\\" + files[i]
    
    e32.file_copy(target, t_file)        
   
   appuifw.note(u"Backup complete!")

def dymz():
    appuifw.app.screen='full'
    img=Image.new((240,320))
    img=Image.open("c:\\Data\\X-SMS\\3.jpg")

    img.line((00,5,640,5),0xff0000)
    img.text((25,70), u'To check for updates, visit...',0xff0000)
    img.text((05,85), u'http://www.sirajsoft.com',0xff0000)
    img.line((00,7,640,7),0xff0000)
    img.text((45,20), u'SIRAJ X-SMS',0xff0000)
    img.line((00,34,640,34),0xff0000)
    img.line((00,36,640,36),0xff0000)
    img.text((65,30), u'v1.5',65280)
    img.text((00,160), u'Developed by:',0xff0000)
    img.text((05,178), u'Siraj',65280)
    img.text((10,198), u'www.sirajsoft.com',65280)
    globalui.global_msg_query(u"New version have  Restore And Backup sms options too. Till then have fun with presently functional features \n Thanx for keeping patience.", u"Help")
    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    e32.ao_sleep(10)
    img.clear()
    draw()
def help():
    appuifw.app.screen='full'
    img=Image.open("c:\\Data\\X-SMS\\2.jpg")
    img.line((00,5,640,5),0xff0000)
    img.text((25,220), u'To Donate, visit...',0xff0000)
    img.text((05,250), u'http://www.sirajsoft.com',0xff0000)
   
    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    e32.ao_sleep(5)
    img.clear()
    draw()

def dymzz():
    appuifw.app.screen='full'
    img=Image.open("c:\\Data\\X-SMS\\4.jpg")
    globalui.global_msg_query(u"Great thanks to the Symbian-Freak and his creator Teo aka Apoc and the forum mass makers like Vinumsv ,Wook,Avisek,Lifenexus,Asterolykos,Aloycasmir,Darkzul,Desperados and all Sf friends and posters.Sorry if i miss any.:-).Visit www.SirajSoft.com", u"Help")

    img.text((030,30), u'This app is developed by...',0xff0000)
    img.text((70,55), u'Siraj',0xff0000)
    def quit():
        global running
        running=0
        appuifw.app.set_exit()


    def handle_redraw(rect):
        canvas.blit(img)

    running=1

    canvas=appuifw.Canvas(event_callback=None, redraw_callback=handle_redraw)
    appuifw.app.body=canvas
    e32.ao_sleep(5)
    img.clear()
    draw()
def helpin():
    globalui.global_msg_query(u"How to use:-\nThis program is to create back up of your smses in your inbox to the format which you select and this supports the formats like doc,txt,html,pdf\nIMPORTANT:\n \n Always before creating backup of the smses  backup the old files using *backup old files* option on menu.", u"Help")
#Restoring starts here

def exit():
    appuifw.app.set_exit()
appuifw.app.menu = [(u"Create",((u"Txt backup", texty), (u"HTML backup", htmlydymz), (u"Doc backup", docy), (u"pdf backup", pdfy))), (u"ShowSMS",show1),  (u"Backup old files", back), (u"About", ((u"Donate", help), (u"Developer", dymzz), (u"Update", dymz))), (u"Help", helpin), (u"Exit", exit)]

def exit_key_handler():
    app_lock.signal()
 
app_lock = e32.Ao_lock()

appuifw.app.exit_key_handler = exit_key_handler
app_lock.wait()