import time

from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior

force_scrape = False

# if page.html does not exist or force_scrape == 1, then this method will scrape new data
if (not os.path.exists("SMP/page.html") or force_scrape):
    print("Gathering course data")
    # start by defining the options
    options = webdriver.ChromeOptions()

    # we run this headless normally, but this is available for debugging purposes
    options.add_argument('--headless')

    # certificate errors should be resolved now, leaving here just in case
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')

    # we don't need it as the page also populated with the running javascript code.
    options.page_load_strategy = 'none'

    # this returns the path web driver downloaded
    chrome_path = ChromeDriverManager().install()
    chrome_service = Service(chrome_path)
    # pass the defined options and service objects to initialize the web driver
    driver = Chrome(options=options, service=chrome_service)
    driver.implicitly_wait(3)

    url = "https://catalog.smcm.edu/"

    driver.get(url)
    # just for debugging
    # driver.maximize_window()

    time.sleep(1)

    # this is the explicit/absolute xpath to the 'programs' button to get to the page with all majors and minors
    driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/p[1]/a[2]/img[1]").click()

    time.sleep(1)

    # now click on the 'computer science BS' link to go to the major page
    driver.find_element(By.LINK_TEXT, "Computer Science, BS").click()

    time.sleep(1)

    # now we're on the page needed to gather all course info after many clicks
    # now we need to click on each course's dropdown to reveal all the information we need to scrape and store

    # TODO here is where we need to take all the required classes and then reroute to the class masterlist for standardized formatting

    # get all links with the aria-expanded attribute set to false
    links = driver.find_elements(By.CSS_SELECTOR, "[aria-expanded='false']")


    # iterate over the links and click on them if they are visible
    for link in links:
        print(link)
        time.sleep(0.1)
        if link.is_displayed():
            link.click()

    # now that everything is dropped down, we can scrape all data from the site
    # Get the HTML of the current page
    html = driver.page_source

    # Print the HTML to the console (Debug)
    # print(html)

    # this writes the current HTML as a new document we can now work with and parse
    with open("SMP/page.html", "w", encoding="utf-8") as f:
        f.write(html)
# end web scrape method


print("Course data gathering complete")


# now we switch over to BeautifulSoup to parse our webpage which contains the info we need

# open the file and create a BS4 object with it
page_as_io = open("SMP/page.html", "r", encoding="utf-8")

# this converts the open file into a single string variable
page_as_str = page_as_io.read()

# turning the downloaded file into a BS4 object, parsed as HTML
page_as_soup = bs(page_as_str, "html.parser")

# now find text specifically from the list items we dropped down with Selenium (all class details)
# pattern matches:
# class="program_description"
# class="acalog-core"
# <table class="td_dark">
# NOT <div class="gateway-toolbar gateway-mini-toolbar clearfix">

# this will keep track of the course codes we have already written
code_list = []

# function to filter out gateway-toolbar class
# def not_gateway_elements(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# method function: takes the webpage html ("page.html")
# and outputs class listings into a text file ("classText.html")
with open("SMP/classText.txt", "w", encoding="utf-8") as f:
    # for each list item which fits the description of a course item

    for item in page_as_soup.find_all("li", "acalog-course"):
        bigString:str = ''
        # check inside the item's first <a> tag to see if the href either contains the number 657 or 658 and print the result
        # TODO fix this thing, it needs to assign required or elective status to the course
        if item.find("a")["href"].find("657") != -1:
            print("657")
        elif item.find("a")["href"].find("658") != -1:
            print("658")
        textBlocks: list[str] = item.get_text(strip=True, separator=' ').splitlines()

        # here, we take the entire course line and remove the share button interactions
        for block in textBlocks:
            # step 1: take the course code matching (ABCD 123)
            course_code = block[0:8]
            # check if the course has already been read in
            # if this is a new course
            if (course_code not in code_list):
                # step 1.5: add the course code to the list of already added courses
                code_list.append(course_code)
                # step 2: find the second occurrence of the course code
                second_code = block.find(course_code, 8)
                # step 3: remove all redundant text before the second course code
                block = block[second_code:]
                # step 4: add the course info to the class list (with a newline character at the end for formatting)
                bigString += '\n' + block
                # get whether the course is required or elective based on the html of the section h3
                # header_id = item.find_previous("div").find("h3")["name"]

            # this marks where already added courses get discarded.

        # finally, we remove all unnecessary tabs
        bigString = bigString.replace("\t","")

        # and we then write the big string to the file
        f.write(bigString)
    f.close()

