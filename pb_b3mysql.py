#!/usr/bin/python
# -*- coding: utf_8 -*-
# 
# PB_B3MySQL Create database - Import SQL Script into database
# Copyright (C) 2012 PtitBigorneau
#
# PtitBigorneau www.ptitbigorneau.fr
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

#import pymysql
import pymysql
import os, sys

__author__  = 'PtitBigorneau'
__version__ = 'b2.0'

def dimportsql():

    datadupnbd = dupnbd()

    user = datadupnbd[0]
    pwduser = datadupnbd[1]
    bdname = datadupnbd[2]
    print ""         

    importsql(user, pwduser, bdname)
    d2importsql(user, pwduser, bdname)

def d2importsql(user, pwduser, bdname):

    print ""
    print "Do you want to import another SQL script ?" 
    q2 = raw_input("(yes/no) ? : ")
    print ""    

    if q2 == "yes":
       
        importsql(user, pwduser, bdname)
        d2importsql(user, pwduser, bdname)        

    if q2 != "yes":

        main()

def dpwdroot():

    print ""
    pwdroot = raw_input("Root Password ? : ")
    testroot = dtestbd("root", pwdroot, "mysql")
    
    if testroot == True:

        data3 = qupnbd()
        user = data3[0]
        pwd = data3[1]
        namebd = data3[2]

        testbd = dtestbd(user, pwd, namebd)
    
        if testbd == True:

            print 'ERROR ! %s Database already exist'%namebd
            sys.exit()

        if testbd == False:

            dcreateuser(pwdroot, user, pwd)
            dcreatebs(pwdroot, user, pwd, namebd)
            print""
            print "Do you want to import SQL script ?" 
            q4 = raw_input("(yes/no) ? : ")
            print ""    

            if q4 == "yes":
       
                importsql(user, pwd, namebd)
                d2importsql(user, pwd, namebd)        

            if q4 != "yes":

                main() 

    if testroot == False:

        print 'ERROR Root Password !'
        sys.exit()

def dupnbd():
    
    data2 = qupnbd()
    user = data2[0]
    pwd = data2[1]
    namebd = data2[2]

    testbd = dtestbd(user, pwd, namebd)
    
    if testbd == True:

        return user, pwd, namebd

    if testbd == False:

        print 'ERROR Access Database'
        sys.exit()

def qupnbd():

    print ""
    user = raw_input("user name : ")
    pwd = raw_input("user password : ")
    namebd = raw_input("database name (%s) : "%user)
    
    if namebd == "":
        namebd = user
    
    return user, pwd, namebd    

def dtestbd(user, pwd, namebd):

    try: 

        conn=pymysql.connect('localhost', user, pwd, namebd)
        
        return True
    
    except:
        
        return False

def importsql(user, pwduser, bdname):

    ficsql  = raw_input("SQL File to import into your database ? : ")
    ficsql = ficsql.replace('/','//')

    try:
    
        file(ficsql)
        print "%s file found"%ficsql
        testfich = "ok"

    except:
  
        print "ERROR ! %s file not found"%ficsql
        testfich = "no"

    if testfich == "ok":

        command = os.system("mysql -u %s -p%s -h localhost -D %s < %s"%(user, pwduser, bdname, ficsql))

        if command == 1: 
               print "ERROR ! %s file not imported ! SQL tables already exist"%ficsql 
        else:
            print "%s file imported into the database"%ficsql

    else:

        print "ERROR ! %s file not imported ! file not found"%ficsql

    return

def dcreateuser(pwdroot, user, pwd):

    proot = pwdroot
    buser = user
    upwd = pwd
    client = "%"

    conn = coroot(proot)
    
    curs = conn.cursor()
    
    print ""

    try:

        curs.execute("CREATE user '%s'@'%s';" %(buser, client))
        curs.execute("SET password FOR '%s'@'%s' = password('%s');" %(buser, client, upwd))
          
        print "%s User created"%buser
    
    except:

        print "The User %s already exist !"%buser
        question1  = raw_input("Do you want to continue ?(yes/no) : ")    

        if question1 != "yes":
            curs.close()
            main()

    curs.close()
    return

def dcreatebs(pwdroot, user, pwd, namebd):

    proot = pwdroot
    buser = user
    upwd = pwd
    bd = namebd
    client = "%"

    conn = coroot(proot)
    curs = conn.cursor()

    print ""

    try:

        curs.execute("CREATE DATABASE %s CHARACTER SET utf8;" % bd)
        curs.execute("GRANT ALL ON %s . * TO '%s'@'%s';" %(bd, buser, client))
        print "%s Database created"%bd
    
    except:

        print "The Database %s already exist !"%bd
        question2  = raw_input("Do you want to continue ?(yes/no) : ")    

        if question2 != "yes":
           curs.close()
           main()

    curs.close()
    return

def coroot(proot):

    try: 

        conn=pymysql.connect('localhost','root', '%s'%(proot))

    except:
 
       print "Acces denied for user 'Root'"
       print "ERROR PASSWORD"
       sys.exit()
    
    return conn

def fin():
    sys.exit()

def main():
    
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print "-----------------------------"

    print ""
    print "Create database or Import SQL script into database ?" 
    q1 = raw_input("(create/import/exit) ? : ")
    
    if q1 == "import":
        
        dimportsql()

    elif q1 == "create":
        
        dpwdroot()

    elif q1 == "exit":
        
        sys.exit()
    
    else:
     
        main()

if __name__ == '__main__':
    main()
