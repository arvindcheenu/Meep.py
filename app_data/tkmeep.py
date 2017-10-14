# -*- coding: cp1252 -*-
'''MEEP: short for MARK ENTRY EVALUATION PROGRAM is a simple straightforward application that does what it says: Evaluates marks. It evaluates marks from a
CBSE POSITION FILE and uses list manipulation and other data transformations to get a concise user friendly output without much fuss.
Just:
1> Run
2> Upload
3> Get file. Done!'''
__author__ = "Arvind Srinivasan"
__copyright__ = "Copyright 2015-18, "
__credits__ = ["Arvind Srinivasan", "Srinivasan Ramaswamy", "Pavithra Murali"]
__license__ = "Attribution-4.0-Commercial-No-Derivs"
__version__ = "2.0.1"
__maintainer__ = "Arvind Srinivasan"
__email__ = "arvind@cheenu.net"
__status__ = "Deployment"
#=======
#IMPORTS
#=======
from Tkinter import *
import tkFileDialog as tkfd
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
#=========
#FUNCTIONS
#=========
def see_for_yourself(text):
    topd = Toplevel(master=None,bg='white')
    topd.title('Preview File...')
    topd.resizable(0,0)
    S = Scrollbar(topd)
    T = Text(topd, height=40, width=80,bg='black',fg='#9acd32')
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=TOP, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    text="The file: \n\n{} .................\n<end of preview>".format(text)
    T.insert(END, text)
    button = Button(topd, text="Looking Good?", bg='#009966' ,fg='white' ,relief='flat',width=90,borderwidth=0, activebackground='black',activeforeground='white',command=success)
    button.pack()
def error_wrongfile():
    topd = Toplevel(master=None,bg='#009966')
    topd.resizable(0,0)
    msg = Message(topd, text='There was a problem found with the file. Please Enter the right file.',bg='#009966',justify=CENTER)
    msg.pack()
    button = Button(topd, text="Okay", bg='black' ,fg='white' ,relief='flat',borderwidth=0, width=22, activebackground='white',activeforeground='white',command=topd.destroy)
    button.pack()
def error_nofile():
    topl = Toplevel(master=None,bg='#009966')
    topl.resizable(0,0)
    msg = Message(topl, text='Please Enter file.',bg='#009966',justify=CENTER)
    msg.pack()
    button = Button(topl, text="Okay", bg='black' ,fg='#009966' ,relief='flat',borderwidth=0, width=22, activebackground='#009966',activeforeground='white',command=topl.destroy)
    button.pack()
def aboutmeep():
    top = Toplevel(master=None,bg='#009966')
    top.resizable(0,0)
    top.title("About m.e.e.p")
    msg = Message(top, text='M.E.E.P. is short for Mark Entry Evaluation Program. Its a program made purely in Python which analyses the Marksheet file provided by the CBSE Board and instantly returns an analysis of scores along with the top-scorers for an easy review, reducing workload for the teachers.\n\nThis program was created by Arvindcheenu (c) 2015-2018. Deploy-Build Version: 2.0.1.',bg='#009966',justify=CENTER)
    msg.pack()
    button = Button(top, text="Okay", width=40, bg='black' ,fg='#009966' ,relief='flat',borderwidth=0, activebackground='#009966',activeforeground='white',command=top.destroy)
    button.pack()
def success():
    tops = Toplevel(master=None,bg='#009966')
    tops.resizable(0,0)
    msgs = Message(tops, text='File successfully analysed. Find the text file in the directory you chose.',bg='#009966',justify=CENTER)
    msgs.pack()
    button = Button(tops, text="Thanks!",width=18, bg='black' ,fg='#009966' ,relief='flat',borderwidth=0, activebackground='#009966',activeforeground='white',command=root.destroy)
    button.pack()
