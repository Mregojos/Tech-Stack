# Import libraries
import streamlit as st
import sqlite3
import os

# Header
st.subheader("Simple Notepad :notebook:")
st.caption("""
            Add your thoughts here! It will be stored in a database! \n
            :warning: :red[Do not add sensitive data].
            """)
st.subheader("",divider="rainbow")

# Variable
database_name = "notes.db"
con = sqlite3.connect(database_name)
cur = con.cursor()

# Create a database
if database_name in os.listdir():
    pass
else:
    con = sqlite3.connect(database_name)
    # Database Cursor (cur)
    cur = con.cursor()
    cur.execute("CREATE TABLE notes(name, note)")

# Inputs
name = st.text_input("Your Name here")
note = st.text_area("Add Note here")
if st.button("Add a note"):
    st.write(name,":", note)
    st.success("Successful Added.")
    # st.balloons()
    ### Insert into adatabase
    cur.execute(f"""
            INSERT INTO notes VALUES
            ("{name}", "{note}")
            """)
    con.commit()
    
# Previous Notes 
st.subheader("",divider="rainbow")
st.write("**Previous Notes**")
# Write the data
result = cur.execute("""
                    SELECT * 
                    FROM notes
                    ORDER BY name DESC
                    """)
for name, note in result.fetchall():
    st.write(name,":", note)
    
# Close Connection
con.close()







