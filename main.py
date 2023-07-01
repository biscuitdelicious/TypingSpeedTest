import random
import time
import tkinter as tk

import customtkinter as ctk


# TODO: Make the stopwatch working
# TODO: Display the WPM at the end of the test

root = tk.Tk()
root.geometry('1200x800')
root.title('Typing Speed')

root.eval('tk::PlaceWindow . center')


def update_stopwatch_time():
    current_time = time.time() - start_time
    seconds = int(current_time)
    stopwatch.config(text="Elapsed Time: {} seconds".format(seconds))
    stopwatch.after(20, update_stopwatch_time)


def start_stopwatch():
    global start_time
    start_time = time.time()
    update_stopwatch_time()


def highlight_text(text_label, text, foreground_color):  # #EBEBEB
    text_label.delete("1.0", "end-1c")
    text_label.tag_config("highlight", foreground=foreground_color)
    start_index = "1.0"

    start_index = text_label.search(text[0], start_index, stopindex="end", nocase=True)
    if not start_index:
        pass
    end_index = f"{start_index}+{len(text[0])}c"
    text_label.tag_add("highlight", start_index, end_index)


def remove_widgets(*arg):
    for widget in arg:
        widget.destroy()


def create_button(button_text, button_command, x_pos, y_pos, anchor, width=50, height=50,
                  font=('Avenir', 16, 'normal')):
    button = ctk.CTkButton(root, text=button_text, hover_color='#A7FFF6', fg_color='white', text_color='black',
                           width=width, height=height, font=font, command=button_command)
    button.place(anchor=anchor, relx=x_pos, rely=y_pos)


def display_level(path, min_words, max_words):
    with open(path) as file:
        data = file.read()
        words = data.splitlines()
        random.shuffle(words)
        no_of_words = random.randint(min_words, max_words)
        text = random.sample(words, no_of_words)
        text_level = ctk.CTkTextbox(root, text=text,
                                    font=('Avenir', 26, 'normal'), height=200,
                                    wraplength=900)
        text_level.place(anchor='center', rely=.4, relx=.5)

        text_input = ctk.CTkTextbox(root, width=300, height=35, corner_radius=2, font=('Avenir', 20, 'normal'),
                                    activate_scrollbars=False)
        text_input.place(anchor='center', rely=.55, relx=.5)
        text_input.focus_set()


def start_test():
    level_text = ctk.CTkLabel(root, text='Choose your level', font=('Avenir', 44, 'normal'),
                              text_color='#95D9C3')
    level_text.place(anchor='center', rely=.2, relx=.5)

    level_1_button = ctk.CTkButton(root, text='Level 1', hover_color='#A7FFF6', fg_color='white', text_color='black',
                                   width=160, height=60, font=('Avenir', 20, 'normal'),
                                   command=lambda: [test('Level 1'),
                                       remove_widgets(level_1_button, level_2_button, level_3_button, level_text)])
    level_1_button.place(anchor='center', rely=.5, relx=.3)

    level_2_button = ctk.CTkButton(root, text='Level 2', hover_color='#A7FFF6', fg_color='white', text_color='black',
                                   width=160, height=60, font=('Avenir', 20, 'normal'),
                                   command=lambda: [test('Level 2'),
                                       remove_widgets(level_1_button, level_2_button, level_3_button, level_text)])
    level_2_button.place(anchor='center', rely=.5, relx=.5)

    level_3_button = ctk.CTkButton(root, text='Level 3', hover_color='#A7FFF6', fg_color='white', text_color='black',
                                   width=160, height=60, font=('Avenir', 20, 'normal'),
                                   command=lambda: [test('Level 3'),
                                       remove_widgets(level_1_button, level_2_button, level_3_button, level_text)])
    level_3_button.place(anchor='center', rely=.5, relx=.7)


