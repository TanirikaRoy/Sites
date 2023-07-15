import streamlit as st

def main():
    st.set_page_config(page_title='College Application', layout='wide')

    # Define color theme
    primary_color = '#8b0000'  # Dark red
    secondary_color = '#ffd700'  # Gold

    # Header
    st.markdown(
        f'<h1 style="color: {primary_color}; text-align: center;">My College Application</h1>',
        unsafe_allow_html=True
    )
    st.write('')

    # Navigation buttons
    st.markdown(
        f'<div style="text-align: center;">'
        f'<a href="#about" style="background-color: {secondary_color}; '
        f'color: {primary_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">About Me</a>'
        f'<a href="#academics" style="background-color: {secondary_color}; '
        f'color: {primary_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">Academics</a>'
        f'<a href="#activities" style="background-color: {secondary_color}; '
        f'color: {primary_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">Activities</a>'
        f'<a href="#contact" style="background-color: {secondary_color}; '
        f'color: {primary_color}; padding: 10px 20px; margin-right: 10px; border-radius: 5px; '
        f'text-decoration: none; font-weight: bold;">Contact</a>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.write('')

    # About Me section
    st.markdown('<h2 id="about" style="color: black;">About Me</h2>', unsafe_allow_html=True)
    st.write('Write a brief introduction about yourself, your background, and your interests.')
    st.write('')

    # Academics section
    st.markdown('<h2 id="academics" style="color: black;">Academics</h2>', unsafe_allow_html=True)
    st.write('Highlight your academic achievements, courses, GPA, and any honors or awards.')
    st.write('')

    # Activities section
    st.markdown('<h2 id="activities" style="color: black;">Activities</h2>', unsafe_allow_html=True)
    st.write('Showcase your extracurricular activities, leadership roles, and community involvement.')
    st.write('')

    # Contact section
    st.markdown('<h2 id="contact" style="color: black;">Contact</h2>', unsafe_allow_html=True)
    st.write('Provide your contact information for college admissions officers to reach you.')
    st.write('- Email: yourname@example.com')
    st.write('- Phone: (123) 456-7890')

if __name__ == '__main__':
    main()
