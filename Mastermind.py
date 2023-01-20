# -*- coding: cp1252 -*-
from Tkinter import *
from random import randrange
from tkFont import*
import gadfly

# Création d'un jeu de réflexion pur
# "MASTERMIND"

##########################################################################################################
##########################################################################################################

def existence_base(choix=0):
    if choix==0:
        try:
            gadfly.gadfly("basedonn","C:/mastermindjl/")
            return 1
        except:
            return 0
        
    if choix==1:
        try:
           gadfly.gadfly("jeu simple","C:/mastermindjl/")
           return 1
        except:
            return 0
        
    if choix==2:
        try:
           gadfly.gadfly("joueur1 joueur2","C:/mastermindjl/")
           return 1
        except:
            return 0


def ajout_based(nom_partie):
    if existence_base(1):
        basedonn=gadfly.gadfly("jeu simple","C:/mastermindjl/")
        cur=basedonn.cursor()
    else:
        basedonn=gadfly.gadfly()
        basedonn.startup("jeu simple","C:/mastermindjl/")
        cur=basedonn.cursor()
        cur.execute("create table simple (nom_partie varchar,victoire varchar,defaite varchar)")

    cur.execute("insert into simple(nom_partie,victoire,defaite) values\
('%s','%s','%s')" % (nom_partie,'/','/'))
    basedonn.commit()
    cur.execute("select * from simple")
    print cur.fetchall()


##########################################################################################################
##########################################################################################################


class Form_basedonn:
    def __init__(self):
        self.fen=Tk()
        self.fen.title("Formulaire d\'inscription")
        self.fen.geometry("400x800")
        if existence_base(0):
            self.basedonn=gadfly.gadfly("basedonn","C:/mastermindjl/")
            self.cur=self.basedonn.cursor()
            
        else:
            self.basedonn=gadfly.gadfly()
            self.basedonn.startup("basedonn","C:/mastermindjl/")
            self.cur=self.basedonn.cursor()
            self.cur.execute("create table identite (nom varchar, prenom varchar, nbrevictoires varchar,\
nbredefaites varchar, nationalite varchar, age varchar)")

    
        font1=Font(family='Courier new',size=9, weight='bold')
        font2=Font(family='Courier new',size=14, weight='bold')
        font3=Font(family='Sergoe',size=10)
        font4=Font(family='Courier',size=11,weight='bold')

        intro=Label(self.fen,text='\nCréez une CARRIERE',font=font2,fg='#8f577d')
        intro.pack(side=TOP)
    
        frame1=Frame(self.fen,width=350)
        label1=Label(self.fen,text='\n\nVotre nom : ',fg='#295875',font=font1)
        label1.pack(pady=12,anchor=CENTER)
        variable1=StringVar()
        self.nom=Entry(self.fen,textvariable=variable1,width=30)
        self.nom.pack()
        frame1.pack()

        frame2=Frame(self.fen,width=350)
        label2=Label(self.fen,text='\nVotre prénom : ',fg='#295875',font=font1)
        label2.pack(pady=12,anchor=CENTER)
        variable2=StringVar()
        self.prenom=Entry(self.fen,textvariable=variable2,width=30)
        self.prenom.pack()
        frame2.pack()

        frame3=Frame(self.fen,width=350)
        label3=Label(self.fen,text='\nVotre nationalité : ',fg='#295875',font=font1)
        label3.pack(pady=12,anchor=CENTER)
        variable3=StringVar()
        self.nationalite=Entry(self.fen,textvariable=variable3,width=30)
        self.nationalite.pack()
        frame3.pack()

        frame4=Frame(self.fen,width=350)
        label4=Label(self.fen,text='\nVotre âge : ',fg='#295875',font=font1)
        label4.pack(pady=12,anchor=CENTER)
        variable4=StringVar()
        self.age=Entry(self.fen,textvariable=variable4,width=30)
        self.age.pack()
        frame4.pack()

        frame5=Frame(self.fen,width=350)
        message=Label(self.fen,text='\n\nEn jouant une carrière,\nvous devenez joueur n1 en permanence\n',\
                      fg='#295875',font=font3)
        message.pack()
        frame5.pack()

        confirmer=Button(self.fen,text='Confirmer',bg='#5a5e6b',fg='orange',\
                         activebackground='brown',font=font4,command=self.insert_base_donn)
        confirmer.pack(side=BOTTOM,pady=30)

        self.fen.mainloop()

    def insert_base_donn(self):
        if self.nom.get()!='':
            if self.prenom.get()!='':
                self.cur.execute("insert into identite(nom,prenom,nbrevictoires,nbredefaites,nationalite,age)\
                values('%s','%s','%s','%s','%s','%s')" % (self.nom.get(),self.prenom.get(),'0','0',\
                                                self.nationalite.get(),self.age.get()))
                self.basedonn.commit()
                self.fen.destroy()
                objet1.affiche_nomcarriere()
                self.cur.execute("select * from identite")
                print self.cur.fetchall() 


################################################################################################
###################################################################################################

