FROM python
WORKDIR /app
COPY . /app
RUN pip install streamlit -q
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
