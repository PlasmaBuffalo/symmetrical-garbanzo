
#Liam Zalubas

#Project Part 1: take in HTML file and dump it in the console

#file = open("Python/CS360-IDS/ClassWebsite.html")
#print(file.read())

#Project Part 2: analyze the file contents by printing:
# - webpage title
# - link count

openTitleTag = "<title>"
closeTitleTag = "</title>"
linkPattern = 'href='
linkCount = 0
pageTitle = ""

with open("CS360-IDS/ClassWebsite.html") as file:
    line = [line.rstrip() for line in file]
    for i in range (0, len(line)):
        #step: find <title>Data Science</title>
        titleIndex = line[i].find(openTitleTag)
        endIndex = line[i].find(closeTitleTag)

        #step: use substring to strip tags from text
        # since the find function returns -1 if not found, this will detect when indices are different
        if (titleIndex != endIndex):
            pageTitle = (line[i][titleIndex+len(openTitleTag):endIndex])

        #step: find each href tag and ensure its link does not begin with '#'
        #make sure we get every href tag for this line, so we keep track of last href tag index
        lastLinkIndex = 0
        for j in range(0, line[i].count(linkPattern)):
            hrefIndex = line[i].find(linkPattern, lastLinkIndex)
            if (hrefIndex != -1):
                lastLinkIndex = hrefIndex+len(linkPattern)
                firstLinkChar = line[i][hrefIndex+len(linkPattern)+1]
                if (firstLinkChar != "#"):
                    linkCount += 1




print("Page Title:",pageTitle)
print("Link Count:",linkCount)