class BSDpartie_simple:
    def __init__(self):
        self.fen_choix=Tk()
        self.fen_choix.geometry("300x200")
        self.fen_choix.title("Choix parties")
        text_font1=Font(family='Courier',size=13,weight='bold')
        label1=Label(self.fen_choix,text='Entez le nom de la partie SVP',fg="#0a1d10",font=text_font1)
        label1.pack(side=TOP,anchor=W,padx=10,pady=15)
        variable1=StringVar()
        self.nom_partie=Entry(self.fen_choix,textvariable=variable1,width=30)
        self.nom_partie.pack()
        
        Button(self.fen_choix,text='Ok',padx=40,pady=6,fg='orange',bg='black',\
               command=self.recup_nom).pack(anchor=CENTER,pady=15)


    def recup_nom(self):
        if self.nom_partie.get()!='':
            ajout_based(self.nom_partie.get())
            self.fen_choix.destroy()
            objet1.pions()
            objet1.couleurs_aleatoires(0,'simple')

        
    def test(self):
        if existence_base(1):
            self.basedonn=gadfly.gadfly("jeu simple","C:/mastermindjl/")
            self.cur=self.basedonn.cursor()
            
        else:
            self.basedonn=gadfly.gadfly()
            self.basedonn.startup("jeu simple","C:/mastermindjl/")
            self.cur=self.basedonn.cursor()
            self.cur.execute("create table simple (nom_partie varchar, victoire varchar, defaite varchar)")
        self.cur.execute("select * from simple")
        return self.cur.fetchall()

    def cherche_parties(self,partie=0):
        if partie!="Aucune partie":
            self.cur.execute("select nom_partie, victoire, defaite from simple where nom_partie='%s'" %(partie))
            return self.cur.fetchall()
        else:
            partie=[]
            return partie

###################################################################################################
###################################################################################################

class Insert_victoire_defaiteBSDsimple:
    def __init__(self,victoire=0,defaite=0):
        basedonn=gadfly.gadfly("jeu simple","C:/mastermindjl/")
        cur=basedonn.cursor()
        cur.execute("select * from simple")
        liste=cur.fetchall()[len(cur.fetchall())-1] # tuple de la derniere partie #

        cur.execute("update simple set nom_partie='%s' where nom_partie='%s'" %\
                         (liste[1],liste[1]))
        cur.execute("update simple set victoire='%s' where nom_partie='%s'" %\
                         (str(victoire),liste[1]))
        cur.execute("update simple set defaite='%s' where nom_partie='%s'" %\
                         (str(defaite),liste[1]))
        basedonn.commit()

        cur.execute("select nom_partie, victoire, defaite from simple where nom_partie='%s'" %(liste[1]))
        print cur.fetchall()


class Insert_victoire_defaiteBSDcarriere(Insert_victoire_defaiteBSDsimple):
    def __init__(self,nom_partie,victoire=0,defaite=0):
        basedonn=gadfly.gadfly("basedonn","C:/mastermindjl/")
        cur=self.basedonn.cursor()
        
        cur.execute("update identite set nbrevictoires='%s' where nom='%s' and prenom='%s'" %\
                         (str(victoire),nom_partie[0],nom_partie[1]))
        cur.execute("update identite set nbredefaites='%s' where nom='%s' and prenom='%s'" %\
                         (str(defaite),nom_partie[0],nom_partie[1]))
        self.basedonn.commit()



###################################################################################################
###################################################################################################

