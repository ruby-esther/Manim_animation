from manim import *

class Date(Scene):
    def construct(self):
        day = 1
        month = 7
        year = 2024

        # Month names
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        # Days in months
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        
        # Text object for date
        date_text = Text(f"{day:02d} {months[month-1]} {year}", font_size=80)
        self.add(date_text)

        target_day = 6
        target_month = 5
        target_year = 2025
        while not(day == target_day and month == target_month and year == target_year):
            # Increment date
            day += 1

            # Check overflowf
            if day > days_in_month[month-1]:
                day -= days_in_month[month-1]
                month += 1
                if month > 12:
                    month = 1
                    year += 1

            new_text = Text(f"{day:02d} {months[month-1]} {year}", font_size=80)

            # Animate the date change
            self.play(Transform(date_text, new_text), run_time=0.07)

        self.play(date_text.animate.set_color(RED_E))
        self.wait(2)
