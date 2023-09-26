## The code for generating my Financial Preparedness. 

import base64
from IPython.display import Image, display
import matplotlib.pyplot as plt
import re
import csv
import requests

##Generate mermaid code using class may be of help. Yet to develop


#Export as list from Excel
##Publish to Web as csv
##https://docs.google.com/spreadsheets/d/e/2PACX-1vQIaRbgAen22hHQ3ScWZKieaRGE0C53yVrqu80TsaP8IBeIv6YZav0ZmGztjuMdrgdKo0_3r5E8TjJD/pub?output=csv

listexcel=[]
url="https://docs.google.com/spreadsheets/d/e/2PACX-1vQIaRbgAen22hHQ3ScWZKieaRGE0C53yVrqu80TsaP8IBeIv6YZav0ZmGztjuMdrgdKo0_3r5E8TjJD/pub?output=csv"

response = requests.get(url)

reader = csv.reader(response.content.decode('utf-8').splitlines())
for row in reader:
    listexcel.append(row)

response.close()


MerStory = """
    section {no}) {Name}
    {target} :active, e1, 2025-{prio}-01, 30d
    {acheived}:done, a1, 2025-{prio}-01, {ach}d
  """
temp_variable = ""
for i in range(len(listexcel)):
  #for j in range(len(listexcel[i])):
  if (i >0):
      ach= int(listexcel[i][2]) / int(listexcel[i][1]) * 30
      temp_variable= temp_variable+re.sub(r"{Name}", str(listexcel[i][0]), MerStory)
      temp_variable= re.sub(r"{no}", str(i), temp_variable)
      temp_variable= re.sub(r"{target}", str(listexcel[i][1]), temp_variable)
      temp_variable= re.sub(r"{acheived}", str(listexcel[i][2]), temp_variable)
      temp_variable= re.sub(r"{prio}", str(listexcel[i][3]), temp_variable)
      temp_variable= re.sub(r"{ach}", str(ach), temp_variable)
      
MerStory1="""
    gantt
    title Planned Expense VS Current Fin Position For 2025
    dateFormat  YYYY-MM-DD
    axisFormat %B-%Y
    tickInterval 1month
    """
t1= MerStory1 + temp_variable
def mm(graph):
  graphbytes = graph.encode("ascii")
  base64_bytes = base64.b64encode(graphbytes)
  base64_string = base64_bytes.decode("ascii")
  display(Image(url="https://mermaid.ink/img/" + base64_string))
mm(t1)
display()
