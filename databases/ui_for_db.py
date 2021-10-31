# run in terminal (ctrl + j)
# streamlit run databases/ui_for_db.py
import streamlit as st
from db_example1 import open_db
from db_example1 import Student, Grade


def show_student_form():
    with st.form('f1'):
        name = st.text_input("enter student's name")
        c1,c2 = st.columns(2)
        klass = c1.text_input("enter student's class")
        section = c2.text_input("enter student's section")
        is_online = st.checkbox("is student attending online?")
        btn = st.form_submit_button("Add student")

    if btn and name and klass and section:
        db = open_db()
        db.add(Student(name = name, section = section, klass= klass)) # add the student detail
        db.commit() # save
        db.close() # close the db
        st.success("Saved Student details")
    

def show_grading_form():
    pass

# UI code
st.title("Database Example")

options = ['View Students','View Grades','Add Students','Add Grades']

choice = st.sidebar.radio("Select any option", options)

if choice == options[0]:
    pass
elif choice == options[1]:
    pass
elif choice == options[2]:
    show_student_form()
elif choice == options[3]:
    show_grading_form()