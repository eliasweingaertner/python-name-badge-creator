#main badge making script
#2014-10 by elias

from openpyxl import load_workbook
import re
import io

#############################
# function definitions
#############################

def generateSVGBadge(firstname, function, svgTemplate):
    
    result = svgTemplate.replace(config["marker_FIRSTNAME"],firstname)
    result = result.replace(config["marker_FUNCTION"], function)
    
    return result


def slugify(value):    
    import unicodedata
    
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '-', value))
    
    return value


def writeSVGBadge(badgenr,firstname,svgbadge):
    
    filename = config["svg_outputdir"]+"/"+str(badgenr)+"-"+slugify(firstname)+".svg"
    outputFile = io.open(filename,"w",encoding="utf8")
    outputFile.write(svgbadge)
    outputFile.close()
    
    
####################################
# main script
####################################



#step 1 - get config
if __name__ == "__main__":
    config = {}
    execfile("badges.conf", config) 
            

#step 2 - read template file into string buffer
svgTemplateFile = open(config["template_file"]) 
svgTemplate = unicode(svgTemplateFile.read())

#step 3 - open xlsx and generate SVG badges
wb = load_workbook(config["people_xslx"])
sheet = wb[config["xlsx_sheetname"]]

badgeNr = 0
for row in range(config["row_OFFSET"],config["row_LASTROW"]+1):
    
    firstNameCell = config["column_FIRSTNAME"]+str(row)
    functionCell = config["column_FUNCTION"]+str(row)
    firstname = unicode(sheet[firstNameCell].value)
    function = unicode(sheet[functionCell].value)
    
    if (function == None):
         function=""
    
    print "Creating badge for", firstname, function 
    
    svgBadge = generateSVGBadge(firstname,function,svgTemplate)
    
    writeSVGBadge(badgeNr,firstname,svgBadge)
    
    badgeNr=badgeNr+1
    




