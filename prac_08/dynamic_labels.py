from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Run the dynamic labels app"""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_label = {"a":"Ashley", "b":"Brian", "c" :"Chloe", "d":"Dylan"}

    def build(self):
        """Build the kivy app and add labels for each dictionary value"""
        root = Builder.load_file('dynamic_labels.kv')

        for name in self.name_to_label.values():
            temp_label = Label(text=name)
            root.ids.names_box.add_widget(temp_label)
        return root

DynamicLabelsApp().run()