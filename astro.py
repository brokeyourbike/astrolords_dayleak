#!/usr/bin/env python3

"""
Some automation for Astrolords.
"""
import sys
import time
import win32api
import win32con
from PIL import ImageGrab
from pywinauto import application, mouse

cords = (1050, 585)
x2_cords = (1050, 585)
x5_cords = (1050, 640)


def run():

	path_to_astro = r'C:\Program Files (x86)\Astro Lords\Astrolords.exe'
	app = application.Application()

	try:
		app.connect(path=path_to_astro, title="Astro Lords")
		sep = '-' * 30
		print(sep)
		print('Connected to Astrolords.')
		print(sep)
		return app
	except application.ProcessNotFoundError:
		print('Can\'t connect to Astrolords :(')
		return False


def core(app):

	app.AstroLords.set_focus()
	app.AstroLords.draw_outline()
	app.AstroLords.move_window(x=200, y=200)

	mouse.move(coords=cords)

	get_box = (906, 641, 910, 644)
	# color_1 = [x for x in range(4, 5)]
	# color_2 = [x for x in range(150, 180)]
	# color_3 = [x for x in range(20, 40)]

	for i in range(10):
		tmp = []
		image = ImageGrab.grab(get_box)
		pre_color = image.getpixel((3, 1))
		tmp.append(pre_color[0])
		if len(tmp) > 2:
			if pre_color[0] == tmp[-1]:
				break

	print('TARGET RGB =', pre_color[0], pre_color[1], pre_color[2])

	while True:
		image = ImageGrab.grab(get_box)
		color = image.getpixel((3, 1))

		if color[0] != pre_color[0]:
			if color[1] != pre_color[1]:
				if color[2] != pre_color[2]:
					click(cords[0], cords[1])
					print('NOT RGB =', color[0], color[1], color[2])
					return True
					break


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


if __name__ == "__main__":
	core(run())
