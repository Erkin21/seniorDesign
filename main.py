import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl

# Functions Like Get Data Here
def enter_data():
    terms = accept_status_var.get()
    
    if terms == 'Accepted':
        # Identification
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        gender = gender_combobox.get()
        ethnicity = ethnicity_combobox.get()

        # Address
        street = street_entry.get()
        city = city_entry.get()
        state = state_entry.get()

        # Medical History
        family = family_alz_entry.get()
        q1 = memory_q1_entry.get()
        q2 = memory_q2_entry.get()
        q3 = memory_q3_entry.get()
        q4 = memory_q4_entry.get()
        q5 = memory_q5_entry.get()

        print("First Name: ", firstname, "Last Name: ", lastname)
        print("Title: ", title, "Age: ", age, "Gender: ", "Ethnicity: ", ethnicity)
        print("Street: ", street, "City: ", city, "State: ", state)
        print("Terms and Conditions: ", terms)
        print("-------------------------------------------------")

        filepath = ""

        if not os.path.exists(filepath):                                                       # Check if the filepath exist if not create it in here
            workbook = openpyxl.Workbook()                                                     # Open workbook like an Excel sheet
            sheet = workbook.worksheets[0]                                                      # workbook.active or The active here is the sheet that is seen at the bottom of excel "sheet 1, sheet 2..."
            heading = ["First Name", "Last Name", "Title","Age", "Gender", "Ethnicity",
                       "Street", "City", "State", "Terms and Conditions",
                       "Family", "Q1", "Q2", "Q3", "Q4", "Q5"]
            sheet.append(heading)                                                              # Write the heading into the excel sheet
            workbook.save(filepath)                                                            # Save it

        # This few lines are for when you after you created the work book and want to save data
        workbook = openpyxl.load_workbook(filepath)
        if not 'Sheet 1' in workbook.sheetnames:
            workbook.create_sheet(title = "Sheet 1")
        sheet = workbook["Sheet 1"]
        sheet.append([firstname, lastname, title, age, gender, ethnicity,
                      street, city, state, terms,
                      family, q1, q2, q3, q4, q5])
        workbook.save(filepath)

    else:
        tkinter.messagebox.showwarning(title = "Error", message = "You have not accepted the terms")

# =====================================================================================

# Create a Data Entry Form
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# User Information
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 0, column = 0, sticky = "news", padx = 10, pady = 10)

# First Declare it then put it into the grid
first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row=0, column = 0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid(row = 0, column = 1)

# This is for input data, again declare it and then put into the grid
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

# Title like Mr. Ms. Dr. and none/""
title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["","Mr.", "Ms.", "Dr."])
title_label.grid(row = 0, column = 2)
title_combobox.grid(row = 1, column = 2)

# Age
age_label = tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_ = 18, to = 110)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

# Gender
gender_label = tkinter.Label(user_info_frame, text = "Gender")
gender_combobox = ttk.Combobox(user_info_frame, values = ["Male", "Female"])
gender_label.grid(row = 2, column = 1)
gender_combobox.grid(row = 3, column = 1)

# Nationality
ethnicity_label = tkinter.Label(user_info_frame, text = "Ethnicity")
ethnicity_combobox = ttk.Combobox(user_info_frame, values = ["Asian", "White","Black","Hispanic", "Native American", "Other"])
ethnicity_label.grid(row = 2, column = 2)
ethnicity_combobox.grid(row = 3, column = 2)

# Change format here for info frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 5, pady = 5)

# ======================================================================================

# Address Frame
user_address_frame = tkinter.LabelFrame(frame, text = "Address")
user_address_frame.grid(row = 1, column = 0, sticky = "news", padx = 10, pady = 10)

# Street
street_label = tkinter.Label(user_address_frame, text = "Street Address")
street_entry = ttk.Entry(user_address_frame)
street_label.grid(row = 0, column = 0)
street_entry.grid(row = 1, column = 0)

# City
city_label = tkinter.Label(user_address_frame, text = "City")
city_entry = ttk.Entry(user_address_frame)
city_label.grid(row = 0, column = 1)
city_entry.grid(row = 1, column = 1)

# State
state_label = tkinter.Label(user_address_frame, text = "State")
state_entry = ttk.Entry(user_address_frame)
state_label.grid(row = 0, column = 3)
state_entry.grid(row = 1, column = 3)

# Change format for Address Frame
for widget in user_address_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# ======================================================================================

# Medical History Frame
history_frame = tkinter.LabelFrame(frame, text = "Medical History")
history_frame.grid(row = 2, column = 0, sticky = "news", padx = 10, pady = 10)

# Family member Alzheimer
family_alz = tkinter.Label(history_frame, text = "Is there a history of Alzheimer’s in your family?")
family_alz_entry = ttk.Combobox(history_frame, values = ["Yes", "No", "Unsure"])
family_alz.grid(row = 0, column = 0)
family_alz_entry.grid(row = 0, column = 1)

# q1 Has your memory worsened in the past two years? 
memory_q1 = tkinter.Label(history_frame, text = "Has your memory worsened in the past two years?")
memory_q1_entry = ttk.Combobox(history_frame, values = ["Yes", "No"])
memory_q1.grid(row = 1, column = 0)
memory_q1_entry.grid(row = 1, column = 1)

# q2 Do you frequently forget appointments and events?
memory_q2 = tkinter.Label(history_frame, text = "Do you frequently forget appointments and events?")
memory_q2_entry = ttk.Combobox(history_frame, values = ["Yes", "No"])
memory_q2.grid(row = 2, column = 0)
memory_q2_entry.grid(row = 2, column = 1)

# q3 Do you frequently forget appointments and events?
memory_q3 = tkinter.Label(history_frame, text = "Do you frequently forget appointments and events?")
memory_q3_entry = ttk.Combobox(history_frame, values = ["Yes", "No"])
memory_q3.grid(row = 3, column = 0)
memory_q3_entry.grid(row = 3, column = 1)

# q4 Do you frequently misplace personal items?
memory_q4 = tkinter.Label(history_frame, text = "Do you frequently misplace personal items?")
memory_q4_entry = ttk.Combobox(history_frame, values = ["Yes", "No"])
memory_q4.grid(row = 4, column = 0)
memory_q4_entry.grid(row = 4, column = 1)

# q5 Do you often exercise or are you active?
memory_q5 = tkinter.Label(history_frame, text = "Do you often exercise or are you active?")
memory_q5_entry = ttk.Combobox(history_frame, values = ["Yes", "No"])
memory_q5.grid(row = 5, column = 0)
memory_q5_entry.grid(row = 5, column = 1)

# Change format for Medical History
for widget in history_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# ======================================================================================

# Terms & Conditions
terms_con_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_con_frame.grid(row = 4, column = 0, sticky = "news", padx = 10, pady = 10)

accept_status_var = tkinter.StringVar(value = "Denied")
accept_check = tkinter.Checkbutton(terms_con_frame, text = "I accept the terms & conditions", variable = accept_status_var, offvalue = "Denied", onvalue = "Accepted")
accept_check.grid(row = 0, column = 0)

# ======================================================================================

# Button to Enter Data
button = tkinter.Button(frame, text = "Enter Data", command = enter_data)
button.grid(row = 5, column = 0, sticky = "news", padx = 10, pady = 10)

window.mainloop()
