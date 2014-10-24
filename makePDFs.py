import os
import subprocess

############################
# this file simply runs all SVGs through Inkscape for converting them to PDF
############################


#get config
if __name__ == "__main__":
    config = {}
    execfile("badges.conf", config)
                    
#iterate over all executed pdf files
for fname in os.listdir(config["svg_outputdir"]):
  fnamePDF = fname.replace("svg","pdf")
  print "Converting " + fname + " to " + fnamePDF
  
  cmdline = ["inkscape", "-f",config["svg_outputdir"]+"/"+fname,"-A",config["pdf_outputdir"]+"/"+fnamePDF]
  #print cmdline
  subprocess.call(cmdline)
