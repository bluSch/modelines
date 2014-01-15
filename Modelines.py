import sublime, sublime_plugin


class DetectModelinesCommand(sublime_plugin.EventListener):

    def check_first_line():
        view.set_status('foobar', view.line(0))

    def on_load(self, view):
        self.check_first_line()

    def on_post_save_async(self, view):
        self.check_first_line()

