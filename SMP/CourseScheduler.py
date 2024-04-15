# course class to store course information
class Course:
    def __init__(self, name, code):
        self._name = name
        self._code = code
        self._credits = 0
        self._description = ""
        self._frequency = ""
        self._prerequisites = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        self._credits = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value

    @property
    def prerequisites(self):
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, value):
        self._prerequisites = value

    def __str__(self):
        return f"Course: {self.name} ({self.code}), Credits: {self.credits}, Description: {self.description}, Frequency: {self.frequency}, Prerequisites: {self.prerequisites}"

# calendar class to store courses for each semester in each year
class Calendar:
    def __init__(self):
        self.calendar = {
            'Year 1': {
                'Fall': [],
                'Spring': []
            },
            'Year 2': {
                'Fall': [],
                'Spring': []
            },
            'Year 3': {
                'Fall': [],
                'Spring': []
            },
            'Year 4': {
                'Fall': [],
                'Spring': []
            }
        }

    def add_course(self, year, semester, course):
        self.calendar[year][semester].append(course)

    def get_courses(self, year, semester):
        return self.calendar[year][semester]

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class CalendarApp(App):
    def build(self):
        # Create an instance of the Calendar class
        calendar = Calendar()

        # Create a GridLayout to display the calendar
        layout = GridLayout(cols=2)

        # Add labels for each year and semester
        for year in calendar.calendar:
            for semester in calendar.calendar[year]:
                label = Label(text=f"{year} - {semester}")
                layout.add_widget(label)

                # Add labels for each course in the semester
                courses = calendar.get_courses(year, semester)
                for course in courses:
                    course_label = Label(text=str(course))
                    layout.add_widget(course_label)

        return layout

if __name__ == '__main__':
    CalendarApp().run()