class Consulter_infos(BSDpartie_simple):
    def __init__(self):
        self.fen=Tk()
        self.fen.geometry("1060x400")
        self.fen.title("Scores")

        # Titre #
        font1=Font(family='Boockman Old Style',size=10, weight='bold')
        label1=Label(self.fen,text='Scores - Historiques',bg='#504559',fg='white',bd=6,\
                     relief=GROOVE,highlightbackground='#8b4b9b',height=3,font=font1)
        label1.pack(side=TOP,fill=X)

        
        # Listbox 'types de parties' #
        fen1=Frame(self.fen)
        font2=Font(family='Boockman Old Style',size=8,slant='italic')
        label2=Label(fen1,text="Types de parties",fg='white',bg='#5f3400',font=font2)
        label2.pack(anchor=N,pady=15)
        self.type_parties=Listbox(fen1,width=28,height=8,bg='#9aa6ba',fg='yellow')
        self.type_parties.pack(pady=10)
        liste=["Parties simples","Carrières"]
        for i in liste:
            self.type_parties.insert(END,i)
        
        fen1.pack(side=LEFT,anchor=N,padx=30,pady=20)

        # Listbox 'Noms des parties' # 
        fen2=Frame(self.fen)
        self.liste=Listbox(fen2,width=28,height=8,bg='white',fg='blue')
        self.liste.pack(side=LEFT,anchor=N)
        ascenseur=Scrollbar(fen2,command=self.liste.yview)
        self.liste.configure(yscrollcommand=ascenseur.set)
        ascenseur.pack(anchor=N,side=LEFT,padx=5,fill=Y)

        #  infos joueur #
        self.label4=Label(fen2,text='Nom partie : ')
        self.label4.pack(anchor=N,padx=25,pady=5)
        
        self.label5=Label(fen2,text='Victoire(s) : ')
        self.label5.pack(anchor=N,padx=25,pady=5)
        
        self.label6=Label(fen2,text='Défaite(s) : ')
        self.label6.pack(anchor=N,padx=25,pady=5)

        self.labelsup1=Label(fen2)
        self.labelsup1.pack(anchor=N,padx=25,pady=5)

        self.labelsup2=Label(fen2)
        self.labelsup2.pack(anchor=N,padx=25,pady=5)
        
        fen2.pack(side=LEFT,anchor=N,pady=80,padx=60)

        # Boutons ok - supprimer #
        Button(self.fen,text='Ok',padx=17,pady=6,fg='orange',bg='black',\
               command=self.fen.destroy).pack(side=LEFT,anchor=S,pady=20,padx=8)
        
        Button(self.fen,text='Supprimer',padx=17,pady=6,fg='orange',bg='black',\
               command=self.supprimer).pack(side=LEFT,anchor=S,pady=20,padx=8)
        
        self.type_parties.bind("<ButtonRelease-1>",self.selection1)
        self.liste.bind("<ButtonRelease-1>",self.selection_liste)

        self.selection_liste=None
        self.rang_selection=None
        self.elems=[]

        self.fen.mainloop()
        
    ############################################

    def selection1(self,event):
        self.selection=self.type_parties.get(self.type_parties.curselection())
        rang_selection=self.type_parties.curselection()[0]
        if rang_selection=='0':
            self.partie_simple()
        if rang_selection=='1':
            self.carrieres()


    def partie_simple(self):
        self.liste.delete(0,END)
        if self.test()==[]:
            self.liste.insert(END,'Aucune partie')
        else:
            for i in self.test():
                self.liste.insert(END,i[1])
        self.label4.configure(text="Nom partie : ")
        self.label5.configure(text="Victoire : ")
        self.label6.configure(text="Défaite : ")
        self.labelsup1.configure(text="")
        self.labelsup2.configure(text="")
        
    def carrieres(self):
        self.liste.delete(0,END)
        if existence_base(0):
            self.basedonn=gadfly.gadfly("basedonn","C:/mastermindjl/")
            self.cur=self.basedonn.cursor()
            self.cur.execute("select * from identite")
            for i in self.cur.fetchall():
                self.liste.insert(END,i[1]+" "+i[2])
        else:
            self.liste.insert(END,'Aucune partie')
            
        self.label4.configure(text="Nom carrière : ")
        self.label5.configure(text="Nbres victoires : ")
        self.label6.configure(text="Nbres Défaites : ")
        self.labelsup1.configure(text="Nationalité : ")
        self.labelsup2.configure(text="Age : ")

    ###########################################

    def selection_liste(self,event):
        self.selection_liste=self.liste.get(self.liste.curselection())
        print self.selection_liste
        self.rang_selection=self.liste.curselection()
        if self.selection=="Parties simples":
            if self.cherche_parties(self.selection_liste)!=[]:
                for i in self.cherche_parties(self.selection_liste):
                    self.label4.configure(text="Nom partie : "+str(i[0]))
                    self.label5.configure(text="Victoire : "+str(i[1]))
                    self.label6.configure(text="Défaite : "+str(i[2]))
                    
        "----------------------------------------------------------------------"

        if self.selection=="Carrières":
            if existence_base(0):
                self.cur.execute("select * from identite")
                if self.cur.fetchall()!=[]:
                    self.elems=self.selection_liste.split()
                    self.cur.execute("select nom, prenom, nbrevictoires, nbredefaites, nationalite,\
age from identite where nom='%s' and prenom='%s'"%(self.elems[0],self.elems[1]))
                    for i in self.cur.fetchall():
                        self.label4.configure(text="Nom carrière : "+str(i[0]+" "+i[1]))
                        self.label5.configure(text="Nbres victoires : "+str(i[2]))
                        self.label6.configure(text="Nbres Défaites : "+str(i[3]))
                        self.labelsup1.configure(text="Nationalité : "+str(i[4]))
                        self.labelsup2.configure(text="Age : "+str(i[5]))

    def supprimer(self):
        if self.selection_liste!=None:
            if self.selection=="Parties simples":
                if existence_base(1):
                    basedonn2=gadfly.gadfly("jeu simple","C:/mastermindjl/")
                    cur2=basedonn2.cursor()
                    cur2.execute("delete from simple where nom_partie='%s'"%(self.selection_liste))
                    self.liste.delete(self.rang_selection)
                    basedonn2.commit()

            if self.selection=="Carrières":
                if existence_base(0):
                    if self.elems!=[]:
                        self.cur.execute("delete from identite where nom='%s' and prenom='%s'"%(self.elems[0],self.elems[1]))
                        self.liste.delete(self.rang_selection)
                        self.basedonn.commit()
            
###########################################################################################   
###########################################################################################


