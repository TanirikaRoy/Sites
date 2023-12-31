'''
import streamlit as st

def main():
    st.set_page_config(page_title='College Application', layout='wide', initial_sidebar_state='collapsed')

    # Define color theme
    primary_color = '#00A6FF'  # MIT Dark Blue
    secondary_color = '#3200FF'  # MIT Gold
    text_color = '#00A6FF'  # Black

    # Header
    st.markdown(
        f'<h1 style="color: {text_color}; text-align: center;">My College Application</h1>',
        unsafe_allow_html=True
    )
    st.write('')

    # Navigation buttons
    st.markdown(
        f'<div style="text-align: center;">'
        f'<a href="#about" style="background-color: {secondary_color}; '
        f'color: {text_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">About Me</a>'
        f'<a href="#academics" style="background-color: {secondary_color}; '
        f'color: {text_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">Academics</a>'
        f'<a href="#activities" style="background-color: {secondary_color}; '
        f'color: {text_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">Activities</a>'
        f'<a href="#contact" style="background-color: {secondary_color}; '
        f'color: {text_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">Contact</a>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.write('')

    # About Me section
    st.markdown('<h2 id="about" style="color: black;">About Me</h2>', unsafe_allow_html=True)
    st.write("I'm [Your Name], an aspiring student with a passion for technology and innovation. I am eager to contribute to the vibrant community at MIT and embrace the challenges of higher education.")
    st.write('Write a brief introduction about yourself, your background, and your interests.')
    st.write('')

    # Academics section
    st.markdown('<h2 id="academics" style="color: black;">Academics</h2>', unsafe_allow_html=True)
    st.write("I have maintained a strong academic record throughout my education, showcasing my commitment to learning and intellectual curiosity. I have excelled in various subjects, including math, science, and computer programming.")
    st.write('Highlight your academic achievements, courses, GPA, and any honors or awards.')
    st.write('')

    # Activities section
    st.markdown('<h2 id="activities" style="color: black;">Activities</h2>', unsafe_allow_html=True)
    st.write("Beyond the classroom, I have been actively involved in extracurricular activities that have shaped my leadership skills, fostered teamwork, and allowed me to make a positive impact in my community. From participating in robotics competitions to volunteering in local STEM initiatives, I have embraced opportunities that align with my passion for innovation.")
    st.write('Showcase your extracurricular activities, leadership roles, and community involvement.')
    st.write('')

    # Contact section
    st.markdown('<h2 id="contact" style="color: black;">Contact</h2>', unsafe_allow_html=True)
    st.write("Thank you for considering my application. Feel free to reach out to me for any further information or to discuss my qualifications in more detail.")
    st.write('- Email: yourname@example.com')
    st.write('- Phone: (123) 456-7890')

if __name__ == '__main__':
    main()
'''

import streamlit as st

def education_section():
    st.header("Education")
    st.subheader("Indian Institute of Technology Bombay, Mumbai, India")
    st.write("Bachelor of Technology in Chemical Engineering")
    st.write("CPI: 8.96/10 | Chemical Course CPI: 9.08/10")
    st.write("Dual Minor in Biosciences & Bioengineering and Humanities & Social Sciences")

    st.subheader("Fergusson College, Pune, India")
    st.write("Higher Secondary Certificate in Science with Electronics")
    st.write("Percentage: 92.62%")

    st.subheader("St. Mary’s School, Pune, India")
    st.write("Matriculation under Indian Certificate of Secondary Education [ICSE] Curriculum")
    st.write("Percentage: 98.40%")

def research_experience_section():
    st.header("Research Experience")
    st.subheader("Development of a Microfluidic Chip to study Cancer Cell Migration")
    st.write("Guide: Prof. Abhijit Majumder | IIT Bombay")
    # ... (details about the research experience)

def professional_experience_section():
    st.header("Professional Experience")
    st.subheader("ITC Limited - KITES Technical Intern - FMCG Gandhidham, Gujarat, India")
    st.write("Guide: Mr. Martin Jojo | Manager, Aashirvaad Salt | Foods Business Division")
    # ... (details about the professional experience)

# Define more sections for Teaching & Mentoring Experiences, Academic Projects, Technical Skills, Co-curricular Activities, etc.

def main():
    st.title("Tanirika Roy - Curriculum Vitae")
    st.markdown("**Contact:** +91 9890015831 | **Email:** tanirika.roy@iitb.ac.in | **Website:** [xyz site](https://www.example.com)")

    education_section()
    research_experience_section()
    professional_experience_section()
    # Call more sections here

    st.write("Generated using Streamlit")

if __name__ == "__main__":
    main()
