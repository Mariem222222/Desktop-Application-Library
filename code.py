import tkinter as tk
from tkinter import ttk
import sqlite3
window =tk.Tk()
window.title('Gestion Bibliothèque')
window.geometry("800x400")
mymenu=tk.Menu()
window.config(menu=mymenu)
frame=tk.Frame(window)
frame.pack()
def ajout():
    for widget in frame.winfo_children():
        widget.destroy()
    
###########################################################################################*********SQL

    def enter_data():
        cin= cin_entry.get()
        nom= nom_entry.get()
        prenom= prenom_entry.get()
        netude= netude_box.get()
        section= sec_box.get()
        daten=dateentry.get()
        mail=mailenty.get()
        tel=telentry.get()
        adr=adrentry.get()
        conn = sqlite3.connect('data.db')###
        table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                        (cin TEXT, nom TEXT, prenom TEXT, netude TEXT, section TEXT, 
                        daten TEXT, mail TEXT, tel TEXT, adr TEXT)
                '''
        conn.execute(table_create_query)
                
                # Insert Data
        data_insert_query = '''INSERT INTO Student_Data (cin, nom, prenom, netude, section, 
                        daten, mail, tel , adr) VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        data_insert_tuple = (cin, nom, prenom, netude, section, daten, mail, tel, adr)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

    ##########################################################################################**********E-INFO

    einfo=tk.LabelFrame(frame,text="Info-Eleve")
    einfo.grid(row=0,column=0,padx=20,pady=5)

    ############################################################****CIN

    cin=tk.Label(einfo,text="Numero inscription")
    cin.grid(row=0,column=0)
    cin_entry=tk.Entry(einfo)
    cin_entry.grid(row=1,column=0)

    ############################################################****NOM

    nom=tk.Label(einfo,text="Nom")
    nom.grid(row=0,column=1)
    nom_entry=tk.Entry(einfo)
    nom_entry.grid(row=1,column=1)

    ############################################################****PRENOM

    prenom=tk.Label(einfo,text="prenom")
    prenom.grid(row=0,column=2)
    prenom_entry=tk.Entry(einfo)
    prenom_entry.grid(row=1,column=2)

    ############################################################****NIVEAU_ETUDE

    netude=tk.Label(einfo,text="Niveau étude")
    netude.grid(row=2,column=0)
    netude_box=ttk.Combobox(einfo,values=["","1ere","2eme","3eme"])
    netude_box.grid(row=3,column=0)

    ############################################################****NIVEAU_ETUDE

    sec=tk.Label(einfo,text="Section")
    sec.grid(row=2,column=1)
    sec_box=ttk.Combobox(einfo,values=["","section 1","section 2"])
    sec_box.grid(row=3,column=1)

    ############################################################****Date
    sec=tk.Label(einfo,text="Date de Naissance")
    sec.grid(row=2,column=2)
    dateentry=DateEntry(einfo,selectmode='day')
    dateentry.grid(row=3,column=2,padx=15)


    for widget in einfo.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    ##########################################################################################**********E-COOR

    ecoor=tk.LabelFrame(frame,text="Coordonnées")
    ecoor.grid(row=1,column=0,sticky="news",padx=20,pady=5)

    ############################################################****E-MAIL

    mail=tk.Label(ecoor,text="E-mail")
    mail.grid(row=0,column=0)
    mailenty=tk.Entry(ecoor)
    mailenty.grid(row=1,column=0)

    ############################################################****TELE

    tel=tk.Label(ecoor,text="Telephone")
    tel.grid(row=0,column=1)
    telentry=tk.Entry(ecoor)
    telentry.grid(row=1,column=1)

    ############################################################****ADRESS

    adr=tk.Label(ecoor,text="Adresse")
    adr.grid(row=0,column=2)
    adrentry=tk.Entry(ecoor)
    adrentry.grid(row=1,column=2)
    for widget in ecoor.winfo_children():
        widget.grid_configure(padx=10,pady=5)#

    #########################################################################################***BOTTON

    button=tk.Button(frame,text="Enter data",command=enter_data)
    button.grid(row=2,column=0,sticky="news",padx=20,pady=5)