# Define the Course class to store information about each course as we read it in
class Course:
    def __init__(self, department, number, name, credit_hours, frequency, satisfies, prerequisites, description, category):
        self.department = department
        self.number = number
        self.name = name
        self.credit_hours = credit_hours
        self.frequency = frequency
        self.satisfies = satisfies
        self.prerequisites = prerequisites
        self.description = description
        self.category = category

# to store all the Course objects we create below
course_object_list = []

# for each line in classText.txt, check if line is valid and create a Course object for it
for line in open("SMP/classText.txt", "r", encoding="utf-8"):
    # if the line is valid (contains a course code) which we have accounted for
    if (line[0:8] in code_list):
        # create a Course object for the course
        course = Course(line[0:4], line[5:8], "", "", "", "", "", "", "")

        # remove the course code from the line
        line = line[8:]

        # add the course name to the Course object, from end of code to "Credit"
        course.name = line[:line.find("Credit") - 1]
        # then remove the course name from the line
        line = line[line.find("Credit") - 1:]

        # add the course credits to the Course object, from beginning of "Credit" to "Frequency"
        course.credit_hours = line[line.find("Credit"):line.find("Frequency")]
        # then remove the course credits from the line
        line = line[line.find("Frequency"):]

        # add the course frequency to the Course object, from beginning of "Frequency" to end of "semester"
        course.frequency = line[line.find("Frequency"):line.find("semester")+8]
        # then remove the course frequency from the line
        line = line[line.find(":"):]

        # if the course satisfies a requirement, add that to the Course object
        if line.find("Course Satisfies") != -1:
            course.satisfies = line[line.find("Course Satisfies")+17:line.find(".")]
        # null otherwise
        else:
            course.satisfies = ""
        # then remove the satisfies from the line
        line = line[line.find(".")+1:]

        # if prerequisites exist, add that to the Course object
        if line.find("Prerequisite(s):") != -1:
            prereq_start = line.find("Prerequisite(s):")
            # then find the end of the prereqs by looking for the next period
            prereq_end = line.find(".", prereq_start)
            # then add the prereqs to the Course object after some filtering
            course.prerequisites = line[prereq_start:prereq_end].replace("Prerequisite(s):", "").replace("or permission of the instructor", "")
            # then remove the prereqs from the line
            line = line[:prereq_start]
        # null otherwise
        else:
            course.prerequisites = ""
        # then remove the prereqs from the line
        # line = line[line.find(".")+1:]

        # add the course description to the Course object; it should be the only thing left
        course.description = line
        # last, assign the course category to be either required or elective depending on the course code
        # if the numerical component is <299, it is a required course. if >= 490, it is a final requirement. Else, it is an elective course.
        #! Note that this is not a perfect system: these rules do not apply to other departments
        if int(course.number) < 299:
            course.category = "Required"
        elif int(course.number) >= 490:
            course.category = "Capstone"
        else:
            course.category = "Elective"
        # add the Course object to the course_object_list
        course_object_list.append(course)

# print the course_object_list to the console
# for course in course_object_list:
#     print(course)
#     print("\n")


