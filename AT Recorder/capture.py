import subprocess
import sys
import argparse
import shlex
import os
import psutil

#First we define the default values of the main parameters
DEFAULT_RESOLUTION = "1366x768"
DEFAULT_CODEC = "h264"
DEFAULT_OUTPUTFILE = "output.mkv"

#Then we define tuples (immutable) of the supported formats and resolutions.
#Hopefully we'll be able to grab these values automatically in the future
RESOLUTION_LIST = ("1920x1080", "1366x768", "1280x720")
CODEC_LIST = ("mpeg4", "flv", "h264")


#Finally, we call the command and start recording (naturally within try/except clause)
class CaptureScreen(object):
	def __init__(self, resolution=DEFAULT_RESOLUTION, outputfile=DEFAULT_OUTPUTFILE):
		if resolution not in RESOLUTION_LIST:
			raise ValueError("Invalid resolution. Run {0} -h for details".format(__file__))
		self.command = "ffmpeg -video_size {0} -framerate 25 \
						-f x11grab -i :0.0 -f pulse -ac 2 -i default {1}"\
						.format(resolution, outputfile)
		self.arguments = shlex.split(self.command)

	def start(self):
		try:
			self.process = subprocess.Popen(self.arguments)
			self.resumable_process = psutil.Process(self.process.pid)
			# self.process.communicate()[0]
			return True
		except Exception as e:
			print("The error is {0}".format(str(e)))
			return False

	def stop(self):
		self.process.kill()

	def resume(self):
		self.resumable_process.resume()

	def pause(self):
		self.resumable_process.suspend()
		
	