class Deplacement(Insert_victoire_defaiteBSDcarriere):
    def __init__(self,can):
        self.can2=can
        self.can2.bind("<Button-1>",self.detection)
        self.can2.bind("<Motion>",self.mouv_objet)
        self.can2.bind("<ButtonRelease-1>",self.arret_mouv)
        self.trouveobjet=None
        self.objet=[0]
        self.nom_pion=''
        self.y_rangee=112.5
        self.info=0


    def detection(self,event):
        if self.info==0:
            if 32.5<=event.x<=47.5:
                for i in range(112,432,40):
                    if i+0.5<=event.y<=i+15.5:
                        self.objet=self.can2.find_enclosed(event.x-15,event.y-15,event.x+15,event.y+15)
                        self.info='ok'
            

            
        if self.objet!=[0]:
            if 32.5<=event.x<=47.5:
                if 112.5<=event.y<=127.5:
                    self.nom_pion='blue'
                if 152.5<=event.y<=167.5:
                    self.nom_pion='yellow'
                if 192.5<=event.y<=207.5:
                    self.nom_pion='black'
                if 232.5<=event.y<=247.5:
                    self.nom_pion='red'
                if 272.5<=event.y<=287.5:
                    self.nom_pion='green'
                if 312.5<=event.y<=327.5:
                    self.nom_pion='white'
                if 352.5<=event.y<=367.5:
                    self.nom_pion='brown'
                if 392.5<=event.y<=407.5:
                    self.nom_pion='orange'
                        
            self.trouveobjet=self.objet[0]
            

    def mouv_objet(self,event):
        if self.trouveobjet!=None:
            if event.x>60:
                self.can2.coords(self.trouveobjet,event.x-7.5,event.y-7.5,event.x+7.5,event.y+7.5)
                self.can2.lift(self.trouveobjet)

    def arret_mouv(self,event):
        if self.trouveobjet!=None:
            x=273.75
            for longeur in range(0,4):
                if x-10<=event.x<=(x+15)+10:
                        if self.y_rangee-10<=event.y<=self.y_rangee+25:
                            self.ajout_nom_objet(self.nom_pion,longeur)
                            self.can2.coords(self.trouveobjet,x,self.y_rangee,x+15,self.y_rangee+15)
                            self.trouveobjet=None
                            self.info=0
                x+=62.5
            x=273.75


###########################################################################################   
###########################################################################################

class Joueur2:
    def __init__(self):
        self.fen2=Tk()
        self.fen2.title("Joueur1 - Joueur2")
        self.can_jeua2=Canvas(self.fen2,width=600,height=300,bg='#b57e7e')
        self.can_jeua2.pack(side=TOP)
        
        font6=Font(family='Courier',size=13)
        self.can_jeua2.create_text(220,30,text="Joueur2, veuillez choisir votre solution\n\
Attention! Il faut que le Joueur1 ne la sache pas!",fill='#d1de00',font=font6)

        # Box pour pions #
        for x in range(220,380,40):
            self.can_jeua2.create_rectangle(x,100,x+40,140,outline='black',width=2)

        # Cercles dans box #
        coul2=['blue','yellow','black','red','green','white','brown','orange']
        for gauchadroite1 in range(232,392,40):
            self.can_jeua2.create_oval(gauchadroite1+0.5,112.5,gauchadroite1+15.5,127.5,outline='#330404',width=1)

        # pions de couleurs #
        cpt1=0
        for gauchadroite1 in range(152,460,40):
            self.can_jeua2.create_oval(gauchadroite1+0.5,180,gauchadroite1+15.5,195,fill=coul2[cpt1],width=1)
            cpt1+=1

        self.can_jeua2.bind("<Button-1>",self.detection2)
        self.can_jeua2.bind("<Motion>",self.mouv_objet2)
        self.can_jeua2.bind("<ButtonRelease-1>",self.arret_mouv2)
        frame_jeua2=Frame(self.fen2)
        Button(self.fen2,text='Ok',padx=40,pady=6,fg='orange',bg='black',command=self.confirmer).pack(padx=30,side=LEFT)
        Button(self.fen2,text='Quitter',padx=26,pady=6,fg='orange',bg='black',command=self.fen2.destroy).pack(pady=5)
        frame_jeua2.pack()
        self.choix=[0]
        self.nom_pion=''
        self.trouveobjet=None
        self.liste=[]
        self.info=0


    def detection2(self,event):
        if self.info==0:
            if 180<=event.y<=195:
                for i in range(152,460,40):
                    if i+0.5<=event.x<=i+15.5:
                        self.choix=self.can_jeua2.find_enclosed(event.x-15,event.y-15,event.x+15,event.y+15)
                        self.info='ok'

        if self.choix!=[0]:
            if 180<=event.y<=195:
                if 152.5<=event.x<=167.5:
                    self.nom_pion='blue'
                if 192.5<=event.x<=207.5:
                    self.nom_pion='yellow'
                if 232.5<=event.x<=247.5:
                    self.nom_pion='black'
                if 272.5<=event.x<=287.5:
                    self.nom_pion='red'
                if 312.5<=event.x<=327.5:
                    self.nom_pion='green'
                if 352.5<=event.x<=367.5:
                    self.nom_pion='white'
                if 392.5<=event.x<=407.5:
                    self.nom_pion='brown'
                if 432.5<=event.x<=447.5:
                    self.nom_pion='orange'
                        
            self.trouveobjet=self.choix[0]
            

    def mouv_objet2(self,event):
        if self.trouveobjet!=None:
            self.can_jeua2.coords(self.trouveobjet,event.x-7.5,event.y-7.5,event.x+7.5,event.y+7.5)
            self.can_jeua2.lift(self.trouveobjet)


    def arret_mouv2(self,event):
        indice=0
        if self.trouveobjet!=None:
            x=232.5
            for longeur in range(0,4):
                if x-10<=event.x<=(x+15)+10:
                    if 112.2<=event.y<=127.5:
                        for i in range(len(self.liste)):
                            if self.liste[i][1]==longeur:
                                indice=1
                        if indice==0:    
                            self.can_jeua2.coords(self.trouveobjet,x,112.5,x+15,127.5)
                            self.liste.append((self.nom_pion,longeur))
                            self.trouveobjet=None
                            self.info=0

                if x<=392.5:
                    x+=40

    def confirmer(self):
        self.solution=[]
        liste_verif=[]
        for i in range(len(self.liste)):
            if self.liste[i][1] not in liste_verif:
                liste_verif.append(self.liste[i][1])

        if len(self.liste)==4:
            self.solution.append(self.liste[0][0])
            self.solution.append(self.liste[1][0])
            self.solution.append(self.liste[2][0])
            self.solution.append(self.liste[3][0])
            self.fen2.destroy()
            objet1.pions()
            objet1.couleurs_aleatoires(self.solution,'joueurs')
        
