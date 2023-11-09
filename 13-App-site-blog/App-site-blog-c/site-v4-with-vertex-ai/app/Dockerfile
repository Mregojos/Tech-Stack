FROM python
WORKDIR /app
RUN pip install streamlit psycopg2-binary google-cloud-aiplatform -q
COPY app.py env.py ./app/
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
