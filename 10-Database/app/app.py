# Import libraries
import streamlit as st
import psycopg2
import os
import time
from env import *

# Header
st.write("# Notepad :notebook:")
st.caption("""
            Add your thoughts here! It will be stored in a database! \n
            :warning: :red[Do not add sensitive data].
            """)
st.subheader("",divider="rainbow")

# Variable
database_name = DBNAME

con = psycopg2.connect(f"""
                       dbname={DBNAME}
                       user={USER}
                       host={HOST}
                       port={PORT}
                       password={PASSWORD}
                       """)
cur = con.cursor()
# Create a table if not exists
cur.execute("CREATE TABLE IF NOT EXISTS notes(id serial PRIMARY KEY, name varchar, header varchar, note varchar, time varchar)")
con.commit()

# Inputs
name = st.text_input("Your Name")
header = st.text_input("Header")
note = st.text_area("Note")
if st.button("Add a note"):
    time = time.strftime("Date: %Y-%m-%d | Time: %H:%M:%S UTC")
    st.write(f""" \n
            ##### :pencil: {header} \n
            #### {note} \n
            :man: {name} \n
            :watch: {time}""")
    st.success("Successfully Added.")
    # st.balloons()
    ### Insert into adatabase
    SQL = "INSERT INTO notes (name, header, note, time) VALUES(%s, %s, %s, %s);"
    data = (name, header, note, time)
    cur.execute(SQL, data)
    con.commit()
    
# Previous Notes 
st.subheader("",divider="rainbow")
st.write("### *Previous Notes*")
# Write the data
cur.execute("""
            SELECT * 
            FROM notes
            ORDER BY time DESC
            """)
for id, name, header, note, time in cur.fetchall():
    st.write(f""" \n
            ##### :pencil: {header} \n
            #### {note} \n
            :man: {name} \n
            :watch: {time}""")
#    if st.button(f"UPDATE ID #: {id}"):
#        name = st.text_input(f"Your Name (ID #: {id})", name)
#        header = st.text_input(f"Header (ID #: {id})", header)
#        note = st.text_area(f"Note (ID #: {id})", note)
#        if st.button(f"CONFIRM UPDATE ID #: {id}"):
#            cur.execute(f"UPDATE notes SET id={id}, name={name}, header={header}, note={note} WHERE id = {id}")
#            con.commit()
#            st.success("Successfully Edited.")
    if st.button(f"DELETE ID #: {id}"):
        cur.execute(f"DELETE FROM notes WHERE id = {id}")
        con.commit()
        st.success("Successfully Deleted.")
    st.subheader("",divider="gray")
    
# Close Connection
cur.close()
con.close()
