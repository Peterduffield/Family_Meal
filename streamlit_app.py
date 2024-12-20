import streamlit as st
import pandas as pd
from snowflake.snowpark import Session

from pages import intro
from pages import analytics
from pages import engineering
from pages import enablement
from pages import apps
from pages import architecture
from pages import managed_services
from pages import tech_ops
from pages import ai_ml
from pages import em

PAGES = {
        "Intro": intro,
        "Analytics": analytics,
        "Engineering": engineering,
        "Enablement": enablement,
        "Apps": apps,
        "Architecture": architecture,
        "Managed Services": managed_services,
        "TechOps": tech_ops,
        "AI/ML": ai_ml,
        "EM": em,
    }

def main():
    st.sidebar.title("Navigation")

    choice = st.sidebar.radio("Select a page:", list(PAGES.keys()))
    if choice in PAGES:
        PAGES[choice].main()
if __name__ == "__main__":
    main()