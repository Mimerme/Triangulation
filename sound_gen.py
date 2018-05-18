#Generates sounds given an equation

import pyaudio

'''
frequency: should probably be calculated in the code
but for now it can be calculated by hand

step_over: length of each step when calculating the
new amplitude

length: how many steps to take over the function 
'''
frequency = 0.2
step_over = 0.01
length = 20000

#Equation of sound
def sound_equation(input):
	pass

def calc_freq(equation):
	for x in range(0, length):
		equation() 