################################################################################################
#################################################################################################
            
class Regles:
    def __init__(self):
        fen_regles=Tk()
        fen_regles.title('Regles de jeu : Mastermind')
        can=Canvas(fen_regles,bg='#c1d0d4',width=900,height=620)
        can.pack(side=TOP)
        font_regles=Font(family='Comic Sans MS',size=6)
        can.create_text(500,310,text='REGLE DE JEU : MASTERMIND\n\n\n\
Le joueur2 place quatre pions de couleurs derrière un cache de façon à masquer la combinaison au joueur n1.\n\
Le nombre de pions de couleurs différentes est de huit : rouge ; jaune ; vert ; bleu ; orange ; blanc ; brun ; noir.\n\n\
Des petits pions blancs et noirs sont utilisés pour donner des indications à chaque étape du jeu.\n\
Il existe de nombreuses variantes suivant le nombre de couleurs, de rangées ou de trous.\n\
Votre objectif est de retrouver les quatre pions dans le même ordre que la solution. Vous avez droit à douze\n\
rangées pour parvenir à trouver la solution. Vous allez donc faire des propositions en plaçant quatre\n\
pions à chaque tour sur les rangées.\n\n\
Une fois les pions placés, l\'autre joueur devra vous indiquer :\n\
    -le nombre de pions de bonne couleur bien placés en utilisant les petits pions noirs ;\n\
    -le nombre de pions de bonne couleur mais mal placés avec les petits pions blancs.\n\n\
Il ne doit en aucun cas indiquer quels sont les pions bien placés. Plus vous faites des propositions,\n\
plus vous la possibilité de trouver. La tactique du joueur actif consiste à sélectionner en fonction\n\
des coups précédents, couleurs et positions, de manière à obtenir le maximum d\'informations.\n\n\
Vous devez le découvrir vous-même avec de la Réflexion.\n\n\
Fin d\'une partie\n\n\
Soit vous avez trouvé la solution, vous gagnez la partie. (moins de rangées vous seront utiles,\n\
plus grande sera la gloire ).\n\
Soit vous n\'avez pas réussi à trouver la solution en douze essais (les douze rangées sont utilisées),\n\
et la gloire ira à votre adversaire.\n\n\
Bonne chance et bonne patiente.',fill='#051b11',font=font_regles)
        Button(fen_regles,text='Ok',padx=40,pady=6,fg='orange',bg='black',\
               command=fen_regles.destroy).pack(anchor=E,padx=30,pady=15)
        
        fen_regles.mainloop()

########################################################################################################
#######################################################################################################

