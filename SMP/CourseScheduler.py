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

    def check_if_dropped_on_label(self, touch, labels):
        # Check if the touch event is within a label
        # If it is, return the year and semester corresponding to the label
        # Otherwise, return None
        for label, (year, semester) in labels.items():
            if label.collide_point(*touch.pos):
                return year, semester
        return None, None

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.button import Button

class DraggableCourse(Button, DragBehavior):
    def __init__(self, course, calendar, labels, **kwargs):
        super(DraggableCourse, self).__init__(**kwargs)
        self.course = course
        self.calendar = calendar
        self.labels = labels

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.drag_start(touch)
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
            return True
        return super(DraggableCourse, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self._drag_touch is touch:
            self.drag_stop(touch)
            return True
        return super(DraggableCourse, self).on_touch_up(touch)

    def drag_stop(self, touch):
        # Add code to handle the drag stop event
        self.opacity = 1.0
        # Check if the course has been dropped on a label
        year, semester = self.calendar.check_if_dropped_on_label(touch, self.labels)
        if year and semester:
            # Add the course to the corresponding spot in the calendar
            self.calendar.add_course(year, semester, self.course)

class CalendarApp(App):
    def build(self):
        # Create an instance of the Calendar class
        calendar = Calendar()

        # Create a GridLayout to display the calendar
        layout = GridLayout(cols=4)

        # Add labels for each semester and year
        for semester in ['Fall', 'Spring']:
            for year in ['Year 1', 'Year 2', 'Year 3', 'Year 4']:
                label = Label(text=f"{semester} - {year}")
                layout.add_widget(label)

                # Add labels for each course in the semester
                courses = calendar.get_courses(year, semester)
                for course in courses:
                    course_label = Label(text=str(course))
                    layout.add_widget(course_label)

        # Add an area to display the course status
        course_status_label = Label(text="Course Status:")
        layout.add_widget(course_status_label)

        # Define the labels variable
        labels = {}

        # Get the list of all courses for the listed major
        all_courses = [Course("Course A", "A"), Course("Course B", "B"), Course("Course C", "C")]

        # Add draggable buttons for each course in the all_courses list
        for course in all_courses:
            draggable_course = DraggableCourse(course, calendar, labels, text=course.name, size_hint=(None, None), size=(100, 50))
            layout.add_widget(draggable_course)

        return layout

if __name__ == '__main__':
    CalendarApp().run()
