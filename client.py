"""
	MKSimulator (Mouse & Keyboard Simulator)
	Description: Send mouse and keyboard behaviours through socket from client 
	and create hardware-level simulation on server using PyUserInput module.
	Author: Phuriphat Boontanon

	About this file: Client-side socket, Mouse and Keyboard Listening
"""

import sys, socket, json, struct, time
import pygame

HOST, PORT = 'localhost', 8888 # TODO: read input from sys.argv instead
socket_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	socket_handle.connect((HOST, PORT))
except socket.error as err_msg:
	print '[>] Connection failed [Error code: ' + str(err_msg[0]) + ' | Error message: ' + err_msg[1] + ']'
	print '[>] Exit program'
	sys.exit()
print '[>] Successfully connected to server'
print socket_handle.recv(1024)


pygame.init()
size = width, height = 0, 0
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
width, height = float(screen.get_width()), float(screen.get_height())
"""
	TODOs
	- Improve logging system
		- Directly draw on pygame screen?
	- Add some features to pygame screen
		- Current connection status
		- Mouse position
		- Key being hold
"""
while 1:
	for event in pygame.event.get():
		data = 'None'
		if event.type == pygame.KEYDOWN:
			data = {'type': 'keydown', 'key': event.key, 'mod': event.mod}
			if hasattr(event, 'unicode'):
				data['unicode'] = event.unicode
		elif event.type == pygame.KEYUP:
			if (event.key == pygame.K_q) and (event.mod & pygame.KMOD_CTRL):
				socket_handle.close()
				sys.exit()
			data = {'type': 'keyup', 'key': event.key, 'mod': event.mod}
			if hasattr(event, 'unicode'):
				data['unicode'] = event.unicode
		elif event.type == pygame.MOUSEMOTION:
			position = [event.pos[0]/width, event.pos[1]/height]
			data = {'type': 'mousemotion', 'pos': position, 'rel': event.rel}
		elif event.type == pygame.MOUSEBUTTONDOWN:
			position = [event.pos[0]/width, event.pos[1]/height]
			data = {'type': 'mousebuttondown', 'button': event.button, 'pos': position}
		elif event.type == pygame.MOUSEBUTTONUP:
			position = [event.pos[0]/width, event.pos[1]/height]
			data = {'type': 'mousebuttonup', 'button': event.button, 'pos': position}
		data = json.dumps(data)
		socket_handle.sendall(struct.pack('<i', len(data)))
		socket_handle.sendall(data)
		print '[>] ' + time.asctime() + ': ' + data