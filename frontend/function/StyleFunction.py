from frontend.function.MainFunction import MainFunction


class StyleFunction(MainFunction):

    def setSelectedEventStyle(self, plan):
        plans = ["QListWidget::item:selected{background-color: rgba(0,0,0,0.3);}",
                 "QListWidget::item:selected{background-color: rgba(255,255,255,0.3);}"]

        self.setStyleSheet(plans[plan])