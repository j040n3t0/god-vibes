import streamlit as st

def add_logo():
  st.markdown(
      """
      <style>
        [data-testid="stSidebarNav"] {
            background-image: url(https://res.cloudinary.com/grand-canyon-university/image/fetch/w_750,h_564,c_fill,g_faces,q_auto/https://www.gcu.edu/sites/default/files/media/images/Blog/theology-ministry/Cross-sunset.jpg);
            background-repeat: no-repeat;
            background-size: 40% 30%;
            padding-top: 100px;
            background-position: 20px 20px;
        }
        [data-testid="stSidebarNav"]::before {
            content: "~~~~~~~";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 30px;
            position: relative;
            top: 80px;
        }
      </style>
      """,
      unsafe_allow_html=True,
  )