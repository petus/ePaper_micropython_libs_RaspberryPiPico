# Raspberry_Pi_Pico_ePaper_Si7021
# Example code for Raspberry Pi Pico with 4.2" b/w/r ePaper and Si7021 
# Thanks to
# https://github.com/mcauser/micropython-waveshare-epaper
# https://github.com/ayoy/micropython-waveshare-epd

from machine import Pin, SPI, I2C
import epaper2in9b #import ePaper 4.2" b/w/r
import utime #import timer
import monaco16bold #import font

COLORED = 1
UNCOLORED = 0
w = 400
h = 300

#SPI pins
dc = Pin(12)
cs = Pin(13)
rst = Pin(11)
busy = Pin(10)

# SPI
spi=SPI(0)
spi=SPI(0,100_000)
spi=SPI(0,100_000,polarity=1,phase=1)

# ePaper
epd = epaper2in9b.EPD(spi, cs, dc, rst, busy) # Init ePaper | CLK GP6, MOSI GP7
epd.init()
epd.set_rotate(1)

# create frames
fb_size = int(w * h / 8)
frame_black = bytearray(fb_size)
frame_red = bytearray(fb_size)

epd.clear_frame(frame_black, frame_red)

# write strings to the buffer
epd.draw_rectangle(frame_black, 5, 5, 230, 70, COLORED)
epd.display_string_at(frame_red, 20, 10, "Raspberry Pi Pico", monaco16bold, COLORED)
epd.display_string_at(frame_black, 20, 40, "and ePaper", monaco16bold, COLORED)

# display the frame
epd.display_frame(frame_black, frame_red)

#sleeps
epd.sleep()

#repeat after 60s
utime.sleep(60)
