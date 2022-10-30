import os
os.system('cls')

import math
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

slot = ["slot"]*5
arr_karcis_motor = [] 
arr_karcis_mobil = []
waktu_mulai_mobil = []
waktu_mulai_motor = []
arr_reservasi = []
arr_check_reservasi = []
arr_keluar_motor = []
arr_keluar_mobil = []

win = Tk()
win.title("PARKING MANAGEMENT SYSTEM")
win.configure(bg = "light blue" )
win.geometry ("800x500")

def parkingmanagementsystem():
    window =Tk()
    window.title("MAIN MENU")
    window.geometry("800x500")
    window.configure(bg = "light blue")

    def reservasiparkir() :
        global slot
        print(f"slot parkir sekarang ada {len(slot)}")
        if len(slot)> 0:
            window = Tk()
            window.title("RESERVASI PARKIR")
            window.geometry ("800x500")
            window.configure(bg = "light yellow")
            window.resizable(False, False)
            def win1():
                def jumlah() :
                    a = int(jam_mulai.get())
                    b = int(menit_mulai.get())
                    c = int(jam_akhir.get())
                    d = int(menit_akhir.get())
                    selisih = (c*60+d)-(a*60+b)
                    jamselisih = selisih/60
                    akhir= (math.ceil(jamselisih))*8000
                    windowx = Toplevel()
                    windowx.title("PEMBAYARAN")
                    windowx.geometry("800x500")
                    windowx.configure(bg = "light yellow")
                    label = Label(windowx, background="#FAC898", text=f"Tolong Bayar Sebesar {akhir}", font = ("timesnewroman", 10, "bold"))
                    label.place(x = 200, y = 200)
                    nominal = ttk.Entry(windowx)
                    nominal.place(x = 500, y = 200 )
                    def kode():
                        k = int(nominal.get())
                        if k >= akhir:
                            window2 = Toplevel()
                            window2.title("Kode Karcis")
                            window2.configure(bg = "light yellow")
                            window2.geometry("400x250")
                            import datetime
                            x = datetime.datetime.now()
                            z = f"X{x.hour*3600+x.minute*60+x.second}"
                            label_k_r = Label(window2, background = "light yellow", text = f"Kode Karcis Anda Adalah", font=("timesnewroman", 9, "bold"))
                            label_k_r.place(x = 125, y = 20)
                            label_k_r_1 = Label(window2, background = "light yellow", text = z, font=("timesnewroman", 30, "bold") )
                            label_k_r_1.place(x = 125, y = 70)
                            label_kr2 = Label(window2, background ="lightyellow", text = "Mohon Simpan dengan baik", font = ("timesnewroman", 9, "bold"))
                            label_kr2.place(x = 125, y = 150 )
                            arr_reservasi.append(z)
                            print(f"kode reservasi : {arr_reservasi}")
                            def penutup():
                                global slot
                                window3 = Toplevel()
                                window3.title("PENUTUP")
                                window3.geometry("400x250")
                                window3.configure(bg = "light yellow")
                                label_penutup = Label(window3, background = "light yellow", text = "TERIMAKASIH SUDAH \n MENGGUNAKAN LAYANAN KAMI", font=("timesnewroman", 14, "bold"))
                                label_penutup.place(x = 40, y = 80)
                                slot.pop()
                                print(f"slot parkir sekarang ada {len(slot)}")

                            btn_next = Button(window2, text = "Next", background = "#FAC898", font = ("timesnewroman", 9 , "bold"),command = lambda: [penutup(), window2.destroy()])
                            btn_next.place(x = 175, y = 200)

                        elif k < akhir:
                            showinfo(message="Maaf, Uang yang Anda berikan tidak cukup")

                    btn_byr = Button (windowx, text = "BAYAR", font = ("timesnewroman", 9 , "bold"), command = kode, background = "#FAC898")
                    btn_byr.place(x= 385, y =250 )

                window1 = Toplevel()
                window1.title("WAKTU")
                window1.geometry ("800x500")
                window1.configure(bg = "light yellow")
                label_1 = Label(window1, text = "Masukkan Waktu Jam Anda Mulai Masuk", background = "#FAC898", font = ("timesnewroman", 9, "bold"))
                label_1.place(x = 300 , y = 50)
                jam_mulai = ttk.Entry(window1)
                jam_mulai.place(x = 350 ,y = 100)
                label_2 = Label(window1, text = "Masukkan Waktu Menit Anda Mulai Masuk", background = "#FAC898", font = ("timesnewroman", 9, "bold"))
                label_2.place(x = 300 ,y = 150)
                menit_mulai = ttk.Entry(window1)
                menit_mulai.place(x = 350 ,y = 200)
                label_3 = Label(window1, text = "Masukkan Waktu Jam Anda Akan Keluar", background = "#FAC898", font = ("timesnewroman", 9, "bold"))
                label_3.place(x = 300 ,y = 250)
                jam_akhir = ttk.Entry(window1)
                jam_akhir.place(x = 350 ,y = 300)
                label_4 = Label(window1, text = "Masukkan Waktu Menit Anda akan Keluar", background = "#FAC898", font = ("timesnewroman", 9, "bold") )
                label_4.place(x = 300 ,y = 350)
                menit_akhir = ttk.Entry(window1)
                menit_akhir.place(x = 350 ,y = 400)
                btn_submit = Button(window1, text="NEXT", font = ("timesnewroman", 9 , "bold"), command= lambda: [jumlah(), window1.destroy()], background = "#FAC898")
                btn_submit.place(x = 385 ,y = 450)

                buttonjumlah = Button(window1, text = "Next", font = ("timesnewroman", 9 , "bold"), command = lambda: [jumlah(), window1.destroy()])
                buttonjumlah.pack

            button1 = Button(window, text = "SELAMAT DATANG DI LAYANAN RESERVASI KAMI \n \n SILAKAN KLIK UNTUK MEMESAN", background = "#FAC898", font = ("timesnewroman", 9, "bold") ,   command = lambda: [win1(), window.destroy()])
            button1.place(width=300, x = 250, y = 150, height= 100)
        
        if len(slot) == 0:
            showinfo(message = "MAAF SLOT PARKIR SUDAH PENUH")


    def masukparkir():
        window =Tk()
        window.title("PARKIR")
        window.configure(background="light green")
        window.geometry("800x500")

        def darurat():
            window1 = Toplevel()
            window1.title("DARURAT")
            window1.geometry("500x300")
            window1.configure(bg = "light green")
            window1.resizable(False,False)
            btn11 = Label(window1, text = "HARAP TUNGGU \n PETUGAS DATANG", font=('timesnewroman',20, 'bold'), bg="light green")
            btn11.pack(pady=120)
        
        def khusus_reservasi():
            windowx = Toplevel()
            windowx.title("GATE KHUSUS RESERVASI")
            windowx.geometry("500x500")
            windowx.configure(bg = "light green")
            def checking():
                a = kode_reservasi.get()
                arr_check_reservasi.append(a)
                for i in arr_reservasi:
                    if i in arr_check_reservasi:
                        arr_check_reservasi.remove(i)
                        arr_reservasi.remove(i)
                        print(arr_check_reservasi)
                        print(arr_reservasi)
                        root = Toplevel()
                        root.geometry("200x200")
                        root.configure(bg = "light green")
                        root.title("MASUK")
                        button = Label (root, text = "PALANG TERBUKA \n SILAKAN MASUK", font = ("timesnewroman", 9, "bold") )
                        button.pack(pady = 50)
                    else:
                        showinfo (message = "Karcis yang dimasukkan tidak valid")

            lbl_khusus = Label(windowx, text = "Masukkan Kode Reservasi Anda", font = ("timesnewroman", 9, "bold"), background = "light green")
            lbl_khusus.place (x =80, y = 100) 
            kode_reservasi = ttk.Entry(windowx)
            kode_reservasi.place(x = 300, y = 100)
            btn_submit = Button(windowx, text = "Submit", font = ("timesnewroman", 9 , "bold") ,command = lambda: [checking(), windowx.destroy()])
            btn_submit.place(x = 230, y = 150)

        def karcis():
            if len(slot)> 0:
                window2 = Toplevel()
                window2.title ("AMBIL KARCIS")
                window2.geometry ("800x500")
                window2.configure(bg = "light green")
                def mobil():
                    window21 = Toplevel()
                    window21.title("KARCIS MOBIL")
                    window21.geometry("400x250")
                    window21.configure(bg = "light green")
                    import datetime
                    x = datetime.datetime.now()
                    waktu_mulai_mobil = x.hour*3600+x.minute*60+x.second
                    lbl210 = Label(window21, text = "silakan ambil karcis anda", bg ="light green" , font= ("timesnewroman", 10, "bold")) 
                    lbl210.pack(pady=20)
                    lbl211 = Label(window21, text = waktu_mulai_mobil, bg="light green", font=("timesnewroman", 30, "bold"))
                    lbl211.pack(pady = 15)
                    arr_karcis_mobil.append(waktu_mulai_mobil)

                    def bukapalang():
                        global slot
                        window221 = Toplevel()
                        window221.title("PALANG TERBUKA")
                        window221.geometry ("200x200")
                        window221.configure(bg = "light green")
                        btn31 = ttk.Button(window221,text = "PALANG TERBUKA \n SILAKAN MASUK!")
                        btn31.pack(pady = 50)

                        slot.pop()
                        print(f"slot parkir sekarang ada {len(slot)}")
                        print(f"karcis masuk mobil adalah {arr_karcis_mobil}")
                

                    btn212 = ttk.Button(window21, text = "CONTINUE", command = lambda : [bukapalang(), window21.destroy()] )
                    btn212.pack()
                frame=Frame(window2,bg="grey",relief=RAISED,borderwidth=3, height=50, width=50)
                frame.pack(pady=200)
                btn_mobil = Button(frame, text="MOBIL", font=10, command = lambda: [mobil(), window2.destroy()])
                btn_mobil.pack(side=LEFT, padx=3, pady=3)

                def motor():
                    window22 = Toplevel()
                    window22.title("KARCIS MOTOR")
                    window22.geometry("400x250")
                    window22.configure(bg = "light green")
                    import datetime
                    x = datetime.datetime.now()
                    waktu_mulai_motor = x.hour*3600+x.minute *60+ x.second
                    label22 = Label (window22, text = "silakan ambil karcis anda", bg ="light green" , font= ("timesnewroman", 10, "bold"))
                    label22.pack(pady= 20)
                    label221 = Label(window22, text = waktu_mulai_motor, bg="light green", font=("timesnewroman", 30, "bold"))
                    label221.pack(pady=15)
                    arr_karcis_motor.append(waktu_mulai_motor)
                    def bukapalang():
                        global slot
                        window221 = Toplevel()
                        window221.title("PALANG TERBUKA")
                        window221.geometry ("200x200")
                        window221.configure(bg = "light green")
                        btn31 = ttk.Button(window221,text = "PALANG TERBUKA \n SILAKAN MASUK!",command = window22.destroy)
                        btn31.pack(pady=50)

                        slot.pop()
                        print(f"slot parkir sekarang ada {len(slot)}")
                        print(f"karcis masuk motor {arr_karcis_motor}")

                    btn222 = ttk.Button (window22, text = "CONTINUE", command = lambda : [bukapalang(), window22.destroy()] )
                    btn222.place(x=160, y= 150)
                btn_motor = Button(frame, text="MOTOR", font=10, command = lambda : [motor(), window2.destroy()])
                btn_motor.pack(side=RIGHT, padx=3, pady=3)
            elif len(slot) == 0:
                showinfo(message = "MAAF SLOT PARKIR SUDAH PENUH")

        bingkai = Frame(window,bg="dark green",relief=GROOVE,borderwidth=3, height=500, width=510)
        bingkai.place(x=250, y=150)
        btn01 = Button(bingkai, text = "TOMBOL DARURAT", font=10,relief=RAISED, borderwidth=5,width=30,command = lambda: [darurat(), window.destroy()])
        btn01.pack(pady=2, padx=2)
        btn02 = Button(bingkai, text = "TEKAN UNTUK AMBIL KARCIS",relief=RAISED, borderwidth=5,font=10, width=30,command = lambda : [karcis(), window.destroy()])
        btn02.pack(pady=2, padx=2)
        btn03 = Button(bingkai, text = "GATE KHUSUS RESERVASI",relief=RAISED, borderwidth=5,font=10, width=30,command = lambda:  [khusus_reservasi(), window.destroy()])
        btn03.pack(pady=2, padx=2)
        

    def keluarparkir():
        window = Tk()
        window.geometry("800x500")
        window.title("KELUAR PARKIR")
        window.configure(bg = "#CBC3E3")

        def darurat():
            top = Toplevel()
            top.title("DARURAT")
            top.geometry("500x300")
            top.configure(bg= "#CBC3E3")
            btn11 = Label(top, text = "HARAP TUNGGU \n PETUGAS DATANG", font = ("timesnewroman", 20, "bold"), background = "#CBC3E3")
            btn11.pack(pady = 100)

        def keluarmobil():
            window11 = Toplevel()
            window11.title("KELUAR MOBIL")
            window11.geometry("800x500")
            window11.configure(bg = "#CBC3E3")
            def getmobil():
                a = int(karcis_mobil.get())
                arr_keluar_mobil.append(a)
                print(arr_keluar_mobil)
                print(arr_karcis_mobil)
                for i in arr_karcis_mobil:
                    if i in arr_keluar_mobil:
                        copy_mobil = 0
                        copy_mobil += i
                        arr_keluar_mobil.remove(i)
                        arr_karcis_mobil.remove(i)
                        window2 = Toplevel()
                        window2.title ("GATE MOBIL")
                        window2.geometry ("400x250")
                        window2.configure(bg = "#CBC3E3")
                        label = Label(window2, text = "KARCIS TERKONFIRMASI", font = ("timesnewroman", 9, "bold"))
                        label.place(x = 130, y = 100)
                        def bayar():
                            global slot
                            window3 = Toplevel()
                            window3.title("PEMBAYARAN")
                            window3.geometry("800x500")
                            window3.configure(bg = "#CBC3E3")
                            import datetime
                            x = datetime.datetime.now()
                            waktukeluar = x.hour*3600 + x.minute*60 + x.second
                            import math
                            a = (waktukeluar-copy_mobil)/3600
                            b = math.ceil(a)
                            tarifkeluarmobil = b*4000
                            label2 = Label(window3, text = f"Mohon membayar sebanyak Rp{tarifkeluarmobil}", background = "#CBC3E3")
                            label2.place(x =200, y =200)
                            byr = ttk.Entry(window3)
                            byr.place(x = 500, y = 200)
                            def penutupmobil():
                                global slot
                                a =int (byr.get())
                                if a >=tarifkeluarmobil:
                                    screen = Toplevel()
                                    screen.title ("Penutup")
                                    screen.geometry("400x250")
                                    screen.configure(bg = "#CBC3E3")
                                    labelll = Label (screen, text = "PALANG TERBUKA \n SILAKAN KELUAR!", font = ("timesnewroman", 15, "bold"), background = "#CBC3E3")
                                    labelll.pack()
                                    slot.append("slot")
                                    print(f"sekarang slot masih tersisa {len(slot)}")

                                elif a < tarifkeluarmobil:
                                    showinfo(message = "Maaf, Uang Yang Anda Berikan Kurang.")


                            button_bayar = ttk.Button(window3, text="BAYAR", command = penutupmobil )
                            button_bayar.place(x= 350 , y = 300)

                        buttonbayar = ttk.Button(window2, text = "LANJUTKAN", command= bayar)
                        buttonbayar.place(x =160, y = 125)

            karcis_mobil = ttk.Entry(window11)
            karcis_mobil.place(x = 350, y = 150)
            btn11 = Button(window11, text= "Submit Nomor karcis", font = ("timesnewroman", 10, "bold"), command = getmobil)
            btn11.place(x =340, y = 200)

        def keluarmotor():
            window12 = Toplevel()
            window12.title("KELUAR MOTOR")
            window12.geometry("800x500")
            window12.configure(bg = "#CBC3E3")
            def getmotor():
                a = int(karcis_motor.get())
                arr_keluar_motor.append(a)
                print("keluar",arr_keluar_motor)
                print("masuk",arr_karcis_motor)
                for i in arr_karcis_motor:
                    if i in arr_keluar_motor:
                        copy_motor = 0
                        copy_motor += i
                        arr_keluar_motor.remove(i)
                        arr_karcis_motor.remove(i)
                        window2 = Toplevel()
                        window2.title ("GATE MOTOR")
                        window2.geometry ("400x250")
                        window2.configure(bg = "#CBC3E3")
                        label = Label(window2, text = "KARCIS TERKONFIRMASI", font = ("timesnewroman", 9, "bold"))
                        label.place(x = 130, y = 100)
                        def bayar():
                            window3 = Toplevel()
                            window3.title("PEMBAYARAN")
                            window3.geometry("800x500")
                            window3.configure(bg = "#CBC3E3")
                            import datetime
                            x = datetime.datetime.now()
                            waktukeluar = x.hour*3600 + x.minute*60 + x.second
                            import math
                            a = (waktukeluar-copy_motor)/3600
                            b = math.ceil(a)
                            tarifkeluarmotor = b*2000
                            label2 = Label(window3, text = f"Mohon membayar sebanyak Rp{tarifkeluarmotor}", background ="#CBC3E3" )
                            label2.place(x =200, y =200)
                            byar = ttk.Entry(window3)
                            byar.place(x = 500, y = 200)
                            
                            def penutupmotor():
                                global slot
                                a =int (byar.get())
                                if a >=tarifkeluarmotor:
                                    screen = Toplevel()
                                    screen.title ("Penutup")
                                    screen.geometry("400x250")
                                    screen.configure(bg = "#CBC3E3")
                                    labell = Label (screen, text = "PALANG TERBUKA \n SILAKAN KELUAR!", font = ("timesnewroman", 15, "bold"), background = "#CBC3E3")
                                    labell.pack()
                                    slot.append("slot")
                                    print(f"sekarang slot masih tersisa {len(slot)}")
                                elif a < tarifkeluarmotor:
                                    showinfo(message = "Maaf, Uang Yang Anda Berikan Kurang.")

                            button_bayar = ttk.Button(window3, text="BAYAR", command = penutupmotor )
                            button_bayar.place(x= 350 , y = 300)
                        buttonbayar = ttk.Button(window2, text = "LANJUTKAN", command= bayar)
                        buttonbayar.place(x = 160, y = 125)
                    else:
                        showinfo(message = "Maaf, Karcis Yang Dimasukkan Tidak Ada Di Daftar")

            karcis_motor= ttk.Entry(window12)
            karcis_motor.place(x = 350, y = 150)
            btn12 = Button(window12, text= "Submit Nomor karcis", command =getmotor, font = ("timesnewroman", 10 , "bold"))
            btn12.place(x = 340, y = 200)
            
        def keluar_reservasi():
            window4 = Toplevel()
            window4.title("GATE KHUSUS RESERVASI")
            window4.geometry("400x250")
            window4.configure(bg = "#CBC3E3")
            def palangterbuka():
                window41 = Toplevel()
                window41.title("SILAKAN KELUAR")
                window41.geometry("400x250")
                window41.configure(bg = "#CBC3E3")
                buttonnn = Label(window41, text = "PALANG TERBUKA \n SILAKAN KELUAR!", font = ("timesnewroman", 15, "bold"), background = "#CBC3E3" )
                buttonnn.pack(pady = 100)
            button4 = ttk.Button(window4, text = "TEKAN UNTUK MEMBUKA PALANG", command = lambda: [palangterbuka(), window4.destroy()])
            button4.pack(pady=100)

        bingkai = Frame(window,bg="#800080",relief=GROOVE,borderwidth=8, height=500, width=510)
        bingkai.place(x=250, y=150)

        btn01 = Button(bingkai, text = "TOMBOL DARURAT", font=10, width= 30,command = lambda: [darurat(), window.destroy()])
        btn01.pack(pady=2, padx=2)
        btn02 = Button (bingkai, text = "GATE KELUAR MOBIL",font=10, width= 30, command = lambda: [keluarmobil(), window.destroy()])
        btn02.pack(pady=2, padx=2)
        btn03 = Button (bingkai, text="GATE KELUAR MOTOR",font=10, width= 30, command = lambda:  [keluarmotor(), window.destroy()])
        btn03.pack(pady=2, padx=2)
        btn04 = Button(bingkai, text = "GATE KHUSUS RESERVASI", font=10, width= 30, command = lambda: [keluar_reservasi(), window.destroy()])
        btn04.pack(pady=2, padx=2)

    def exitMenu() :
        print("Exit")

    frame=Frame(window,bg="grey",relief=RAISED,borderwidth=5, height=200, width=500)
    frame.pack(pady=200)

    first_menu=Menubutton(frame,text="RESERVASI PARKIR", borderwidth=2, font=10)
    first_menu.pack(side=LEFT, padx=3, pady=3)
    first_menu.menu=Menu(first_menu, tearoff=False)
    first_menu.menu.add_command(label="RESERVASI PARKIR",command= lambda : [reservasiparkir(), window.destroy()])
    first_menu.menu.add("separator")
    first_menu.menu.add_command(label="Exit",command= exitMenu)
    first_menu['menu']=first_menu.menu

    second_menu=Menubutton(frame,text="PARKIR MANUAL", borderwidth=2, font=10)
    second_menu.pack(side=RIGHT, padx=3, pady=3)
    second_menu.menu=Menu(second_menu, tearoff=False)
    second_menu.menu.add_command(label="MASUK PARKIR",command= lambda: [masukparkir(), window.destroy()])
    second_menu.menu.add_command(label="KELUAR PARKIR",command= lambda: [keluarparkir(), window.destroy()])
    second_menu.menu.add("separator")
    second_menu.menu.add_command(label="Exit",command = exitMenu)
    second_menu['menu']=second_menu.menu

    Labelele = Label(window, text = "Silahkan Pilih!", font=20, bg="light blue")
    Labelele.place(x=345, y=150)

    window.mainloop()

buttonawal = ttk.Button(win, text = "KLIK UNTUK LANJUTKAN", command = parkingmanagementsystem, width=80)
buttonawal.pack(pady=220)

win.mainloop()