class Jeu(Deplacement):
    def __init__(self):
        "Fenetre principale + canvas"
        self.fen=Tk()
        self.fen.title("MasterMind")
        self.can2=Canvas(self.fen,width=800,height=800,relief=GROOVE,cursor="pencil",bd=2)
        self.can2.pack(side=LEFT,padx=6,pady=6)
        self.arriere_plan=PhotoImage(file='C:/mastermindjl/planche.gif')
        self.can2.create_image(403,350,image=self.arriere_plan)
        Deplacement.__init__(self,self.can2)

        # Variables utiles pour d'autres fonctions #
        self.liste_objets=[]
        self.type_partie='simple'
        self.coul_aleat=[]

        # Bouton valider #
        fen1=Frame(self.fen)
        text_font1=Font(family='Courier',size=14,weight='bold')
        Button(self.fen,text='Valider',padx=45,bg='#5a5e6b',fg='orange',activebackground='brown',\
               cursor='hand1',font=text_font1,command=self.valider).pack(anchor=CENTER,side=TOP,padx=60,pady=30)
        fen1.pack()

        # Boutons #
        fen2=Frame(self.fen)
        self.font1=Font(family='Boockman Old Style',size=9,weight='bold')
        Button(self.fen,text='Simple',command=BSDpartie_simple,font=self.font1,relief=RAISED,fg="#deecff",\
               bg="#798081").pack(pady=5)
        Button(self.fen,text='Un joueur2',command=Joueur2,font=self.font1,relief=RAISED,fg="#deecff",\
               bg="#798081").pack(pady=5)
        Button(self.fen,text='Règles',command=Regles,font=self.font1,relief=RAISED,fg="#deecff",\
               bg="#798081").pack(pady=5)
        Button(self.fen,text='Scores',command=Consulter_infos,font=self.font1,relief=RAISED,fg="#deecff",\
               bg="#798081").pack(pady=5)
        Button(self.fen,text='Carrière',command=Form_basedonn,font=self.font1,relief=RAISED,fg="#deecff",\
               bg="#798081").pack(pady=5)
        fen2.pack()

        self.fen3=Frame(self.fen)

        # La listbox #
        label_sep=Label(self.fen3,text="///////////////////////////////////")
        label_sep.pack(side=TOP,pady=15)
        fen3a=Frame(self.fen3)
        self.liste_carrieres=Listbox(fen3a,width=25,height=20,bg="#efebff")
        self.liste_carrieres.pack(side=LEFT,padx=5,pady=15)
        ascenseur=Scrollbar(fen3a,command=self.liste_carrieres.yview)
        self.liste_carrieres.configure(yscrollcommand=ascenseur.set)
        ascenseur.pack(side=RIGHT,fill=Y)
        fen3a.pack()


        # Boutons poursuivre - précédent #
        fen3b=Frame(self.fen3)
        Button(fen3b,text='Précédent',command=self.affiche_nomcarriere,font=self.font1,relief=RAISED,fg="#deecff",\
               bg="#798081").pack(side=LEFT,pady=5,padx=8)
        self.poursuivre=Button(fen3b,text='Poursuivre',command=self.poursuivre_carriere,\
                               font=self.font1,relief=RAISED,fg="#deecff",\
                               bg="#798081").pack(side=RIGHT,pady=5,padx=8)
        fen3b.pack(pady=10)
        
        self.fen3.pack()

        self.liste2=[]
        self.selection=0
        self.liste_carrieres.bind("<ButtonRelease-1>",self.infos_carriere)
        
        self.affiche_nomcarriere()

    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    def affiche_nomcarriere(self):
        if existence_base(0):
            self.liste2=[]
            self.liste_carrieres.delete(0,END)
            self.basedonn=gadfly.gadfly("basedonn","C:/mastermindjl/")
            self.cur=self.basedonn.cursor()
            self.cur.execute("select * from identite")
            self.liste_carrieres.insert(0,'Liste carrières')
            self.liste_carrieres.insert(END,'')
            for i in self.cur.fetchall():
                nom_partie=str(i[1])+" "+str(i[2])
                if nom_partie not in self.liste2:
                    self.liste_carrieres.insert(END,nom_partie)
                    self.liste2.append(nom_partie)
                

    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    def infos_carriere(self,event):
        if self.liste_carrieres.curselection()[0]!='0' and '1':
            self.selection=self.liste_carrieres.get(self.liste_carrieres.curselection())
            if len(self.selection)>2:
                self.liste_carrieres.delete(0,END)
                self.liste_carrieres.insert(0,'Liste carrières')
                self.liste_carrieres.insert(END,'')
                self.nbre_victoires=int()
                self.nbre_defaites=int()
                self.elems=self.selection.split()
                self.cur.execute("select nom, prenom, nbrevictoires, nbredefaites, nationalite,\
age from identite where nom='%s' and prenom='%s'"%(self.elems[0],self.elems[1]))
            
                for i in self.cur.fetchall():
                    self.liste_carrieres.insert(END,i[0])
                    self.liste_carrieres.insert(END,i[1])
                    self.liste_carrieres.insert(END,i[4])
                    self.liste_carrieres.insert(END,i[5])
                    self.nbre_victoires=int(i[2])
                    self.nbre_defaites=int(i[3])

    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    def poursuivre_carriere(self):
        if self.liste_carrieres.bbox(3)!=None:
            objet1.pions()
            objet1.couleurs_aleatoires(0,'carriere')
            self.type_partie='carriere'
            self.liste_carrieres.insert(END,'')
            self.liste_carrieres.insert(END,'-> Nouvelle partie...')
        
        
    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    
    def pions(self):
        "PIONS"
        # Quadrillage fin #
        # Lignes verticales| #          
        for padex in range(22,59,2):
            self.can2.create_line(padex,102,padex,418,fill='#c7b6db')
        # Lignes horizontales- #
        for padey in range(102,419,2):
            self.can2.create_line(22,padey,59,padey,fill='#c7b6db')

        # Box pour pions #
        for y in range(100,420,40):
            self.can2.create_rectangle(20,y,60,y+40,outline='black',width=2)

        # Cercles dans Box #
        cpt=0
        self.coul=['blue','yellow','black','red','green','white','brown','orange']
        for hautabas in range(112,432,40):
            for repetition in range(0,80):
                self.can2.create_oval(32.5,hautabas+0.5,47.5,hautabas+15.5,outline='#c4c087',fill=self.coul[cpt],width=1)
            cpt+=1
            
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

        "PLATE-FORME"
        # Cadre #   
        self.can2.create_rectangle(250,100,550,580,width=3,fill='#d9d8e4',outline='#4b3126')

        # Separation rangées #
        for i in range(140,580,40):
            self.can2.create_line(250,i,550,i,fill='#4b3126',width=2)

        # Separation indicateurs #
        self.can2.create_line(500,100,500,580,fill='#4b3126',width=2)

        # points indicateurs #
        y1=110
        for rangee in range(0,12):
            self.can2.create_oval(510,y1,515,y1+5,outline='#4b3126');self.can2.create_oval(535,y1,540,y1+5,outline='#4b3126')
            y1+=15
            self.can2.create_oval(510,y1,515,y1+5,outline='#4b3126');self.can2.create_oval(535,y1,540,y1+5,outline='#4b3126')
            y1+=25

        # cercles rangées #
        x=273.75
        for hauteur in range(112,592,40):
            for longeur in range(0,4):
                self.can2.create_oval(x,hauteur+0.5,x+15,hauteur+15.5,width=1)
                self.can2.create_oval(x+2,hauteur+2.5,x+13,hauteur+13.5,width=1)
                x+=62.5
            x=273.75


        # Image "Ameliore ta concentration"
        self.image3=PhotoImage(file='C:/mastermindjl/mot_encourage.gif')
        self.can2.create_image(140,50,image=self.image3)


        # Cache #
        self.can2.create_rectangle(215,580,585,650,fill='#5a5e6b',outline='#4b3126',width=2)
        self.rectangle1=self.can2.create_rectangle(275,600,525,624,fill='#4b3126')


    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    def couleurs_aleatoires(self,choix=0,typepartie=0):
        Deplacement.__init__(self,self.can2)
        self.type_partie=typepartie
        self.y_placement=110
        self.coul_aleat=[]
        if choix==0:
            while 1:
                coul1=randrange(8);coul2=randrange(8)
                coul3=randrange(8);coul4=randrange(8)
                # 4 Couleurs différentes #
                if coul1!=coul2 and coul1!=coul3 and coul1!=coul4:
                    if coul2!=coul1 and coul2!=coul3 and coul2!=coul4:
                        if coul3!=coul1 and coul3!=coul2 and coul3!=coul4:
                            if coul4!=coul1 and coul4!=coul2 and coul4!=coul3:
                                self.coul_aleat.append(self.coul[coul1])
                                self.coul_aleat.append(self.coul[coul2])
                                self.coul_aleat.append(self.coul[coul3])
                                self.coul_aleat.append(self.coul[coul4])
                                break
            print self.coul_aleat

        else:
            self.coul_aleat=choix

    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    def affichage_resultat(self):
        self.can2.itemconfigure(self.rectangle1,fill='#f5f5dc')
            
        self.can2.create_oval(313,604.5,328,619.5,fill=self.coul_aleat[0])
        self.can2.create_oval(366,604.5,381,619,fill=self.coul_aleat[1])
        self.can2.create_oval(419,604.5,434,619,fill=self.coul_aleat[2])
        self.can2.create_oval(472,604.5,487,619,fill=self.coul_aleat[3])
                
    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    def message_reussite(self):
            fen_ok=Tk()
            can_ok=Canvas(fen_ok,bg='black',width=300,height=80,relief=GROOVE,cursor='pencil',bd=2)
            can_ok.pack(side=TOP)
            text_font=Font(family='Comic Sans MS',size=15,underline=1)
            can_ok.create_text(140,40,text='BRAVO \n\
VOUS REMPORTEZ LA MANCHE!',fill='orange',font=text_font)
            Button(fen_ok,text='ok',command=fen_ok.destroy).pack(padx=15)

    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
            
    def ajout_nom_objet(self,couleur,numero):
        # Liste des couleurs sur rangée + n° de placement #
        self.liste_objets.append((couleur,numero))

    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        
    def valider(self):
        # !Vérifier si 4 couleurs sur rangée! #
        info=0
        liste_verif=[]
        liste0,liste1,liste2,liste3=[],[],[],[]
        self.liste_proposition=[]
        for verif in range(0,len(self.liste_objets)):
            if self.liste_objets[verif][1] not in liste_verif:
                liste_verif.append(self.liste_objets[verif][1])

        # Liste nbre couleurs sur chaque "trou" #        
        if len(liste_verif)==4:
            for i in range(0,len(self.liste_objets)):
                if self.liste_objets[i][1]==0:
                    liste0.append(self.liste_objets[i])
                if self.liste_objets[i][1]==1:
                    liste1.append(self.liste_objets[i])
                if self.liste_objets[i][1]==2:
                    liste2.append(self.liste_objets[i])
                if self.liste_objets[i][1]==3:
                    liste3.append(self.liste_objets[i])

            # Filtrage des 4 récentes couleurs sur chaque "trou" #
            self.liste_proposition.append(liste0[len(liste0)-1])
            self.liste_proposition.append(liste1[len(liste1)-1])
            self.liste_proposition.append(liste2[len(liste2)-1])
            self.liste_proposition.append(liste3[len(liste3)-1])
            print self.liste_proposition

            self.indicateurs()


    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"


    def indicateurs(self):
        if self.coul_aleat==[]:
            refus=Tk()
            refus.title("Message d\'erreur")
            label=Label(refus,text="Vous devez cliquez sur le bouton 'Simple' pour démarrer une partie simple")
            label.pack(anchor=N,padx=45,pady=5)
            Button(refus,text='Ok',padx=40,pady=6,fg='orange',bg='black',\
                   command=refus.destroy).pack(anchor=CENTER,pady=10)

            "--------------------------------------------------------------"

        else:
            # Couleurs de la solution et correctement placées #
            juste_place=[]
            cpt1,cpt2=0,0
            while cpt1<4:
                while cpt2<4:
                    if self.liste_proposition[cpt1][0]==self.coul_aleat[cpt2]:
                        juste_place.append(cpt1)
                    cpt1+=1
                    cpt2+=1

            # Couleurs de la solution et mal placées #
            juste_mal_place=[]
            for sol in range(0,len(self.coul_aleat)):
                for prop in range(0,len(self.liste_proposition)):
                    if sol!=prop:
                        if self.liste_proposition[prop][0]==self.coul_aleat[sol]:
                            juste_mal_place.append(prop)


            limite_pions=552.5
            if self.y_placement<limite_pions:

                # Affichage des bien placés #
                x1=510
                if len(juste_place)>0:
                    for i in range(0,len(juste_place)):
                        if i==0:
                            self.can2.create_oval(x1,self.y_placement,x1+5,self.y_placement+5,fill='black')
                        if i==1:
                            self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='black')
                        if i==2:
                            self.y_placement+=15
                            self.can2.create_oval(x1,self.y_placement,x1+5,self.y_placement+5,fill='black')
                        if i==3:
                            self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='black')
                poss_blanc=4-len(juste_place)

                if len(juste_place)==4:
                    self.affichage_resultat()
                    self.message_reussite()
                    if self.type_partie=='simple':
                        Insert_victoire_defaiteBSDsimple.__init__(self,1,0)
                        self.coul_aleat=[]
                    else:
                        self.nbre_victoires+=1
                        Insert_victoire_defaiteBSDcarriere.__init__(self,self.elems,self.nbre_victoires,self.nbre_defaites)
                        self.coul_aleat=[]

                # Affichage des mals placés #
                if len(juste_mal_place)>0:
                    for i in range(0,len(juste_mal_place)):
                        if poss_blanc==4:
                            if i==0:
                                self.can2.create_oval(x1,self.y_placement,x1+5,self.y_placement+5,fill='white')
                            if i==1:
                                self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='white')
                            if i==2:
                                self.y_placement+=15
                                self.can2.create_oval(x1,self.y_placement,x1+5,self.y_placement+5,fill='white')
                            if i==3:
                               self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='white')
                        
                        if poss_blanc==3:
                            if i==0:
                                self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='white')
                            if i==1:
                                self.y_placement+=15
                                self.can2.create_oval(x1,self.y_placement,x1+5,self.y_placement+5,fill='white')
                            if i==2:
                                self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='white')
                    
                        if poss_blanc==2:
                            if i==0:
                                self.y_placement+=15
                                self.can2.create_oval(x1,self.y_placement,x1+5,self.y_placement+5,fill='white')
                            if i==1:
                                self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='white')
                            
                        if poss_blanc==1:
                            self.y_placement+=15
                            if i==0:
                                self.can2.create_oval(x1+25,self.y_placement,x1+30,self.y_placement+5,fill='white')

                if (len(juste_place)+len(juste_mal_place))>2:
                    self.y_placement+=25
                if (len(juste_place)+len(juste_mal_place))<=2:
                    self.y_placement+=40

            self.y_rangee+=40
            if self.y_rangee>limite_pions:
                if self.type_partie=='simple':
                    Insert_victoire_defaiteBSDsimple.__init__(self,0,1)
                    self.coul_aleat=[]
                else:
                    self.nbre_defaites+=1
                    Insert_victoire_defaiteBSDcarriere.__init__(self,self.elems,self.nbre_victoires,self.nbre_defaites)
                    self.coul_aleat=[]
                        
            self.liste_objets=[]


