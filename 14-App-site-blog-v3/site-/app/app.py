# Import libraries
import streamlit as st
import psycopg2
import os
import time
from env import *

#----------Agent Section Only using chat_messgae----------#
import time
st.header(":computer: Agent :construction:",divider="rainbow")
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
        message = st.chat_message("user")
        message.write(f":blue[{input_name}]: {prompt}")
        message.caption(f"{time}")
        message = st.chat_message("assistant")
        output = "I'm still learning :book:. Check back later."
        message.success(f"Agent: {output}")
        message.caption(f"{time}")
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
                        ORDER BY time ASC
                        """)
            for id, name, prompt, output, time in cur.fetchall():
                message = st.chat_message("user")
                message.write(f":blue[{name}]: {prompt}")
                message.caption(f"{time}")
                message = st.chat_message("assistant")
                output = "I'm still learning :book:. Check back later."
                message.success(f"Agent: {output}")
                message.caption(f"{time}")
# Close Connection
cur.close()
con.close()
#----------End of Agent Section----------#

