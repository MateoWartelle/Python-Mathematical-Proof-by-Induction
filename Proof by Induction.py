import string
import random

used_variables = []
evaluated_data = []
top =""
bottom = ""
middle = ""
evaluating = ""
basecase = 0
topeval = ""
bottomeval = ""

Html_file= open("index.html","w")
Css_file = open("styles.css", "w")
Html_file.write("""<link rel="stylesheet" href="styles.css">""")

def generate_top_bottom(top, bottom):
    Css_file.write("""p {
    height: 50px;
    line-height: 50px;
    }
    span {
        position: relative;
        font-size: 2.5em;
        display: inline-block;
        line-height: .7em;
        vertical-align: middle;
    }
    span::before {
        font-size: 12px;
        display: block;
        position absolute;
        left: 0;
        top: 0;
        content: "%s";
        width: 22px;
        text-align: center;
    }
    span::after {
        font-size: 12px;
        display: block;
        position absolute;
        left: 0;
        bottom: 0;
        content: "%s";
        width: 27px;
        text-align: center;
    }
    """ % (top, bottom))
    

def generate_html_page(top, bottom, middle, evaluating, topeval, bottomeval):
    Html_file.write("""   <p>
        <span>&Sigma;</span>
        {} = <sup>{}</sup>&frasl;<sub>{}</sub>
    </p>""".format(middle, topeval, bottomeval))

    Css_file.write("""p {
    height: 50px;
    line-height: 50px;
    }
    span {
        position: relative;
        font-size: 2.5em;
        display: inline-block;
        line-height: .7em;
        vertical-align: middle;
    }
    span::before {
        font-size: 12px;
        display: block;
        position absolute;
        left: 0;
        top: 0;
        content: "%s";
        width: 22px;
        text-align: center;
    }
    span::after {
        font-size: 12px;
        display: block;
        position absolute;
        left: 0;
        bottom: 0;
        content: "%s";
        width: 27px;
        text-align: center;
    }
    """ % (top, bottom))

def summation(top, bottom, middle, evaluating, basecase):
    topeval = ""
    bottomeval = ""
    for stringdata in top:
        if stringdata.isalpha():
            used_variables.append(stringdata)
    for stringdata in bottom:
        if stringdata.isalpha():
            used_variables.append(stringdata)
            
    top = top.replace(" ", "")
    bottom = bottom.replace(" ", "")
    if len(top) > 1:
        topdata = top.split("=")[1]
    if len(bottom) > 1:
        bottomdata = bottom.split("=")[1]
    for i in evaluating:
      if i == "/":
          topeval = evaluating.split("/")[0]
          bottomeval = evaluating.split("/")[1]
    evaluated_data.insert(0, top)
    evaluated_data.insert(1, bottom)
    evaluated_data.insert(2, middle)
    evaluated_data.insert(3, evaluating)
    evaluated_data.insert(4, basecase)
    evaluated_data.insert(5, topeval)
    evaluated_data.insert(6, bottomeval)
    return evaluated_data
 
# Base Case
evaluated_data = summation("n", "i=1", "i", "n(n+1)/2", 0)
generate_html_page(evaluated_data[0], evaluated_data[1], evaluated_data[2], evaluated_data[3], evaluated_data[5], evaluated_data[6])

#Inductive Hypothesis
unused_variable = random.choice(string.ascii_letters).lower()
Html_file.write("<br>")
Html_file.write("Assume for some {} = {}".format(unused_variable, evaluated_data[0]))
Html_file.write("""<p>
        <span>&Sigma;</span>
        {} = <sup>{}</sup>&frasl;<sub>{}</sub>
    </p>""".format(evaluated_data[2], evaluated_data[5], evaluated_data[6]))


#Proving variable + 1
##Html_file.write("<br>")
##Html_file.write("Show true for {}+1".format(used_variables[0]))
##
##summation("i = 1", "n", "i", "n(n+1)/2", 0)   
Html_file.close()
Css_file.close()

    