def file_open():
        """open a file to read"""
        mask = \
        [("Text and Python files","*.txt *.py *.pyw"),
        ("HTML files","*.htm *.html"),
        ("All files","*.*")]
        fin = tkfd.askopenfile(filetypes=mask, mode='r', title='Open CBSE File to read...')
        if fin==None:
            error_nofile()
        else:
            text = fin.read()
            try:
                meep_run(text)
            except Exception:
                error_wrongfile()
#=======================
#MAIN FUNCTION TO BE RUN
#=======================
def meep_run(string):
    content = string.splitlines()
    maindata=content[8:-4]
    report=[]
    names_unedited=[]
    names_edited=[]
    for line in maindata:
        word=list(line.split(' '))
        datalist=[]
        for i in range(len(word)):
            if word[i]=='':
                pass
            else:
                datalist.append(word[i])
            #COMBINING NAME:
            str=' '
            namelist=[]
            for i in range(0,len(datalist)):
                if datalist[i].isalpha()==True and datalist[i]!='PASS' and datalist[i]!='FAIL' :
                    namelist.append(datalist[i])
                else:
                    pass
        names_unedited.append(namelist)
        report.append(datalist)
    for i in range(0,len(names_unedited)):
        str=' '
        named=str.join(names_unedited[i])
        names_edited.append(named)
    rolllist=[]
    for i in range(0,len(report)):
        roll=report[i][0]
        rolllist.append(roll)
    studict=OrderedDict(zip(rolllist, names_edited))
    subdict=OrderedDict([('301','ENGLISH\nCORE'),
    ('030','ECONOMICS'),
    ('041','MATHS'),
    ('042','PHYSICS'),
    ('043','CHEMISTRY'),
    ('044','BIOLOGY'),
    ('054','BUSINESS\nSTUDIES'),
    ('083','COMPUTER\nSCIENCE'),
    ('075','HUMANITIES'),
    ('055','ACCOUNTANCY')])
    nameless_data=[]
    passes=[]
    fails=[]
    for lists in report:
        for item in lists:
            if item=='PASS':
                passes.append('PASS')
            if item=='FAIL':
                fails.append('FAIL')
            if item.isalpha()==True and item!='PASS' and item!='FAIL' :
                lists.remove(item)
    passed=(len(passes)/len(rolllist))*100
    failed=(len(fails)/len(rolllist))*100
    pie=[passed,failed]
    sub_attended=[]
    for L in report:
        l=L[2:17]#works for only 5 subject grading system
        sub_attend=[]
        for i in range(0,len(l),3):
            sub_attend.append(l[i])
        sub_attended.append(sub_attend)
    for i in range(0,len(rolllist)):
        for j in range(0,len(sub_attended)):
            if i==j:
                sub_attended[j].insert(0,(rolllist[i]))
    mark_scored=[]
    for L in report:
        l=L[3:17]#works for only 5 subject grading system
        mark_score=[]
        for i in range(0,len(l),3):
            mark_score.append(l[i])
        mark_scored.append(mark_score)
    for i in range(0,len(rolllist)):
        for j in range(0,len(mark_scored)):
            if i==j:
                mark_scored[j].insert(0,(rolllist[i]))
    grade_scored=[]
    for L in report:
        l=L[4:17]#works for only 5 subject grading system
        grade_score=[]
        for i in range(0,len(l),3):
            grade_score.append(l[i])
        grade_scored.append(grade_score)
    for i in range(0,len(rolllist)):
        for j in range(0,len(grade_scored)):
            if i==j:
                grade_scored[j].insert(0,(rolllist[i]))
    #======================================================================
    #MANIPULATION OF LISTS:
    #======================================================================
    filePath= tkfd.asksaveasfilename(title='Save Analysed CBSE Marksheet as...')
    with open(filePath,'w+') as fr:
        avglist=[]
        fr.write('=============================================================================\n')
        fr.write(' M.E.E.P. ANALYSIS OF FILE:\n')
        fr.write((' FILEPATH: {}\n').format(filePath))
        for subcode in subdict:
            mainsub=[]
            for l in mark_scored:
                for j in sub_attended:
                    sub=[]
                    for i in range(0,len(l)):
                        if l[0]==j[0]:
                            if j[i]==subcode:
                                sub.append(l[i])
                    mainsub.append(sub)
            mainsub_filtered = [int(''.join(x)) for x in mainsub if x != []]
            submarks= mainsub_filtered #filtered subject-mark list
            maxm=int(max(tuple(submarks)))
            minm=int(min(tuple(submarks)))
            avg=int(sum(submarks)/len(submarks))
            favg=float(avg)
            avglist.append(favg)
            above_ninety=[]
            eighty_to_ninety=[]
            seventy_to_eighty=[]
            sixty_to_seventy=[]
            fifty_to_sixty=[]
            forty_to_fifty=[]
            below_forty=[]
            toppers=[]
            for i in range(0,len(submarks)):
                if submarks[i]>90:
                    above_ninety.append(submarks[i])
                elif submarks[i]>80 and submarks[i]<=90:
                    eighty_to_ninety.append(submarks[i])
                elif submarks[i]>70 and submarks[i]<=80:
                    seventy_to_eighty.append(submarks[i])
                elif submarks[i]>60 and submarks[i]<=70:
                    sixty_to_seventy.append(submarks[i])
                elif submarks[i]>50 and submarks[i]<=60:
                    fifty_to_sixty.append(submarks[i])
                elif submarks[i]>40 and submarks[i]<=50:
                    forty_to_fifty.append(submarks[i])
                elif submarks[i]<40:
                    below_forty.append(submarks[i])
            #TOPPER LIST:
            topperlist=[]
            topperlist_filtered=[]
            complete_topperlist=[]
            for sublists in sub_attended:
                if subcode in sublists:
                    for mark_score in mark_scored:
                        toppers=[]
                        if sublists[0]==mark_score[0]:
                            markonsub=mark_score[sublists.index(subcode)]
                            correspondroll=mark_score[0]
                            if markonsub==('0{}'.format(maxm)):
                                toppers.append(correspondroll)
                                for i in toppers:
                                    if i!=[]:
                                        topperlist.append(toppers)
            [topperlist_filtered.append(topper) for topper in topperlist if topper not in topperlist_filtered]
            toppertuple=[]        
            try:
                for i in range(len(sub_attended)):
                    toppertuple.append([subcode, ''.join(topperlist[i])])
            except IndexError:
                pass
            fr.write('=============================================================================\n')
            fr.write( ' BRIEF SUMMARY OF CLASS PERFORMANCE IN {}:'.format(subdict[subcode])+'\n')
            fr.write('=============================================================================\n')
            fr.write(' MAXIMUM SCORED IN '+subdict[subcode]+' : {}'.format(maxm)+'\n')
            fr.write(' MINIMUM SCORED IN '+subdict[subcode]+' : {}'.format(minm)+'\n')
            fr.write(' CLASS PERCENTAGE IN '+subdict[subcode]+' : {}'.format(avg)+'%\n')
            fr.write(' NUMBER OF STUDENTS SCORING ABOVE 90 : {}'.format(len(above_ninety))+'\n')
            fr.write(' NUMBER OF STUDENTS SCORING 80 TO 90 : {}'.format(len(eighty_to_ninety))+'\n')
            fr.write(' NUMBER OF STUDENTS SCORING 70 TO 80 : {}'.format(len(seventy_to_eighty))+'\n')
            fr.write(' NUMBER OF STUDENTS SCORING 60 TO 70 : {}'.format(len(sixty_to_seventy))+'\n')
            fr.write(' NUMBER OF STUDENTS SCORING 50 TO 60 : {}'.format(len(fifty_to_sixty))+'\n')
            fr.write(' NUMBER OF STUDENTS SCORING 40 TO 50 : {}'.format(len(forty_to_fifty))+'\n')
            fr.write(' NUMBER OF STUDENTS SCORING BELOW 40 : {}'.format(len(below_forty))+'\n')
            fr.write('=============================================================================\n')
            fr.write( ' TOPPERS IN {}:'.format(subdict[subcode])+'\n')
            fr.write('=============================================================================\n')
            fr.write(' ROLL.NO -------+------- STUDENT-NAME'+'\n')
            for i in toppertuple:
                if i[0]==subcode:
                    fr.write((' {0} -------|------- {1} ').format(i[1],studict[i[1]])+'\n')
            fr.write('=============================================================================\n')
            fr.write('\n')
        schoolavg=float(sum(avglist)/len(avglist))
        #============
        #PREVIEW FILE
        #============
        txt=open(filePath,'r+')
        text=txt.read()
        see_for_yourself(text)
        #===================
        #PASS/FAIL PIE CHART
        #===================
        pies=plt.figure(figsize=(5,5),facecolor='black')
        pies.canvas.set_window_title('Pass or Fail percentage Graph')
        labels = 'Pass ({}%)'.format(pie[0]), 'Fail ({}%)'.format(pie[1])
        sizes = pie
        colors = ['yellowgreen', 'orangered']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.figtext(0.5, 0.95, "Pass or Fail percentage", fontsize='large', color='white', ha ='center')
        plt.axis('equal')
        #=================================
        #SCHOOL AVERAGE CONTRIBUTORS GRAPH
        #=================================
        dictionary=plt.figure(figsize=(10,10),facecolor='#009966')
        dictionary.canvas.set_window_title('Graph for Average Score Contributors (view in fullscreen and use snipping tool to save graph)')
        ax = dictionary.add_subplot(111)
        ax.spines['bottom'].set_color('yellowgreen')
        ax.spines['top'].set_color('yellowgreen')
        ax.spines['right'].set_color('yellowgreen')
        ax.spines['left'].set_color('yellowgreen')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.set_axis_bgcolor('#009966')
        dictionary.patch.set_facecolor('black')
        subjects=subdict.values()
        dicts=OrderedDict(zip(subjects,avglist))
        rects=ax.bar(range(len(dicts)),dicts.values(),align='center', color='black',edgecolor='none')
        plt.xticks(range(len(dicts)),dicts.keys())
        plt.figtext(0.5, 0.95, "School Average Contributors", fontsize='large', color='white', ha ='center')
        plt.plot([-0.5,float(len(subjects))], [schoolavg,schoolavg], "k--", color='white')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Average Scores (in %)')
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                '%d' % int(height),
                ha='center', va='bottom',color='black')
        im = plt.imread("stripe.png") 
        plt.xlim([-0.5,float(len(subjects))]) 
        plt.ylim([0.00,100.0])
        plt.imshow(im, aspect="auto", extent=(-0.5, float(len(subjects)), 0.00, 100.0))
        plt.show()
#===
#GUI
#===
root = Tk()
root.title('M-E-E-P')
root.iconbitmap(default='meeptitlebar.ico')
root.resizable(0,0)
root.config(bg='#009966')
root.wm_geometry('250x250')
cwgt=Canvas(root)
cwgt.config(bg='#009966')
cwgt.pack(expand=True, fill=BOTH)
image1=PhotoImage(file="tkbg.gif")
info=PhotoImage(file="info.gif")
upload=PhotoImage(file="openfile.gif")
cwgt.img=image1
cwgt.create_image(0, 0, anchor=NW, image=image1)
b1=Button(cwgt, compound=TOP, image=info, command=aboutmeep, background='white', bd=0)
cwgt.create_window(63,140, window=b1,anchor=NW)
b2=Button(cwgt, compound=TOP, image=upload, command=file_open, background='white', bd=0)
cwgt.create_window(157,140, window=b2, anchor=NW)
root.mainloop()
