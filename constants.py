"""
	MKSimulator (Mouse & Keyboard Simulator)
	Description: Send mouse and keyboard behaviours through socket from client 
	and create hardware-level simulation on server using PyUserInput module.
	Author: Phuriphat Boontanon

	About this file: Constant variables for key comparison
"""
GL_STEREO = 12
K_F3 = 284
KMOD_LALT = 256
K_F5 = 286
K_F6 = 287
K_F1 = 282
K_F8 = 289
K_F9 = 290
K_COMMA = 44
K_F2 = 283
BLEND_RGBA_MAX = 16
KMOD_RALT = 512
K_COLON = 58
KMOD_NONE = 0
K_AMPERSAND = 38
KMOD_LCTRL = 64
K_CLEAR = 12
K_KP_PLUS = 270
K_KP_EQUALS = 272
AUDIO_U8 = 8
GL_BUFFER_SIZE = 4
SRCALPHA = 65536
K_INSERT = 277
GL_ACCUM_GREEN_SIZE = 9
OPENGLBLIT = 10
K_LSUPER = 311
BLEND_RGB_MAX = 5
HWACCEL = 256
HAT_DOWN = 4
K_RALT = 307
K_KP_PERIOD = 266
K_LSHIFT = 304
JOYBALLMOTION = 8
K_LAST = 323
K_HASH = 35
K_DOWN = 274
JOYAXISMOTION = 7
K_RSUPER = 312
K_ASTERISK = 42
AUDIO_S8 = 32776
AUDIO_U16LSB = 16
SWSURFACE = 0
K_EXCLAIM = 33
K_HELP = 315
K_F12 = 293
K_MENU = 319
K_UNDERSCORE = 95
FULLSCREEN = -2147483648
K_LEFTBRACKET = 91
KMOD_LMETA = 1024
GL_DOUBLEBUFFER = 5
HAT_LEFTDOWN = 12
K_LALT = 308
K_NUMLOCK = 300
K_RMETA = 309
K_SPACE = 32
AUDIO_S16 = 32784
HWSURFACE = 1
K_QUESTION = 63
KMOD_CAPS = 8192
GL_MULTISAMPLESAMPLES = 14
BLEND_RGBA_ADD = 6
MOUSEBUTTONUP = 6
GL_ACCUM_ALPHA_SIZE = 11
BLEND_MIN = 4
JOYBUTTONUP = 11
USEREVENT = 24
BLEND_RGBA_MULT = 8
BIG_ENDIAN = 4321
QUIT = 12
K_LMETA = 310
K_SLASH = 47
K_y = 121
K_x = 120
K_z = 122
K_o = 111
K_q = 113
K_p = 112
K_s = 115
K_r = 114
K_u = 117
K_t = 116
K_w = 119
K_v = 118
K_i = 105
K_h = 104
K_k = 107
K_j = 106
K_m = 109
K_l = 108
IYUV_OVERLAY = 1448433993
K_n = 110
K_a = 97
K_c = 99
K_b = 98
K_e = 101
K_d = 100
K_g = 103
K_f = 102
BUTTON_X2 = 7
K_AT = 64
BUTTON_X1 = 6
YVYU_OVERLAY = 1431918169
K_LESS = 60
KEYDOWN = 2
AUDIO_U16SYS = 16
ACTIVEEVENT = 1
K_9 = 57
K_8 = 56
K_1 = 49
RLEACCELOK = 8192
K_3 = 51
KMOD_LSHIFT = 1
K_5 = 53
K_4 = 52
K_7 = 55
K_6 = 54
YUY2_OVERLAY = 844715353
K_PLUS = 43
K_RIGHTPAREN = 41
MOUSEBUTTONDOWN = 5
NOFRAME = 32
JOYBUTTONDOWN = 10
K_RCTRL = 305
K_SYSREQ = 317
K_KP_MINUS = 269
K_PAUSE = 19
BLEND_MULT = 3
YV12_OVERLAY = 842094169
RLEACCEL = 16384
BLEND_RGBA_MIN = 9
GL_GREEN_SIZE = 1
HAT_LEFTUP = 9
KMOD_META = 3072
TIMER_RESOLUTION = 10
HWPALETTE = 536870912
HAT_CENTERED = 0
K_RETURN = 13
SCRAP_CLIPBOARD = 0
AUDIO_U16 = 16
BLEND_RGB_MULT = 3
MOUSEMOTION = 4
K_HOME = 278
GL_ACCUM_RED_SIZE = 8
BLEND_RGB_MIN = 4
K_RIGHT = 275
GL_RED_SIZE = 0
HAT_RIGHT = 2
K_GREATER = 62
K_FIRST = 0
K_RIGHTBRACKET = 93
K_LEFTPAREN = 40
BLEND_RGBA_SUB = 7
K_KP_ENTER = 271
NUMEVENTS = 32
K_END = 279
HAT_LEFT = 8
GL_DEPTH_SIZE = 6
RESIZABLE = 16
OPENGL = 2
K_LCTRL = 306
K_BACKSLASH = 92
K_MINUS = 45
K_0 = 48
SYSWMEVENT = 13
K_2 = 50
BLEND_ADD = 1
K_ESCAPE = 27
K_BACKSPACE = 8
JOYHATMOTION = 9
K_QUOTEDBL = 34
SRCCOLORKEY = 4096
K_RSHIFT = 303
GL_SWAP_CONTROL = 16
KMOD_MODE = 16384
ASYNCBLIT = 4
K_KP_DIVIDE = 267
K_LEFT = 276
SCRAP_SELECTION = 1
GL_ALPHA_SIZE = 3
K_F4 = 285
K_EQUALS = 61
AUDIO_S16LSB = 32784
K_SEMICOLON = 59
KMOD_ALT = 768
KMOD_RMETA = 2048
HAT_RIGHTDOWN = 6
K_UNKNOWN = 0
KMOD_NUM = 4096
BLEND_RGB_ADD = 1
GL_BLUE_SIZE = 2
GL_ACCELERATED_VISUAL = 15
K_EURO = 321
KMOD_CTRL = 192
K_PERIOD = 46
BLEND_SUB = 2
K_KP_MULTIPLY = 268
K_DELETE = 127
K_CARET = 94
LIL_ENDIAN = 1234
KMOD_SHIFT = 3
K_F7 = 288
KMOD_RSHIFT = 2
GL_MULTISAMPLEBUFFERS = 13
HAT_RIGHTUP = 3
K_TAB = 9
GL_ACCUM_BLUE_SIZE = 10
K_MODE = 313
PREALLOC = 16777216
NOEVENT = 0
K_F13 = 294
K_F10 = 291
K_F11 = 292
K_F14 = 295
K_F15 = 296
KEYUP = 3
UYVY_OVERLAY = 1498831189
AUDIO_S16MSB = 36880
KMOD_RCTRL = 128
GL_STENCIL_SIZE = 7
K_UP = 273
ANYFORMAT = 268435456
BLEND_RGB_SUB = 2
K_PAGEUP = 280
K_CAPSLOCK = 301
DOUBLEBUF = 1073741824
K_PRINT = 316
K_SCROLLOCK = 302
VIDEOEXPOSE = 17
K_DOLLAR = 36
K_PAGEDOWN = 281
VIDEORESIZE = 16
AUDIO_U16MSB = 4112
K_BREAK = 318
K_POWER = 320
K_KP6 = 262
K_QUOTE = 39
BLEND_MAX = 5
AUDIO_S16SYS = 32784
HAT_UP = 1
K_KP8 = 264
K_KP9 = 265
K_KP4 = 260
K_KP5 = 261
K_BACKQUOTE = 96
K_KP7 = 263
K_KP0 = 256
K_KP1 = 257
K_KP2 = 258
K_KP3 = 259