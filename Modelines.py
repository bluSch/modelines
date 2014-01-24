import sublime
import sublime_plugin


def do_modelines(flags):
    # if modelines enabled and total_lines > 0:
    if total_lines > 0:

        # Prevent recursive entry
        if entered:
            return
        entered += 1

        # Check modeline_count lines at the beginning of the file
        for line_num in range(1, modeline_count +1):
            # if the line exists and checking if it's a modeline encounters an error, pretent the file is empty from now on
            if line_num <= total_lines and check_modeline(line_num, flags) == FAIL:
                total_lines = 0

        # Check modeline_count lines from the end of the file
        for line_num in [total_lines - d for d in range(modeline_count)]:
            if (line_num > 0
                and line_num > modeline_count
                and line_num > modeline_count - total_lines
                and check_modeline(line_num, flags) == FAIL):
                total_lines = 0

        entered -= 1


def check_modeline(line_num, flags):
    line = line_at(line_num)
    for i in range(len(line)):
        if (i - 1 == -1 or line[i - 1] == ' '
            and line[i:i + 4].lower() == 'vim:'
            or line[i:i+3] == 'vi:' or (i != 0 and line[i:i+3] == 'ex:')):
                # skipping vim version checking @ ll5137-5150 in buffer.c
            break

    # if modeline init found
    if i + 1 != len(line):
        while not line[i - 1] == ':':
            i += 1

        line = line[i:]
        if line == '':
            return FAIL


class DetectModelinesCommand(sublime_plugin.EventListener):

    def _check_first_line(self, view):
        print(view.line_endings())

    def on_load(self, view):
        self._check_first_line(view)

    def on_post_save_async(self, view):
        self._check_first_line(view)