def ajoutl():
    for widget in frame.winfo_children():
        widget.destroy()
    def enter_data():
        ref= ref_entry.get()
        tit= tit_entry.get()
        noa=noa_entry.get()
        ann= ann_entry.get()
        nbr=nbr_entry.get()
        conn = sqlite3.connect('data.db')###
        table_create_query = '''CREATE TABLE IF NOT EXISTS Livre 
                        (ref TEXT, tit TEXT, noa TEXT, ann TEXT, nbr TEXT)
                '''
        conn.execute(table_create_query)
                
                # Insert Data
        data_insert_query = '''INSERT INTO Livre (ref, tit, noa, ann , nbr) VALUES 
                (?, ?, ?, ?, ?)'''
        data_insert_tuple = (ref, tit, noa, ann , nbr)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

    ##########################################################################################**********E-INFO

    einfo=tk.LabelFrame(frame,text="Info-Livre")
    einfo.grid(row=0,column=0,padx=20,pady=5)

    ############################################################****CIN

    ref=tk.Label(einfo,text="Reference")
    ref.grid(row=0,column=0)
    ref_entry=tk.Entry(einfo)
    ref_entry.grid(row=1,column=0)

    ############################################################****NOM

    tit=tk.Label(einfo,text="Titre")
    tit.grid(row=0,column=1)
    tit_entry=tk.Entry(einfo)
    tit_entry.grid(row=1,column=1)

    ############################################################****PRENOM

    noa=tk.Label(einfo,text="nom et prenom auteur")
    noa.grid(row=0,column=2)
    noa_entry=tk.Entry(einfo)
    noa_entry.grid(row=1,column=2)

    ############################################################****NIVEAU_ETUDE

    ann=tk.Label(einfo,text="Annee edition")
    ann.grid(row=0,column=3)
    ann_entry=tk.Entry(einfo)
    ann_entry.grid(row=1,column=3)

    ############################################################****NIVEAU_ETUDE

    nbr=tk.Label(einfo,text="Nombre d'exemplaires")
    nbr.grid(row=2,column=0)
    nbr_entry=tk.Entry(einfo)
    nbr_entry.grid(row=3,column=0)
    for widget in einfo.winfo_children():
        widget.grid_configure(padx=10,pady=5)

    button=tk.Button(frame,text="Enter data",command=enter_data)
    button.grid(row=2,column=0,sticky="news",padx=20,pady=5)
