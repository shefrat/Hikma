#!/usr/bin/env python
#! -*- coding:WINDOWS-1256 -*-
# Peferance.py

import pygtk
pygtk.require('2.0')
import gtk
import os

hikma_icon = 'icons/hikma.png'

def ok_window():
  window = gtk.Window()
  window.set_title('حكمة')
  window.set_border_width(20)
  window.set_icon_from_file(hikma_icon)
  window.connect('destroy', lambda w: gtk.main_quit())
  label = gtk.Label('تم تحديث البيانات')
  window.add(label)
  window.show_all()
  gtk.main()

def changed_cb(combobox1):
	index = combobox1.get_active()
	Fopen1 = open('src/userdata.sh', 'w')
	Fopen1.write('')
	if index == 1:
		Fopen1.write('./hikma 1in1')
		ok_window()
	elif index == 2:
		Fopen1.write('./hikma 1')
		ok_window()
	elif index == 3:
		Fopen1.write('./hikma 5')
		ok_window()
	elif index == 4:
		Fopen1.write('./hikma 10')
		ok_window()
	elif index == 5:
		Fopen1.write('./hikma 15')
		ok_window()
	elif index == 6:
		Fopen1.write('./hikma 30')
		ok_window()
	elif index == 7:
		Fopen1.write('./hikma 60')
		ok_window()
	elif index == 8:
		Fopen1.write('./hikma 120')
		ok_window()
	else:
		index = str(index)
		Fopen1.write(index)

last = ''
def lastdef():
	global last
	Fopen2 = open('src/userdata.sh', 'r')
	ifcon = Fopen2.read()
	if ifcon == './hikma 1in1' :
		last = 'حكمة واحدة فقط'
	if ifcon == './hikma 1' :
		last = 'حكمة كل دقيقة'
	if ifcon == './hikma 5' :
		last = 'حكمة كل 5 دقائق'
	if ifcon == './hikma 10' :
		last = 'حكمة كل 10 دقائق'
	if ifcon == './hikma 15' :
		last = 'حكمة كل ربع ساعة'
	if ifcon == './hikma 30' :
		last = 'حكمة كل نصف ساعة'
	if ifcon == './hikma 60' :
		last = 'حكمة كل ساعة'
	if ifcon == './hikma 120' :
		last = 'حكمة كل ساعتين'

lastdef()
window = gtk.Window()
window.set_title('حكمة')
window.set_border_width(20)
window.set_icon_from_file(hikma_icon)
window.connect('destroy', lambda w: gtk.main_quit())
combobox = gtk.combo_box_new_text()
window.add(combobox)
combobox.append_text(last)
combobox.append_text('حكمة واحدة فقط')
combobox.append_text('حكمة كل دقيقة')
combobox.append_text('حكمة كل 5 دقائق')
combobox.append_text('حكمة كل 10 دقائق')
combobox.append_text('حكمة كل ربع ساعة')
combobox.append_text('حكمة كل نصف ساعة')
combobox.append_text('حكمة كل ساعة')
combobox.append_text('حكمة كل ساعتين')
combobox.connect('changed', changed_cb)
combobox.set_active(0)
window.show_all()
gtk.main()
