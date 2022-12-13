# The Pi Hut Advent

### Exploring the Raspberry Pi Pico with 12 Projects from The Pi Hut

This repo is for me to keep track of the projects I build with the components in the [the Pi Hut Advent Calendar](https://thepihut.com/pages/advent) and to have as a reference for myself.

## Day 1 - Set up

### The [first day](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-1-getting-started) focuses on setting up and getting familiar with the Pico.

Pico Info:

- RP2040 microcontroller chip
- GPIO (General Purpose Input Output) pins
- [A map of Pico pins here](https://cdn.shopify.com/s/files/1/0176/3274/files/Pico-R3-A4-Pinout_f22e6644-b3e4-4997-a192-961c55fc8cae.pdf?v=1664490511)

### Software set up with [Thonny](https://thonny.org/).

The instructions here didn't work for me as there is a known issue with Mac. There's a [blog post](https://www.raspberrypi.com/news/the-ventura-problem/) from Raspberry Pi going into detail on this, but their suggested fixes didn't work for me. After some reading for potential fixes, I did the following, which ended up being closer to the actual Raspberry Pi docs:

- connected Pico to Mac holding the `BOOTSEL` button on the Pico
- A drive called `RP1-RP2` appears in the sidebar in finder
- Navigate to the [Raspberry Pi Docs for MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html). Or go through the Pico by:
  - Open the `RP1-RP2` drive
  - Open the `index.htm` file ([takes you here](https://www.raspberrypi.com/documentation/microcontrollers/))
  - Open the link to the Getting help with MicroPython
- Go to section on Drag and Drop MicroPython
- Download the correct MicroPython UF2 file for the Pico board
- Drag and drop the UF2 file from downloads to the `RP1-RP2` drive
- The file copies over and the Pico reboots
- Here you'll encounter the bug, a message is displayed saying `Disk Not Ejected Properly` - ignore it
- Disconnect/reconnect the USB **without** holding the `BOOTSEL` button - the drive should not appear in the sidebar
- Open a terminal and run this command `ls -ls /dev/cu.*`
- Listed you should see something like `/dev/cu.usb...` - showing the Pico is connected
- Open Thonny
- In the bottom right hand corner click on `Local Python 3 - Thonny Python`
- Select `MicroPython (Raspberry Pi Pico)` - you should see `/dev/cu.usb...` referenced after on the same line
- That should be it, try writing some code to run on the Pico!

Following on from this I did check the [day 1 instructions on the Pi Hut's website](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-1-getting-started) under 'Setting up Thonny' and did the following when the Pico was connected:

- Open Thonny and navigate to `Run > Configure Interpreter` in the menu bar
- Under `Port`, there's drop down which should have your Pico listed something like `Board in FS Mode (/dev/cu.usb...)`

### Setting up with VS Code

To do

## Day 2 - LEDs

### The [second day](https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-2-let-s-get-blinky) focuses on LEDs.

![Day 2 Full Circuit](day2/day-02-full-circuit.webp)

text
