#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-07-28 15:06:00
# @Author  : Yj (1017955226@qq.com)
# @Link    : HVDC & FACTS GROUP @ http://www.hvdc.cn/
# @Version : $Id$

import os
import Tkinter, Tkconstants, tkFileDialog
from globalvar import *

class TkOpenCsv(Tkinter.Frame):

    def __init__(self, root):  

        Tkinter.Frame.__init__(self, root)  

        # options for buttons  
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 100, 'pady': 100}  

        # define buttons  
        Tkinter.Button(self, text='选择直流输入文件', command=self.askopenfilename).pack(**button_opt)  

        t_path = os.getcwd()

        self.file_opt = options = {}  
        options['defaultextension'] = '.csv'  
        options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]  
        options['initialdir'] = t_path  
        options['initialfile'] = 'Dcinput.csv'  
        options['parent'] = root  
        options['title'] = 'Choose Dcinput file '  

    def askopenfilename(self):  

        """Returns an opened file in read mode. 
        This time the dialog just returns a filename and the file is opened by your own code. 
        """  

        # get filename  
        filename = tkFileDialog.askopenfilename(**self.file_opt)  
        set_Filepath(filename)

        # open file on your own  
        if filename:  
            return open(filename, 'r')  


if __name__== "__main__":
    root = Tkinter.Tk()  
    TkOpenCsv(root).pack()  
    root.mainloop() 
    mypath = get_Filepath()
    print mypath
    print 'Finish!'