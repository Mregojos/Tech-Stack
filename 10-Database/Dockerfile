FROM python
WORKDIR /app
RUN pip install streamlit psycopg2-binary -q
COPY app.py .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
