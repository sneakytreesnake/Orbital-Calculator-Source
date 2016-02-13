from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font
import math
from math import log10, floor
import webbrowser
import re
import time
import os
import sys
import fileinput #Order the modules logicaly
class OrbitalCalculator():
    def __init__(self):
        self.t1 = time.time()
        def orbitcalc():
            if self.windowdict['root'] == False:
                self.windowdict['root'] = True
                if "Difficultymode = Hard" in open('orbitprefs.txt','r').read(): #Make this dissallow new printing is nothing has changed
                    if self.layerprevent == False:
                        self.shiprunbutton = Button(self.advancedframe,text = "Run Ship Animation", command=spacecraft_draw)
                        self.entershipmass = Button(self.advancedframe, text = "Optional - Confirm Mass (t)", command = shipmassset)
                        self.bodybutton = Button(self.advancedframe,text = "Confirm Body", command=planetbox)
                        self.animationstop = Button(self.advancedframe, text = "Stop Animation", command = stopanimation,bg = 'gray70', foreground = 'gray70',borderwidth=0, state = DISABLED,disabledforeground='gray70')
                        self.entershipmass.grid(column=2, row=20, columnspan = 2, sticky = W)
                        self.shiprunbutton.grid(row=19, column=1, columnspan = 2)
                        self.bodybutton.grid(row=15, column=3, columnspan = 1, sticky=W)
                        self.animationstop.grid(row = 19, column = 3)
                        self.LINELAB1 = Label(self.advancedframe, text="- - - - - - - - - - - - - - - - - Run Ship Animation - - - - - - - - - - - - - - - - -", font="arial",bg='gray70')
                        self.LINELAB1.grid(row=17, column=1, columnspan = 5)
                        self.LINELAB2 =  Label(self.advancedframe, text="- - - - - - - - - - - - - - - - - - - Body Selection - - - - - - - - - - - - - - - - - - -", font="arial",bg='gray70')
                        self.LINELAB2.grid(row=14, column=1, columnspan = 5)
                        self.LINELAB3 = Label(self.advancedframe, text="- - - - - - - - - - - - - - - - - - - Run Simulation - - - - - - - - - - - - - - - - - - -", font="arial",bg='gray70')
                        self.LINELAB3.grid(row=10, column=1, columnspan = 5)
                        self.speedSlide = Scale(self.advancedframe, from_=1, to=(50),length=165, orient = HORIZONTAL)
                        self.speedSlide.grid(row = 20, column =4 , columnspan = 2, sticky = W)
                        self.speedLab = Label(self.advancedframe, text = "Animation Speed", bg = 'gray70')
                        self.speedLab.grid(row = 19 , column=4, columnspan = 2)
                        self.shipmassBox = Entry(self.advancedframe, textvariable=self.shipmassentry,width= 12)
                        self.shipmassBox.grid(row=20, column=1,sticky = E)
                        self.planetcombobox = ttk.Combobox(self.advancedframe,state= 'readonly',width= 15)
                        self.planetcombobox['values'] = self.planetlist[0]
                        self.planetcombobox.set('Select Body')
                        
                        self.planetcombobox.grid(column=1, row=15, columnspan = 2, sticky = E)  
                        self.resetdv = Button(self.advancedframe, text = "Reset Total dV", command = resetdv)
                        self.resetdv.grid(row=13, column=4, columnspan = 2, sticky = W)
                        self.dvchangelab = Label(self.advancedframe, text =( "Delta_V=0"))
                        self.tdvchangelab = Label(self.advancedframe, text =( "Total_Delta_V=0"))
                        self.dvchangelab.grid(row = 13, column = 1, columnspan = 1, sticky = W)
                        self.tdvchangelab.grid(row = 13, column = 2, columnspan = 2, sticky = W)
                        self.layerprevent = True
                else:
                    try:
                        removelabel(self.shiprunbutton)
                        removelabel(self.entershipmass)
                        removelabel(self.bodybutton)
                        removelabel(self.animationstop)
                        removelabel(self.LINELAB1)
                        removelabel(self.LINELAB2)
                        removelabel(self.LINELAB3)
                        removelabel(self.speedSlide)
                        removelabel(self.speedLab)
                        removelabel(self.shipmassBox)
                        removelabel(self.planetcombobox)
                        removelabel(self.resetdv)
                        removelabel(self.dvchangelab)
                        removelabel(self.tdvchangelab)
                        removelabel(self.fMlab)
                        removelabel(self.fplanetradiuslab)
                        self.layerprevent = False
                    except:
                        pass
                    
                self.changeamount = (int(open('benchmarkprefs.txt','r').read()))
                try:
                    self.blurbwindow.destroy()
                except:
                    pass
                self.root = Toplevel()
                self.advancedframe.grid(row=1,column=1)
                self.startframe.grid_remove()
                try:
                    windowdictclose(self.oproot,'oproot')
                    windowdictclose(self.credroot,'credroot')
                except:
                    pass
                self.root.focus_set()
                if "Resolution = Auto" in open('orbitprefs.txt','r').read():
                    self.canvasx = self.root.winfo_screenwidth()/1.3
                    self.canvasy = self.root.winfo_screenheight()/1.3
                if "Fullscreen = True" in open('orbitprefs.txt','r').read():
                    self.canvasx= (int(open('resxprefs.txt','r').read()))
                    self.canvasy= (int(open('resyprefs.txt','r').read()))
                    self.root.overrideredirect(1)
                else:
                    try:
                        self.canvasx= (int(open('resxprefs.txt','r').read()))
                        self.canvasy= (int(open('resyprefs.txt','r').read()))
                    except:
                        pass
                if self.canvasx <= 960 or self.canvasy <= 560:
                    self.canvasx = 960
                    self.canvasy = 540
                self.groot.attributes("-topmost", True)
                self.groot.resizable(0,0)
                self.root.wm_title("Orbital Calculator v 1.09")
                self.groot.wm_title("Mission Control")
                self.root.configure(bg='gray70') # windoow bg
                self.groot.configure(bg='gray70')
                self.root.resizable(0,0)
                self.root.protocol('WM_DELETE_WINDOW',grootwindowclose)
                self.ovalheadway = 0
                self.w = Canvas(self.root, width = self.canvasx, height = self.canvasy,bg='white')
                self.w.pack()
                self.incline = 0
                self.dvchange = 0
                self.tdvchange = 0
                self.planetradius = 6370000
                self.atmospheresize = 100000
                self.G = 6.673*10**-11
                self.E = 0
                self.UA= 300000
                self.M = 5.972*10**24 #Intital start
                self.V = 8000 
                self.A=6678000 
                self.g = 9.8
                self.loopvalue = 0
                self.loopcurrent = 0
                self.looptime = int(1500/self.changeamount)
                self.ArialBVel = tkinter.font.Font(family='Arial',size=11, weight='bold')
                self.ArialBorb = tkinter.font.Font(family='Arial',size=17, weight='bold')
                self.ArialBg = tkinter.font.Font(family='Arial',size=8, weight='bold')
                self.ArialBi = tkinter.font.Font(family='Arial',size=8, weight='bold')
                self.ArialBAlt = tkinter.font.Font(family='Arial',size=11, weight='bold')
                self.shipmass = 0
                self.notification=""
                self.miniplanet = 25
                self.first = 1
                self.spacecraftx = self.ovalheadway
                self.phase = 1
                self.reset = 1
                self.repeat = 1
                self.stopall = 0
                self.shipdraw = 0
                self.shipdrawchange = 0
                self.smallban = self.w.create_image(-1000, -100,image=self.FcImage)
                self.smalltext = self.w.create_text(95,125)
                self.loopcurrent -= 1 #Here to make intial frame
                self.zoom = 1
                self.oldzoom = 1
                zoom()
                planetdetails()
                update_frame() #This calls back and redraws objects
        def stopanimation():
            self.repeat = 0
        def windowdictclose(windowvar,windowname):
            windowvar.destroy()
            self.windowdict[windowname] = False
        def notification(text,level):
            self.w.create_text(self.canvasx/2, self.canvasy - level, text=text, font = self.ArialBg) #Yes I know it doubles up
        def loopchangeposition():
            if self.B >= self.planetradius:
                self.changedict['Ichange'] = -2 * self.incline
                self.changedict['Vchange'] = (self.U * (2/self.B - 1/self.L))**0.5- self.V
                self.changedict['Achange'] = self.B - self.A
                self.loopvalue = 1
                update_frame()
            else:
                notification("Cannot warp inside body.",170)
        def simpleloopchange(enta,entb,var,change,valt):
            resetchangedict()
            if change == 'Ichange':
                short = -1* enta.get()
            elif change != 'Vchange':
                short = abs(enta.get() * 10** entb.get())
            else:
                if valt == True:
                    short = (self.U * (2/(self.planetradius + self.UA)- 1/((self.planetradius + self.UA + (enta.get()* 10** entb.get()))/2)))**0.5
                else:
                    short = abs(enta.get())
            if change == 'Achange':
                if short <= self.A:
                    notification("Cannot have an altitude below body surface.",130)

                    short = self.planetradius
            elif change == 'Vchange':
                if short > self.eV:
                    short = math.trunc(self.eV)
                    notification("Escape velocity exceeded, setting velocity to highest possible orbital velocity.",150)
                else:
                    if valt == False:
                        if short == 0:
                            short = 1
                            notification("Setting velocity to nearest value of 1." ,150)
            userchange = short-var
            changing = (userchange/self.changeamount)
            self.changedict[change] = changing
            self.loopvalue =  userchange/changing
            if change == 'Vchange':
                self.dvchange = userchange
                self.tdvchange = self.dvchange + self.tdvchange
                
            elif change == 'Ichange':
                self.dvchange = ((2*self.V**2 )*(1- math.cos (userchange*( 0.0175))))**0.5
                self.tdvchange = self.dvchange + self.tdvchange
            else:
                if userchange != 0:
                    self.dvchange = 0
                    self.tdvchange = 0
        def shipmassset():
            self.w.delete(self.smallban)
            self.w.delete(self.smalltext)
            self.shipmass =  abs(self.shipmassentry.get())
            self.Fc = (self.shipmass * self.shipg) *1000 # in N
            if self.Fc != 0:
                self.smallban = self.w.create_image(90, 84,image=self.FcImage)
                self.smalltext = self.w.create_text(57,107, text =( "Fc=", round(self.Fc/1000, 1),"kN"), font = self.ArialBg)
        def reset():
            self.UA= 300000
            self.planetradius = 6370000
            self.M = 5.972*10**24
            self.V = 800
            self.A= 6670000
            self.incline = 0
            self.loopcurrent = 100
            update_frame()
        def updatedvchange():
            try:
                self.dvchangelab['text'] =("Delta_V=" , abs(round(self.dvchange,1)))
                self.tdvchangelab['text'] =("Total_Delta_V=",abs(round(self.tdvchange,1)))
            except:
                pass
        def looprun():
            updatedvchange()
            self.resetbutton.configure(bg = 'crimson',foreground = 'snow',borderwidth=2,state = NORMAL)
            self.loopcurrent = 0
            configurebuttons('disabled')
            self.resetbutton.configure (state = NORMAL)
            self.waitnes = Label(self.advancedframe, text =("Calculating..."), bg = 'gray70')
            self.waitnes.grid(row = 12, column = 1, columnspan = 2)
            if self.windowdict['proot'] == True:
                self.waitmes = Label(self.proot, text =("Calculating..."), bg = 'gray70')
                self.waitmes.grid(row = 6, column = 1, columnspan = 3)
            update_frame()
        def planetbox():
            planetdetails()
            self.changedict['Mchange'] =  (((self.planetlist[1][self.planetcombobox.current()]) - self.M)/self.changeamount)
            self.changedict['Pchange'] =  ((self.planetlist[2][self.planetcombobox.current()] - self.planetradius)/self.changeamount)
            self.changedict['Vchange'] =  ((((self.G * self.planetlist[1][self.planetcombobox.current()] )/(self.UA + self.planetlist[2][self.planetcombobox.current()]))**0.5 - self.V)/self.changeamount) 
            self.loopvalue = self.changeamount
            looprun()
        def grootwindowclose():
            self.groot.attributes("-topmost", False)
            try:
                windowdictclose(self.oroot,'oroot')
            except:
                pass
            try:
                windowdictclose(self.froot,'froot')
            except:
                pass                                     
            try:
                windowdictclose(self.proot,'proot')
            except:
                pass
            try:
                windowdictclose(self.croot,'croot')
            except:
                pass
            try:
                windowdictclose(self.mroot,'mroot')
            except:
                pass
            windowdictclose(self.root,'root')
            self.advancedframe.grid_remove()
            self.startframe.grid(row=1,column=1)

        def mrootwindow():
            if self.windowdict['mroot'] == False:
                self.mroot = Toplevel()
                self.windowdict['mroot'] = True

                self.mroot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.mroot,'mroot'))
                self.mroot.wm_title("Math")
                self.mroot.resizable(0,0)
                self.mroot.configure(bg='gray70')
                self.mathslideshow = 1
                mathslide()
                self.nextbutton = Button(self.mroot, text='Next',command = mathplusone)
                self.nextbutton.grid(row=5,column=1, sticky = E)
                self.backbutton = Button(self.mroot, text='Back',command = mathminusone)
                self.backbutton.grid(row=5,column=1, sticky = W)
                Label(self.mroot, text = "* Click on formulae to link to web source.", bg = 'gray70', font = (tkinter.font.Font(family='Arial',size=10))).grid(row = 6, column = 2, sticky = E)
                self.mathcombust = Button(self.mroot, text = "Close", command = lambda:windowdictclose(self.mroot,'mroot'))
                self.mathcombust.grid(row = 6, column = 1, sticky = W)
        def mathresetslide():
            if self.mathslideshow ==1:
                removelabel(self.Vbutton)
                removelabel(self.Vlab)
                removelabel(self.FGbutton)
                removelabel(self.FGlab)
                removelabel(self.Gbutton)
                removelabel(self.Glab)
            else:
                removelabel(self.Tbutton)
                removelabel(self.Tlab)
                removelabel(self.Ebutton)
                removelabel(self.Elab)
        def mathslide():
            if self.mathslideshow ==1: #Move most of this elsewhere
                self.Vbutton = Button(self.mroot, image=self.Vviva,command=lambda:webbrowser.open('https://en.wikipedia.org/wiki/Vis-viva_equation#Equation'))
                self.Vbutton.grid(row = 3, column = 2)
                self.Vlab = Label(self.mroot, text = "Vis - Viva Equation")
                self.Vlab.grid(row=3,column=1)
                self.Vbutton.configure(bg = 'gray90', foreground = 'gray70',borderwidth=5,disabledforeground='gray70')
                self.FGbutton = Button(self.mroot, image=self.FGrav,command=lambda:webbrowser.open('https://en.wikipedia.org/wiki/Gravitational_acceleration#For_point_masses'))
                self.FGbutton.grid(row = 2, column = 2)
                self.FGlab = Label(self.mroot, text = "Force of Gravity")
                self.FGlab.grid(row=2,column=1)
                self.FGbutton.configure(bg = 'gray90', foreground = 'gray70',borderwidth=5,disabledforeground='gray70')
                self.Gbutton = Button(self.mroot, image=self.Gconstant,command=lambda:webbrowser.open('https://en.wikipedia.org/wiki/Gravitational_constant#Laws_and_constants'))
                self.Gbutton.grid(row = 1, column = 2)
                self.Glab = Label(self.mroot, text = "Gravational Constant")
                self.Glab.grid(row=1,column=1)
                self.Gbutton.configure(bg = 'gray90', foreground = 'gray70',borderwidth=5,disabledforeground='gray70')
            elif self.mathslideshow ==2:
                self.Tbutton = Button(self.mroot, image=self.Trocket,command=lambda:webbrowser.open('https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation'))
                self.Tbutton.grid(row = 1, column = 2)
                self.Tlab = Label(self.mroot, text = "Tsiolkovsky Rocket Equation")
                self.Tlab.grid(row=1,column=1)
                self.Tbutton.configure(bg = 'gray90', foreground = 'gray70',borderwidth=5,disabledforeground='gray70')
                self.Ebutton = Button(self.mroot, image=self.Evelocity,command=lambda:webbrowser.open('https://en.wikipedia.org/wiki/Specific_impulse#Specific_impulse_as_a_speed_.28effective_exhaust_velocity.29'))
                self.Ebutton.grid(row = 2, column = 2)
                self.Elab = Label(self.mroot, text = "Effective Exhaust Velocity")
                self.Elab.grid(row=2,column=1)
                self.Ebutton.configure(bg = 'gray90', foreground = 'gray70',borderwidth=5,disabledforeground='gray70')
        def mathplusone():
            mathresetslide()
            if self.mathslideshow == 1:
                self.mathslideshow += 1
            mathslide()
        def mathminusone():
            mathresetslide()
            if self.mathslideshow == 2:
                self.mathslideshow -= 1
            mathslide()        
        def orootwindow():
            if self.windowdict['oroot'] == False:
                self.oroot = Toplevel()
                self.oroot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.oroot,'oroot'))
                self.windowdict['oroot'] = True
                self.oroot.wm_title("Glossary")
                self.oroot.configure(bg='gray70')
                self.oroot.resizable(0,0)
                #Label(self.oroot,text = " ",bg='gray70').grid(row = 1 , column = 3)
                #for level in range (32):
                #    Label(self.oroot,text = "|").grid(row = level , column = 2)
                Label(self.oroot,bg = 'gray70',justify = LEFT, text = "\nAltitude\t\t\t|\tDistance from the current position to bodies centre of mass.\nApoapsis\t\t|\tPoint of orbit that is furthest from the body. Lowest possible orbital speed is here.\nBody\t\t\t|\tThe planet/sun/moon a satellite is orbiting.\nBurnout\t\t\t|\tShutdown of engine due to lack of fuel.\nBurn Time\t\t|\tHow long an engine can run for before burnout.\nCentre of Mass\t\t|\tPoint where all mass is concentrated. Assumed Centre of Mass in centre of body for calculations.\nCentripetal Force\t\t|\tHow much force is acting on an object to keep it in the circle/ellipse that it is travelling in. Expressed as Fc.\nDelta V\t\t\t|\tChange in velocity.\nDry Mass\t\t|\tMass of a spacecraft when fuel is empty.\nEccentricity\t\t|\tA measure of how much a conic section deviates from being circular.\nEquatorial Plane\t\t|\tPlane parrellel with equatorial line.\nEscape Velocity\t\t|\tVelocity needed to escape orbit of the body being orbited.\nFocal Length\t\t|\tDistance from the centre of orbit to where the orbiting body is.\nFuel Mass\t\t|\tHow much mass of a spacecraft is fuel.\nGravational Acceleration\t|\tMeasurement of how much acceleration an object will inherit when no other forces are active.\nGravational Constant\t|\tUse to calculate the attractive forces of two bodies as proportionate to their own mass. Approximately 6.674x 10 ^ -11 Nm^2/kg^2.\nGravational Parameter\t|\tExpressed as μ and and shown in unit m^3/s. Product of Gravational Constant and mass of body.\nInclination\t\t|\tAngle of orbit measured from equatorial plane.\nManoeuvre\t\t|\tA movement.\nMass\t\t\t|\tHow much matter is in an object. The more matter the 'heavier' when combined with gravational acceleration.\nOrbit\t\t\t|\tPath of satellite around a body.\nPeriapsis\t\t\t|\tPoint of orbit that is closest to body. Highest possible orbital speed is here.\nPeriod\t\t\t|\tTime required for one circuit of orbit.\nPrograde\t\t|\tThe direction in the orbit is travelling.\nRadar Altitude\t\t|\tHow high something is from the surface beneath it. Eg. Altitude of spacecraft from sea level of body.\nRetrograde\t\t|\tThe direction opposite from the direction the orbit is travelling.\nSemi-Major Axis\t\t|\tHalf of the longest part of an orbit.\nSemi-Minor Axis\t\t|\tHalf of the shortest part of an orbit.\nSpecific Impulse\t\t|\tExpressed as Isp, and measured in seconds. It is a measurement of how effeciency of converting fuel into thrust.\nThrust\t\t\t|\tHow much force an engine can exhert.\nVelocity\t\t\t|\tHow fast an object is travelling in a particular direction.\nWet Mass\t\t|\tMass of a spacecraft when full of fuel.\n").grid(row = 1)
                self.glosscombust = Button(self.oroot, text = "Close", command = lambda:windowdictclose(self.oroot,'oroot'))
                self.glosscombust.grid(row = 2,sticky= W)
        def faqdictopen(var,name,layer):
            if self.faqdict[name] == True:
                var.grid_remove()
                self.faqdict[name] = False
            else:
                var.grid(row=layer,column=1,columnspan = 10, sticky = W)  #dictionary the layers
                self.faqdict[name] = True
        def frootwindow():
            if self.windowdict['froot'] == False:
                self.faqdict = {'radiusexp':False,'mathexp':False,'inclinedexp':False,'shipspeed':False,'oberth':False,'craftmass':False}
                self.froot = Toplevel()
                self.windowdict['froot'] = True
                self.froot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.froot,'froot'))
                self.froot.wm_title("Frequently Asked Questions")
                self.froot.configure(bg='gray70')
                self.froot.resizable(0,0)
                self.radiusexpframe = Frame(self.froot) #remove frames
                Label(self.radiusexpframe,justify = LEFT, text = "When there is a larger planet radius, there is a larger distance between the spacecraft and\nthe CoM of the planet. This results in a lower gravitational acceleration. As shown by the\nequation g = GM/r^2, when the value of r (distance to CoM) increases, the values of g will\nshrink. Since there is less gravitational acceleration, there is less centripetal force\npulling the spacecraft toward the planet. Thus, a lower velocity is needed to obtain orbit.\nIf the velocity stays the same but the radius of the planet increases, the orbit will appear\nto ‘grow’.").grid(row = 1 , column = 1,sticky = W)
                self.mathexpframe = Frame(self.froot)
                Label(self.mathexpframe,justify = LEFT ,text = "With a higher mass, the gravitational parameter increases (product of the Gravitational Constant\nand mass of the body). With a higher gravitational parameter, a higher gravitational acceleration is\npresent. To obtain an orbit with a higher gravitational acceleration, there is more centripetal\nforce ‘pulling’ the spacecraft toward the planet. To combat this, a higher orbital velocity\nis needed to obtain an orbit. If the velocity stays the same but the mass of the planet\nincreases, the orbit will appear to ‘shrink’.").grid(row=1,column=1,sticky=W)
                self.inclinedexpframe = Frame(self.froot)
                Label(self.inclinedexpframe,justify = LEFT, text = "Inclination changes are directly related to the current velocity. Making a velocity change\nat periapsis (where the spacecraft is at its fastest point) is much less efficient than at\napoapsis (where the spacecraft is at its slowest point) because it is travelling much faster.\nThe most efficient time for an inclination change is at apoapsis because that is when orbital\nvelocity is it its lowest. Sometimes it is even more efficient to perform a bi-elliptical\nmanoeuvre (making the orbit much bigger than it needs to be, so the orbital speed is even\nlower than otherwise. After which an inclination change is performed and then slowed back\ndown to the desired altitude)").grid(row = 1 , column = 1, sticky = W)        
                self.shipspeedframe = Frame(self.froot)
                Label(self.shipspeedframe,justify = LEFT, text = "A ship will gain a higher velocity when coming closer to a planet because it is getting\npulled by gravity. When a ball is thrown into the air, it is slowest when furthest from\nthe ground, and fastest when closest. The same thing happens in orbits. A spacecraft is\nslowest at its apoapsis (furthest point from planet) and fastest at its periapsis\n(closest point to planet). The spacecraft uses its kinetic energy to get ‘flung’ to the\nfurthest point in its orbit, and while doing so is losing speed as it is fighting against\ngravity in doing so. One it reaches its furthest point, gravity is now helping the craft\nspeed up and it accelerates faster and faster until it reaches periapsis. In this stage it\nis the longest period of acceleration and therefore it is fastest.").grid(row = 1 , column = 1, sticky = W)
                self.oberthframe = Frame(self.froot)
                Label(self.oberthframe,justify = LEFT, text = "This is an example of the Oberth effect. Hermann Oberth discovered that the most efficient time\nto perform a 'burn' is at orbital periapsis, where orbital speed is the highest. When burning,\nkinetic energy is increased as speed increases. However, since the equation for kinetic energy is \nEk = 0.5mv^2, velocity is squared. So going from 10m/s to 20m/s will produce significantly more energy than\ngoing from 0m/s to 10m/s. This is utilised when burning at periapsis. Since speed is the highest\npossible at this point, kinetic energy is increased to the square of the added velocity.").grid(row = 1 , column = 1, sticky = W)
                self.craftmassframe = Frame(self.froot)
                Label(self.craftmassframe,justify = LEFT, text = "The mass of the spacecraft is irrelevant when considering gravitational acceleration. In a perfect\nvacuum, a feather and a bowling ball will fall at the exact same rate, assuming no force other than\ngravitation is acting. In space, there is almost no atmosphere and so the only relevant force is\ngravity. Whether a spacecraft is 100 tons or 1 kg, the orbit of the two crafts will be exactly the\nsame assuming all other variables are the same.").grid(row = 1 , column = 1, sticky = W)
                self.OBERTH = Button(self.froot, text = "Why does the orbit get much larger when the ship is travelling faster?",  font = self.ArialBg,command = lambda:faqdictopen(self.oberthframe,'oberth',2))
                self.OBERTH.grid(row = 1 , column = 1, columnspan = 10, sticky = W)
                self.SHIPSPEED = Button(self.froot, text = "Why does the ship speed up when getting closer to the planet?",  font = self.ArialBg,command = lambda:faqdictopen(self.shipspeedframe,'shipspeed',11))
                self.SHIPSPEED.grid(row = 10 , column = 1, columnspan = 10, sticky = W)
                self.INCLINEDVEXP = Button(self.froot, text = "Why is the inclination dV change so much higher when travelling at faster speeds?",  font = self.ArialBg,command = lambda:faqdictopen(self.inclinedexpframe,'inclinedexp',21))
                self.INCLINEDVEXP.grid(row = 20 , column = 1, columnspan = 10, sticky = W)
                self.MASSEXP = Button(self.froot, text = "Why does the orbit shrink when the body has a higher mass?",  font = self.ArialBg,command = lambda:faqdictopen(self.mathexpframe,'mathexp',31))
                self.MASSEXP.grid(row = 30 , column = 1, columnspan = 10, sticky = W)
                self.RADIUSEXP = Button(self.froot, text = "Why does the orbit get bigger when the radius of body increases?",  font = self.ArialBg,command = lambda:faqdictopen(self.radiusexpframe,'radiusexp',41))
                self.RADIUSEXP.grid(row = 40 , column = 1, columnspan = 10, sticky = W)
                self.CRAFTMASSEXP = Button(self.froot, text = "How come when the spacecraft's mass changes the orbit doesn't change?",  font = self.ArialBg,command = lambda:faqdictopen(self.craftmassframe,'craftmass',51))
                self.CRAFTMASSEXP.grid(row = 50 , column = 1, columnspan = 10, sticky = W)
                self.faqcombust = Button(self.froot, text = "Close", command = lambda:windowdictclose(self.froot,'froot'))
                self.faqcombust.grid(row = 100, column = 1, columnspan = 3)
        def prootdisplay():
            self.sua['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.UA,1))),"m")
            self.sa['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.A,1))),"m")
            self.sm['text']=(round(self.M,1),"kg")
            self.sv['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.V,1))),"m/s")
            self.su['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.U,1))),"m^3/s")
            self.sb['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.B,1))),"m")
            self.sl['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.L,1))),"m")
            self.se['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.E,1))),"m")
            self.sh['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.H,1))),"m")
            self.sp['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.T,1))),"s")
            self.sd['text']=((round(self.Ec,1)))
            self.sev['text']=(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.eV,1))), "m/s")
            if self.A >= self.B:
                self.sbt['text']=("Periapsis")
                self.sat['text']=("Apoapsis")
            else:
                self.sbt['text']=("Apoapsis")
                self.sat['text']=("Periapsis")
        def prootwindow():
            if self.windowdict['proot'] == False:
                self.proot = Toplevel()
                self.windowdict['proot'] = True
                self.proot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.proot,'proot'))
                self.proot.wm_title("Orbital Characteristics")
                self.proot.resizable(0,0)
                self.proot.configure(bg='gray70')
                self.prootframe = Frame(self.proot, bg='gray70')
                self.prootframe.grid(row=2,column=1)
                self.sua =Label(self.prootframe) #Maybe put this in start
                self.sa =Label(self.prootframe)
                self.sm =Label(self.prootframe)
                self.sv =Label(self.prootframe)
                self.su =Label(self.prootframe)
                self.sb =Label(self.prootframe)
                self.sl =Label(self.prootframe)
                self.se =Label(self.prootframe)
                self.sh =Label(self.prootframe)
                self.sp =Label(self.prootframe)
                self.sd =Label(self.prootframe)
                self.sev =Label(self.prootframe)
                self.sbt =Label(self.prootframe)
                self.sat =Label(self.prootframe)
                self.suat =Label(self.prootframe, text="Radar Altitude")
                self.smt =Label(self.prootframe, text="Body Mass")
                self.svt =Label(self.prootframe, text="Spacecraft Velocity")
                self.sut =Label(self.prootframe, text="Gravational Parameter")
                self.slt =Label(self.prootframe, text="Semi-Major Axis")
                self.set =Label(self.prootframe, text="Focal Length")
                self.sht =Label(self.prootframe, text="Semi-Minor Axis")
                self.spt =Label(self.prootframe, text="Orbital Period")
                self.sdt =Label(self.prootframe, text="Eccentricity")
                self.sevt =Label(self.prootframe, text="Escape Velocity")
                self.sua.grid(row=2, column = 1, sticky=W)
                self.sa.grid(row=3, column = 1, sticky=W)
                self.sm.grid(row=6, column = 1, sticky=W)
                self.sv.grid(row=5, column = 1, sticky=W)
                self.su.grid(row=7, column = 1, sticky=W)
                self.sb.grid(row=4, column = 1, sticky=W)
                self.sl.grid(row=8, column = 1, sticky=W)
                self.se.grid(row=9, column = 1, sticky=W)
                self.sh.grid(row=10, column = 1, sticky=W)
                self.sp.grid(row=11, column = 1, sticky=W)
                self.sd.grid(row=12, column = 1, sticky=W)
                self.sev.grid(row=13, column = 1, sticky=W)
                self.suat.grid(row=2, column = 2, sticky=W)
                self.smt.grid(row=6, column = 2, sticky=W)
                self.svt.grid(row=5, column = 2, sticky=W)
                self.sut.grid(row=7, column = 2, sticky=W)
                self.sat.grid(row=3, column = 2, sticky=W)
                self.sbt.grid(row=4, column = 2, sticky=W)
                self.slt.grid(row=8, column = 2, sticky=W)
                self.set.grid(row=9, column = 2, sticky=W)
                self.sht.grid(row=10, column = 2, sticky=W)
                self.spt.grid(row=11, column = 2, sticky=W)
                self.sdt.grid(row=12, column = 2, sticky=W)
                self.sevt.grid(row=13, column = 2, sticky=W)
                prootdisplay()
                self.pcombust = Button(self.proot, text = "Close", command = lambda:windowdictclose(self.proot,'proot'))
                self.pcombust.grid(row = 20, column = 1, columnspan = 3)
        def crootwindow():
            if self.windowdict['croot'] == False:
                self.croot = Toplevel()
                self.windowdict['croot'] = True
                self.croot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.croot,'croot'))
                self.croot.wm_title("Calculator")
                self.croot.resizable(0,0)
                self.croot.configure(bg='gray70')
                self.dvbutton = Button(self.croot, text = "Calculate Delta V", command = dvCalculator)
                self.burnbutton = Button(self.croot, text = "Calculate Burn Time", command = burntimeCalculator)
                self.ispBox = Entry(self.croot, textvariable=self.ispentry)
                self.ispBox.grid(row=1, column=1)
                self.wetBox = Entry(self.croot, textvariable=self.wetmassentry)
                self.wetBox.grid(row=2, column=1)
                self.dryBox = Entry(self.croot, textvariable=self.drymassentry)
                self.dryBox.grid(row=3, column=1)
                self.dvbutton.grid(row = 2, column = 3)
                self.burnbutton.grid(row = 7, column = 3)
                Label(self.croot, text="\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", font="arial",bg='gray70').grid(row=4, column=1, columnspan = 5)
                self.shipispBox = Entry(self.croot, textvariable=self.shipispentry)
                self.shipispBox.grid(row=6, column=1)
                self.shipthrustBox = Entry(self.croot, textvariable=self.shipenginethrustentry)
                self.shipthrustBox.grid(row=7, column=1)
                self.shipfuelBox = Entry(self.croot, textvariable=self.shipfuelmassentry)
                self.shipfuelBox.grid(row=8, column=1)
                self.dvlab = Label(self.croot, text=("DeltaV=",0, "m/s"), bg='gray70')
                self.dvlab.grid(row=3, column = 3, columnspan = 5, sticky=W)
                self.btlab = Label(self.croot, text=("DeltaV=",0, "m/s"), bg='gray70')
                self.btlab.grid(row=8, column = 3, columnspan = 5, sticky=W)
                self.combust = Button(self.croot, text = "Close", command = lambda:windowdictclose(self.croot,'croot'))
                self.combust.grid(row = 9, column = 1)
                Label(self.croot,text = "Specific Impulse (s)").grid( row=1, column = 2, sticky=W)
                Label(self.croot,text = "Wet Mass (t)").grid( row=2, column = 2, sticky=W)
                Label(self.croot,text = "Dry Mass (t)").grid( row=3, column = 2, sticky=W)
                Label(self.croot,text = "Specific Impulse (s)").grid( row=6, column = 2, sticky=W)
                Label(self.croot,text = "Force of Engine (kN)").grid( row=7, column = 2, sticky=W)
                Label(self.croot,text = "Mass of Fuel (t)").grid( row=8, column = 2, sticky=W)
        def removelabel(labelname):
            labelname.grid_remove()
        def planetdetails():
            if "Difficultymode = Hard" in open('orbitprefs.txt','r').read():
                try:
                    removelabel(self.fMlab)
                    removelabel(self.fplanetradiuslab) #Change
                except:
                    pass
                self.fMlab =Label(self.advancedframe, text = ("Body_Mass=",self.planetlist[1][self.planetcombobox.current()],"kg"))
                self.fMlab.grid(column=4, row=15, columnspan = 2,sticky = W)
                self.fplanetradiuslab = Label(self.advancedframe, text = ("Body_Radius=",(re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (self.planetlist[2][self.planetcombobox.current()]))),"m"))
                self.fplanetradiuslab.grid(column=4, row=16, columnspan = 2,sticky = W)
                if self.windowdict['root'] == True:
                    self.groot.after(1000, planetdetails)
        def burntimeCalculator():
            self.enginethrust = self.shipenginethrustentry.get() #In kN
            self.engineisp = self.shipispentry.get() #in s
            self.shipfuelmass = self.shipfuelmassentry.get() #in tons
            self.fuelrate = (1/((9.81* self.engineisp) /  self.enginethrust))
            self.burntime = self.shipfuelmass/self.fuelrate
            self.btlab['text']=("Time=",round(self.burntime,1), "s")
        def dvCalculator():
            self.dv = round((self.ispentry.get() * 9.8 * math.log(self.wetmassentry.get()/self.drymassentry.get())), 1)
            self.dvlab['text']=("DeltaV=",round(self.dv,1), "m/s")
        def safelower():
            self.w.tag_lower(self.shipdraw)
            self.w.tag_lower(self.planet)
            self.w.tag_lower(self.arc1)
            self.w.tag_lower(self.arc2)
        def spacecraft_draw():
            try:
                if self.B >= self.planetradius:
                    configurebuttons('disabled')
                    self.w.delete(self.shipdraw) #Maybe make others like this, rpboably doesn't mateer
                    self.animationstop.configure(bg = 'crimson',foreground = 'snow',borderwidth=2,state = NORMAL)
                    if self.phase == 1 and self.spacecraftx >= self.canvasx - self.ovalheadway - self.shipdrawchange:
                        self.phase = 2
                    elif self.phase == 2 and self.spacecraftx <= self.ovalheadway + self.shipdrawchange:
                        self.phase = 1
                        self.reset = 1
                        if self.repeat != 1:
                            self.stopall = 1
                    if self.phase == 1:
                        if ((self.incline) >= 0 and (self.incline) <= 180):
                            self.rl = -1
                        else:
                            self.rl = 1
                        if (abs(self.incline) >= 90 and abs(self.incline) <= 180):
                            self.shipl = -1
                        else:
                            self.shipl = 1
                        self.spacecrafty2 = (self.shipl * 1)*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2 
                    elif self.phase == 2:
                        if self.reset == 1:
                            self.rl = self.rl * -1
                            self.shipl = self.shipl * -1
                            self.spacecraftx =  self.canvasx-self.ovalheadway
                            self.spacecrafty2 = self.canvasy/2
                            self.shipdraw = self.w.create_image(self.spacecraftx + 5, self.spacecrafty2,image=self.shipImage)
                            self.reset = 0
                        self.spacecrafty2 = (self.shipl * 1)*(((self.OvalH/2)**2)*(1-(((self.spacecraftx  - self.canvasx/2)**2)/(((self.canvasx-2*self.ovalheadway)/2)**2))))**0.5 + self.canvasy/2
                        self.w.delete(self.shipdraw)
                    self.shipxdis = abs(self.ovalheadway + self.UA/self.S + self.planetsize - self.spacecraftx)
                    self.shipydis = abs(self.spacecrafty2 - self.canvasy/2)
                    self.shipdis = ((self.shipxdis **2 + self.shipydis**2)**0.5)
                    self.shipR = self.shipdis * self.S
                    self.shipg = (self.U)/(self.shipR**2)
                    self.w.delete(self.smallban)
                    self.w.delete(self.smalltext)
                    self.Fc = (self.shipmass * self.shipg) *1000 # in N
                    if self.Fc != 0:
                        self.smallban = self.w.create_image(90, 84,image=self.FcImage)
                        self.smalltext = self.w.create_text(57,107, text =( "Fc=", round(self.Fc/1000, 1),"kN"), font = self.ArialBg)
                    self.shipV = ((self.U * (2/self.shipR - 1/self.L))**0.5)
                    self.shipVinit = self.shipV
                    self.sR = self.B
                    self.sL = (self.B + self.A)/2 #From planetsurface, remove self.planetradius to do from planet centre
                    self.sVshort = (self.U * (2/self.sR - 1/self.sL))**0.5
                    self.avgshipspeed = (self.V +self.sVshort)/2
                    self.shipdrawchange = (self.speedSlide.get()) * ((int((self.shipV / self.avgshipspeed)*10))/10 + 0.1) * (100 / self.changeamount)
                    if self.phase == 1:
                        self.spacecraftx += self.shipdrawchange
                    elif self.phase == 2:
                        self.spacecraftx -= self.shipdrawchange
                    hudupdate(self.shipV,self.shipR,self.shipg)
                    self.shipdraw = self.w.create_image((self.spacecraftx + 5), self.spacecrafty2,image=self.shipImage)
                    if self.B >= self.planetradius:
                        if self.rl == 1:
                            self.w.tag_lower(self.shipdraw)
                            if int(self.incline) == 0:
                                safelower()
                            elif ((self.incline) <= -90 and (self.incline) >= -180) or (((self.incline) >= 0 and (self.incline) <= 90)):
                                self.w.tag_lower(self.arc1)
                                self.w.tag_lower(self.planet)
                                self.w.tag_lower(self.arc2)
                            elif ((self.incline) <= 0 and (self.incline) >= -90) or (((self.incline) >= 90 and (self.incline) <= 180)):
                                self.w.tag_lower(self.arc2)
                                self.w.tag_lower(self.planet)
                                self.w.tag_lower(self.arc1)
                        elif self.rl == -1:
                            if int(self.incline) == 0:
                                safelower()
                            elif ((self.incline) <= -90 and (self.incline) >= -180) or (((self.incline) >= 0 and (self.incline) <= 90)):
                                self.w.tag_lower(self.arc1)
                                self.w.tag_lower(self.planet)
                                self.w.tag_lower(self.shipdraw)
                                self.w.tag_lower(self.arc2)
                            elif ((self.incline) <= 0 and (self.incline) >= -90) or (((self.incline) >= 90 and (self.incline) <= 180)):
                                self.w.tag_lower(self.arc2)
                                self.w.tag_lower(self.planet)
                                self.w.tag_lower(self.shipdraw)
                                self.w.tag_lower(self.arc1)
                    else:
                        safelower()
                        
                    self.w.tag_lower(self.athoval)
                    if self.stopall == 0:
                        self.root.after(self.looptime, spacecraft_draw)
                    elif self.stopall != 0:
                        shipinitial()            
                else:
                    notification("Collision Imminent.",190)
                    self.w.create_text(self.canvasx/2, self.canvasy - 17, text=self.notification, font = self.ArialBg) #Yes I know it doubles up #WHAT IS THIS
            except:
                shipinitial()
        def prefixcalc(var):
            for numlevel in range(12):
                ans = (var/1000)/(10**(numlevel-1))
                if ans <= 1000:
                    return (numlevel)
                
        def hudupdate(velvariable,altvariable,gravariable):
            try:
                self.w.delete(self.VELread)
                self.w.delete(self.ALTread)
                self.w.delete(self.gread)
            except:
                pass
            self.VELread = self.w.create_text(self.canvasx-79  ,50 , text=((''.join(["Velocity(",self.valuelist[prefixcalc(velvariable)],"m)="])), int(round(velvariable/(10**(int(math.log(velvariable)/math.log(10))-3)),0))), font=self.ArialBVel)
            self.ALTread = self.w.create_text(79  ,60 , text=((''.join(["Altitude(",self.valuelist[prefixcalc(velvariable)],"m)="])), int(round(altvariable/(10**(int(math.log(altvariable)/math.log(10))-3)),0))), font=self.ArialBAlt)
            self.gread= self.w.create_text(self.canvasx-53 ,95 , text=((''.join(["Grav(",self.valuelist[prefixcalc(velvariable)],"m/s)="])), (round(gravariable/((10**(int(math.log(gravariable)/math.log(10))-3)))/1000,2))),font=self.ArialBg)
            #Make this into a function that returns a value
        def shipinitial():
            self.w.delete(self.shipdraw)
            hudupdate(self.V,self.A,self.g)
            self.spacecraftx = self.ovalheadway
            self.spacecrafty2 = self.canvasy/2
            self.shipdraw = self.w.create_image(self.spacecraftx + 5, self.spacecrafty2,image=self.shipImage)
            self.phase = 1
            self.reset = 1
            self.stopall = 0
            self.repeat = 1
            configurebuttons('normal')
            self.animationstop.configure(bg = 'gray70', foreground = 'gray70',borderwidth=0, state = DISABLED,disabledforeground='gray70')
        def zoom():
            self.zoom = self.ZoomSlide.get() * (int(self.canvasx)/300) # + 100 # self.zoom
            if (self.zoom - self.oldzoom) != 0:
                zoomcontrol()
            self.oldzoom = self.zoom
            self.root.after(100, zoom)
        def zoomcontrol():
            self.ovalheadway = self.zoom
            update_frame()
        def resetdv():
            self.tdvchange = 0
            self.tdvchangelab['text'] ="Total_Delta_V=0"
        def SIGround(x, n):
            return float(("%." + str(n-1) + "e") % x)
        def configurebuttons(status):
            self.enterbutton.configure (state = status)
            self.entercorebutton.configure (state = status)
            self.entermassbutton.configure (state = status)
            self.enteraltbutton.configure (state = status)
            self.enterorbbutton.configure (state = status)
            self.enterathbutton.configure (state = status)
            self.enterincbutton.configure (state = status)
            self.buttonrun.configure (state = status)
            self.ZoomSlide.configure (state = status)
            self.InclineSlide.configure (state = status)
            self.changeposition.configure(state = status)
            try:
                self.shiprunbutton.configure (state = status)
                self.bodybutton.configure (state = status)
                self.entershipmass.configure (state = status)
                self.resetdv.configure(state = status)
            except:
                pass
        def update_frame():
            self.w.delete("all")
            self.V += self.changedict['Vchange']
            self.planetradius += self.changedict['Pchange'] 
            self.M += self.changedict['Mchange']
            self.UA += self.changedict['Achange']
            self.incline += self.changedict['Ichange']
            self.atmospheresize += self.changedict['Atchange']
            if (SIGround(self.M, 4)) == 1.988 * 10 ** 30 and (SIGround(self.planetradius, 3)) == 695000000:  #make this chaning according to planet listt
                self.planetname = "Sun"
                self.planetcolor = "darkorange"
            elif (SIGround(self.M, 4)) == 3.302 * 10 ** 23 and (SIGround(self.planetradius, 3)) == 2440000: 
                self.planetname = "Mercury"
                self.planetcolor = "gray"
            elif (SIGround(self.M, 4))  == 4.867 * 10 ** 24 and (SIGround(self.planetradius, 3)) == 6050000:
                self.planetname = "Venus"
                self.planetcolor = "Burlywood"
            elif (SIGround(self.M, 4)) == 5.972 * 10 ** 24 and (SIGround(self.planetradius, 3)) == 6370000: 
                self.planetname = "Earth"
                self.planetcolor = "green"
            elif (SIGround(self.M, 4)) == 7.348 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 1740000:
                self.planetname = "Moon"
                self.planetcolor = "dimgray"
            elif (SIGround(self.M, 4)) == 6.418 * 10 ** 23 and (SIGround(self.planetradius, 3)) == 3390000:
                self.planetname = "Mars"
                self.planetcolor = "chocolate"
            elif (SIGround(self.M, 4)) == 1.898 * 10 ** 27 and (SIGround(self.planetradius, 3)) == 69900000:
                self.planetname = "Jupiter"
                self.planetcolor = "darkkhaki"
            elif (SIGround(self.M, 4)) == 5.683 * 10 ** 26 and (SIGround(self.planetradius, 3)) == 58200000:
                self.planetname = "Saturn"
                self.planetcolor = "khaki"
            elif (SIGround(self.M, 4)) == 8.681 * 10 ** 25 and (SIGround(self.planetradius, 3)) == 25400000:
                self.planetname = "Uranus"
                self.planetcolor = "powderblue"
            elif (SIGround(self.M, 4)) == 1.024 * 10 ** 26 and (SIGround(self.planetradius, 3)) == 24600000:
                self.planetname = "Neptune"
                self.planetcolor = "royalblue"
            elif (SIGround(self.M, 4)) == 1.756 * 10 ** 28 and (SIGround(self.planetradius, 3)) == 262000000:
                self.planetname = "Kerbol"
                self.planetcolor = "yellow"
            elif (SIGround(self.M, 4)) == 2.526 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 250000:
                self.planetname = "Moho"
                self.planetcolor = "Darkgoldenrod"
            elif (SIGround(self.M, 4)) == 1.224 * 10 ** 23 and (SIGround(self.planetradius, 3)) == 700000:
                self.planetname = "Eve"
                self.planetcolor = "purple"
            elif (SIGround(self.M, 4)) == 1.242 * 10 ** 17 and (SIGround(self.planetradius, 3)) == 13000:
                self.planetname = "Gilly"
                self.planetcolor = "Navajowhite"
            elif (SIGround(self.M, 4))  == 5.292 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 600000: 
                self.planetname = "Kerbin"
                self.planetcolor = "forestgreen"
            elif (SIGround(self.M, 4)) == 9.76 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 200000:
                self.planetname = "Mun"
                self.planetcolor = "gray"
            elif (SIGround(self.M, 4)) == 2.646 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 60000:
                self.planetname = "Minmus"
                self.planetcolor = "Palegreen"
            elif (SIGround(self.M, 4)) == 4515000000000000000000 and (SIGround(self.planetradius, 3)) == 320000:
                self.planetname = "Duna"
                self.planetcolor = "Sienna"
            elif (SIGround(self.M, 4)) == 2.782 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 130000:
                self.planetname = "Ike"
                self.planetcolor = "Dimgray"
            elif (SIGround(self.M, 4)) == 3.219 * 10 ** 20 and (SIGround(self.planetradius, 3)) == 138000:
                self.planetname = "Dres"
                self.planetcolor = "gray70"
            elif (SIGround(self.M, 4)) == 4233000000000000000000000 and (SIGround(self.planetradius, 3)) == 6000000:
                self.planetname = "Jool"
                self.planetcolor = "OliveDrab"
            elif (SIGround(self.M, 4)) == 2.939 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 500000:
                self.planetname = "Laythe"
                self.planetcolor = "SteelBlue"
            elif (SIGround(self.M, 4)) == 3.109 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 300000:
                self.planetname = "Vall"
                self.planetcolor = "Lightseagreen"
            elif (SIGround(self.M, 4)) == 4.233 * 10 ** 22 and (SIGround(self.planetradius, 3)) == 600000:
                self.planetname = "Tylo"
                self.planetcolor = "Antiquewhite"
            elif (SIGround(self.M, 4)) == 3.726 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 65000:
                self.planetname = "Bop"
                self.planetcolor = "firebrick4"
            elif (SIGround(self.M, 4)) == 1.081 * 10 ** 19 and (SIGround(self.planetradius, 3)) == 44000:
                self.planetname = "Pol"
                self.planetcolor = "Moccasin"
            elif (SIGround(self.M, 4)) == 1.115 * 10 ** 21 and (SIGround(self.planetradius, 3)) == 210000:
                self.planetname = "Eeloo"
                self.planetcolor = "Whitesmoke"
            else:
                self.planetname = "Custom"
                self.planetcolor = "SlateGray"        
            self.planetdiameter = self.planetradius * 2
            self.U = self.G*self.M
            self.A= self.planetradius+self.UA
            self.B = (2*self.A*self.U - self.A*(2*self.U - self.A * self.V ** 2))/(2*self.U - self.A * self.V ** 2)
            self.L = (self.A+self.B)/2
            self.S = 2*self.L/(self.canvasx-self.ovalheadway*2)
            self.planetsize = self.planetradius / self.S
            self.E = abs(self.L - self.A)
            self.H = (self.L**2 - self.E**2)** 0.5
            self.tH = self.H * math.cos(self.incline * (0.0175))
            self.D =  self.L/self.tH
            self.OvalH = (self.canvasx-self.ovalheadway*2)/self.D
            self.T = (2*math.pi * (( (self.L ** 3)/ self.U )**0.5))
            self.Ec = self.E/self.L
            self.dM = self.M/(10**(int(math.log(self.M)/math.log(10))-3))
            self.pdsign = ((self.valuelist[int(((math.log(self.M)/math.log(10)))/3)]),'g') 
            self.miniplanet = self.planetradius/ (self.H / 55)
            self.LineLength = 1/((self.planetradius/44.26)/self.H)
            self.g = (self.G * self.M)/(self.A**2)
            self.shipg = self.g
            self.eV = ((2*self.G*self.M)/self.A)**0.5
            self.Fc = (self.shipmass * self.shipg) *1000 # in N
            if self.Fc != 0:
                self.smallban = self.w.create_image(90, 84,image=self.FcImage)
                self.smalltext = self.w.create_text(57,107, text =( "Fc=", round(self.Fc/1000, 1),"kN"), font = self.ArialBg)
            if self.A>=self.B:
                self.apov = "Periapsis="
                self.periv = "Apoapsis="
            else:
                self.apov = "Apoapsis="
                self.periv = "Periapsis="
            self.ox1 = self.ovalheadway
            self.oy1 = self.canvasy/2 - self.OvalH/2
            self.ox2 = self.canvasx - self.ovalheadway #STICK THIS BACK INTO CODE
            self.oy2 = self.canvasy/2 + self.OvalH/2
            self.spacecraftx = self.ovalheadway
            self.spacecrafty2 = self.canvasy/2
            self.athoval = self.w.create_oval(self.ovalheadway + (self.UA-self.atmospheresize)/self.S,self.canvasy/2 - self.planetsize - self.atmospheresize/self.S,self.ovalheadway + (self.UA+self.atmospheresize)/self.S + 2 * self.planetsize,self.canvasy/2 + self.planetsize + self.atmospheresize/self.S, fill = "skyblue", outline = "") #Athmosphere
            self.planet = self.w.create_oval(self.ovalheadway + self.UA/self.S,self.canvasy/2 - self.planetsize,self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize,self.canvasy/2 + self.planetsize, fill = self.planetcolor , outline = "") #Planet
            self.w.create_oval(self.ovalheadway + self.A - self.planetradius/10, self.canvasy/2 - self.planetradius/10,self.ovalheadway + self.UA + self.A + self.planetradius/10,self.canvasy/2 + self.planetradius/10, fill = 'red' , outline = "") #Planetcaps
            self.arc1 = self.w.create_arc(self.ox1,self.oy1,self.ox2,self.oy2, extent =  180,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3, style = ARC) # Orbit
            self.arc2 = self.w.create_arc(self.ox1,self.oy1,self.ox2,self.oy2, extent =  -180,  activeoutline= "deepskyblue", outline = "dodgerblue", width = 3, style = ARC) # Orbit
            if self.B >= self.planetradius:
                if (self.incline <= 0 and self.incline >= -90) or  (self.incline >= 90 and self.incline <= 180):
                    self.w.tag_raise(self.arc2)
                    self.w.tag_lower(self.arc1)
                else:
                    self.w.tag_raise(self.arc1)
                    self.w.tag_lower(self.arc2)
            else:
                self.w.tag_lower(self.arc1)
                self.w.tag_lower(self.arc2)
            self.w.tag_lower(self.athoval)
            self.w.create_line(self.ovalheadway, self.canvasy  - self.canvasy/100, self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize, self.canvasy  - self.canvasy/100, width = 10, fill = "gray") #Baseline for planet
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy  - self.canvasy/100 - 80, self.canvasx - self.ovalheadway, self.canvasy - self.canvasy/100 - 80, width = 10, fill = "darkgray") # BaselineOpposing Ship
            self.w.create_line(self.ovalheadway, self.canvasy - self.canvasy/100 - 40, self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy - self.canvasy/100 - 40, width = 10, fill = "darkgray") #Baseline With ship
            self.w.create_line(self.ovalheadway, self.canvasy - self.canvasy/100, self.ovalheadway, self.canvasy  - self.canvasy/100- 60, width = 5, fill = "gray70")# Ship/ Orbit Start
            self.w.create_line(self.canvasx - self.ovalheadway, self.canvasy - self.canvasy/100, self.canvasx - self.ovalheadway, self.canvasy  - self.canvasy/100- 100, width = 5, fill = "gray70")# Orbit End
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy  - self.canvasy/100, self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy  - self.canvasy/100- 100, width = 5, fill = "lightgray") #Panet cen
            self.w.create_line(self.ovalheadway + self.UA/self.S, self.canvasy - self.canvasy/100, self.ovalheadway + self.UA/self.S, self.canvasy - self.canvasy/100- 20, width = 5, fill = "black") #Planet line start
            self.w.create_line(self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize, self.canvasy - self.canvasy/100,self.ovalheadway + (self.UA/self.S) + 2 * self.planetsize, self.canvasy- self.canvasy/100- 20, width = 5, fill = "black") #Planet line end
            self.w.create_line(self.ovalheadway, self.canvasy  - self.canvasy/100, self.canvasx - self.ovalheadway, self.canvasy - self.canvasy/100, width = 10, fill = "gray") #Baseline
            self.w.create_image(self.canvasx - 95, 75,image=self.banImage) #Banner
            self.w.tag_raise(self.smallban)
            self.w.tag_raise(self.smalltext)
            self.w.create_image(95, 65,image=self.altImage) #MOVE THESE UP
            self.w.create_oval(self.ovalheadway + self.UA/self.S +  self.planetsize  + self.planetsize  * 0.01, self.canvasy/2 + self.planetsize* 0.01 ,self.ovalheadway + self.UA/self.S +self.planetsize -  self.planetsize * 0.01, self.canvasy/2 -   self.planetsize* 0.01,fill="maroon", outline = '')
            self.w.create_text(self.ovalheadway + self.UA/self.S + self.planetsize, self.canvasy/2 + 20 , text=self.planetname, font = self.ArialBVel) #planetname
            self.planetdetailsy = (self.canvasy / (self.planetsize / 1300 + 2)) -  80
            self.planetdetailsx = self.ovalheadway + self.UA/self.S + self.planetsize  - self.planetsize/4 + 100 # CHAGNE LAST VALUE LESSE AGGRESSIVE
            self.w.create_text(self.planetdetailsx, self.planetdetailsy - 20, text=("Mass=",((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (SIGround(self.dM, 4))))),''.join(self.pdsign)), font = self.ArialBg) #planetdetails
            self.w.create_text(self.planetdetailsx, self.planetdetailsy, text=("Body_Radius=",((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.planetradius,1))))), "m"), font = self.ArialBg) #planetdetails
            self.w.create_text(self.planetdetailsx, self.planetdetailsy + 20, text=("Atmosphere_Altitude=",((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.atmospheresize,1))))), "m"), font = self.ArialBg) 
            self.w.create_line(self.ovalheadway + self.UA/self.S + self.planetsize  , self.canvasy/2  - 20, self.planetdetailsx, self.planetdetailsy + 30 , width = 1) #TO PLANETDETAILS
            self.w.create_text(self.canvasx/2  , self.canvasy  - self.canvasy/100 - 10 , text=("Major_Axis=", ((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(2*self.L,1))))), "m"), font = self.ArialBg) #orbit text
            self.w.create_text((self.ovalheadway + self.UA/self.S + self.planetsize)/2 + self.ovalheadway/2  , self.canvasy  - self.canvasy/100 - 50 , text = (self.periv , ((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.A,1))))),"m"), font = self.ArialBg) #A
            self.w.create_text((self.ovalheadway + self.UA/self.S + self.planetsize + self.canvasx - self.ovalheadway)/2  , self.canvasy  - self.canvasy/100 - 90 , text = (self.apov,((re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % (round(self.B,1))))),"m"), font = self.ArialBg) # B
            self.w.create_text(self.canvasx/2, self.canvasy - 150, text=self.notification, font = self.ArialBg) #Yes it doubles up ssh, make font settings go on both
            hudupdate(self.V,self.A,self.g)
            self.shipdraw = self.w.create_image(self.spacecraftx + 5, self.spacecrafty2,image=self.shipImage)
            self.inclayers = self.w.create_image(self.canvasx - 85, self.canvasy - 137,image=self.incImage)
            self.w.create_text(self.canvasx -125, self.canvasy - 218,text = "Orbital Inclination",  font = self.ArialBorb)
            if self.miniplanet <= 44.26:
                self.w.create_oval(self.canvasx - 125+ self.miniplanet, self.canvasy -125 + self.miniplanet, self.canvasx - 125- self.miniplanet, self.canvasy -125 - self.miniplanet, fill = self.planetcolor, outline = "")
                self.w.create_arc(self.canvasx - 85, self.canvasy -85 , self.canvasx - 165, self.canvasy -165, extent = -1 * self.incline, width = 2, style = ARC)
                self.w.create_line(self.canvasx - 200, self.canvasy -125, self.canvasx - 50, self.canvasy -125, width = 3, fill = "darkred", dash = (20,5))
                self.w.create_line(self.canvasx - 125 +  (55 * ( math.cos (self.incline *( 0.0175)))), (self.canvasy -125) + (55 * ( math.sin (self.incline *(0.0175)))) , self.canvasx - 125 - (55 * ( math.cos (self.incline *(0.0175)))), (self.canvasy -125) - (55 * ( math.sin (self.incline *( 0.0175)))), fill = "dodgerblue" , width = 3)
                self.w.create_polygon(self.canvasx - 125 +  (40 * ( math.cos (self.incline *( 0.0175)))),(self.canvasy -125) + (40 * ( math.sin (self.incline *( 0.0175)))),self.canvasx - 125 +  (31.622 * ( math.cos (math.asin (10/30) + (self.incline *( 0.0175))))),(self.canvasy -125) + (31.622  * ( math.sin (math.asin (0.333) + (self.incline *( 0.0175))))),self.canvasx - 125 +  (31.622  * ( math.cos (math.asin (-0.333) + (self.incline *( 0.0175))))), (self.canvasy -125) + (31.622 * ( math.sin (math.asin (-0.333) + (self.incline *( 0.0175))))), width = 100, fill="deep sky blue")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 - self.miniplanet,self.canvasx -130, self.canvasy -140 - self.miniplanet,self.canvasx -120, self.canvasy -140 - self.miniplanet, fill="maroon")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 + self.miniplanet,self.canvasx -130, self.canvasy -110 + self.miniplanet,self.canvasx -120, self.canvasy -110 + self.miniplanet, fill="maroon")
                self.w.create_text (self.canvasx - 170, self.canvasy -56 , text =("Orbital Inclination ="), justify = LEFT, font = self.ArialBi)
                self.w.create_text (self.canvasx - 100, self.canvasy -56 , text =((-1 *( round(self.incline, 1)))), justify = LEFT, font = self.ArialBi)
            else:
                self.w.create_oval(self.canvasx - 125+ 44.26, self.canvasy -125 + 44.26, self.canvasx - 125- 44.26, self.canvasy -125 - 44.26, fill = self.planetcolor, outline = "")
                self.w.create_arc(self.canvasx - 85, self.canvasy -85 , self.canvasx - 165, self.canvasy -165, extent = -1 * self.incline, width = 2, style = ARC)
                self.w.create_line(self.canvasx - 200, self.canvasy -125, self.canvasx - 50, self.canvasy -125, width = 3, fill = "darkred", dash = (20,5))
                self.w.create_line(self.canvasx - 125 +  (self.LineLength * ( math.cos (self.incline *( 0.0175)))), (self.canvasy -125) + (self.LineLength * ( math.sin (self.incline *( 0.0175)))) , self.canvasx - 125 - (self.LineLength * ( math.cos (self.incline *( 0.0175)))), (self.canvasy -125) - (self.LineLength * ( math.sin (self.incline *( 0.0175)))), fill = "dodgerblue" , width = 3)
                self.shrink = self.LineLength / 150
                self.w.create_polygon(self.canvasx - 125 +  (((self.shrink*1.65) * self.LineLength+10) * ( math.cos (self.incline *( 0.0175)))),(self.canvasy -125) + (((self.shrink*1.65) * self.LineLength+10) * ( math.sin (self.incline *( 0.0175)))),self.canvasx - 125 +  ((10**2 + (self.shrink*self.LineLength+10)**2)**0.5 * ( math.cos (math.asin (10/(self.shrink * self.LineLength+10)) + (self.incline *( 0.0175))))),(self.canvasy -125) + ((10**2 + (self.shrink * self.LineLength+10)**2)**0.5 * ( math.sin (math.asin (10/(self.shrink * self.LineLength+10)) + (self.incline *( 0.0175))))),self.canvasx - 125 +  ((10**2 + (self.shrink * self.LineLength+10)**2)**0.5 * ( math.cos (math.asin (-10/(self.shrink * self.LineLength+10)) + (self.incline *( 0.0175))))), (self.canvasy -125) + ((10**2 + (self.shrink * self.LineLength+10)**2)**0.5* ( math.sin (math.asin (-10/(self.shrink* self.LineLength+10)) + (self.incline *( 0.0175))))), width = 100, fill="deep sky blue")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 - 44.26,self.canvasx -130, self.canvasy -140 - 44.26,self.canvasx -120, self.canvasy -140 - 44.26, fill="maroon")
                self.w.create_polygon(self.canvasx -125, self.canvasy -125 + 44.26,self.canvasx -130, self.canvasy -110 + 44.26,self.canvasx -120, self.canvasy -110 + 44.26, fill="maroon")
                self.w.create_text (self.canvasx - 170, self.canvasy -56 , text =("Orbital Inclination ="), justify = LEFT, font = self.ArialBi)
                self.w.create_text (self.canvasx - 100, self.canvasy -56 , text =((-1 *( round(self.incline, 1)))), justify = LEFT, font = self.ArialBi)
            self.loopcurrent += 1
            if self.loopcurrent <= abs(self.loopvalue)-1:
                self.root.after(self.looptime, update_frame)
            else:
                resetchangedict()
                self.loopvalue = 0
                self.loopcurrent = 0
                configurebuttons('normal')
                if self.windowdict['proot'] == True:
                    prootdisplay()
                    try:
                        removelabel(self.waitmes)
                    except:
                        pass
                if self.A >= self.B:
                    self.changeposition.configure(text = "Warp to Periapsis")
                    self.enterorbbutton.configure(text = "Set Periapsis (m)")
                    self.enteraltbutton.configure(text = "Set Apoapsis (m)")
                else:
                    self.changeposition.configure(text = "Warp to Apoapsis")
                    self.enterorbbutton.configure(text = "Set Apoapsis (m)")
                    self.enteraltbutton.configure(text = "Set Periapsis (m)")
                
                if self.first != 1:
                    updatedvchange()
                    self.resetbutton.configure(bg = 'gray70', foreground = 'gray70',borderwidth=0, state = DISABLED,disabledforeground='gray70')
                else:
                    self.first += 1
                removelabel(self.waitnes)
        def tutwindowopen():
            if self.windowdict['tutroot'] == False:
                self.windowdict['tutroot'] = True
                self.tutroot = Toplevel()
                self.tutcombust = Button(self.tutroot, text = "Close", command = lambda:windowdictclose(self.tutroot,'tutroot'))
                self.tutcombust.grid(row = 200, column = 1, columnspan = 1,sticky = W)
                self.tutroot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.tutroot,'tutroot'))
                self.tutroot.configure(bg = 'gray70')
                self.tutroot.wm_title("Tutorial")
                self.tutroot.resizable(0,0)
                self.slideshow = 0
                self.Basicbutton = Button(self.tutroot, text = 'Basic Window Controls', command = basictut)
                self.Basicbutton.grid(row = 10, column = 1,sticky = W)
                self.Windowbutton = Button(self.tutroot, text = 'Miscellaneous Window Controls', command = windowtut)
                self.Windowbutton.grid(row = 20, column = 1,sticky = W)
                self.Allbutton = Button(self.tutroot, text = 'Advanced Window Controls', command = allcommand)
                self.Allbutton.grid(row = 30, column = 1,sticky = W)
                self.nextbutton = Button(self.tutroot, text='Next',command = plusone)
                self.nextbutton.grid(row=100,column=2)
                self.backbutton = Button(self.tutroot, text='Back',command = minusone)
                self.backbutton.grid(row=100,column=1)
                removelabel(self.nextbutton)
                removelabel(self.backbutton)
                self.PhotoLabel = Label(self.tutroot, image=self.CurrentImage)
                self.PhotoLabel.grid(row = 1, column = 3,rowspan = 1000)
                self.PhotoLabel.configure(bg = 'gray70')
                removelabel(self.PhotoLabel)
                self.HintLabel = Label(self.tutroot, image=self.HintImage)
                self.HintLabel.grid(row = 10, column = 3, rowspan =30)
                self.HintLabel.configure(bg = 'gray70')
        def resetslide():
            if self.currenttutmenu == 1:
                if self.slideshow == 1:
                    self.CurrentImage= PhotoImage(file="BASICMISSIONTUT.png") #move these out
                    self.nextbutton.configure(state = NORMAL)
                    self.backbutton.configure(state = DISABLED)
                elif self.slideshow ==2:
                    self.CurrentImage= PhotoImage(file="VARMISSIONTUT.png") #Make this better
                    self.nextbutton.configure(state = NORMAL)
                    self.backbutton.configure(state = NORMAL)
                elif self.slideshow ==3:
                    self.CurrentImage= PhotoImage(file="DISPLAYTUT.png")
                    self.nextbutton.configure(state = DISABLED)
                    self.backbutton.configure(state = NORMAL)
            elif self.currenttutmenu == 2:
                if self.slideshow == 1:
                    self.CurrentImage= PhotoImage(file="MATHTUT.png")
                    self.nextbutton.configure(state = NORMAL)
                    self.backbutton.configure(state = DISABLED)
                elif self.slideshow ==2:
                    self.CurrentImage= PhotoImage(file="CALCTUT.png")
                    self.nextbutton.configure(state = NORMAL)
                    self.backbutton.configure(state = NORMAL)
                elif self.slideshow ==3:
                    self.CurrentImage= PhotoImage(file="ORBTUT.png")
                    self.nextbutton.configure(state = NORMAL)
                    self.backbutton.configure(state = NORMAL)
                elif self.slideshow ==4:
                    self.CurrentImage= PhotoImage(file="FAQTUT.png")
                    self.nextbutton.configure(state = NORMAL)
                    self.backbutton.configure(state = NORMAL)
                elif self.slideshow ==5:
                    self.CurrentImage= PhotoImage(file="GLOSSTUT.png")
                    self.nextbutton.configure(state = DISABLED)
                    self.backbutton.configure(state = NORMAL)
            elif self.currenttutmenu == 3:
                if self.slideshow == 1:
                    self.CurrentImage= PhotoImage(file="FULLMISISONTUT.png")
                    self.backbutton.configure(state = DISABLED)
                    self.nextbutton.configure(state = DISABLED)
            removelabel(self.PhotoLabel)
            self.PhotoLabel = Label(self.tutroot, image=self.CurrentImage)
            self.PhotoLabel.grid(row = int((10 * self.currenttutmenu) + 8), column = 2)
            self.PhotoLabel.configure(bg = 'gray70')
        def plusone():
            if self.currenttutmenu == 1:
                if self.slideshow <= 2:
                    self.slideshow += 1
            elif self.currenttutmenu == 2:
                if self.slideshow <= 4:
                    self.slideshow += 1
            resetslide()
        def minusone():
            if self.slideshow >= 2:
                self.slideshow -= 1
            resetslide()
        def basictut():
            self.currenttutmenu = 1
            self.slideshow = 1
            resetslide()
            removelabel(self.nextbutton)
            removelabel(self.backbutton)
            removelabel(self.HintLabel)
            self.backbutton = Button(self.tutroot, text='Back',command = minusone)
            self.backbutton.grid(row=19,column=1,columnspan = 2)
            self.nextbutton = Button(self.tutroot, text='Next',command = plusone)
            self.nextbutton.grid(row=19,column=2, columnspan = 2)
            self.nextbutton.configure(state = NORMAL)
            self.backbutton.configure(state = DISABLED)
        def windowtut():
            self.currenttutmenu = 2
            self.slideshow = 1
            resetslide()
            removelabel(self.nextbutton)
            removelabel(self.backbutton)
            removelabel(self.HintLabel)
            self.backbutton = Button(self.tutroot, text='Back',command = minusone)
            self.backbutton.grid(row=29,column=1,columnspan = 2)
            self.nextbutton = Button(self.tutroot, text='Next',command = plusone)
            self.nextbutton.grid(row=29,column=2, columnspan = 2)
            self.nextbutton.configure(state = NORMAL)
            self.backbutton.configure(state = DISABLED)
        def allcommand():
            self.currenttutmenu = 3
            self.slideshow = 1
            resetslide()
            removelabel(self.nextbutton)
            removelabel(self.backbutton)
            removelabel(self.HintLabel)
        def credrootwindow():
            if self.windowdict['credroot'] == False:
                self.credroot = Toplevel()
                self.windowdict['credroot'] = True
                self.credroot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.credroot,'credroot'))
                self.credroot.configure(bg = 'gray70')
                self.credroot.wm_title("Credits")
                self.windowdict['credroot'] == False
                Label(self.credroot, text = "Martin Lambrechtse - Reid\n\nCreated on Python 3 as a demonstration on Celestial Mechanics\nto L3 NCEA students. This script is free to be edited as long\nas credit is given. This project has been created to comply\nwith NCEA unit standard AS91354 and AS91370. This program was created\ncreated by a L2 student that is fascinated by space and its theory.\n", bg = 'gray70').grid(row = 3,column = 1)
                Label(self.credroot, justify = LEFT, text = "Assumptions:\n•The spacecraft exherts no gravational pull on the body it orbits.\n•Langrange points are not modelled.\n•No external forces are acting.\n•Number rounding is used when displaying, usually 4 s.f. or 1-2 dp.\n•The default atmosphere height is 100km, based on the Karman line.\n•Atmospheres are not changed when changing body like mass or radius.\n•Orbit speed of spacecraft is scaled down when animating.\n•No SOI radius implented. It's possible to make an orbit 'too big'.\n•A very small computational inaccuracy is present.\n\nKnown bugs:\n•The spacecraft animation freezes the script at low resolutions & high zoom.\n••Fix - Close and reopen script. Use a lower zoom level next time.\n•Orbital Window goes white when changing altitude too much.\n••Cause - Orbit exceeds escape velocity and therefore cannot physically exist.\n••Fix - Click the red reset button.\n•Inclination animates -170° to 170° the long way rather than the short.\n••Fix - None, it's a visual bug. Delta V calculations work properly.\n•Neptune in planet selection gives a long decimal string rather than 4 s.f.\n••Cause - Sometimes 1=/= 1 due to the way floating point numbers work.\n••Fix - It is as inaccurate as anything else due to computing rounding errors.\n", bg = 'gray70').grid(row =4,column = 1,sticky = W)
                self.credcombust = Button(self.credroot, text = "Close", command = lambda:windowdictclose(self.credroot,'credroot'))
                self.credcombust.grid(row = 500, column = 1)
        def optionmenu():
            if self.windowdict['oproot'] == False:
                self.oproot = Toplevel()
                self.oproot.protocol('WM_DELETE_WINDOW',lambda:windowdictclose(self.oproot,'oproot'))
                self.oproot.configure(bg = 'gray70')
                self.oproot.wm_title("Options")
                self.windowdict['oproot'] = True
                self.desxres = IntVar()
                self.desyres = IntVar()
                Label(self.oproot, text = "- - - - - -  - - Resolution- - - - - - - - - - - - - - - - - -",bg = 'gray70').grid(row = 2, column = 1, columnspan = 4)
                Label(self.oproot, text = "  Display Mode  ", bg = 'gray70').grid(row=1,column = 2)
                self.fulopen = Button(self.oproot, text="FullScreen", command=fullscreen)
                self.fulopen.grid(row = 1, column = 1, columnspan = 2, sticky = W)
                self.winopen = Button(self.oproot, text="Windowed", command=windowed)
                self.winopen.grid(row = 1, column = 3, columnspan = 2, sticky = W)
                self.reslab = Label(self.oproot,bg = 'gray70')
                self.reslab.grid(row=39,column = 1, columnspan =4, sticky = W)
                self.AmountSlide = Scale(self.oproot, from_=1, to=(500),length=150, orient = HORIZONTAL)
                self.AmountSlide.grid(row = 101, column =1 , columnspan = 2, sticky = W)
                self.confirmcalc = Button(self.oproot, text = "Confirm Animation Quality", command = animationoverride)
                self.confirmcalc.grid(row = 101, column = 3, columnspan = 2, sticky = W)
                Label(self.oproot, text = "\n- - - - - -  - - Program Mode - - - - - - - - - - - - - - - - - -", bg = 'gray70').grid(row=148,column = 1, columnspan = 4)
                self.BasicMode = Button(self.oproot, text = "Basic", command = basics)
                self.BasicMode.grid(row = 150, column = 2, sticky = W)
                self.AdvancedMode = Button(self.oproot, text = "Advanced", command  = advanceds)
                self.AdvancedMode.grid(row = 150, column = 3, sticky = W)
                Label(self.oproot, text = '', bg = 'gray70').grid(row = 199, column =1)
                self.optioncombust = Button(self.oproot, text = "Close", command = lambda:windowdictclose(self.oproot,'oproot'))
                self.optioncombust.grid(row = 200, column = 1, columnspan = 2)
                self.qHD = Button(self.oproot, text="960x540",command=lambda:presetres(960,540))
                self.qHD.grid(row=4,column = 1)
                self.HD = Button(self.oproot, text="1280x720",command=lambda:presetres(1280,720))
                self.HD.grid(row=4,column = 2)
                self.fHD = Button(self.oproot, text="1366x768",command=lambda:presetres(1366,768))
                self.fHD.grid(row=4,column = 3)
                self.HDp = Button(self.oproot, text="1600x900",command=lambda:presetres(1600,900))
                self.HDp.grid(row=5,column = 1)
                self.FHD = Button(self.oproot, text="1920x1080",command=lambda:presetres(1920,1080))
                self.FHD.grid(row=5,column = 2)
                self.QHD = Button(self.oproot, text="2560x1440",command=lambda:presetres(2560,1440))
                self.QHD.grid(row=5,column = 3)
                self.auto = Button(self.oproot, text="Auto", command = lambda:preferancechange('Resolution = Set','Resolution = Auto'))
                self.auto.grid(row=4,column = 4)
                self.custom = Button(self.oproot, text="Custom", command = custombox)
                self.custom.grid(row=5,column = 4)
                Label(self.oproot, text = "\n- - - - - - - - - -  - - Misc - - - - - - - - - - - - - - - - - - - - - -", bg = 'gray70').grid(row=170,column = 1, columnspan = 4)
                self.blurbshow = Button(self.oproot, text="Show Blurb on Startup", command = lambda:preferancechange('Blurbwindowopen = False','Blurbwindowopen = True'))#add function
                self.blurbshow.grid(row = 171, column = 1, columnspan = 3)
                self.oproot.resizable(0,0)
        def fullscreen():
            self.fulopen.configure(state=DISABLED)
            self.winopen.configure(state=NORMAL)
            resvalchange('resxprefs.txt','self.resxpreference',self.oproot.winfo_screenwidth())#resxprefs.txt,resxpreference
            resvalchange('resyprefs.txt','self.resypreference',self.oproot.winfo_screenheight())#resxprefs.txt,resxpreference
            preferancechange('Resolution = Auto','Resolution = Set')
            preferancechange('Fullscreen = False','Fullscreen = True')
            currentres()
        def windowed():
            self.fulopen.configure(state=NORMAL)
            self.winopen.configure(state=DISABLED)
            preferancechange('Resolution = Auto','Resolution = Set')
            preferancechange('Fullscreen = True','Fullscreen = False')
            currentres()
        def custombox():
            self.xBox = Entry(self.oproot, textvariable=self.desxres, width = 25)
            self.xBox.grid(row=6, column=1, columnspan = 2, sticky = W)
            self.yBox = Entry(self.oproot, textvariable=self.desyres, width = 25)
            self.yBox.grid(row=7, column=1, columnspan = 2, sticky = W)
            self.fulopen.configure(state=NORMAL)
            self.winopen.configure(state=DISABLED)
            self.resset = Button(self.oproot, text="Confirm Resolution", command=lambda:presetres(abs(int(self.xBox.get())),abs(int(self.yBox.get()))))
            self.resset.grid(row = 6, column = 3, columnspan = 2, rowspan = 2, sticky = W)
        def presetres(screenxres,screenyres): #SHORTEN ALL OF THESE
            self.fulopen.configure(state=NORMAL)
            self.winopen.configure(state=DISABLED)
            resvalchange('resxprefs.txt','self.resxpreference',screenxres)#resxprefs.txt,resxpreference
            resvalchange('resyprefs.txt','self.resypreference',screenyres)#resxprefs.txt,resxpreference
            preferancechange('Resolution = Auto','Resolution = Set')
            preferancechange('Fullscreen = True','Fullscreen = False')
            currentres()
        def currentres():
            if "Fullscreen = False" in open('orbitprefs.txt','r').read():
                self.message = "Windowed"
            else:
                self.message = "Fullscreen"
            self.reslab.configure(text = (format("Current_Resolution="), (int(open('resxprefs.txt','r').read())),"x",(int(open('resyprefs.txt','r').read())),"@", self.message))
            
        def basics():
            preferancechange('Difficultymode = Hard','Difficultymode = Easy')
        def advanceds():
            preferancechange('Difficultymode = Easy','Difficultymode = Hard')
        def animationoverride():
            resvalchange('benchmarkprefs.txt','self.changepreference',self.AmountSlide.get())
        def blurbclose():
            self.blurbwindow.destroy()
        def preferancechange(textfind,textreplace):
            self.preference = open('orbitprefs.txt','r+')
            for line in fileinput.input( 'orbitprefs.txt' ):
                self.preference.write(line.replace(textfind,textreplace ))
            self.preference.close()
        def resetchangedict():
            self.changedict = {'Pchange':0,'Mchange':0,'Achange':0,'Atchange':0,'Vchange':0,'Ichange':0}
        def resvalchange(txtname,varname,value):#resxprefs.txt,resxpreference
            open(txtname,'w').close()
            varname = open(txtname,'w')
            print ((value),file = varname)
            varname.close()
        self.groot = tkinter.Tk()
        self.groot.wm_title("Menu")
        self.groot.resizable(0,0) #make instead all of this variable nonsense that is dependant on files be in orbit window
        self.groot.configure(bg = 'gray70')
        self.planetlist = [['Sun','Mercury', 'Venus', 'Earth', '      Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Kerbol', 'Moho', 'Eve', '      Gilly', 'Kerbin',
                            '        Mun' , '        Minmus','Duna', '       Ike', 'Dres', 'Jool', '      Laythe', '      Vall', '      Tylo', '      Bop', '      Pol', 'Eeloo'],
                           [1.988 * 10 ** 30,3.302 * 10 ** 23,4.867 * 10 ** 24,5.972 * 10 ** 24,7.348 * 10 ** 22, 6.418 * 10 ** 23,1.898 * 10 ** 27,5.683 * 10 ** 26 , 8.681 * 10 ** 25,102400000000000000000000000, 1.756 * 10 ** 28,
                            2.526 * 10 ** 21,1.224 * 10 ** 23,1.242 * 10 ** 17, 5.292 * 10 ** 22 ,9.76 * 10 ** 20,2.646 * 10 ** 19,4515000000000000000000, 2.782 * 10 ** 20, 3.219 * 10 ** 20,4233000000000000000000000, 2.939 * 10 ** 22,
                            3.109 * 10 ** 21,4.233 * 10 ** 22,3.726 * 10 ** 19,1.081 * 10 ** 19,1.115 * 10 ** 21],
                           [695000000,2440000,6050000,6370000,1740000, 3390000,69900000,58200000,25400000,24600000,262000000,250000, 700000, 13000,600000,200000,60000,320000,130000,138000,6000000,500000,300000,600000,65000,44000,210000],
                           ]
        self.CALCmenu = PhotoImage(file="OPENCALCPs.png")
        self.CREDmenu = PhotoImage(file="OPENCREDPs.png")
        self.TUTmenu = PhotoImage(file="OPENTUTPs.png")
        self.OPmenu = PhotoImage(file="OPENOPTPs.png")
        self.Emenu= PhotoImage(file="MENUEARTH.png")
        self.banImage = PhotoImage(file="Banner.png")
        self.altImage = PhotoImage(file="AltBanner.png")
        self.FcImage = PhotoImage(file="AltBannerBot.png")
        self.shipImage = PhotoImage(file="apollopixelartsmall.png")
        self.incImage = PhotoImage(file="InclineLayerLight.png")             
        self.CurrentImage= PhotoImage(file="MENUEARTH.png")
        self.HintImage= PhotoImage(file="TUThints.png")
        self.startframe = Frame(self.groot, bg='gray70')
        self.advancedframe = Frame(self.groot, bg='gray70')
        self.Vviva= PhotoImage(file="VISVIVA.png")
        self.FGrav = PhotoImage(file="FGRAV.png")
        self.Gconstant = PhotoImage(file="GCONSTANT.png")
        self.Trocket = PhotoImage(file="ROCKEQ.png")
        self.Evelocity = PhotoImage(file="EFFEXHVEL.png")
        self.enterbutton = Button(self.advancedframe,text = "Set Velocity (m/s)", command=lambda:simpleloopchange(self.Ventry,'fake',self.V,'Vchange',False))   
        self.entercorebutton = Button(self.advancedframe,text = "Set Body Radius (m)", command=lambda:simpleloopchange(self.PRdentry,self.PReentry,self.planetradius,'Pchange',False))  
        self.entermassbutton = Button(self.advancedframe,text = "Set Body Mass (kg)", command=lambda:simpleloopchange(self.Mdentry,self.Meentry,self.M,'Mchange',False))
        self.enteraltbutton = Button(self.advancedframe,text = "Set Altitude (m)", command=lambda:simpleloopchange(self.Adentry,self.Aeentry,self.A,'Achange',False))
        self.enterorbbutton = Button(self.advancedframe,text = "Set Apo/Peri (m)", command=lambda:simpleloopchange(self.Odentry,self.Oeentry,self.V,'Vchange',True)) 
        self.enterathbutton = Button(self.advancedframe,text = "Set Atmosphere (m)", command=lambda:simpleloopchange(self.Atdentry,self.Ateentry,self.atmospheresize,'Atchange',False))
        self.enterincbutton = Button(self.advancedframe,text = "Set Inclination (°)", command=lambda:simpleloopchange(self.InclineSlide,'fake',self.incline,'Ichange',False))
        self.buttonrun = Button(self.advancedframe,text='Run!',command=looprun)
        self.resetbutton = Button(self.advancedframe,text = "Reset", command=reset,bg = 'gray70')          
        self.changeposition = Button(self.advancedframe, text = "Warp to Apo/Peri", command = loopchangeposition)
        self.crootwindowopen = Button(self.advancedframe, text = "Calculator", command = crootwindow)
        self.prootwindowopen = Button(self.advancedframe, text = "Orbital Characteristics", command = prootwindow)
        self.frootwindowopen = Button(self.advancedframe, text = "FAQ", command = frootwindow)
        self.orootwindowopen = Button(self.advancedframe, text = "Glossary", command = orootwindow)
        self.mrootwindowopen = Button(self.advancedframe, text = "Math", command = mrootwindow)
        self.Ventry = IntVar()
        self.PRdentry = DoubleVar()
        self.Mdentry = DoubleVar()
        self.Adentry = DoubleVar()
        self.Odentry = DoubleVar()
        self.Atdentry = DoubleVar()
        self.PReentry = IntVar()
        self.Meentry = IntVar()
        self.Aeentry = IntVar()
        self.Oeentry = IntVar()
        self.Ateentry = IntVar()
        self.ispentry = DoubleVar()
        self.wetmassentry = DoubleVar()
        self.drymassentry = DoubleVar()
        self.shipispentry = DoubleVar()
        self.shipenginethrustentry = DoubleVar()
        self.shipfuelmassentry = DoubleVar()
        self.shipmassentry = DoubleVar()
        self.VelBox = Entry(self.advancedframe, textvariable=self.Ventry, width= 47)
        self.VelBox.grid(row=1, column=1,columnspan=5 , sticky=W) # add length
        self.PRBox = Entry(self.advancedframe, textvariable=self.PRdentry)
        self.PRBox.grid(row=6, column=1)
        self.MBox = Entry(self.advancedframe, textvariable=self.Mdentry)
        self.MBox.grid(row=5, column=1)
        self.ABox = Entry(self.advancedframe, textvariable=self.Adentry)
        self.ABox.grid(row=3, column=1)
        self.OBox = Entry(self.advancedframe, textvariable=self.Odentry)
        self.OBox.grid(row=2, column=1)
        self.AtBox = Entry(self.advancedframe, textvariable=self.Atdentry)
        self.AtBox.grid(row=7, column=1)
        self.PReBox = Entry(self.advancedframe, textvariable=self.PReentry)
        self.PReBox.grid(row=6, column=3)
        self.MeBox = Entry(self.advancedframe, textvariable=self.Meentry)
        self.MeBox.grid(row=5, column=3)
        self.AeBox = Entry(self.advancedframe, textvariable=self.Aeentry)
        self.AeBox.grid(row=3, column=3)
        self.OeBox = Entry(self.advancedframe, textvariable=self.Oeentry)
        self.OeBox.grid(row=2, column=3)
        self.AteBox = Entry(self.advancedframe, textvariable=self.Ateentry)
        self.AteBox.grid(row=7, column=3)
        self.PrLab = Label(self.advancedframe, text="x10^")
        self.PrLab.grid(row=6, column=2)
        self.MLab = Label(self.advancedframe, text="x10^")
        self.MLab.grid(row=5, column=2)
        self.ALab = Label(self.advancedframe, text="x10^")
        self.ALab.grid(row=3, column=2)
        self.OLab = Label(self.advancedframe, text="x10^")
        self.OLab.grid(row=2, column=2)
        self.AtLab = Label(self.advancedframe, text="x10^")
        self.AtLab.grid(row=7, column=2)
        self.LINELAB4 = Label(self.advancedframe, text="- - - - - - - - - - - - - - - - - - - - - Navigation - - - - - - - - - - - - - - - - - - - - -", font="arial",bg='gray70')
        self.LINELAB4.grid(row=21, column=1, columnspan = 5)
        self.enterbutton.grid(row=1, column=4, sticky=W)
        self.entermassbutton.grid(row=5, column=4, sticky=W)
        self.entercorebutton.grid(row=6, column=4, sticky=W)
        self.enterathbutton.grid(row=7, column =4, sticky=W)
        self.enterincbutton.grid(row=9, column =4, sticky = W)
        self.buttonrun.grid(row=12, column=2, columnspan = 1)
        self.changeposition.grid(row=12, column=4, columnspan = 2, sticky = W)
        self.changeposition.grid(row=12, column=4, columnspan = 2, sticky = W)
        self.enterorbbutton.grid(row=2, column =4, sticky=W)
        self.enteraltbutton.grid(row=3, column =4, sticky=W)
        self.crootwindowopen.grid(row = 29, column = 1, columnspan = 2)
        self.prootwindowopen.grid(row = 29, column = 2, columnspan = 4, sticky = W)
        self.frootwindowopen.grid(row = 29, column = 4, columnspan = 4, sticky = W)
        self.orootwindowopen.grid(row = 29, column = 4, columnspan = 2)
        self.mrootwindowopen.grid(row = 29, column = 1, columnspan = 1,sticky = W)
        self.resetbutton.grid(row=8, column=5, columnspan = 4, sticky = W)
        self.InclineSlide = Scale(self.advancedframe, from_=-180, to=180,length=280 ,orient=HORIZONTAL)
        self.InclineSlide.grid(row = 9, column =1 , columnspan = 4, sticky = W)
        self.ZoomSlide = Scale(self.advancedframe, from_=0, to=(100),length=130)
        self.ZoomSlide.grid(row = 1, column =5 , columnspan = 1, rowspan = 6, sticky = W)
        self.zoomlab = Label(self.advancedframe, text = "ZOOM",bg='gray70')
        self.zoomlab.grid(row = 7, column = 5)
        self.calccombust = Button(self.advancedframe, text = "Close", command = grootwindowclose)
        self.calccombust.grid(row = 29, column = 5, sticky = W)
        self.waitnes = Label(self.advancedframe, text =("Calculating..."), bg = 'gray70')
        self.waitnes.grid(row = 14, column = 1, columnspan = 3)
        self.uplab = Label(self.advancedframe, text = "Spacecraft variables. ↑", bg = 'gray70')
        self.uplab.grid(row=4, column =1)
        self.downlab = Label(self.advancedframe, text = "↓ Body variables.", bg = 'gray70')
        self.downlab.grid(row=4, column =3)
        self.startframe.grid(row=1,column =1)
        self.orbitopen = Button(self.startframe, text="Open Calculator", command=orbitcalc, image = self.CALCmenu,bg = 'gray70',borderwidth=0)
        self.orbitopen.grid(row = 1, column = 1,sticky=W)
        self.tutopen = Button(self.startframe, text="Open Tutorial", command=tutwindowopen, image = self.TUTmenu,bg = 'gray70',borderwidth=0)
        self.tutopen.grid(row = 20, column = 1,sticky=W)
        self.optopen = Button(self.startframe, text="Open Options", command=optionmenu, image = self.OPmenu,bg = 'gray70',borderwidth=0)
        self.optopen.grid(row = 30, column = 1,sticky=W)
        self.credopen = Button(self.startframe, text="Open Credits", command = credrootwindow,image = self.CREDmenu,bg = 'gray70',borderwidth=0)
        self.credopen.grid(row = 40,column = 1,sticky=W)
        self.EMbutton = Label(self.startframe, image=self.Emenu)
        self.EMbutton.grid(row = 1, column = 3,rowspan = 1000)
        self.EMbutton.configure(bg = 'gray70')
        self.blurbwindow = Toplevel()
        self.blurbwindow.wm_title("Blurb")
        self.blurbwindow.configure(bg = 'gray70')
        self.blurbwindow.resizable(0,0)
        Label(self.blurbwindow,justify= LEFT, text = "This program simulates orbital motion under the\ninfluence of Newtonian gravity. It displays how\nfactors such as orbital velocity, orbit radius\nand gravational parameters of bodies affect an\norbit in a visual way. This program has been\ndesigned to be easily editible with many variables\nthat a user can edit and change, to control many\ncharacteristics of an orbit.\n\nThings to Note:\n•To run the simulation, enter a variable into a\nbox, and then select 'Set xxxxx'. Then click 'Run!'\nto run the simulation.\n•The simulation is set to basic mode by default.\nTo set unlock extra features, set the program to\nadvanced mode in the options.\n•There is a chance of crashing the program due\nto variables that exceed escape velocity. To fix this\njust press the red 'Reset' button.\n•You can only edit the spacecraft variable group or\nthe body variable group at a time. Please refer to the\ntutorial for more information.").grid(row = 1,sticky = W)
        self.blurbcombust = Button(self.blurbwindow, text = "Close", command = blurbclose)
        self.blurbcombust.grid(row = 200)
        self.showagain = Button(self.blurbwindow, text = "Don't show this again", command = lambda:preferancechange('Blurbwindowopen = True','Blurbwindowopen = False'))
        self.showagain.grid(row = 201)
        self.blurbwindow.attributes("-topmost", True)
        self.layerprevent = False
        self.windowdict = {'oproot':False,'credroot':False,'tutroot':False,'mroot':False,'oroot':False,'froot':False, 'proot':False,'croot':False,'root':False}
        self.faqdict = {'radiusexp':False,'mathexp':False,'inclinedexp':False,'shipspeed':False,'oberth':False,'craftmass':False}
        self.valuelist = ['','k','M','G','T','P','E','Z','Y']
        resetchangedict()
        self.t2 = time.time()
        try:
            if "Benchmarkstart = True" in open('orbitprefs.txt','r').read():
                resvalchange('benchmarkprefs.txt','self.changepreference',(int((12/ (self.t2-self.t1)))))
            if "Blurbwindowopen = False" in open('orbitprefs.txt','r').read():
                self.blurbwindow.destroy()
        except:
            self.preference = open('orbitprefs.txt','w') #Creates file to print to
            print ("Blurbwindowopen = True\nResolution = Auto\nFullscreen = False\nDifficultymode = Easy\nBenchmarkstart = True", file = self.preference)
            resvalchange('benchmarkprefs.txt','self.changepreference',(int((12/ (self.t2-self.t1)))))
            self.preference.close()
        preferancechange('Benchmarkstart = True','Benchmarkstart = False')
        self.groot.mainloop()
app=OrbitalCalculator()

