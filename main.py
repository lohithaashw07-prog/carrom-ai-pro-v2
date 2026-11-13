
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp, sp


class CarromAIApp(App):

    def build(self):
        Window.clearcolor = (0.05, 0.06, 0.09, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(14)
        )

        title = Label(
            text="CARROM AI PRO V2",
            font_size=sp(27),
            bold=True,
            color=(1, 0.75, 0.2, 1),
            size_hint_y=None,
            height=dp(65)
        )
        root.add_widget(title)

        subtitle = Label(
            text="AI POWERED CARROM ASSISTANT",
            font_size=sp(13),
            color=(0.7, 0.75, 0.85, 1),
            size_hint_y=None,
            height=dp(35)
        )
        root.add_widget(subtitle)

        board = Label(
            text="CARROM BOARD PREVIEW\n\nYour board will appear here",
            font_size=sp(20),
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
            size_hint_y=0.5
        )
        root.add_widget(board)

        self.status = Label(
            text="Welcome! Ready to play?",
            font_size=sp(15),
            color=(0.3, 1, 0.6, 1),
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.status)

        scan = Button(
            text="SCAN CARROM BOARD",
            size_hint_y=None,
            height=dp(55),
            background_normal="",
            background_color=(0.1, 0.55, 0.9, 1)
        )
        scan.bind(on_press=self.scan_board)
        root.add_widget(scan)

        suggest = Button(
            text="SUGGEST BEST SHOT",
            size_hint_y=None,
            height=dp(55),
            background_normal="",
            background_color=(0.1, 0.65, 0.35, 1)
        )
        suggest.bind(on_press=self.suggest_shot)
        root.add_widget(suggest)

        reset = Button(
            text="RESET",
            size_hint_y=None,
            height=dp(48),
            background_normal="",
            background_color=(0.35, 0.35, 0.4, 1)
        )
        reset.bind(on_press=self.reset_app)
        root.add_widget(reset)

        return root

    def scan_board(self, instance):
        self.status.text = "Board scanner: Coming next!"

    def suggest_shot(self, instance):
        self.status.text = "AI shot engine: Coming next!"

    def reset_app(self, instance):
        self.status.text = "Welcome! Ready to play?"


if __name__ == "__main__":
    CarromAIApp().run()
