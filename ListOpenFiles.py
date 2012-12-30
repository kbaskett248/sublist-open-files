import sublime, sublime_plugin

class ListOpenFilesCommand(sublime_plugin.WindowCommand):
    source_options = ['active_window','all_windows']

    def run(self, source = "active_window"):
        file_list = ""
        file_count = 0

        if (source in self.source_options):
            if (source == 'active_window'):
                windows = [self.window]
            else:
                windows = sublime.windows()

            for w in windows:
                for v in w.views():
                    file_name = str(v.file_name())
                    if file_name != "None":
                        file_list += file_name + "\n"
                        file_count += 1 

            if file_count != 0:
                if file_count == 1:
                    file_list += "\nTotal: 1 open file"
                elif file_count > 1:
                    file_list += "\nTotal: " + str(file_count) + " open files"

                list_buffer = self.window.new_file()
                list_buffer.set_scratch(True)
                list_buffer.set_name("Open Files")

                edit = list_buffer.begin_edit()
                row, col = list_buffer.rowcol(list_buffer.sel()[0].begin())
                list_buffer.insert(edit,list_buffer.text_point(row, col),file_list)
                list_buffer.end_edit(edit)
        
    def is_visible(self, source = "active_window"):
        result = False
        if (source in self.source_options):
            if (source == 'active_window'):
                result = len(self.window.views()) > 0
            elif (source == 'all_windows'):
                if (len(sublime.windows()) > 1):
                    view_count = 0
                    for w in sublime.windows():
                        view_count += len(w.views())
                        if view_count > 0:
                            break
                    result = (view_count > 0)
        return result

