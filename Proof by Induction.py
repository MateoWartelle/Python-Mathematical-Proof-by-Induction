import string
import random

used_variables = []
evaluated_data = []

Html_file= open("index.html","w")
Css_file = open("styles.css", "w")
Html_file.write("""<link rel="stylesheet" href="styles.css">""")

def summation(top, bottom, middle, evaluating, basecase):
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
    print(top)
    if len(bottom) > 1:
        bottomdata = bottom.split("=")[1]
    print(bottom)
    Html_file.write("""   <p>
        <span>&Sigma;</span>
        {} = {}
    </p>""".format(middle, evaluating))

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
    
    evaluated_data.insert(0, top)
    evaluated_data.insert(1, bottom)
    evaluated_data.insert(2, middle)
    evaluated_data.insert(3, evaluating)
    evaluated_data.insert(4, basecase)
    
    # TOP
    # if in form { n = ? }
    # if in form { n }
    
    # Bottom
    # if in form { i = ?}
    # if in form { i }
summation("i = 1", "n", "i", "n(n+1)/2", 0)    
print(used_variables)
# Base Case


#Inductive Hypothesis
unused_variable = random.choice(string.ascii_letters).lower()


print ("Assume for some {} = {}".format(unused_variable, used_variables[0]))


#Proving variable + 1
print ("Show true for {}+1".format(used_variables[0]))


Html_file.close()
Css_file.close()

    

