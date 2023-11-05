# Import libraries
import streamlit as st
import sqlite3
import os
import time

# Header
st.subheader("Simple Notepad :notebook:")
st.caption("""
            Add your thoughts here! It will be stored in a database! \n
            :warning: :red[Do not add sensitive data].
            """)
st.subheader("",divider="rainbow")

# Variable
database_name = "notes.db"

# Create a database
if database_name in os.listdir():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
else:
    con = sqlite3.connect(database_name)
    # Database Cursor (cur)
    cur = con.cursor()
    cur.execute("CREATE TABLE notes(name, note, time)")
    con.commit()

# Inputs
name = st.text_input("Your Name here")
note = st.text_area("Add Note here")
if st.button("Add a note"):
    time = time.strftime("Date: %Y-%m-%d | Time: %H:%M:%S UTC")
    st.write(f""" \n
            ### :pencil: {note} \n
            :man: {name} \n
            :watch: {time}""")
    st.success("Successful Added.")
    # st.balloons()
    ### Insert into adatabase
    cur.execute(f"""
            INSERT INTO notes VALUES
            ("{name}", "{note}", "{time}")
            """)
    con.commit()
    
# Previous Notes 
st.subheader("",divider="rainbow")
st.write("## *Previous Notes*")
# Write the data
result = cur.execute("""
                    SELECT * 
                    FROM notes
                    ORDER BY time DESC
                    """)
for name, note, time in result.fetchall():
    st.write(f""" \n
            ### :pencil: {note} \n
            :man: {name} \n
            :watch: {time}""")
    st.subheader("",divider="gray")
    
# Close Connection
con.close()







