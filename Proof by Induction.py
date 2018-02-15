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
  <title>MathJax example</title>
  <script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
</head>
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
    evaluating = evaluating.replace(topdata, "("+str(basecase)+")")
    middle = middle.replace(bottomdata, "("+str(basecase)+")")
    return evaluating, middle

def get_top(top):
    if len(top) > 1:
        topdata = top.split("=")
        topdata = topdata[0]
        return topdata
    else:
        topdata = top
        return topdata
        
def random_generate(in_list):
    x = string.ascii_lowercase
    random_ = ''.join(list((random.choice(x) for num in range(1))))
    while random_ in in_list:
        random_ = ''.join(list((random.choice(x) for num in range(1))))
    return random_
    print(random_)
          
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
    print(used_variables)
    return evaluated_data

evaluated_data = summation("k", "i=1", "2i - 1", "k^2", 1)
top = evaluated_data[0].strip()
bottom = evaluated_data[1].strip().strip()
middle = frac_to_Tex(evaluated_data[2]).strip()
evaluating = frac_to_Tex(evaluated_data[3]).strip()
basecase = evaluated_data[4]

#Setup
Html_file.write("Prove by Mathmatical Induction" )
middle = frac_to_Tex(middle)
evaluating = frac_to_Tex(evaluating)
Phase1 = """$$\sum_{%s}^%s %s = %s $$""" % (bottom, top, middle, evaluating)
Html_file.write(Phase1)

# Base Case
Html_file.write("Base case n = {}".format(basecase))
evaluating, middle = base_case_top_bottom(top, bottom, middle, evaluating, basecase)
Phase2 = """$$\sum_{%s}^%s %s = %s $$""" % (bottom, basecase, middle, evaluating)
Html_file.write(Phase2)

#Inductive Hypothesis
Random_variable = random_generate(used_variables)
topdata = get_top(top)
Html_file.write("Assume for some {} = {}".format(Random_variable, topdata))

#Phase3 = """$$\sum_{%s}^%s %s = %s $$""" % (bottom, basecase, middle, evaluating)


Html_file.write("""</p></body></html>""")
Html_file.close()

    

