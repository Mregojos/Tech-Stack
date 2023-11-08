# Import libraries
import streamlit as st
import psycopg2
import os
import time
from env import *

#----------Page Configuration----------# 
st.set_page_config(page_title="Matt Cloud Tech",
                   page_icon=":cloud:",
                   menu_items={
                       'About':"# Matt Cloud Tech"})

#----------About Me Section----------#
st.title(":cloud: Matt Cloud Tech")
st.subheader("", divider="rainbow")

st.write("""
        ### Good day :wave:.
        ### My name is :blue[Matt]. I am a Cloud Technology Enthusiast.
        ### Currently, I am learning and building Cloud Infrastructure, Data and CI/CD Pipelines, and Intelligent Systems. 
        """) 
st.divider()
st.write(":link: :computer: [Personal Website](https://)")
st.write(":link: :book: [Project Repository](https://)")
st.write(":link: :notebook: [Blog](https://)")
st.write(":link: :hand: [Connect with me](https://)")
#----------End of About Me Section----------#

#----------Portfolio Section----------#
st.header("Project Collections",divider="rainbow")

st.write("#### :link: [PROJECT TITLE #1](https://)")
st.caption("Caption")
with st.expander(f"Learn more"):
    st.write("Description")
    
st.divider()

st.write("#### :link: [PROJECT TITLE #2](https://)")
st.caption("Caption")
with st.expander(f"Learn more"):
    st.write("Description")
st.divider()

#----------End of Portfolio Section----------#


#----------Notepad Section----------#
# Notepad Section
# Header
st.header("Notepad :notebook:",divider="rainbow")
st.caption("""
            Add your thoughts here! It will be stored in a database! \n
            :warning: :red[Do not add sensitive data.]
            """)
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
            :man: {name} \n""")
    st.caption(f":watch: {time}")
    st.success("Successfully Added.")
    # st.balloons()
    ### Insert into adatabase
    SQL = "INSERT INTO notes (name, header, note, time) VALUES(%s, %s, %s, %s);"
    data = (name, header, note, time)
    cur.execute(SQL, data)
    con.commit()
    
# Previous Notes 
st.divider()
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
            :man: {name} \n""")
    st.caption(f":watch: {time}")

    with st.expander(f"Edit or Delete (ID #: {id})"):
        name = st.text_input(f"Your Name (ID #: {id})", name)
        header = st.text_input(f"Header (ID #: {id})", header)
        note = st.text_area(f"Note (ID #: {id})", note)
        if st.button(f"UPDATE ID #: {id}"):
            SQL = " UPDATE notes SET id=%s, name=%s, header=%s, note=%s WHERE id = %s"
            data = (id, name, header, note, id)
            cur.execute(SQL, data)
            con.commit()
            st.success("Successfully Edited.")
        if st.button(f"DELETE ID #: {id}"):
            cur.execute(f"DELETE FROM notes WHERE id = {id}")
            con.commit()
            st.success("Successfully Deleted.")
    st.subheader("",divider="gray")
    
# Close Connection
cur.close()
con.close()
#----------End of Notepad Section----------#

#----------Counter----------#
# Title
st.header("Counter")
st.caption("""
            Count every request in this app.
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
cur.execute("CREATE TABLE IF NOT EXISTS counter(id serial PRIMARY KEY, view int, time varchar)")
con.commit()

# Counter
import time
time = time.strftime("Date: %Y-%m-%d | Time: %H:%M:%S UTC")
view = 1
### Insert into a database
SQL = "INSERT INTO counter (view, time) VALUES(%s, %s);"
data = (view, time)
cur.execute(SQL, data)
con.commit()

# Total views
cur.execute("""
                SELECT SUM(view) 
                FROM counter
                """)
st.write(f"### Total views: **{cur.fetchone()[0]}**")

# Current view
st.write(f"Current: {time}")
# Previous hits
st.divider()
with st.expander("See Previous Views"):
    st.write("**Previous Views**")
    # Write the data
    cur.execute("""
                SELECT * 
                FROM counter
                ORDER BY time DESC
                """)
    for _, _, time in cur.fetchall():
        st.text(f"{time}")
    
# Close Connection
cur.close()
con.close()

#----------Agent Section----------#
import time
st.header(":eyeglasses: Agent :construction:",divider="rainbow")
st.caption("### Chat with my agent (still under construction)")
st.write(f":violet[Your chat will be stored in a database, so use the same name to see your past conversations]")
st.caption(":warning: :red[Do not add sensitive data.]")


               
# Variable
database_name = DBNAME
# Connect to a database
con = psycopg2.connect(f"""
                       dbname={DBNAME}
                       user={USER}
                       host={HOST}
                       port={PORT}
                       password={PASSWORD}
                       """)
cur = con.cursor()
# Create a table if not exists
cur.execute("CREATE TABLE IF NOT EXISTS chats(id serial PRIMARY KEY, name varchar, prompt varchar, output varchar, time varchar)")
con.commit()

# Prompt
input_name = st.text_input("Your Name:")
agent = st.toggle("**Let's go**")
if agent:
    st.write(f"Your name for this chat is :blue[{input_name}]")
    prompt = st.chat_input("Talk to my agent")
    if prompt:
        time = time.strftime("Date: %Y-%m-%d | Time: %H:%M:%S UTC")
        st.write(f":blue[{input_name}]: {prompt}")
        st.caption(f"{time}")
        output = "I'm still learning :book:. Check back later."
        st.success(f":eyeglasses: Agent: {output}")
        st.divider()

        ### Insert into a database
        SQL = "INSERT INTO chats (name, prompt, output, time) VALUES(%s, %s, %s, %s);"
        data = (input_name, prompt, output, time)
        cur.execute(SQL, data)
        con.commit()


        with st.expander(f"See Previous Conversation for {input_name}"):
            cur.execute(f"""
                        SELECT * 
                        FROM chats
                        WHERE name='{input_name}'
                        ORDER BY time DESC
                        """)
            for id, name, prompt, output, time in cur.fetchall():
                    st.write(f":blue[{name}]: {prompt}")
                    st.caption(f"{time}")
# Close Connection
cur.close()
con.close()
#----------End of Agent Section----------#