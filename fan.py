#!/usr/bin/python3
import subprocess
import syslog
import os
os.environ['DISPLAY']=":0.0"
def setFanSpeed(speed=0):
		settemp_cmd=['/usr/bin/nvidia-settings','-a', '[gpu:0]/GPUFanControlState=1' ,'-a', "[fan:0]/GPUTargetFanSpeed={}".format(speed)]
		subprocess.run(settemp_cmd)

def getCurrentTemp():
		coretmp_cmd=['/usr/bin/nvidia-settings', '-q', 'gpucoretemp', '-t']
#		coretmp_cmd=['nvidia-smi','--query-gpu=temperature.gpu', '--format=csv,noheader,nounits']
		with subprocess.Popen(coretmp_cmd, stdout=subprocess.PIPE) as proc:
				v=int(proc.stdout.read())
				if v>=45:
					setFanSpeed(v)
					syslog.syslog("[D3nFan] Setting GPU Fan speed to {}".format(v))
				else:
					setFanSpeed(0)
					syslog.syslog("[D3nFan] Stopping GPU Fans")
def __main__():
	getCurrentTemp()
	
				
__main__()
