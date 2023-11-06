# Import libraries
import streamlit as st
import sqlite3
import os
import time

# Title
st.title("Counter App")
st.caption("""
            Count every request in this app.
            """)
st.subheader("",divider="rainbow")

# Variable
database_name = "counter.db"

# Create a database
if database_name in os.listdir():
    con = sqlite3.connect(database_name)
    cur = con.cursor()
else:
    con = sqlite3.connect(database_name)
    # Database Cursor (cur)
    cur = con.cursor()
    cur.execute("CREATE TABLE counter(hit, time)")
    con.commit()

# Counter
time = time.strftime("Date: %Y-%m-%d | Time: %H:%M:%S UTC")
hit = 1
### Insert into adatabase
cur.execute(f"""
        INSERT INTO counter VALUES
        ("{hit}", "{time}")
        """)
con.commit()

# Total hits
result = cur.execute("""
                    SELECT SUM(hit) 
                    FROM counter
                    """)
st.write(f"### Total hits: **{result.fetchone()[0]}**")

# Current hit
st.write(f"Current: {time}")
# Previous hits
st.subheader("",divider="rainbow")
st.write("### *Previous Hits*")
# Write the data
result = cur.execute("""
                    SELECT * 
                    FROM counter
                    ORDER BY time DESC
                    """)
for name, time in result.fetchall():
    st.text(f"{time}")
    
# Close Connection
con.close()
