import string
import random

used_variables = []
evaluated_data = []

Html_file= open("index.html","w")
Html_file.write("""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Proof by Mathmatical Induction Solver by Mateo Wartelle</title>
  <script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
</head>
<center><h1>Proof by Mathmatical Induction Solver by Mateo Wartelle</h1></center>
<body>
<p>
""")

def frac_to_Tex(frac):
    for i in frac:
      if i == "/":
          topeval = frac.split("/")[0]
          bottomeval = frac.split("/")[1]
          return "\\frac{%s}{%s}" % (topeval, bottomeval)
    return frac

def base_case_top_bottom(top, bottom, middle, evaluating, basecase):    
    if len(top) > 1:
        topdata = top.split("=")
        topdata = topdata[0]
    else:
        topdata = top
    if len(bottom) > 1:
        bottomdata = bottom.split("=")
        bottomdata = bottomdata[0]
    else:
        bottomdata = bottom
    evaluating = evaluating.replace(topdata,str(basecase))
    middle = middle.replace(bottomdata, str(basecase))
    return evaluating, middle

def get_top(top):
    if len(top) > 1:
        topdata = top.split("=")
        topdata = topdata[0]
        return topdata
    else:
        topdata = top
        return topdata

def base_case_Phase3(top, Random_variable, middle, evaluating):
    for element in middle:
        if element == top:
            middle = middle.replace(top, Random_variable)
    for secondelement in evaluating:
        if secondelement == top:
            evaluating = evaluating.replace(top, Random_variable)
    return middle, evaluating

def inductive_hypothesis_plus_one(top, Random_variable, middle, evaluating):
    temp = top
    top = top.replace(top, Random_variable + " + 1")
    middle = middle.replace(temp, "("+top+")")
    evaluating = evaluating.replace(temp, "("+top+")")
    return top, evaluating, middle
           
def random_generate(in_list):
    x = string.ascii_lowercase
    random_ = ''.join(list((random.choice(x) for num in range(1))))
    while random_ in in_list:
        random_ = ''.join(list((random.choice(x) for num in range(1))))
    return random_
          
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
    if len(bottom) > 1:
        bottomdata = bottom.split("=")[1]
    evaluated_data.insert(0, top)
    evaluated_data.insert(1, bottom)
    evaluated_data.insert(2, middle)
    evaluated_data.insert(3, evaluating)
    evaluated_data.insert(4, basecase)
    return evaluated_data

evaluated_data = summation("n", "i=1", "i", "n(n+1)/2", 1)
top = evaluated_data[0].strip()
bottom = evaluated_data[1].strip().strip()
middle = frac_to_Tex(evaluated_data[2]).strip()
evaluating = frac_to_Tex(evaluated_data[3]).strip()
basecase = evaluated_data[4]

#Setup
Html_file.write("Prove by Mathmatical Induction" )
Phase1 = """\[\sum_{%s}^%s %s = %s \]""" % (bottom, top, middle, evaluating)
Html_file.write(Phase1)

# Base Case
temp = get_top(top)
Html_file.write("Base case {} = {}".format(temp, basecase))
evaluating_base_case, middle_base_case = base_case_top_bottom(top, bottom, middle, evaluating, basecase)
Phase2 = """\[\sum_{%s}^%s %s = %s \]""" % (bottom, basecase, middle_base_case, evaluating_base_case)
Html_file.write(Phase2)
Html_file.write("\[" + middle_base_case  + "=" + evaluating_base_case + "\]<br>")

#Inductive Hypothesis
Random_variable = random_generate(used_variables)
topdata = get_top(top)
Html_file.write("Assume for some {} = {}".format(Random_variable, topdata))

middle_phase3, evaluating_phase3 = base_case_Phase3(top, Random_variable, middle, evaluating)
Phase3 = """\[\sum_{%s}^%s %s = %s \]""" % (bottom, Random_variable, middle_phase3, evaluating_phase3)
Html_file.write(Phase3)

Html_file.write("Show true for {} + 1".format(Random_variable))
top_phase4, evaluating_phase4, middle_phase4 = inductive_hypothesis_plus_one(top, Random_variable, middle, evaluating)
Phase4 = """\[\sum_{%s}^{%s} %s = %s \]""" % (bottom, top_phase4, middle_phase4, evaluating_phase4)
Html_file.write(Phase4)

Html_file.write("""</p></body></html>""")
Html_file.close()