def find():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Student_Data""")
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    button=tk.Button(frame,text="Lister",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def find1():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Student_Data WHERE cin = ?""",(rec,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="CIN :")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def find2():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Student_Data WHERE section = ?""",(rec,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="section :")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def find3():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        rec1=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Student_Data WHERE section = ? AND netude =?""",(rec,rec1,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="section")
    rec.grid(row=1,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=0,column=0)
    rec1=tk.Label(einfo,text="niveau")
    rec1.grid(row=1,column=1,padx=20,pady=5,ipadx=100)
    rec_entry1=tk.Entry(einfo)
    rec_entry1.grid(row=0,column=1)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def find4():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Student_Data WHERE netude = ?""",(rec,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="Niveau etude")
    rec.grid(row=1,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=0,column=0)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def suppl1():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Livre WHERE tit = ?""",(rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="Livre est supprimer",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="Titre")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="supprimer",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def suppl2():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Livre WHERE noa = ?""",(rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="Livre est supprimer",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="Nom et Prenom de l'auteur")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="supprimer",command=rfind)
def suppl3():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Livre WHERE ann = ?""",(rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="Livre est supprimee",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="annee :")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="supprimer",command=rfind)
def supp1():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec1=rec_entry1.get()
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Student_Data WHERE (nom = ? AND prenom = ?)""",(rec,rec1,))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est supprimer",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="nom")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    rec1=tk.Label(einfo,text="prenom")
    rec1.grid(row=0,column=1,padx=20,pady=5,ipadx=100)
    rec_entry1=tk.Entry(einfo)
    rec_entry1.grid(row=1,column=1)
    button=tk.Button(frame,text="supprimer",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def supp2():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Student_Data WHERE section = ?""",(rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est supprimer",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="section")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=0,column=0)
    button=tk.Button(frame,text="supprimer",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def supp3():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Student_Data WHERE netude = ?""",(rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est supprimer",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="niveau etude")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=0,column=0)
    button=tk.Button(frame,text="supprimer",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def supp4():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec1=rec_entry1.get()
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""DELETE FROM Student_Data WHERE (section = ? AND netude = ?)""",(rec,rec1,))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est supprimer",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="supprimer")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="section")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    rec1=tk.Label(einfo,text="niveau etude")
    rec1.grid(row=0,column=1,padx=20,pady=5,ipadx=100)
    rec_entry1=tk.Entry(einfo)
    rec_entry1.grid(row=1,column=1)
    button=tk.Button(frame,text="supprimer",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def mod1():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        rec1=rec_entry1.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""UPDATE Student_Data SET tel = ? WHERE cin = ?""",(rec1,rec))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est modifier",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="modifier")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="CIN")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    rec1=tk.Label(einfo,text="nouveu numero de telephone")
    rec1.grid(row=0,column=1,padx=20,pady=5,ipadx=100)
    rec_entry1=tk.Entry(einfo)
    rec_entry1.grid(row=1,column=1)
    for widget in einfo.winfo_children():
        widget.grid_configure(padx=10,pady=5)
    button=tk.Button(frame,text="Modifier",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def mod2():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        rec1=rec_entry1.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""UPDATE Student_Data SET mail = ? WHERE cin = ?""",(rec1,rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est modifier",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="modifier")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="CIN")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    rec1=tk.Label(einfo,text="nouveu mail")
    rec1.grid(row=0,column=1,padx=20,pady=5,ipadx=100)
    rec_entry1=tk.Entry(einfo)
    rec_entry1.grid(row=1,column=1)
    for widget in einfo.winfo_children():
        widget.grid_configure(padx=10,pady=5)
    button=tk.Button(frame,text="Modifier",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def mod3():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        rec1=rec_entry1.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute("""UPDATE Student_Data SET adr = ? WHERE cin = ?""",(rec1,rec,))
        e=tk.Label(einfo,width=30,fg='blue',text="etudiant est modifier",anchor='w')
        e.grid(row=3,column=0)
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="modifier")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="CIN")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    rec1=tk.Label(einfo,text="nouveu adresse")
    rec1.grid(row=0,column=1,padx=20,pady=5,ipadx=100)
    rec_entry1=tk.Entry(einfo)
    rec_entry1.grid(row=1,column=1)
    for widget in einfo.winfo_children():
        widget.grid_configure(padx=10,pady=5)
    button=tk.Button(frame,text="Modifier",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def findl1():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Livre WHERE tit = ?""",(rec,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="Titre :")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def findl2():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Livre WHERE noa = ?""",(rec,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="Auteur :")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def findl3():
    for widget in frame.winfo_children():
        widget.destroy()
    def rfind():
        rec=rec_entry.get()
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        r=c.execute("""SELECT * FROM Livre WHERE ann = ?""",(rec,))
        i=3
        for student in r:
            for j in range(len(student)):
                e=tk.Label(einfo,width=10,fg='blue',text=student[j],anchor='w')
                e.grid(row=i,column=j)
            i=i+1
        conn.commit()
        conn.close()
    einfo=tk.LabelFrame(frame,text="Recherche")
    einfo.grid(row=0,column=0,padx=20,pady=5)
    rec=tk.Label(einfo,text="Annee :")
    rec.grid(row=0,column=0,padx=20,pady=5,ipadx=100)
    rec_entry=tk.Entry(einfo)
    rec_entry.grid(row=1,column=0)
    button=tk.Button(frame,text="Enter data",command=rfind)
    button.grid(row=2,column=0,columnspan=2,padx=20,pady=5,ipadx=100)
def donothing():
    return
##########################################################################################**********MENU

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="ajouter etudiant", command=ajout)

sub_menu =tk. Menu(filemenu, tearoff=0)
sub_menu.add_command(label='tous', command=find)
sub_menu.add_command(label='cin', command=find1)
sub_menu.add_command(label='section', command=find2)
sub_menu.add_command(label='section et niveau', command=find3)
sub_menu.add_command(label='niveau etude', command=find4)

# add the File menu to the menubar
filemenu.add_cascade(
    label="chercher par",
    menu=sub_menu
)
sub_menu1 =tk. Menu(filemenu, tearoff=0)
sub_menu1.add_command(label='nom', command=supp1)
sub_menu1.add_command(label='section', command=supp2)
sub_menu1.add_command(label='niveau', command=supp3)
sub_menu1.add_command(label='niveau et section', command=supp4)

# add the File menu to the menubar
filemenu.add_cascade(
    label="supprimer par",
    menu=sub_menu1
)
sub_menu2 =tk. Menu(filemenu, tearoff=0)
sub_menu2.add_command(label='telephone', command=mod1)
sub_menu2.add_command(label='mail', command=mod2)
sub_menu2.add_command(label='adresse', command=mod3)

# add the File menu to the menubar
filemenu.add_cascade(
    label="modifier le ...",
    menu=sub_menu2
)


filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Gestion etudiant", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)

editmenu.add_command(label="ajout livre", command=ajoutl)
sub_menu =tk. Menu(editmenu, tearoff=0)
sub_menu.add_command(label='Titre', command=suppl1)
sub_menu.add_command(label='Auteur', command=suppl2)
sub_menu.add_command(label='annee', command=suppl3)

# add the File menu to the menubar
editmenu.add_cascade(
    label="Supprimer par",
    menu=sub_menu
)
sub_menu1 =tk. Menu(editmenu, tearoff=0)
sub_menu1.add_command(label='Titre', command=findl1)
sub_menu1.add_command(label='Auteur', command=findl2)
sub_menu1.add_command(label='annee', command=findl3)
#OUssama dhiaa arouay
#mohammed abdouli
#Djerba
#mounir
#monji
#a7la monji
#ma9souda
#Sidi abi zid
# add the File menu to the menubar
editmenu.add_cascade(
    label="Rechercher par",
    menu=sub_menu1
)
menubar.add_cascade(label="Gestion matiere", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
window.config(menu=menubar)
window.mainloop()
