import streamlit as st

st.set_page_config(page_title="Learning Path Generator")

st.title("🎓 AI Learning Path Generator")
st.write("Create your personal learning roadmap!")

topic = st.text_input("What do you want to learn?")

level = st.selectbox(
    "Select your level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Generate Learning Path"):
    if topic:
        st.success("Your learning path is ready!")

        steps = [
            f"Understand the basics of {topic}",
            f"Learn important concepts of {topic}",
            f"Practice {topic} with exercises",
            f"Build a small project using {topic}",
            f"Review and improve your {topic} skills"
        ]

        for i, step in enumerate(steps, 1):
            st.write(f"{i}. {step}")
    else:
        st.warning("Please enter a topic!")
