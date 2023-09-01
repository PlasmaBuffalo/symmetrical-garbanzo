
#Liam Zalubas

#Project Part 1: take in HTML file and dump it in the console
#submit as .ipynb

#file = open("Python/CS360-IDS/ClassWebsite.html")
#print(file.read())

#Project Part 2: analyze the file contents by printing:
# - webpage title
# - link count

openTitleTag = "<title>"
closeTitleTag = "</title>"
hrefLinkPattern = 'href="..."'
linkCount = 0
pageTitle = ""

with open("Python/CS360-IDS/ClassWebsite.html") as file:
    line = [line.rstrip() for line in file]
    for i in range (0, len(line)):
        #step: find <title>Data Science</title>
        titleIndex = line[i].find(openTitleTag)
        endIndex = line[i].find(closeTitleTag)
        #step: find each href tag and ensure its link does not begin with '#'
        #pattern is href="..."
        hrefIndex = line[i].find(openTitleTag)
        #step: use substring to strip tags from text
        if (titleIndex != endIndex):
            pageTitle = (line[i][titleIndex+len(openTitleTag):endIndex])



print(pageTitle)