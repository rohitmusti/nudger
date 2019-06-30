import subprocess
import sys, os
from time import sleep

climate_change = ["climate", "climate change", "earth", "climate issues",
                  "ocean rising", "nature preservation", "ocean", 
                  "global warming", "sustainable companies"]

with open(os.devnull, 'w') as devnull:
	while 1:
		for term in climate_change:
			subprocess.run(["googler", "--np", "earth", term], stdout=devnull)
			sleep(1)
