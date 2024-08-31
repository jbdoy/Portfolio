import streamlit as st

# Sidebar with profile picture and name
st.sidebar.image("prof_p.jpg", width=300)
st.sidebar.title("Jennifer Bendoy")
st.sidebar.markdown("**4th year BSIT Student**")

# Main page title
st.title("Welcome to My Portfolio")

# About Me section
st.header("About Me")
st.write("""
Hello! I'm Jennifer Bendoy, a passionate BSIT student with a strong interest in technology and design.
I enjoy working on projects that involve software development, UI/UX design, and data analysis.
""")

# Education section
st.header("Education")
st.write("- **Bachelor of Science in Information Technology** - Cebu Institute of Technology University")
st.write("- **Senior High Strand**: TVL - ICT - Southwestern University PHINMA")

# Skills section
st.header("Skills")
st.write("""
- **Programming Languages**: Python, JavaScript
- **Web Development**: HTML, CSS, React.js, Django
- **Design Tools**: Figma, Adobe XD
- **Code Editors**: Visual Studio Code (VS Code)
""")

# Portfolio Section
st.header("Portfolio")
st.write("Here are some of my projects:")

#Projects   
st.subheader("NutriChef (2024)")
st.write("NutriChef is a smart recipe assistant that tailors recipes to your dietary needs, preferences, and available ingredients. Built with Python, Django, and React.js, it uses natural language processing to deliver personalized, context-aware recipe suggestions through an intuitive interface.")
st.image("nutrichef.jpg", use_column_width=True)

st.subheader("DeliverYey (2024)")
st.write("DeliverYey is a web app that lets students order food from the school canteen. It allows menu browsing, item selection, optional online payment, and classroom delivery. The app aims to streamline ordering, cut wait times, and improve convenience for students and staff.")
st.image("deliveryey.jpg")

# Contact section
st.header("Contact")
st.write("Email: jenniferbendoy02@gmail.com")

# Footer
st.markdown("---")
st.markdown("© 2024 Jennifer Bendoy")
