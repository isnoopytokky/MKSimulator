"""
	MKSimulator (Mouse & Keyboard Simulator)
	Description: Send mouse and keyboard behaviours through socket from client 
	and create hardware-level simulation on server using PyUserInput module.
	Author: Phuriphat Boontanon

	About this file: Server-side socket, Mouse and Keyboard Simulator
"""

import socket, sys, errno, json, struct
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from constants import *

def ascii_printable(k):
	if not len(k):
		return False
	return ord(k) < 127 and ord(k) > 32

"""
	TODOs
	- Add other special keys
	- Fix arrow key bugs
"""
def map_special_key(k, k_obj):
	if k >= K_F1 and k <= K_F12:
		k = k_obj.function_keys[k - K_F1 + 1]
	elif k == K_BACKSPACE:
		k = k_obj.backspace_key
	elif k == K_TAB:
		k = k_obj.tab_key
	elif k == K_RETURN:
		k = k_obj.return_key
	elif k == K_RSHIFT:
		k = k_obj.shift_r_key
	elif k == K_LSHIFT:
		k = k_obj.shift_l_key
	elif k == K_RCTRL:
		k = k_obj.ctrl_r_key
	elif k == K_LCTRL:
		k = k_obj.ctrl_l_key
	elif k == K_RALT:
		k = k_obj.alt_r_key
	elif k == K_LALT:
		k = k_obj.alt_l_key
	elif k == K_CAPSLOCK:
		k = k_obj.caps_lock_key
	elif k == K_ESCAPE:
		k = k_obj.escape_key
	elif k == K_SPACE:
		k = 16
	return k


HOST, PORT = '', 8888
version = 'v0.1alpha'
socket_handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	socket_handle.bind((HOST, PORT))
except socket.error as err_msg:
	print '[>] Binding failed [Error code: ' + str(err_msg[0]) + ' | Error message: ' + err_msg[1] + ']'
	print '[>] Exit program'
	sys.exit()
print '[>] Succesfully binded to ' + HOST + ':' + str(PORT) 
socket_handle.listen(1)
print '[>] Initiate listening to incoming connection'
while True:
	connection, client = socket_handle.accept()
	if connection:
		print '[>] Initiate Mouse and Keyboard Object'
		mouse_object = PyMouse()
		keyboard_object = PyKeyboard()
		screen_x, screen_y = mouse_object.screen_size()
		connection.sendall('Welcome to MKSimulator (Mouse & Keyboard Simulator) ' + version)
		print '[<] ' + str(client[0]) + ':' + str(client[1])
		while True:
			try:
				data_len = connection.recv(4)
			except:
				continue
			data_len = struct.unpack('<i', data_len)[0]
			try: 
				recieved_data = connection.recv(data_len)
			except socket.error as err_msg:
				print '[>] Connection closed [Reason: ' + err_msg[1] + ']'
				break
			if not recieved_data:
				print '[>] Connection closed'
				break
			event = json.loads(recieved_data)
			if type(event) != dict:
				continue
			if event['type'] == 'keydown':
				print event
				print_out  = '[>] Pressing key ' + str(event['key'])
				if 'unicode' in event and ascii_printable(event['unicode']):
					keyboard_object.press_key(event['unicode'])
					print_out += ' (' + event['unicode'] + ')'
				else:
					keyboard_object.press_key(map_special_key(event['key'], keyboard_object))
				print print_out

			elif event['type'] == 'keyup':
				print_out = '[>] Releasing key ' + str(event['key'])
				if 'unicode' in event and ascii_printable(event['unicode']):
					keyboard_object.release_key(event['unicode'])
					print_out += ' (' + event['unicode'] + ')'
				else:
					keyboard_object.release_key(map_special_key(event['key'], keyboard_object))
				print print_out
			elif event['type'] == 'mousemotion':
				mouse_object.move(event['pos'][0]*screen_x, event['pos'][1]*screen_y)
				print '[>] Moving mouse cursor to ' + str(event['pos'][0]*screen_x) + ', ' + str(event['pos'][1]*screen_y)
			elif event['type'] == 'mousebuttondown':
				button = 1 if event['button'] == 1 else 2
				mouse_object.press(event['pos'][0]*screen_x, event['pos'][1]*screen_y, button)
				print '[>] Mouse pressing at ' + str(event['pos'][0]*screen_x) + ', ' + str(event['pos'][1]*screen_y)
			elif event['type'] == 'mousebuttonup':
				button = 1 if event['button'] == 1 else 2
				mouse_object.release(event['pos'][0]*screen_x, event['pos'][1]*screen_y, button)
				print '[>] Mouse releasing at ' + str(event['pos'][0]*screen_x) + ', ' + str(event['pos'][1]*screen_y)
		connection.close()
		print '[>] Connection closed'
		break
socket_handle.close()
print '[>] Socket closed'
print '[>] Exit program'

