from tkinter import*
from tkinter import ttk
import random 
import time
import datetime
import tkinter.messagebox

class Travel:
    def __init__(self,root):
        self.root = root
        self.root.title = (" Travel Management Systems" )
        self.root.geometry("1450x750+0+0")
        self.root.configure(background = "black")
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d-%m-%y"))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()
        
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = StringVar()
        var12 = StringVar()
        var13 = StringVar()
        
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Telephone = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        
        AirportTax = StringVar()
        Mile = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        
        Standard = StringVar()
        Economy = StringVar()
        FirstClass = StringVar()
        
        AirportTax.set(0)
        Mile.set(0)
        Travel_Ins.set(0)
        Luggage.set(0)
        
        Standard.set(0)
        Economy.set(0)
        FirstClass.set(0)
#================================================Define Function========================================================================
      
        def iExit():
            iExit=tkinter.messagebox.askyesno("Travel Planner Application","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return   
        def Reset():
            AirportTax.set("0")
            Mile.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            Economy.set("0")
            FirstClass.set("0")

            Firstname = StringVar("")
            Surname = StringVar("")
            Address = StringVar("")
            PostCode = StringVar("")
            Telephone = StringVar("")
            Mobile = StringVar("")
            Email = StringVar("")

            PaidTax.set = StringVar()
            SubTotal.set = StringVar()
            TotalCost.set = StringVar()
            self.txtRecepipt.delete("1.0",END)

            var1 = IntVar("0")
            var2 = IntVar("0")
            var3 = IntVar("0")
            var4 = IntVar("0")
            var5 = IntVar("0")
            var6 = IntVar("0")
            var7 = IntVar("0")
            var8 = IntVar("0")
            var9 = IntVar("0")
            var10 = IntVar("0")
            var11 = StringVar("0")
            var12 = StringVar("0")
            var13 = StringVar("0")

            self.cboDeparture.current(0)
            self.cboDestination.current(0)
            self.cboAccommodation.current(0)

            self.txtAirporTax.configure(state = DISABLED)
            self.txtMile.configure(state = DISABLED)
            self.txtTravelling_Insurance.configure(state = DISABLED)
            self.txtExtLuggage.configure(state = DISABLED)

            self.txtStandard.configure(state = DISABLED)
            self.txtEconomy.configure(state = DISABLED)
            self.txtFirstClass.configure(state = DISABLED)
        
        def Receipt():
            self.txtReceipt.delete("1.0",END)  
            x=random.randint(10853, 500831)  
            randomRef = str(x)
            Receipt_Ref.set("Travel Bill: " + randomRef)

            self.txtReceipt.insert(END,'Receipt Ref:\t\t\t\t\t' + Receipt_Ref.get() + "\n") 
            self.txtReceipt.insert(END,'Date Ref:\t\t\t\t\t' + DateofOrder.get() + "\n")  
            self.txtReceipt.insert(END,'Flight:\t\t\t\t\t' + "Travelling Details \n")  
            self.txtReceipt.insert(END,'Firstname:\t\t\t\t\t' + Firstname.get() + "\n")  
            self.txtReceipt.insert(END,'Surname:\t\t\t\t\t' + Surname.get() + "\n")  
            self.txtReceipt.insert(END,'Address:\t\t\t\t\t' + Address.get() + "\n") 
            self.txtReceipt.insert(END,'PostCode:\t\t\t\t\t' + PostCode.get() + "\n")  
            self.txtReceipt.insert(END,'Telephone:\t\t\t\t\t' + Telephone.get() + "\n")  
            self.txtReceipt.insert(END,'Mobile:\t\t\t\t\t' + Mobile.get() +"\n")  
            self.txtReceipt.insert(END,'Email:\t\t\t\t\t' + Email.get() + "\n")  
            self.txtReceipt.insert(END,'Standard:\t\t\t\t\t' + var11.get() + "\n")  
            self.txtReceipt.insert(END,'Economy:\t\t\t\t\t' + var12.get() + "\n") 
            self.txtReceipt.insert(END,'FirstClass:\t\t\t\t\t' + var13.get() + "\n")  
            self.txtReceipt.insert(END,'Standard:\t\t\t\t\t' + Standard.get() + "\n")  
            self.txtReceipt.insert(END,'Economy:\t\t\t\t\t' + Economy.get() + "\n") 
            self.txtReceipt.insert(END,'FirstClass:\t\t\t\t\t' + FirstClass.get() + "\n")  
            self.txtReceipt.insert(END,'Paid:\t\t\t\t\t' + PaidTax.get() + "\n")  
            self.txtReceipt.insert(END,'SubTotal:\t\t\t\t\t' + SubTotal.get() + "\n") 
            self.txtReceipt.insert(END,'TotalCost:\t\t\t\t\t' + TotalCost.get()) 
                
        def Airport_Tax():
            global paid1
            if(var1.get() == 1):
                self.txtAirportTax.configure(state = NORMAL)
                Item1=float(45)

                AirporTax.set("$" + str(Item1))
                paid1 = AirporTax.get()
                AirporTax.set("$" +str(Item1))
            elif var1.get()==0:
                self.txtAirportTax.configure(state = DISABLED)
                AirporTax.set("0")
        def Mileage():
            global Item2
            if(var2.get() == 1):
                self.txtMile.configure(state = NORMAL)
                Item2=(23345)
                Mile.set((Item2))
        
            elif(var1.get()==0):
                self.txtMile.configure(state = DISABLED)
                Mile.set("0")

        def Travelling():
            global Item3
            if(var3.get() == 1):
                self.txtTravelling_Insurance.configure(state = NORMAL)
                Item3=float(63)
                Travel_Ins.set("$" + str(Item3))
              
            elif(var3.get()==0):
                self.txtTravelling_Insurance.configure(state = DISABLED)
                Travel_Ins.set("0")

        def Lug():
            global Item4
            if(var4.get() == 1):
                self.txtExt_Luggage.configure(state = NORMAL)
                Item4=float(334.59)
                Luggage.set("$" + str(Item4))
              
            elif(var4.get()==0):
                self.txtExt_Luggage.configure(state = DISABLED)
                Luggage.set("0")
 
        def Standard_Fees():
              global Item5
              if(var5.get() == 1):
                self.txtStandard.configure(state = NORMAL)
                Item5=float(274.9)
                Standard.set("$" + str(Item5))
              
              elif(var5.get()==0):
                self.txtStandard.configure(state = DISABLED)
                Standard.set("0")
 
        def Economy_Fees():
             global Item6
             if(var7.get() == 1):
                self.txtEconomy.configure(state = NORMAL)
                Item6=float(365.5)
                Economy.set("$" + str(Item5))
        
             elif(var7.get()==0):
                self.txtEconomy.configure(state = DISABLED)
                Economy.set("0")

        def FirstClass_Fees():
            global Item7
            if(var9.get() == 1):
                self.txtFirstClass.configure(state = NORMAL)
                Item7=float(564.3)
                FirstClass.set("$" + str(Item5))
              
            elif(var9.get()==0):
                self.txtFirstClass.configure(state = DISABLED)
                FirstClass.set("0")

    
        def Total_Paid(): 
              if (var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 
                  and var5.get() == 1 and var11.get() == "Heathrow" and var12.get() =="Paris"
                  and var13.get() =="1"):

                    q1 = float(45)
                    q2 = float(63)   
                    q3 = float(334.59)
                    q4 = float(274.90) 

                    Cost_of_Fare = q1 + q2 + q3 + q4

                    Tax = "$" + str('%.2f'%((Cost_of_Fare) *0.09)
                    ST =  "$"  + str('%.2f'%((Cost_of_Fare)))
                    TT = "$"  + str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))  

                    PaidTax.set(Tax)
                    SubTotal.set(ST)
                    TotalCost.set(TT) 
                                           
            elif (var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 
              and var7.get() == 1 and var11.get() == "Heathrow" and var12.get() =="Paris"
              and var13.get() =="L"):

                    q1 = float(45)
                    q2 = float(63)   
                    q3 = float(334.59)
                    q4 = float(274.90) 

                    Cost_of_Fare = q1 + q2 + q3 + q4

                    Tax = "$" + str('%.2f'%((Cost_of_Fare) *0.09 )
                    ST = "$" + str('%.2f'%((Cost_of_Fare))) 
                    TT = "$" + str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))  

                    PaidTax.set(Tax)
                    SubTotal.set(ST)
                    TotalCost.set(TT)  
                                          
             elif (var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 
                  and var7.get() == 1 and var11.get() == "Heathrow" and var12.get() =="Morocco"
                  and var13.get() =="L"):

                    q1 = float(45)
                    q2 = float(63)   
                    q3 = float(334.59)
                    q4 = float(365.90) 

                    Cost_of_Fare = q1 + q2 + q3 + q4

                    Tax = "$" + str('%.2f'%((Cost_of_Fare) *0.09)
                    ST = "$" + str('%.2f'%((Cost_of_Fare))) 
                    TT = "$" + str('%.2f'%(Cost_of_Fare + ((Cost_of_Fare)*0.09)))  

                    PaidTax.set(Tax)
                    SubTotal.set(ST)
                    TotalCost.set(TT)  
#========================================================================================================================
        MainFrame = Frame(self.root)
        MainFrame.grid()
        
        Tops = Frame(MainFrame , bd = 20 , width = 1350 , relief = RIDGE)
        Tops.pack(side = TOP)
        self.lblTitle = Label(Tops , font=('arial' , 70 , 'bold') , text = " Travel Planner Application ")
        self.lblTitle.grid()
        
        CustomerDetailsFrame = LabelFrame(MainFrame , width = 1450 , height= 500 , bd = 20 , pady = 5, relief = RIDGE)
        CustomerDetailsFrame.pack(side = BOTTOM)
        
        FrameDetails = Frame(CustomerDetailsFrame , width = 880 , height= 400 , bd = 10 , relief = RIDGE)
        FrameDetails.pack(side = LEFT)
        
        CustomerName = LabelFrame(FrameDetails , width = 150 , height= 250 , bd = 20 ,
                                  font=('arial' , 20 , 'bold') , text ="Customer Name" , relief = RIDGE)
        CustomerName.grid(row = 0 , column = 0)
        
        TravelFrame = LabelFrame(FrameDetails , bd = 10 , width = 300 , height= 250 ,
                                  font=('arial' , 20 , 'bold') , text ="Travel Details" , relief = RIDGE)
        TravelFrame.grid(row = 0 , column = 1)
        
        Ticket_Frame = LabelFrame(FrameDetails , width = 300 , height= 250 , relief = FLAT)
        Ticket_Frame.grid(row = 1 , column = 0)
        
        CostFrame = LabelFrame(FrameDetails , width = 150 , height= 250 , relief = FLAT)
        CostFrame.grid(row = 1 , column = 1)
        
        Receipt_ButtonFrame = Frame(CustomerDetailsFrame , bd = 10 , width = 450 , height= 400 , relief = RIDGE)
        Receipt_ButtonFrame.pack(side = RIGHT)
        
        ReceiptFrame = LabelFrame(Receipt_ButtonFrame , width = 350 , height= 400 , 
                                  font=('arial' , 20 , 'bold') , text ="Receipt" , relief = RIDGE)
        ReceiptFrame.grid(row = 0 , column = 0)
        
        ButtonFrame = LabelFrame(Receipt_ButtonFrame , width = 350 , height= 100 , relief = RIDGE)
                                   
        ButtonFrame.grid(row = 1 , column = 0)
        
#=============================================CustomerName====================================================================
        self.lblFirstname = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "FirstName" , bd = 7)
        self.lblFirstname.grid(row = 0 , column = 0 , sticky = W)
        
        self.txtFirstname = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Firstname
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtFirstname.grid(row = 0 , column = 1)
        
        self.lblSurname = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "SurName" , bd = 7)
        self.lblSurname.grid(row = 1 , column = 0 , sticky = W)
        
        self.txtSurname = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Surname
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtSurname.grid(row = 1 , column = 1)
        
        self.lblAddress = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Address" , bd = 7)
        self.lblAddress.grid(row = 2 , column = 0 , sticky = W)
        
        self.txtAddress = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Address
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtAddress.grid(row = 2 , column = 1)
        
        self.lblPostCode = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "PostCode" , bd = 7)
        self.lblPostCode.grid(row = 3 , column = 0 , sticky = W)
        
        self.txtPostCode = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = PostCode
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtPostCode.grid(row = 3 , column = 1)
        
        self.lblTelephone = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Telephone" , bd = 7)
        self.lblTelephone.grid(row = 4 , column = 0 , sticky = W)
        
        self.txtTelephone = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Telephone
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtTelephone.grid(row = 4 , column = 1)
        
        self.lblMobile = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Mobile" , bd = 7)
        self.lblMobile.grid(row = 5 , column = 0 , sticky = W)
        
        self.txtMobile = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Mobile
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtMobile.grid(row = 5 , column = 1)
        
        self.lblEmail = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Email" , bd = 7)
        self.lblEmail.grid(row = 6 , column = 0 , sticky = W)
        
        self.txtEmail = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Email
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtEmail.grid(row = 6 , column = 1)
#=============================================Flight Information==============================================================
        self.lblDeparture = Label(TravelFrame , font=('arial' , 14 , 'bold') , text = "Departure" , bd = 7)
        self.lblDeparture.grid(row = 0 , column = 0 , sticky = W)
        
        self.cboDeparture = ttk.Combobox(TravelFrame , textvariable = var11 , state = 'readonly' , 
                                         font=('arial' , 20 , 'bold') , width = 14)
        self.cboDeparture['value'] = ('' , 'Heathrow' , 'Lagos MM' , 'DFW' , 'Luton')
        self.cboDeparture.current(0)
        self.cboDeparture.grid(row = 0 , column = 1)
        
        self.lblDestination = Label(TravelFrame , font=('arial' , 14 , 'bold') , text = "Destination" , bd = 7)
        self.lblDestination.grid(row = 1 , column = 0 , sticky = W)
        
        self.cboDestination = ttk.Combobox(TravelFrame , textvariable = var12 , state = 'readonly' , 
                                         font=('arial' , 20 , 'bold') , width = 14)
        self.cboDestination['value'] = ('' , 'Oslo' , 'Dublin' , 'Paris' , 'Kenya')
        self.cboDestination.current(0)
        self.cboDestination.grid(row = 1 , column = 1)
        
        self.lblAccommodation = Label(TravelFrame , font=('arial' , 14 , 'bold') , text = "Accommodation" , bd = 7)
        self.lblAccommodation.grid(row = 2 , column = 0 , sticky = W)
        
        self.cboAccommodation = ttk.Combobox(TravelFrame , textvariable = var13 , state = 'readonly' , 
                                         font=('arial' , 20 , 'bold') , width = 14)
        self.cboAccommodation['value'] = ('' , '1' , '2' , '3' , '4')
        self.cboAccommodation.current(0)
        self.cboAccommodation.grid(row = 2 , column = 1)
        
        self.chkAirportTax = Checkbutton(TravelFrame , text = 'Airport Tax' , variable = var1 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command = AirporT_Tax).grid(row = 3 , column = 0 , sticky = W)
        
        self.txtAirportTax = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = AirportTax
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtAirportTax.grid(row = 3 , column = 1)
        
        self.chkMile = Checkbutton(TravelFrame , text = 'Air Mile' , variable = var1 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command = Mileage).grid(row = 4 , column = 0 , sticky = W)
        
        self.txtMile = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Mile
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtMile.grid(row = 4 , column = 1)
        
        self.chkTravel_Ins = Checkbutton(TravelFrame , text = 'Travelling Insurance' , variable = var1 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command = Travelling).grid(row = 5 , column = 0 , sticky = W)
        
        self.txtTravel_Ins = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Travel_Ins
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtTravel_Ins.grid(row = 5 , column = 1)
        
        self.chkLuggage = Checkbutton(TravelFrame , text = 'Ext.Luggage' , variable = var1 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command = Lug).grid(row = 6 , column = 0 , sticky = W)
        
        self.txtLuggage = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Luggage
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtLuggage.grid(row = 6 , column = 1)
#=============================================Payment Information==============================================================
        self.lblPaidTax = Label(CostFrame , font=('arial' , 14 , 'bold') , text = "PaidTax" , bd = 7)
        self.lblPaidTax.grid(row = 0 , column = 2 , sticky = W)
        
        self.txtPaidTax = Entry(CostFrame , font=('arial' , 14 , 'bold')  , textvariable = PaidTax
                                  , bd = 7 , width = 26 , justify = RIGHT)
        self.txtPaidTax.grid(row = 0 , column = 3)
        
        self.lblSubTotal = Label(CostFrame , font=('arial' , 14 , 'bold') , text = "SubTotal" , bd = 7)
        self.lblSubTotal.grid(row = 1 , column = 2 , sticky = W)
        
        self.txtSubTotal = Entry(CostFrame , font=('arial' , 14 , 'bold')  , textvariable = SubTotal
                                  , bd = 7 , width = 26 , justify = RIGHT)
        self.txtSubTotal.grid(row = 1 , column = 3)
        
        self.lblTotalCost = Label(CostFrame , font=('arial' , 14 , 'bold') , text = "TotalCost" , bd = 7)
        self.lblTotalCost.grid(row = 2 , column = 2 , sticky = W)
        
        self.txtTotalCost = Entry(CostFrame , font=('arial' , 14 , 'bold')  , textvariable = TotalCost
                                  , bd = 7 , width = 26 , justify = RIGHT)
        self.txtTotalCost.grid(row = 2 , column = 3)


        self.chkStandard = Checkbutton(Ticket_Frame , text = 'Standard' , variable = var5 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command=Standard_Fees).grid(row = 0 , column = 0 , sticky = W)
        
        self.txtStandard = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Standard
                                  , bd = 7 , width = 6 , state = DISABLED , justify = RIGHT)
        self.txtStandard.grid(row = 0 , column = 1)
        
        self.chkSingle = Checkbutton(Ticket_Frame , text = 'Single' , variable = var6 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold')).grid(row = 0 , column = 2 , sticky = W)
        
        
        self.chkEconomy = Checkbutton(Ticket_Frame , text = 'Economy' , variable = var7 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command=Economy_Fees).grid(row = 1 , column = 0 , sticky = W)
        
        self.txtEconomy = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Economy
                                  , bd = 7 , width = 6 , state = DISABLED , justify = RIGHT)
        self.txtEconomy.grid(row = 1 , column = 1)
        
        
        self.chkReturn = Checkbutton(Ticket_Frame , text = 'Return' , variable = var8 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold')).grid(row = 1 , column = 2 , sticky = W)
        
        self.chkFirstClass = Checkbutton(Ticket_Frame , text = 'FirstClass' , variable = var9 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command=FirstClass_Fees).grid(row = 2 , column = 0 , sticky = W)
        
        self.txtFirstClass = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = FirstClass
                                  , bd = 7 , width = 6 , state = DISABLED , justify = RIGHT)
        self.txtFirstClass.grid(row = 2 , column = 1)
        
        self.chkSpecialNeeds = Checkbutton(Ticket_Frame , text = 'SpecialNeeds' , variable = var10 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold')).grid(row = 2 , column = 2 , sticky = W)
        
#================================================Receipt========================================================================
        self.txtReceipt = Text(ReceiptFrame , width = 60 , height = 21 ,font=('arial' , 16 , 'bold'))
        self.txtReceipt.grid(row=0,column=0)
      
#================================================Buttons======================================================================
       self.btnTotal=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4, 
                            text='Total',command=Total_Paid).grid(row=0,column=0)
                                
       self.btnReceipt=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4, 
                            text='Receipt', command=Receipt).grid(row=0,column=1)
                                
       self.btnReset=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4, 
                            text='Reset', command=Reset).grid(row=0,column=2)
                                
       self.btnExit=Button(ButtonFrame, padx=18, bd=7,font=('arial', 16,'bold'), width=4, 
                            text='Exit', command=iExit).grid(row=0,column=3)

if __name__ == "__main__":
    root = Tk()
    application = Travel(root)
    root.mainloop()