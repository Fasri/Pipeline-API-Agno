import streamlit as st
from agno.agent import Agent
from agno.tools.postgres import PostgresTools
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Configuração do banco de dados PostgreSQL
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host=HOST,
    port=PORT,
    db_name=DB_NAME,
    user=USER,
    password=PASSWORD,
    table_schema="public",
)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools], model=Groq(id="llama-3.3-70b-versatile"),
   )

agent.print_response("List the tables in the database", markdown=True)

agent.print_response("""
Please run a SQL query to get all sessions in `agent_sessions` created in the last 24 hours.
""")