def test(level):
    test_text = ctk.CTkLabel(root, text=level, font=('Avenir', 44, 'normal'),
                             text_color='#95D9C3')
    test_text.place(anchor='center', rely=.05, relx=.5)

    if level == 'Level 1':
        with open('words/english') as file:
            data = file.read()
            words = data.splitlines()
            random.shuffle(words)
            no_of_words = random.randint(15, 30)
            text = random.sample(words, no_of_words)
            text_level = tk.Text(root, width=45, height=5, font=('Avenir', 26, 'normal'), wrap=tk.WORD)
            text_level.insert('1.0', text)
            text_level.place(anchor='center', rely=.4, relx=.5)
            text_level.configure(state='disabled')
            text_level.bindtags((str(text_level), str(root), "all"))

            text_input = ctk.CTkTextbox(root, width=300, height=35, corner_radius=2, font=('Avenir', 20, 'normal'),
                                        activate_scrollbars=False)
            text_input.place(anchor='center', rely=.55, relx=.5)
            text_input.focus_set()
    elif level == 'Level 2':
        with open('words/english_1k') as file:
            data = file.read()
            words = data.splitlines()
            random.shuffle(words)
            no_of_words = random.randint(20, 40)
            text = random.sample(words, no_of_words)
            text_level = tk.Text(root, width=55, height=5, font=('Avenir', 26, 'normal'), wrap=tk.WORD)
            text_level.insert('1.0', text)
            text_level.place(anchor='center', rely=.4, relx=.5)
            text_level.configure(state='disabled')
            text_level.bindtags((str(text_level), str(root), "all"))

            text_input = ctk.CTkTextbox(root, width=300, height=35, corner_radius=2, font=('Avenir', 20, 'normal'),
                                        activate_scrollbars=False)
            text_input.place(anchor='center', rely=.55, relx=.5)
            text_input.focus_set()
    else:
        with open('words/english_5k') as file:
            data = file.read()
            words = data.splitlines()
            random.shuffle(words)
            no_of_words = random.randint(30, 45)
            text = random.sample(words, no_of_words)
            text_level = tk.Text(root, width=70, height=6, font=('Avenir', 26, 'normal'), wrap=tk.WORD)
            text_level.insert('1.0', text)
            text_level.place(anchor='center', rely=.4, relx=.5)
            text_level.configure(state='disabled')
            text_level.bindtags((str(text_level), str(root), "all"))

            text_input = ctk.CTkTextbox(root, width=300, height=35, corner_radius=2, font=('Avenir', 20, 'normal'),
                                        activate_scrollbars=False)
            text_input.place(anchor='center', rely=.56, relx=.5)
            text_input.focus_set()

    main_menu_button = ctk.CTkButton(root, text='Main Menu', hover_color='#A7FFF6', fg_color='white',
                                     text_color='black',
                                     width=120, height=40, font=('Avenir', 16, 'normal'),
                                     command=lambda: [
                                         remove_widgets(text_input, text_level, test_text, main_menu_button),
                                         start_test()])
    main_menu_button.place(anchor='center', relx=.06, rely=.05)

    stopwatch = ctk.CTkLabel(root, text='Elapsed 0 seconds', font=('Avenir', 16, 'normal'))
    stopwatch.place(anchor='center', relx=.06, rely=.1)

    def on_key_press(event):
        if event.keysym == 'space':
            content = text_input.get("1.0", "end-1c").strip()
            text_input.delete("1.0", "end-1c")

            text_level.tag_remove("incorrect", "1.0", "end")

            text_level.tag_config("highlight", foreground="#EBEBEB")
            text_level.tag_config("incorrect", foreground="red")

            start_index_correct = "1.0"

            if not start_stopwatch:
                start_stopwatch()

            if content == text[0]:
                start_index_correct = text_level.search(text[0], start_index_correct, stopindex="end", nocase=True)
                end_index = f"{start_index_correct}+{len(text[0])}c"
                text_level.tag_add("highlight", start_index_correct, end_index)
                start_index_correct = end_index
                text.pop(0)
            else:
                start_index_incorrect = text_level.search(text[0], start_index_correct, stopindex="end", nocase=True)
                if start_index_incorrect:
                    end_index = f"{start_index_incorrect}+{len(text[0])}c"
                    text_level.tag_add("incorrect", start_index_incorrect, end_index)
                else:
                    text_level.tag_add("incorrect", "1.0", "end")

    text_input.bind('<Key>', on_key_press)


welcome_text = ctk.CTkLabel(root, text='Welcome to test your limits', font=('Avenir', 44, 'normal'),
                            text_color='#95D9C3')
welcome_text.place(anchor='center', rely=.2, relx=.5)

start_button = ctk.CTkButton(root, text='Start Test', hover_color='#A7FFF6', fg_color='white', text_color='black',
                             width=350, height=80, font=('Avenir', 26, 'normal'),
                             command=lambda: [remove_widgets(start_button, welcome_text),
                                 start_test()])
start_button.place(anchor='center', rely=.5, relx=.5)

root.mainloop()
