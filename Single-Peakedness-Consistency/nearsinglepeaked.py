'''
	*File:		nearsinglepeaked.py
	*Author:	Yung Pheng Thor
	*Date:		May 17, 2022
	
MIT License

Copyright (c) 2022 Yung Pheng Thor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
	

ABOUT
------------------------------
This prgram calculates the proximity to single-peakedness of a profile.
Definition of proximity to single-peakedness is based on (Niemi 1969; List 2001)


INSTRUCTION
------------------------------
Place all the '.soc' files in the folder 'soc_files' and run this program
'nearsinglepeaked.py'. 

'''


import sys
import glob
import time
from generate_profile import generate_profile
from algo_singlepeaked import algo_isSP
from algo_nearsinglepeaked import calc_nearSP
import time


if __name__ == '__main__':

	start = time.time()
	count = 1
	
	# takes in all files in the soc_files folder
	soc_files = glob.glob('soc_files/*.soc', recursive = True)
	
	for soc_file in soc_files: 
		with open(soc_file, 'r') as file:
			content = file.read().splitlines()
		
		print("  Processing file {} out of {} : {}".format(count, len(soc_files), soc_file[10:]))
		
		# generate a profile for each '.soc' file
		profile = generate_profile(content)

		# calculate the proximity to single-peakedness of the profile and returns 
		# the largest structuring dimension
		proxSP, max_axis_SP = calc_nearSP(profile['nb_voters'], profile['list_weight_preferences'])
		
		print("\t Proximity of single-peakedness :", proxSP)
		print("\t Largest Structuring Dimention :", max_axis_SP)
		
		count += 1
	
	end = time.time()
	print("The time of execution of above program is :", end-start)
	
	input('Press ENTER to exit')