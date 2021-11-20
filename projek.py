import sys
import math
import time
import random as rd
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

l, t = 1300,650
pos_kotak_awal_x = 0
pos_kotak_awal_y = 0
r,g,b = 232, 93, 4
r2,g2,b2 = 232, 93, 4
bg_r1,bg_g1,bg_b1 = 0.0,0.0,0.2
l_kotak, t_kotak = 1300,650
usap_mulai = t - 1950 # + 800
mulai = 0
tombol_mulai = True
tombol_awal_efek = True
envi_start = 0
ubah_warna_awal = 0
posisi_x_pesawat = 0
posisi_y_pesawat = 0
pause = 0
gerak_benda = 0

def init():
    glClearColor(bg_r1,bg_g1,bg_b1,0.8)
    gluOrtho2D(-l,l,-t,t)

def latar_belakang():
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(l,0)
    glVertex2f(-l,0)
    glVertex2f(0,t)
    glVertex2f(0,-t)
    glEnd()

def kotak_mulai():
    global r,g,b
    global pos_kotak_awal_x, pos_kotak_awal_y

    glColor3ub(r,g,b)
    glBegin(GL_POLYGON)
    glVertex2f(-250,-250)
    glVertex2f(250,-250)
    glVertex2f(250,-50)
    glVertex2f(-250,-50)
    glEnd()

def kotak_mulai_hover():
    global r,g,b

    glColor3ub(r,g,b)
    glBegin(GL_POLYGON)
    glVertex2f(-260,-240)
    glVertex2f(-250,-250)
    glVertex2f(250,-250)
    glVertex2f(260,-240)
    glVertex2f(260,-60)
    glVertex2f(250,-50)
    glVertex2f(-250,-50)
    glVertex2f(-260,-60)
    glEnd() 

def tombol_play():
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-30, -200)
    glVertex2f(-30, -100)
    glVertex2f(50, -150)
    glEnd()

def kotak_keluar():
    global r2,g2,b2

    glColor3ub(r2,g2,b2)
    glBegin(GL_POLYGON)
    glVertex2f(-200,-300)
    glVertex2f(-200,-425)
    glVertex2f(200,-425)
    glVertex2f(200,-300)
    glEnd()

def kotak_keluar_hover():
    global r2,g2,b2

    glColor3ub(r2,g2,b2)
    glBegin(GL_POLYGON)
    glVertex2f(-190,-290)
    glVertex2f(-200,-300)
    glVertex2f(-200,-425)
    glVertex2f(-190,-435)
    glVertex2f(200,-435)
    glVertex2f(210,-425)
    glVertex2f(210,-300)
    glVertex2f(200,-290)
    glEnd()

def opening_mulai_usap(tambah_usap):
    tambah_usap -= 100
    return tambah_usap