############################################################################################################
############################################################################################################


# Page d'accueil #
class Accueil:
    def __init__(self):
        self.fen1=Tk()
        self.fen1.title("Master Mind")
        can1=Canvas(self.fen1,bg='black',width=700,height=600,relief=GROOVE,cursor="pencil",\
                    highlightbackground='yellow',bd=3)
        can1.pack()

        # titre + image jeu #
        text_font2=Font(family='Courier',size=14,weight='bold')
        image1=PhotoImage(file='C:/mastermindjl/titre.gif')
        image_1=can1.create_image(350,170,image=image1)
        image2=PhotoImage(file='C:/mastermindjl/mastermind.gif')
        image_2=can1.create_image(350,380,image=image2)

        # boutons enter - quit #
        fen0=Frame(self.fen1)
        enter=Button(self.fen1,text='Enter',bg='#5a5e6b',font=text_font2,fg='#f5f5dc',cursor="hand1",\
                     padx=145,activebackground='#f5f5dc',command=self.prem_lancement)
        enter.pack(side=LEFT)
        quitter=Button(self.fen1,text='Quit',bg='#5a5e6b',font=text_font2,fg='#f5f5dc',cursor="hand1",\
                       padx=145,activebackground='#f5f5dc',command=self.fen1.destroy)
        quitter.pack(side=RIGHT)
        fen0.pack(side=BOTTOM)
        self.fen1.mainloop()

    # démarrage du jeu #
    def prem_lancement(self):
        self.fen1.destroy()
        global objet1
        objet1=Jeu()
        objet1.pions()


objet=Accueil()