# we need to know if the course is a required or elective course
# - all required courses need to be in the final calendar
# - a certain number of elective courses need to be in the final calendar
# - a capstone course needs to be in the final calendar
# - a certain number of credits need to be in the final calendar
class DraggableCourse(Button, DragBehavior):
    def __init__(self, course, **kwargs):
        super(DraggableCourse, self).__init__(**kwargs)
        self.course = course
        self.semester = None
        self.year = None
        # self.size_hint = (100, 100) (currently breaks drag functionality)
        self.size = self.texture_size
        self.background_color = (1, 0, 0, 1)
        # make the label text appear in the center of the button
        self.halign = 'center'
        self.valign = 'center'

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.drag_start(touch)
            # then reset the semester and year attributes to None
            self.semester = None
            self.year = None
            self.update_course_status()
            return True
        return super(DraggableCourse, self).on_touch_down(touch)

    def drag_update(self, touch):
        if self._drag_touch is touch:
            self.pos = (touch.x - self.width / 2, touch.y - self.height / 2)

    def drag_start(self, touch):
        # Add code to handle the drag start event
        self._drag_touch = touch
        self._drag_offset = self.pos[0] - touch.x, self.pos[1] - touch.y
        self.opacity = 0.5

    def on_touch_move(self, touch):
        if self._drag_touch is touch:
            self.drag_update(touch)

    def update_course_status(self):
            # Add code to update the schedule status
            if self.year is not None and self.semester is not None:
                self.background_color = (0, 1, 0, 1)  # Change color to green
            else:
                self.background_color = (1, 0, 0, 1)  # Change color to red

    def on_touch_up(self, touch):
        if self._drag_touch is touch:
            for widget in self.parent.parent.parent.children[0].children: # This is a hacky way to get the calendar_layout
                if isinstance(widget, Label) and self.collide_widget(widget):
                    print(f"Collided with {widget.text}")
                    label_text = widget.text.split(" - ")
                    self.semester = label_text[0]
                    self.year = label_text[1]
                    self.update_course_status()

            self.opacity = 1
            self._drag_touch = None
            return True
        return super(DraggableCourse, self).on_touch_up(touch)

class CoursePlannerApp(App):
    def build(self):

        root = BoxLayout(padding=25)

        # Create a new GridLayout with 3 columns
        side_list_layout = GridLayout(cols=3, spacing=(10, 10))

        ## Add widgets to the top layout:

        # Add labels for each column
        label1 = Label(text="Required")
        label2 = Label(text="Elective")
        label3 = Label(text="Capstone")

        # Create box layouts for each column
        column1_layout = BoxLayout(orientation='vertical')
        column2_layout = BoxLayout(orientation='vertical')
        column3_layout = BoxLayout(orientation='vertical')

        # Add labels to the box layouts
        column1_layout.add_widget(label1)
        column2_layout.add_widget(label2)
        column3_layout.add_widget(label3)

        # Add draggable buttons for each course in the all_courses list
        for course in course_object_list:
            draggable_course = DraggableCourse(course, text=course.department + ' ' + course.number + '\n' + course.name)
            if course.category == "Required":
                column1_layout.add_widget(draggable_course)
            elif course.category == "Elective":
                column2_layout.add_widget(draggable_course)
            elif course.category == "Capstone":
                column3_layout.add_widget(draggable_course)

        # Add the box layouts to the top layout
        side_list_layout.add_widget(column1_layout)
        side_list_layout.add_widget(column2_layout)
        side_list_layout.add_widget(column3_layout)

        # Add the top layout to the root layout
        root.add_widget(side_list_layout)

        # Create a GridLayout to display the calendar
        calendar_layout = GridLayout(cols=4, spacing=(40, 40))

        # Add labels for each semester and year
        for semester in ['Fall', 'Spring']:
            for year in ['Year 1', 'Year 2', 'Year 3', 'Year 4']:
                label = Label(text=f"{semester} - {year}")
                calendar_layout.add_widget(label)
                # column1_layout.add_widget(draggable_course)

        root.add_widget(calendar_layout)
        return root

if __name__ == '__main__':
    CoursePlannerApp().run()