def pesawat():
    global posisi_x_pesawat, posisi_y_pesawat
    global tempat_pesawat_x1, tempat_pesawat_x2, tempat_pesawat_x3, tempat_pesawat_x4
    global tempat_pesawat_y1, tempat_pesawat_y2, tempat_pesawat_y3

    # Daerah Pinggir Pesawat
    glColor3ub(255,255,255)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(0+posisi_x_pesawat,-275+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-375+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-375+posisi_y_pesawat)
    glVertex2f(-200+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-200+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-60+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-60+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-50+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-50+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-0+posisi_x_pesawat,-470+posisi_y_pesawat)
    glVertex2f(-0+posisi_x_pesawat,-470+posisi_y_pesawat)
    glVertex2f(50+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(50+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(60+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(60+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(200+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(200+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-375+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-375+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(0+posisi_x_pesawat,-275+posisi_y_pesawat)
    glEnd()

    # Badan Pesawat
    glColor3ub(200,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0+posisi_x_pesawat,-275+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-375+posisi_y_pesawat)
    glVertex2f(-200+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-60+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-50+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-0+posisi_x_pesawat,-470+posisi_y_pesawat)
    glVertex2f(50+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(60+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(200+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-375+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(0+posisi_x_pesawat,-275+posisi_y_pesawat)
    glEnd()

    # Kepala Pesawat
    glColor3ub(0,255,0)
    glBegin(GL_POLYGON)
    glVertex2f(0+posisi_x_pesawat,-300+posisi_y_pesawat)
    glVertex2f(-30+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(-30+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(-80+posisi_x_pesawat,-360+posisi_y_pesawat)
    glColor3ub(0,0,255)
    glVertex2f(-80+posisi_x_pesawat,-360+posisi_y_pesawat)
    glVertex2f(-30+posisi_x_pesawat,-380+posisi_y_pesawat)
    glVertex2f(-30+posisi_x_pesawat,-380+posisi_y_pesawat)
    glColor3ub(255,0,0)
    glVertex2f(0+posisi_x_pesawat,-430+posisi_y_pesawat)
    glVertex2f(0+posisi_x_pesawat,-430+posisi_y_pesawat)
    glVertex2f(30+posisi_x_pesawat,-380+posisi_y_pesawat)
    glVertex2f(30+posisi_x_pesawat,-380+posisi_y_pesawat)
    glVertex2f(80+posisi_x_pesawat,-360+posisi_y_pesawat)
    glVertex2f(80+posisi_x_pesawat,-360+posisi_y_pesawat)
    glVertex2f(30+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(30+posisi_x_pesawat,-350+posisi_y_pesawat)
    glVertex2f(0+posisi_x_pesawat,-300+posisi_y_pesawat)
    glEnd()

    # Nitro / Nos Sisi Kiri
    glColor3ub(255,100,0)
    glBegin(GL_POLYGON)
    glVertex2f(-100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(-80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(-70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glColor3ub(255,0,0)
    glVertex2f(-70+posisi_x_pesawat,-470+posisi_y_pesawat)
    glVertex2f(-100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glEnd()

    # Nitro / Nos Sisi Kanan
    glColor3ub(255,100,0)
    glBegin(GL_POLYGON)
    glVertex2f(100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glVertex2f(80+posisi_x_pesawat,-440+posisi_y_pesawat)
    glVertex2f(70+posisi_x_pesawat,-440+posisi_y_pesawat)
    glColor3ub(255,0,0)
    glVertex2f(70+posisi_x_pesawat,-470+posisi_y_pesawat)
    glVertex2f(100+posisi_x_pesawat,-450+posisi_y_pesawat)
    glEnd()

def efek_turun():
    global gerak_benda
    if gerak_benda <= -1500:
        gerak_benda = 0
    else:
        gerak_benda -= 0.5

def animasi_turun():
    # data = [asteroid_1, asteroid_2,asteroid_3,asteroid_4,asteroid_5,asteroid_6,asteroid_7,asteroid_8,serpihan_1]
    # data = [asteroid_1(), asteroid_2(),asteroid_3(),asteroid_4(),asteroid_5(),asteroid_6(),asteroid_7(),asteroid_8(),serpihan_1()]
    # data = [asteroid_1(),asteroid_2(),asteroid_3()]
    data = [asteroid_5()]
    # rd.sample(data,k=2)

def asteroid_1():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(151,151,151)
    glBegin(GL_POLYGON)
    glVertex2f(-1000,600+gerak_benda)
    glVertex2f(-1100,600+gerak_benda)
    glVertex2f(-1150,575+gerak_benda)
    glVertex2f(-1125,575+gerak_benda)
    glVertex2f(-1150,555+gerak_benda)
    glColor3ub(117,117,117)
    glVertex2f(-1150,530+gerak_benda)
    glVertex2f(-1120,500+gerak_benda)
    glVertex2f(-1050,500+gerak_benda)
    glVertex2f(-1000,530+gerak_benda)
    glVertex2f(-990,570+gerak_benda)
    glVertex2f(-1000,600+gerak_benda)
    glEnd()

    glColor3ub(102,102,102)
    glBegin(GL_POLYGON)
    glVertex2f(-1075,575+gerak_benda)
    glVertex2f(-1100,550+gerak_benda)
    glVertex2f(-1075,550+gerak_benda)
    glVertex2f(-1075,575+gerak_benda)
    glEnd()

    glColor3ub(102,102,102)
    glBegin(GL_POLYGON)
    glVertex2f(-1030,575+gerak_benda)
    glVertex2f(-1050,525+gerak_benda)
    glVertex2f(-1010,560+gerak_benda)
    glVertex2f(-1030,575+gerak_benda)
    glEnd()

def asteroid_2():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(117,117,117)
    glBegin(GL_POLYGON)
    glVertex2f(1000,575+gerak_benda)
    glVertex2f(965,540+gerak_benda)
    glVertex2f(1025,500+gerak_benda)
    glVertex2f(1060,500+gerak_benda)
    glColor3ub(151,151,151)
    glVertex2f(1075,550+gerak_benda)
    glVertex2f(1070,590+gerak_benda)
    glVertex2f(1040,570+gerak_benda)
    glVertex2f(1040,600+gerak_benda)
    glVertex2f(1000,575+gerak_benda)
    glEnd()

    glColor3ub(102,102,102)
    glBegin(GL_POLYGON)
    glVertex2f(1020,540+gerak_benda)
    glVertex2f(1050,540+gerak_benda)
    glVertex2f(1050,520+gerak_benda)
    glVertex2f(1020,540+gerak_benda)
    glEnd()

def asteroid_3():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(100,50,50)
    glBegin(GL_POLYGON)
    glVertex2f(-900,520+gerak_benda)
    glVertex2f(-870,500+gerak_benda)
    glVertex2f(-820,490+gerak_benda)
    glVertex2f(-770,520+gerak_benda)
    glVertex2f(-750,550+gerak_benda)
    glColor3ub(150,100,100)
    glVertex2f(-760,587+gerak_benda)
    glVertex2f(-790,590+gerak_benda)
    glVertex2f(-820,600+gerak_benda)
    glVertex2f(-860,600+gerak_benda)
    glVertex2f(-890,580+gerak_benda)
    glVertex2f(-900,550+gerak_benda)
    glEnd()
    #bintik
    glColor3ub(50,20,20)
    glBegin(GL_POLYGON)
    glVertex2f(-890,580+gerak_benda)
    glVertex2f(-880,570+gerak_benda)
    glVertex2f(-860,580+gerak_benda)
    glVertex2f(-850,590+gerak_benda)
    glVertex2f(-850,600+gerak_benda)
    glVertex2f(-860,600+gerak_benda)
    glVertex2f(-890,580+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-880,560+gerak_benda)
    glVertex2f(-890,550+gerak_benda)
    glVertex2f(-880,530+gerak_benda)
    glVertex2f(-860,520+gerak_benda)
    glVertex2f(-830,530+gerak_benda)
    glVertex2f(-840,540+gerak_benda)
    glVertex2f(-840,550+gerak_benda)
    glVertex2f(-860,560+gerak_benda)
    glVertex2f(-880,560+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-820,580+gerak_benda)
    glVertex2f(-830,570+gerak_benda)
    glVertex2f(-820,550+gerak_benda)
    glVertex2f(-800,560+gerak_benda)
    glVertex2f(-790,580+gerak_benda)
    glVertex2f(-810,590+gerak_benda)
    glVertex2f(-840,550+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-760,570+gerak_benda)
    glVertex2f(-760,550+gerak_benda)
    glVertex2f(-770,530+gerak_benda)
    glVertex2f(-810,510+gerak_benda)
    glVertex2f(-790,540+gerak_benda)
    glVertex2f(-770,560+gerak_benda)
    glVertex2f(-760,570+gerak_benda)
    glEnd()

def asteroid_4():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(50,100,50)
    glBegin(GL_POLYGON)
    glVertex2f(-650,550+gerak_benda)
    glVertex2f(-640,530+gerak_benda)
    glVertex2f(-650,500+gerak_benda)
    glVertex2f(-580,500+gerak_benda)
    glVertex2f(-520,520+gerak_benda)
    glColor3ub(100,150,100)
    glVertex2f(-500,540+gerak_benda)
    glVertex2f(-516,580+gerak_benda)
    glVertex2f(-548,600+gerak_benda)
    glVertex2f(-580,592+gerak_benda)
    glVertex2f(-600,600+gerak_benda)
    glVertex2f(-630,560+gerak_benda)
    glVertex2f(-650,550+gerak_benda)
    glEnd()
    #bintik
    glColor3ub(20,50,20)
    glBegin(GL_QUADS)
    glVertex2f(-580,500+gerak_benda)
    glVertex2f(-630,515+gerak_benda)
    glVertex2f(-620,540+gerak_benda)
    glVertex2f(-550,510+gerak_benda)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-585,580+gerak_benda)
    glVertex2f(-600,550+gerak_benda)
    glVertex2f(-570,550+gerak_benda)
    glVertex2f(-550,565+gerak_benda)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-520,520+gerak_benda)
    glVertex2f(-500,540+gerak_benda)
    glVertex2f(-507,560+gerak_benda)
    glEnd()

def asteroid_5():
    global pause
    
    if pause != 1:
        efek_turun() 

    glColor3ub(243, 91, 4)
    glBegin(GL_POLYGON)
    glVertex2f(-100,520+gerak_benda)
    glVertex2f(-70,500+gerak_benda)
    glVertex2f(-20,490+gerak_benda)
    glVertex2f(30,520+gerak_benda)
    glVertex2f(50,550+gerak_benda)
    glColor3ub(241, 135, 1)
    glVertex2f(40,587+gerak_benda)
    glVertex2f(10,590+gerak_benda)
    glVertex2f(-20,600+gerak_benda)
    glVertex2f(-60,600+gerak_benda)
    glVertex2f(-90,580+gerak_benda)
    glVertex2f(-100,550+gerak_benda)
    glEnd()
    #bintik
    glColor3ub(136, 76, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-90,580+gerak_benda)
    glVertex2f(-80,570+gerak_benda)
    glVertex2f(-60,580+gerak_benda)
    glVertex2f(-50,590+gerak_benda)
    glVertex2f(-50,600+gerak_benda)
    glVertex2f(-60,600+gerak_benda)
    glVertex2f(-90,580+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-80,560+gerak_benda)
    glVertex2f(-90,550+gerak_benda)
    glVertex2f(-80,530+gerak_benda)
    glVertex2f(-60,520+gerak_benda)
    glVertex2f(-30,530+gerak_benda)
    glVertex2f(-40,540+gerak_benda)
    glVertex2f(-40,550+gerak_benda)
    glVertex2f(-60,560+gerak_benda)
    glVertex2f(-80,560+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-20,580+gerak_benda)
    glVertex2f(-30,570+gerak_benda)
    glVertex2f(-20,550+gerak_benda)
    glVertex2f(0,560+gerak_benda)
    glVertex2f(10,580+gerak_benda)
    glVertex2f(-10,590+gerak_benda)
    glVertex2f(-40,550+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(40,570+gerak_benda)
    glVertex2f(40,550+gerak_benda)
    glVertex2f(30,530+gerak_benda)
    glVertex2f(-10,510+gerak_benda)
    glVertex2f(10,540+gerak_benda)
    glVertex2f(30,560+gerak_benda)
    glVertex2f(40,570+gerak_benda)
    glEnd()

def asteroid_6():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(157, 78, 221)
    glBegin(GL_POLYGON)
    glVertex2f(150,530+gerak_benda)
    glVertex2f(160,590+gerak_benda)
    glVertex2f(190,600+gerak_benda)
    glVertex2f(350,600+gerak_benda)
    glColor3ub(90, 24, 154)
    glVertex2f(360,570+gerak_benda)
    glVertex2f(330,510+gerak_benda)
    glVertex2f(200,500+gerak_benda)
    glVertex2f(170,510+gerak_benda)
    glVertex2f(150,530+gerak_benda)
    glEnd()
    #bintik
    glColor3ub(60, 9, 108)
    glBegin(GL_QUADS)
    glVertex2f(180,580+gerak_benda)
    glVertex2f(170,540+gerak_benda)
    glVertex2f(220,520+gerak_benda)
    glVertex2f(200,580+gerak_benda)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(220,600+gerak_benda)
    glVertex2f(240,580+gerak_benda)
    glVertex2f(300,570+gerak_benda)
    glVertex2f(280,600+gerak_benda)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(320,590+gerak_benda)
    glVertex2f(340,590+gerak_benda)
    glVertex2f(350,570+gerak_benda)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(230,502+gerak_benda)
    glVertex2f(250,540+gerak_benda)
    glVertex2f(300,507+gerak_benda)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(330,510+gerak_benda)
    glVertex2f(280,550+gerak_benda)
    glVertex2f(350,550+gerak_benda)
    glEnd()

def asteroid_7():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(30, 136, 229)
    glBegin(GL_POLYGON)
    glVertex2f(450,550+gerak_benda)
    glVertex2f(460,530+gerak_benda)
    glVertex2f(450,500+gerak_benda)
    glVertex2f(520,500+gerak_benda)
    glVertex2f(580,520+gerak_benda)
    glColor3ub(100, 181, 246)
    glVertex2f(600,540+gerak_benda)
    glVertex2f(584,580+gerak_benda)
    glVertex2f(552,600+gerak_benda)
    glVertex2f(520,592+gerak_benda)
    glVertex2f(500,600+gerak_benda)
    glVertex2f(470,560+gerak_benda)
    glVertex2f(450,550+gerak_benda)
    glEnd()
    #bintik
    glColor3ub(25, 118, 210)
    glBegin(GL_QUADS)
    glVertex2f(520,500+gerak_benda)
    glVertex2f(470,515+gerak_benda)
    glVertex2f(480,540+gerak_benda)
    glVertex2f(550,510+gerak_benda)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(515,580+gerak_benda)
    glVertex2f(500,550+gerak_benda)
    glVertex2f(530,550+gerak_benda)
    glVertex2f(550,565+gerak_benda)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(580,520+gerak_benda)
    glVertex2f(600,540+gerak_benda)
    glVertex2f(593,560+gerak_benda)
    glEnd()
    
def asteroid_8():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(164, 22, 26)
    glBegin(GL_POLYGON)
    glVertex2f(700,520+gerak_benda)
    glVertex2f(730,500+gerak_benda)
    glVertex2f(780,490+gerak_benda)
    glVertex2f(830,520+gerak_benda)
    glVertex2f(850,550+gerak_benda)
    glColor3ub(229, 56, 59)
    glVertex2f(840,587+gerak_benda)
    glVertex2f(810,590+gerak_benda)
    glVertex2f(780,600+gerak_benda)
    glVertex2f(740,600+gerak_benda)
    glVertex2f(710,580+gerak_benda)
    glVertex2f(700,550+gerak_benda)
    glEnd()
    #bintik
    glColor3ub(102, 7, 8)
    glBegin(GL_POLYGON)
    glVertex2f(710,580+gerak_benda)
    glVertex2f(720,570+gerak_benda)
    glVertex2f(740,580+gerak_benda)
    glVertex2f(750,590+gerak_benda)
    glVertex2f(750,600+gerak_benda)
    glVertex2f(740,600+gerak_benda)
    glVertex2f(710,580+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(720,560+gerak_benda)
    glVertex2f(710,550+gerak_benda)
    glVertex2f(720,530+gerak_benda)
    glVertex2f(740,520+gerak_benda)
    glVertex2f(770,530+gerak_benda)
    glVertex2f(760,540+gerak_benda)
    glVertex2f(760,550+gerak_benda)
    glVertex2f(740,560+gerak_benda)
    glVertex2f(720,560+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(780,580+gerak_benda)
    glVertex2f(770,570+gerak_benda)
    glVertex2f(780,550+gerak_benda)
    glVertex2f(800,560+gerak_benda)
    glVertex2f(810,580+gerak_benda)
    glVertex2f(790,590+gerak_benda)
    glVertex2f(760,550+gerak_benda)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(840,570+gerak_benda)
    glVertex2f(840,550+gerak_benda)
    glVertex2f(830,530+gerak_benda)
    glVertex2f(790,510+gerak_benda)
    glVertex2f(810,540+gerak_benda)
    glVertex2f(830,560+gerak_benda)
    glVertex2f(840,570+gerak_benda)
    glEnd()

def serpihan_1():
    global gerak_benda

    if pause != 1:
        efek_turun()

    glColor3ub(150,150,150)
    glBegin(GL_QUADS)
    glVertex2f(-400,500+gerak_benda)
    glVertex2f(-440,560+gerak_benda)
    glVertex2f(-260,600+gerak_benda)
    glVertex2f(-220,540+gerak_benda)
    glEnd()
    glColor3ub(120,120,120)
    glBegin(GL_QUADS)
    glVertex2f(-160,540+gerak_benda)
    glVertex2f(-180,600+gerak_benda)
    glVertex2f(-260,600+gerak_benda)
    glVertex2f(-220,540+gerak_benda)
    glEnd()
    glColor3ub(243, 50, 0)
    glBegin(GL_QUADS)
    glVertex2f(-400,500+gerak_benda)
    glVertex2f(-440,560+gerak_benda)
    glVertex2f(-400,570+gerak_benda)
    glVertex2f(-360,510+gerak_benda)
    glEnd()
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(-350,580+gerak_benda)
    glVertex2f(-310,520+gerak_benda)
    glVertex2f(-300,590+gerak_benda)
    glVertex2f(-260,530+gerak_benda)
    glVertex2f(-380,540+gerak_benda)
    glVertex2f(-200,585+gerak_benda)
    glEnd()

def pintu_keluar_awal():
    glColor3ub(255,255,255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0,-400)
    glVertex2f(30,-400)
    glVertex2f(30,-400)
    glVertex2f(30,-325)
    glVertex2f(30,-325)
    glVertex2f(-25,-325)
    glEnd()

    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-25,-325)
    glVertex2f(5,-330)
    glVertex2f(5,-330)
    glVertex2f(5,-410)
    glVertex2f(5,-410)
    glVertex2f(-25,-400)
    glVertex2f(-25,-400)
    glVertex2f(-25,-325)
    glEnd()

    glColor3ub(255,255,255)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(-2,-365)
    glEnd()

def pintu_keluar_pause():
    glColor3ub(255,255,255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(300,-125)
    glVertex2f(400,-125)
    glVertex2f(400,-125)
    glVertex2f(400,-250)
    glVertex2f(400,-250)
    glVertex2f(350,-250)
    glEnd()

    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(300,-125)
    glVertex2f(350,-130)
    glVertex2f(350,-250)
    glVertex2f(350,-275)
    glVertex2f(300,-250)
    glVertex2f(300,-125)
    glEnd()

    glColor3ub(255,255,255)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(330,-190)
    glEnd()

def opening():
    global usap_mulai
    global l, t
    
    # dinding / slide permainan
    glBegin(GL_QUADS)
    glColor3ub(0,0,20)
    glVertex2f(usap_mulai, -t)
    glVertex2f(usap_mulai, t)
    glColor3ub(0, 0, 200)
    glVertex2f(l, l)
    glVertex2f(l, -t)
    glEnd()
    
    # if usap_mulai > -l:
    #     time.sleep(0.08)
    #     proses = opening_mulai_usap(usap_mulai)
    #     usap_mulai = proses
    # if usap_mulai <= -l:
    #     mulai_permainan()

def pausing():
    global pausing

    glPushMatrix()
    tanda_pause()
    glPopMatrix()
    
    glPushMatrix()
    layar_pause()
    glPopMatrix()
    
    glPushMatrix()
    pilihan_pause_1()
    glPopMatrix()

    glPushMatrix()
    tanda_kembali()
    glPopMatrix()

    glPushMatrix()
    pilihan_pause_2()
    glPopMatrix()
    
    glPushMatrix()
    pintu_keluar_pause()
    glPopMatrix()

def time_edit_kotak_mulai(value):
    global r,g,b

    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    glutTimerFunc(100, time_edit_kotak_mulai, 0)

def time_edit_kotak_keluar(value):
    global r2,g2,b2

    r2,g2,b2 = randint(0,255),randint(0,255),randint(0,255)
    glutTimerFunc(100, time_edit_kotak_keluar, 0)

def input_mouse(button, state,x,y):
    global r,g,b
    global r2,g2,b2
    global mulai
    global pause
    global tombol_mulai
    global tombol_awal_efek

    # Tombol Awal
    if pause == 0 and tombol_mulai == True and tombol_awal_efek == True:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if ((525 <= x <= 774) and (350 <= y <= 452)):
                time_edit_kotak_mulai(0) 
            if ((550 <= x <= 750) and (475 <= y <= 536)):
                time_edit_kotak_keluar(0)
                mulai = 1

        if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
            if ((525 <= x <= 774) and (350 <= y <= 452)):
                time_edit_kotak_mulai(0)
                mulai = 2
            if ((550 <= x <= 750) and (475 <= y <= 536)):
                glutLeaveMainLoop()

    # Tombol Pause
    if (pause == 0 or pause == 1) and tombol_mulai == False and tombol_awal_efek == False:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            # Tombol Pause 
            if ((12 <= x <= 31) and (25 <= y <= 50)):
                pause += 1
                if pause == 2:
                    pause = 0
            # Tombol Kembali
            if ((327 <= x <= 621) and (351 <= y <= 489)):
                pause = 0
            # Tombol Keluar
            if ((681 <= x <= 921) and (351 <= y <= 489)):
                glutLeaveMainLoop()

def input_keyboard(key,x,y):
    global posisi_x_pesawat, posisi_y_pesawat
    global pause 

    if pause != 1:
        if key == GLUT_KEY_UP:
            posisi_y_pesawat += 20
        if key == GLUT_KEY_DOWN:
            posisi_y_pesawat -= 20
        if key == GLUT_KEY_RIGHT:
            posisi_x_pesawat += 20
        if key == GLUT_KEY_LEFT:
            posisi_x_pesawat -= 20            

        if posisi_x_pesawat == -1120:
            posisi_x_pesawat += 20
        if posisi_x_pesawat == 1120:
            posisi_x_pesawat -= 20
        if posisi_y_pesawat == -200:
            posisi_y_pesawat += 20
        if posisi_y_pesawat == 940:
            posisi_y_pesawat -= 20

def tanda_pause():
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-1275,600)
    glVertex2f(-1260,600)
    glVertex2f(-1260,550)
    glVertex2f(-1275,550)
    glEnd()
    
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-1250,600)
    glVertex2f(-1235,600)
    glVertex2f(-1235,550)
    glVertex2f(-1250,550)
    glEnd()

def layar_pause():
    glColor3ub(0,0,100)
    glBegin(GL_POLYGON)
    glVertex2f(-800,400)
    glColor3ub(0,100,200)
    glVertex2f(800,400)
    glColor3ub(0,0,100)
    glVertex2f(800,-400)
    glColor3ub(0,100,200)
    glVertex2f(-800,-400)
    glEnd()

def pilihan_pause_1():
    glColor3ub(100,0,250)
    glBegin(GL_POLYGON)
    glVertex2f(-600,-50)
    glVertex2f(-100,-50)
    glVertex2f(-50, -75)
    glVertex2f(-50, -300)
    glVertex2f(-100,-325)
    glVertex2f(-600,-325)
    glVertex2f(-650,-300)
    glVertex2f(-650,-75)
    glVertex2f(-600,-50)
    glEnd()

def pilihan_pause_2():
    glColor3ub(100,0,250)
    glBegin(GL_POLYGON)
    glVertex2f(600,-50)
    glVertex2f(100,-50)
    glVertex2f(50, -75)
    glVertex2f(50, -300)
    glVertex2f(100,-325)
    glVertex2f(600,-325)
    glVertex2f(650,-300)
    glVertex2f(650,-75)
    glVertex2f(600,-50)
    glEnd()

def tanda_kembali():
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-425,-200)
    glVertex2f(-350,-125)
    glVertex2f(-350,-200)
    glVertex2f(-275,-125)
    glVertex2f(-275,-250)
    glVertex2f(-350,-200)
    glVertex2f(-350,-250)
    glVertex2f(-425,-200)
    glEnd()

def mulai_permainan():
    global tombol_mulai
    global tombol_awal_efek

    tombol_mulai = False
    tombol_awal_efek = False

    glPushMatrix()
    bintang()
    glPopMatrix()

    glPushMatrix()
    pesawat()
    glPopMatrix()

    glPushMatrix()
    asteroid_1()
    glPopMatrix()

    glPushMatrix()
    asteroid_2()
    glPopMatrix()

    glPushMatrix()
    asteroid_3()
    glPopMatrix()
    
    glPushMatrix()
    serpihan_1()
    glPopMatrix()

    glPushMatrix()
    asteroid_4()
    glPopMatrix()

    glPushMatrix()
    asteroid_5()
    glPopMatrix()

    glPushMatrix()
    asteroid_6()
    glPopMatrix()

    glPushMatrix()
    asteroid_7()
    glPopMatrix()

    glPushMatrix()
    asteroid_8()
    glPopMatrix()

    glPushMatrix()
    tanda_pause()
    glPopMatrix()

    if pause == 1:
        pausing()

def nama():
    #t
    glBegin(GL_QUADS)
    glVertex2f(-775,320)
    glVertex2f(-920,320)
    glVertex2f(-950,286)
    glVertex2f(-775,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-875,320)
    glVertex2f(-840,320)
    glVertex2f(-840,150)
    glVertex2f(-875,150)
    glEnd()

    #u
    glBegin(GL_POLYGON)
    glVertex2f(-720,320)
    glVertex2f(-755,320)
    glVertex2f(-755,218)
    glVertex2f(-754,200)
    glVertex2f(-752,190)
    glVertex2f(-750,180)
    glVertex2f(-745,170)
    glVertex2f(-735,160)
    glVertex2f(-730,155)
    glVertex2f(-725,153)
    glVertex2f(-723,152)
    glVertex2f(-720,151)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-590,184)
    glVertex2f(-720,184)
    glVertex2f(-720,150)
    glVertex2f(-590,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-720,184)
    glVertex2f(-720,200)
    glVertex2f(-715,190)
    glVertex2f(-705,184)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-590,320)
    glVertex2f(-625,320)
    glVertex2f(-625,150)
    glVertex2f(-590,150)
    glEnd()
    
    #r
    glBegin(GL_QUADS)
    glVertex2f(-535,320)
    glVertex2f(-570,320)
    glVertex2f(-570,150)
    glVertex2f(-535,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-405,320)
    glVertex2f(-570,320)
    glVertex2f(-570,286)
    glVertex2f(-405,286)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-405,320)
    glVertex2f(-440,320)
    glVertex2f(-440,218)
    glVertex2f(-435,220)
    glVertex2f(-430,224)
    glVertex2f(-420,234)
    glVertex2f(-407,250)
    glVertex2f(-405,252)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-440,252)
    glVertex2f(-515,252)
    glVertex2f(-515,218)
    glVertex2f(-440,218)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-440,150)
    glVertex2f(-400,150)
    glVertex2f(-450,218)
    glVertex2f(-490,218)
    glEnd()

    #b
    glBegin(GL_QUADS)
    glVertex2f(-350,320)
    glVertex2f(-385,320)
    glVertex2f(-385,150)
    glVertex2f(-350,150)
    glEnd()
    glBegin(GL_POLYGON) #kembung atas
    glVertex2f(-255,320)
    glVertex2f(-250,318)
    glVertex2f(-230,310)
    glVertex2f(-220,295)
    glVertex2f(-220,260)
    glVertex2f(-230,245)
    glVertex2f(-250,237)
    glVertex2f(-255,235)
    glEnd()
    glBegin(GL_POLYGON) #kembung bawah
    glVertex2f(-255,235)
    glVertex2f(-250,233)
    glVertex2f(-230,225)
    glVertex2f(-220,210)
    glVertex2f(-220,175)
    glVertex2f(-230,160)
    glVertex2f(-250,152)
    glVertex2f(-255,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-255,320)
    glVertex2f(-385,320)
    glVertex2f(-385,286)
    glVertex2f(-255,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-255,252)
    glVertex2f(-330,252)
    glVertex2f(-330,218)
    glVertex2f(-255,218)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-255,184)
    glVertex2f(-385,184)
    glVertex2f(-385,150)
    glVertex2f(-255,150)
    glEnd()

    #o
    glBegin(GL_POLYGON)
    glVertex2f(-165,320)
    glVertex2f(-170,318)
    glVertex2f(-190,310)
    glVertex2f(-200,295)
    glVertex2f(-200,150)
    glVertex2f(-165,150)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-70,320)
    glVertex2f(-35,320)
    glVertex2f(-35,175)
    glVertex2f(-45,160)
    glVertex2f(-65,152)
    glVertex2f(-70,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-35,320)
    glVertex2f(-165,320)
    glVertex2f(-165,286)
    glVertex2f(-35,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-70,184)
    glVertex2f(-200,184)
    glVertex2f(-200,150)
    glVertex2f(-70,150)
    glEnd()

    #s
    glBegin(GL_QUADS)
    glVertex2f(70,320)
    glVertex2f(200,320)
    glVertex2f(170,286)
    glVertex2f(70,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(70,252)
    glVertex2f(165,252)
    glVertex2f(165,218)
    glVertex2f(70,218)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(65,184)
    glVertex2f(165,184)
    glVertex2f(165,150)
    glVertex2f(35,150)
    glEnd()
    glBegin(GL_POLYGON) #kembung bawah
    glVertex2f(165,252)
    glVertex2f(170,250)
    glVertex2f(190,242)
    glVertex2f(200,227)
    glVertex2f(200,175)
    glVertex2f(190,160)
    glVertex2f(170,152)
    glVertex2f(165,150)
    glEnd()
    glBegin(GL_POLYGON) #kembung atas
    glVertex2f(70,320)
    glVertex2f(65,318)
    glVertex2f(45,310)
    glVertex2f(35,295)
    glVertex2f(35,243)
    glVertex2f(45,228)
    glVertex2f(65,220)
    glVertex2f(70,218)
    glEnd()

    #p
    glBegin(GL_QUADS)
    glVertex2f(220,320)
    glVertex2f(255,320)
    glVertex2f(255,150)
    glVertex2f(220,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(220,320)
    glVertex2f(385,320)
    glVertex2f(385,286)
    glVertex2f(220,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(275,252)
    glVertex2f(350,252)
    glVertex2f(350,218)
    glVertex2f(275,218)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(385,320)
    glVertex2f(350,320)    
    glVertex2f(350,218)
    glVertex2f(355,220)
    glVertex2f(375,228)
    glVertex2f(385,243)
    glEnd()

    #a
    glBegin(GL_QUADS)
    glVertex2f(405,184)
    glVertex2f(490,184)
    glVertex2f(505,150)
    glVertex2f(405,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(405,184)
    glVertex2f(445,184)
    glVertex2f(505,320)
    glVertex2f(465,320)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(530,150)
    glVertex2f(575,150)
    glVertex2f(505,320)
    glVertex2f(465,320)
    glEnd()

    #c
    glBegin(GL_POLYGON)
    glVertex2f(625,320)
    glVertex2f(620,318)
    glVertex2f(600,310)
    glVertex2f(590,295)
    glVertex2f(590,150)
    glVertex2f(625,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(625,320)
    glVertex2f(755,320)
    glVertex2f(735,286)
    glVertex2f(625,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(590,184)
    glVertex2f(755,184)
    glVertex2f(755,150)
    glVertex2f(590,150)
    glEnd()

    #e
    glBegin(GL_POLYGON)
    glVertex2f(810,320)
    glVertex2f(805,318)
    glVertex2f(785,310)
    glVertex2f(775,295)
    glVertex2f(775,150)
    glVertex2f(810,150)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(810,320)
    glVertex2f(940,320)
    glVertex2f(910,286)
    glVertex2f(810,286)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(775,252)
    glVertex2f(910,252)
    glVertex2f(910,218)
    glVertex2f(775,218)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(775,184)
    glVertex2f(910,184)
    glVertex2f(940,150)
    glVertex2f(775,150)
    glEnd()

def bayang():
    glScaled(1.05,1.05,0)
    glTranslated(0,20,1)
    nama()

def kotak_satelit():
    glColor3ub(200,200,200)
    glBegin(GL_QUADS)
    glVertex2f(-1170,-160)
    glVertex2f(-1210,-290)
    glVertex2f(-1090,-330)
    glVertex2f(-1050,-200)
    glEnd()

    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    #horizontal
    glVertex2f(-1145,-165)
    glVertex2f(-1190,-300)
    glVertex2f(-1120,-170)
    glVertex2f(-1165,-310)
    glVertex2f(-1095,-175)
    glVertex2f(-1140,-320)
    glVertex2f(-1070,-180)
    glVertex2f(-1115,-330)
    #vertical
    glVertex2f(-1210,-270)
    glVertex2f(-1085,-313)
    glVertex2f(-1195,-250)
    glVertex2f(-1060,-295)
    glVertex2f(-1190,-225)
    glVertex2f(-1025,-275)
    glVertex2f(-1185,-200)
    glVertex2f(-1020,-250)
    glVertex2f(-1180,-175)
    glVertex2f(-1015,-225)
    glEnd()

def solar():
    glPushMatrix()
    kotak_satelit()
    glPopMatrix()

    glPushMatrix()
    glTranslated(140,-45,1)
    kotak_satelit()
    glPopMatrix()

    glPushMatrix()
    glTranslated(400,-130,1)
    kotak_satelit()
    glPopMatrix()

    glPushMatrix()
    glTranslated(540,-175,1)
    kotak_satelit()
    glPopMatrix()

def badan_satelit():
    #warna oren
    glColor3ub(r,g,b)
    glBegin(GL_QUADS)
    glVertex2f(-1180,-230)
    glVertex2f(-1190,-240)
    glVertex2f(-550,-440)
    glVertex2f(-540,-430)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-940,-410)
    glVertex2f(-928,-433)
    glVertex2f(-856,-456)
    glVertex2f(-835,-445)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-885,-240)
    glVertex2f(-860,-230)
    glVertex2f(-788,-254)
    glVertex2f(-780,-275)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-828,-150)
    glVertex2f(-820,-145)
    glVertex2f(-757,-170)
    glVertex2f(-755,-178)
    glEnd()
    #abu-abu
    glBegin(GL_QUADS)
    glColor3ub(100,100,100)
    glVertex2f(-885,-240)
    glVertex2f(-940,-410)
    glColor3ub(200,200,200)
    glVertex2f(-835,-445)
    glVertex2f(-780,-275)
    glEnd()
    glBegin(GL_QUADS)
    glColor3ub(100,100,100)
    glVertex2f(-833,-148)
    glVertex2f(-854,-199)
    glColor3ub(200,200,200)
    glVertex2f(-770,-230)
    glVertex2f(-752,-180)
    glEnd()

    glColor3ub(100,100,100)
    glBegin(GL_QUADS)
    glVertex2f(-835,-206)
    glVertex2f(-790,-222)
    glVertex2f(-800,-250)
    glVertex2f(-846,-234)
    glEnd()
    #antena
    glColor3ub(255,255,255)
    glBegin(GL_LINE_STRIP)
    glVertex2f(-816,-146)
    glVertex2f(-774,-128)
    glVertex2f(-788,-158)
    glVertex2f(-774,-128)
    glVertex2f(-760,-169)
    glEnd()
    glColor3ub(r,g,b)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(-774,-128)
    glEnd()

def komet_kuning():
    glBegin(GL_POLYGON)
    glColor3ub(208, 0, 0)
    glVertex2f(-1200,600)
    glColor3ub(255, 186, 8)
    glVertex2f(-1000,500)
    glVertex2f(-993,490)
    glVertex2f(-990,480)
    glVertex2f(-990,470)
    glVertex2f(-1000,450)
    glVertex2f(-1020,440)
    glVertex2f(-1030,440)
    glVertex2f(-1050,450)
    glEnd()

def komet_biru():
    glBegin(GL_POLYGON)
    glColor3ub(63, 55, 201)
    glVertex2f(-1200,600)
    glColor3ub(76, 201, 240)
    glVertex2f(-1000,500)
    glVertex2f(-993,490)
    glVertex2f(-990,480)
    glVertex2f(-990,470)
    glVertex2f(-1000,450)
    glVertex2f(-1020,440)
    glVertex2f(-1030,440)
    glVertex2f(-1050,450)
    glEnd()

def komet_pink():
    glBegin(GL_POLYGON)
    glColor3ub(181, 23, 158)
    glVertex2f(-1200,600)
    glColor3ub(247, 37, 133)
    glVertex2f(-1000,500)
    glVertex2f(-993,490)
    glVertex2f(-990,480)
    glVertex2f(-990,470)
    glVertex2f(-1000,450)
    glVertex2f(-1020,440)
    glVertex2f(-1030,440)
    glVertex2f(-1050,450)
    glEnd()

def kumpulan_komet():
    glPushMatrix()
    komet_kuning()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.5,0.5,0)
    glTranslated(-800,500,1)
    komet_biru()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.7,0.7,0)
    glTranslated(800,100,1)
    komet_kuning()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.7,0.7,0)
    glTranslated(-400,-400,1)
    komet_kuning()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.5,0.5,0)
    glTranslated(-100,300,1)
    komet_kuning()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.3,0.3,0)
    glTranslated(-3000,1300,1)
    komet_biru()
    glPopMatrix()

    glPushMatrix()
    glScaled(1.2,1.2,0)
    glTranslated(500,-550,1)
    komet_biru()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.8,0.8,0)
    glTranslated(-350,-70,1)
    komet_pink()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.9,0.9,0)
    glTranslated(500,80,1)
    komet_pink()
    glPopMatrix()

def bintang():
    glColor3ub(200,200,255)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(-975,-1325)
    glVertex2f(-1118,-528)
    glVertex2f(-778,-479)
    glVertex2f(-510,-186)
    glVertex2f(-412,-265)
    glVertex2f(-760,475)
    glVertex2f(-326,547)
    glVertex2f(-322,547)
    glVertex2f(-614,52)
    glVertex2f(-50,-400)
    glVertex2f(-300,-550)
    glVertex2f(123,-348)
    glVertex2f(330,-389)
    glVertex2f(127,578)
    glVertex2f(166,400)
    glVertex2f(222,70)
    glVertex2f(380,502)
    glVertex2f(80,-20)
    glVertex2f(600,565)
    glVertex2f(700,450)
    glVertex2f(950,560)
    glVertex2f(1170,280)
    glVertex2f(-300,-42)
    glVertex2f(450,0)
    glVertex2f(520,-40)
    glVertex2f(570,30)
    glVertex2f(470,-70)
    glVertex2f(410,-60)
    glVertex2f(390,-10)
    glVertex2f(360,-90)
    glVertex2f(460,-130)
    glVertex2f(510,-150)
    glVertex2f(560,-180)
    glVertex2f(540,-220)
    glVertex2f(630,-80)
    glVertex2f(660,-130)
    glVertex2f(700,-1000)
    glVertex2f(750,-90)
    glEnd()

def ufo():
    #seng
    glColor3ub(100,100,100)
    glBegin(GL_QUADS)
    glVertex2f(800,460)
    glVertex2f(900,400)
    glVertex2f(1060,400)
    glVertex2f(1160,460)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(800,480)
    glVertex2f(900,520)
    glVertex2f(1060,520)
    glVertex2f(1160,480)
    glEnd()
    #kaca
    glColor3ub(76, 201, 240)
    glBegin(GL_QUADS)
    glVertex2f(800,460)
    glVertex2f(800,480)
    glVertex2f(1160,480)
    glVertex2f(1160,460)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(900,520)
    glVertex2f(920,580)
    glVertex2f(940,600)
    glVertex2f(1020,600)
    glVertex2f(1040,580)
    glVertex2f(1060,520)
    glEnd()

def tanah():
    glBegin(GL_POLYGON)
    glColor3ub(165, 99, 54)
    glVertex2f(1300,-520)
    glVertex2f(800,-520)
    glVertex2f(720,-560)
    glVertex2f(400,-560)
    glVertex2f(200,-600)
    glColor3ub(98, 23, 8)
    glVertex2f(100,-650)
    glVertex2f(1300,-650)
    glEnd()
    glColor3ub(50,50,50)
    glBegin(GL_QUADS)
    glVertex2f(1300,-520)
    glVertex2f(1300,-480)
    glVertex2f(840,-480)
    glVertex2f(840,-520)
    glEnd()

def roket():
    #badan besar
    glBegin(GL_POLYGON)
    glColor3ub(255, 7, 0 )
    glVertex2f(970,-450)
    glVertex2f(970,30)
    glVertex2f(980,70)
    glVertex2f(1000,100)
    glVertex2f(1020,120)
    glColor3ub(219, 14, 0)
    glVertex2f(1050,140)
    glVertex2f(1080,120)
    glVertex2f(1100,100)
    glVertex2f(1120,70)
    glVertex2f(1130,30)
    glVertex2f(1130,-450)
    glEnd()
    #samping
    glBegin(GL_POLYGON)
    glColor3ub(244, 140, 6)
    glVertex2f(1130,-460)
    glVertex2f(1130,-100)
    glVertex2f(1140,-60)
    glVertex2f(1165,-50)
    glVertex2f(1190,-60)
    glVertex2f(1200,-100)
    glVertex2f(1200,-460)
    glEnd()
    glPushMatrix()
    glTranslated(-230,0,0)
    glBegin(GL_POLYGON)
    glColor3ub(250, 163, 7)
    glVertex2f(1130,-460)
    glVertex2f(1130,-100)
    glVertex2f(1140,-60)
    glVertex2f(1165,-50)
    glVertex2f(1190,-60)
    glVertex2f(1200,-100)
    glVertex2f(1200,-460)
    glEnd()
    glPopMatrix()
    #tengah
    glBegin(GL_POLYGON)
    glColor3ub(250,250,250)
    glVertex2f(1050,-400)
    glVertex2f(1000,-400)
    glVertex2f(1000,-80)
    glVertex2f(1020,0)
    glVertex2f(1050,20)
    glColor3ub(200,200,200)
    glVertex2f(1080,0)
    glVertex2f(1100,-80)
    glVertex2f(1100,-400)
    glEnd()
    glColor3ub(150,150,150)
    glBegin(GL_QUADS)
    glVertex2f(1000,-450)
    glVertex2f(1000,-350)
    glVertex2f(1100,-350)
    glVertex2f(1100,-450)
    glEnd()
    glColor3ub(0,0,50)
    glBegin(GL_POLYGON)
    glVertex2f(1050,-30)
    glVertex2f(1020,-40)
    glVertex2f(1030,-20)
    glVertex2f(1050,-10)
    glVertex2f(1070,-20)
    glVertex2f(1080,-40)
    glVertex2f(1050,-30)
    glEnd()
    #sayap
    glColor3ub(200,200,200)
    glBegin(GL_TRIANGLES)
    glVertex2f(1100,-450)
    glVertex2f(1100,-150)
    glVertex2f(1250,-450)
    glEnd()
    glColor3ub(250,250,250)
    glBegin(GL_TRIANGLES)
    glVertex2f(1000,-450)
    glVertex2f(1000,-150)
    glVertex2f(850,-450)
    glEnd()
    #alas
    glColor3ub(106, 4, 15)
    glBegin(GL_QUADS)
    glVertex2f(1200,-460)
    glVertex2f(1230,-480)
    glVertex2f(1100,-480)
    glVertex2f(1130,-460)
    glEnd()
    glPushMatrix()
    glTranslated(-230,0,0)
    glBegin(GL_QUADS)
    glVertex2f(1200,-460)
    glVertex2f(1230,-480)
    glVertex2f(1100,-480)
    glVertex2f(1130,-460)
    glEnd()
    glPopMatrix()
    glColor3ub(200,200,200)
    glBegin(GL_QUADS)
    glVertex2f(1040,-480)
    glVertex2f(1040,-300)
    glVertex2f(1060,-300)
    glVertex2f(1060,-480)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(1000,-250)
    glVertex2f(1100,-250)
    glVertex2f(1000,-150)
    glVertex2f(1100,-150)
    glEnd()

def astro():
    #badan
    glColor3ub(250,250,250)
    glBegin (GL_POLYGON)
    glVertex2f (50,50)
    glVertex2f (46,5)
    glVertex2f (25,15)
    glVertex2f (30,110)
    glVertex2f (70,110)
    glVertex2f (75,15)
    glVertex2f (54,5)
    glVertex2f (50,50)
    glEnd ()
    #sepatu
    glColor3ub(200,200,200)
    glBegin (GL_POLYGON)
    glVertex2f (46,5)
    glVertex2f (30,0)
    glVertex2f (19,5)
    glVertex2f (20,10)
    glVertex2f (25,15)
    glEnd ()
    glBegin (GL_POLYGON)
    glVertex2f (54,5)
    glVertex2f (70,0)
    glVertex2f (81,5)
    glVertex2f (80,10)
    glVertex2f (75,15)
    glEnd ()
    #kepala
    glColor3ub (255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(30,110)
    glVertex2f(20,116)
    glVertex2f(15,120)
    glVertex2f(10,130)
    glVertex2f(6,140)
    glVertex2f(6,160)
    glVertex2f(10,170)
    glVertex2f(20,180)
    glVertex2f(30,186)
    glVertex2f(40,189)
    glVertex2f(50,190)
    glVertex2f(60,189)
    glVertex2f(70,186)
    glVertex2f(80,180)
    glVertex2f(90,170)
    glVertex2f(94,160)
    glVertex2f(94,140)
    glVertex2f(90,130)
    glVertex2f(85,120)
    glVertex2f(80,116)
    glVertex2f(70,110)
    glVertex2f(50,108)
    glEnd()
    #kaca helm
    glColor3ub(20,20,30)
    glBegin (GL_POLYGON)
    glVertex2f(50,166)
    glVertex2f(30,164)
    glVertex2f(12,155)
    glVertex2f(12.5,140)
    glVertex2f(15,130)
    glVertex2f(30,117.5)
    glVertex2f(50,115)
    glVertex2f(70,117.5)
    glVertex2f(85,130)
    glVertex2f(87.5,140)
    glVertex2f(88,155)
    glVertex2f(70,164)
    glEnd()
    #telinga
    glColor3ub (200,200,200)
    glBegin (GL_QUADS)
    glVertex2f(6,140)
    glVertex2f(6,150)
    glVertex2f(2,150)
    glVertex2f(2,140)
    glEnd()
    glBegin (GL_QUADS)
    glVertex2f(94,140)
    glVertex2f(94,150)
    glVertex2f(98,150)
    glVertex2f(98,140)
    glEnd()
    #tongkat
    glColor3ub (100,100,50)
    glBegin (GL_QUADS)
    glVertex2f (90,2)
    glVertex2f (98,0)
    glVertex2f (120,200)
    glVertex2f (112,202)
    glEnd()
    #bendera
    glColor3ub (255,0,0)
    glBegin (GL_QUADS)
    glVertex2f (120,200)
    glVertex2f (118,175)
    glVertex2f (188,170)
    glVertex2f (190,195)
    glEnd()
    glColor3ub (255,255,255)
    glBegin (GL_QUADS)
    glVertex2f (116,150)
    glVertex2f (118,175)
    glVertex2f (188,170)
    glVertex2f (186,145)
    glEnd()
    #tangan
    glColor3ub (250,250,250)
    glBegin (GL_QUADS)
    glVertex2f (30,110)
    glVertex2f (13,80)
    glColor3ub (200,200,200)
    glVertex2f (28,67)
    glVertex2f (30.5,95)
    glEnd()
    glColor3ub (250,250,250)
    glBegin (GL_QUADS)
    glVertex2f (70,110)
    glVertex2f (101,80)
    glVertex2f (99,70)
    glVertex2f (70,90)
    glEnd()
    glBegin (GL_POLYGON)
    glVertex2f (99,70)
    glVertex2f (101,80)
    glVertex2f (103,83)
    glVertex2f (113,78)
    glVertex2f (110,65)
    glEnd()
    #dada
    glColor3ub(200,200,200)
    glBegin(GL_QUADS)
    glVertex2f(37,95)
    glVertex2f(35,70)
    glVertex2f(65,70)
    glVertex2f(63,95)
    glEnd()

def layar():
    global pause
    global mulai
    global tombol_mulai
    global tombol_awal_efek

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    kumpulan_komet()
    bintang()

    glPushMatrix()
    glColor3ub(33, 35, 72)
    bayang()
    glPopMatrix()

    glPushMatrix()
    glColor3ub(255,255,255)
    nama()
    glPopMatrix()

    solar()
    badan_satelit()

    glPushMatrix()
    glScaled(0.8,0.7,0)
    glRotated(10,0,0,1)
    glTranslated(400,-80,0)
    ufo()
    glPopMatrix()

    glPushMatrix()
    glScaled(0.4,0.4,0)
    glRotated(-25,0,0,1)
    glTranslated(200,1550,0)
    ufo()
    glPopMatrix()

    tanah()
    roket()

    glPushMatrix()
    glScaled(1.1,1.1,0)
    glTranslated(500,-510,0)
    astro()
    glPopMatrix()
    
    if mulai == 0:
        glPushMatrix()
        kotak_mulai()
        glPopMatrix()
        
        glPushMatrix()
        tombol_play()
        glPopMatrix()

        glPushMatrix()
        kotak_keluar()
        glPopMatrix()
        
        glPushMatrix()
        pintu_keluar_awal()
        glPopMatrix()

    if mulai > 0:

        if mulai == 1:

            glPushMatrix()
            kotak_mulai()
            glPopMatrix()
           
            glPushMatrix()
            tombol_play()
            glPopMatrix()

            glPushMatrix()
            kotak_keluar_hover()
            glPopMatrix()
           
            glPushMatrix()
            pintu_keluar_awal()
            glPopMatrix()

        if mulai == 2:
            tombol_mulai = False
            tombol_awal_efek = False

            glPushMatrix()
            kotak_mulai_hover()
            glPopMatrix()
            
            # opening / mulai permainan
            glPushMatrix()
            opening()
            glPopMatrix()
    
    ##################### BAGIAN PERMAINAN ####################
    tombol_mulai = False
    tombol_awal_efek = False

    glPushMatrix()
    opening()
    glPopMatrix()

    glPushMatrix()
    pesawat()
    glPopMatrix()

    glPushMatrix()
    tanda_pause()
    glPopMatrix()

    animasi_turun()

    # glPushMatrix()
    # asteroid_1()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_2()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_3()
    # glPopMatrix()
    
    # glPushMatrix()
    # serpihan_1()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_4()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_5()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_6()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_7()
    # glPopMatrix()

    # glPushMatrix()
    # asteroid_8()
    # glPopMatrix()

    ##################### BAGIAN PAUSE ########################
    # glPushMatrix()
    # opening()
    # glPopMatrix()
    if pause == 1:
        tombol_awal_efek = False
        pausing()
    # pause = 1
    # pausing()

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(l,t)
    glutInitWindowPosition(30,30)
    glutCreateWindow("202410103009 | 202410103039")
    glutDisplayFunc(layar)
    glutIdleFunc(layar)

    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_mouse)

    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
