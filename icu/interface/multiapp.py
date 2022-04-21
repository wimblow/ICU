"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from PIL import Image

class MultiApp:

    def __init__(self):
        st.set_page_config(layout="wide")

        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        app = st.sidebar.radio(
            "Display",
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
