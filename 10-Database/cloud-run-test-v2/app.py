# Import libraries
import streamlit as st
import psycopg2
import os
import time
import vertexai
from vertexai.language_models import TextGenerationModel
from env import *

#----------Page Configuration----------# 
st.set_page_config(page_title="Matt Cloud Tech",
                   page_icon=":cloud:",
                   menu_items={
                       'About':"# Matt Cloud Tech Version 4"})

#----------About Me Section----------#
st.title(":cloud: Matt Cloud Tech v4")
st.header("", divider="rainbow")

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
# with st.expander(f"Learn more"):
#    st.write("Description")
    
st.divider()

st.write("#### :link: [PROJECT TITLE #2](https://)")
st.caption("Caption")
# with st.expander(f"Learn more"):
#    st.write("Description")
st.divider()

#----------End of Portfolio Section----------#

#----------Counter----------#
st.header("Counter")
st.caption("""
            Count every request in this app.
            """)
st.subheader("",divider="rainbow")

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
# Previous views
st.divider()
with st.expander("See Previous Views"):
    st.write("**Previous Views**")
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
#----------End of Counter----------#

st.write("It's working. tag4")
st.write(USER)
