""" UNIR: Unresolved Network Issues Resolver """
__version__ = '1.4'
__author__ = 'Michael Jeans'
# Contributor: Virgil Hoover

import tkinter as tk
from tkinter import ttk
from mysql import connector


def execute_sql():
    """ Execute the generated SQL Query. """
    query = generate_sql()
    mydb = connector.connect(host='nocweb', user='*removed*', passwd='*removed*', database='noctracker')
    mycursor = mydb.cursor()
    mycursor.execute(f'{query}')
    usdf_sql_results.configure(text=f'{str(mycursor.rowcount)} records updated.')


def generate_sql():
    """ Generate the SQL Query to execute. """
    query = 'UPDATE tracker SET Resolved = 1, SolutionID = 6 WHERE IssueID = 4 AND Resolved = 0'
    usdf_sql.delete('1.0', tk.END)
    if excluded_sites:
        query += f' AND Site NOT IN {str(tuple(excluded_sites))};'
    else:
        query += ';'
    usdf_sql.insert(tk.END, query)
    return query


def add_to_excluded_sites(a):
    """ Add sites to be excluded for the update SQL Query. """
    excluded_sites.append(site_entry_box.get())
    excluded_site_list.delete(0, 'end')
    for item in excluded_sites:
        excluded_site_list.insert('end', item)
    site_entry_box.delete(0, 'end')


def remove_from_excluded_sites():
    """ Remove selected sites from the exclusion list. """
    selection = int(excluded_site_list.curselection()[0])
    excluded_sites.remove(excluded_site_list.get(selection))
    excluded_site_list.delete(selection)


def change_mode(tog=[0]):
    """ Changes window colors for less stain on eyes. """
    tog[0] = not tog[0]
    frames = (unir_tab_frame, unir_site_list_frame, unir_button_frame, unir_sql_display_frame)
    widgets = (site_entry_label, space_holder, excluded_site_list_label, excluded_site_list,
               delete_button, construct_button, execute_button, usdf_title_label, usdf_sql,
               usdf_sql_results, night_mode_switch)

    night_background = '#000000'
    night_text = '#66ffff'
    day_background = '#f2f2f2'
    day_text = '#000000'

    if tog[0]:
        main_window.option_add('*Background', night_background)
        main_window.option_add('*Foreground', night_text)
        main_window.configure(background=night_background)
        for i in frames:
            i.config(background=night_background,
                     highlightbackground=night_background,
                     highlightcolor=night_background)
        for item in widgets:
            item.config(background=night_background, foreground=night_text)
        night_mode_switch.config(text='Day Mode')
    else:
        main_window.option_add('*Background', day_background)
        main_window.option_add('*Foreground', day_text)
        main_window.configure(background=day_background)
        for i in frames:
            i.config(background=day_background,
                     highlightbackground=day_background,
                     highlightcolor=day_background)
        for item in widgets:
            item.config(background=day_background, foreground=day_text)
        night_mode_switch.config(text='Night Mode')


excluded_sites = []

# Tkinter window properties
main_window = tk.Tk()
main_window.title('Unresolved Network Issues Resolver 1.4')
# main_window.iconbitmap('images/update.ico')
main_window.option_add('*Font', 'arial 9')
main_window.resizable(False, False)
unir_tab = ttk.Frame(main_window)

# UNIR Tab Top Frame
unir_tab_frame = tk.Frame(main_window)
unir_tab_frame.grid(row=0, column=0)
site_entry_label = tk.Label(unir_tab_frame, text='Enter Clinic to ignore (i.e. clinic is currently down): ')
site_entry_label.grid(row=0, column=0)
site_entry_box = tk.Entry(unir_tab_frame)
site_entry_box.grid(row=0, column=1, sticky='ew')
space_holder = tk.Label(unir_tab_frame, text='            ')
space_holder.grid(row=0, column=2, sticky='ew')
night_mode_switch = tk.Button(unir_tab_frame, text='Night Mode', command=change_mode)
night_mode_switch.grid(row=0, column=3, sticky='e')

# UNIR Site List Frame
unir_site_list_frame = tk.Frame(main_window)
unir_site_list_frame.grid(row=1, column=0)
excluded_site_list_label = tk.Label(unir_site_list_frame, text='Sites to exclude from resolving issues:')
excluded_site_list_label.grid(row=0, column=0)
excluded_site_list = tk.Listbox(unir_site_list_frame)
excluded_site_list.grid(row=1, column=0, sticky='ew')
excluded_site_list_scrollbar = tk.Scrollbar(unir_site_list_frame)
excluded_site_list_scrollbar.grid(row=1, column=1, sticky='nsw')
excluded_site_list.config(yscrollcommand=excluded_site_list_scrollbar.set)
excluded_site_list_scrollbar.config(command=excluded_site_list.yview)

# UNIR Button Frame
unir_button_frame = tk.Frame(main_window)
unir_button_frame.grid(row=2, column=0)
delete_button = tk.Button(unir_button_frame, text='Remove Site', command=remove_from_excluded_sites)
delete_button.grid(row=0, column=0)
construct_button = tk.Button(unir_button_frame, text='Construct SQL Script', command=generate_sql)
construct_button.grid(row=0, column=1, padx=10)
execute_button = tk.Button(unir_button_frame, text='Execute SQL', command=execute_sql)
execute_button.grid(row=0, column=2)

# UNIR SQL Display Frame
unir_sql_display_frame = tk.Frame(main_window)
unir_sql_display_frame.grid(row=3, column=0)
usdf_title_label = tk.Label(unir_sql_display_frame, text='SQL Code to Resolve Unresolved Network Issues:')
usdf_title_label.grid(row=0, column=0)
usdf_sql = tk.Text(unir_sql_display_frame, height=4)
usdf_sql.grid(row=1, column=0, padx=10)
usdf_sql_results = tk.Label(unir_sql_display_frame, text='', anchor='w')
usdf_sql_results.grid(row=2, column=0, sticky='ew', padx=10)

# Bindings, Focus, and Mainloop
site_entry_box.bind('<Return>', add_to_excluded_sites)
site_entry_box.focus()
main_window.mainloop()
