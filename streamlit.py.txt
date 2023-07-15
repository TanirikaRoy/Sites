import streamlit as st

def main():
    st.title('My College Application')
    
    menu = ['About Me', 'Academics', 'Activities', 'Contact']
    choice = st.sidebar.selectbox('Menu', menu)
    
    if choice == 'About Me':
        about_me()
    elif choice == 'Academics':
        academics()
    elif choice == 'Activities':
        activities()
    elif choice == 'Contact':
        contact()
    
def about_me():
    st.header('About Me')
    st.write('Write a brief introduction about yourself, your background, and your interests.')

def academics():
    st.header('Academics')
    st.write('Highlight your academic achievements, courses, GPA, and any honors or awards.')

def activities():
    st.header('Activities')
    st.write('Showcase your extracurricular activities, leadership roles, and community involvement.')

def contact():
    st.header('Contact')
    st.write('Provide your contact information for college admissions officers to reach you.')
    st.write('- Email: yourname@example.com')
    st.write('- Phone: (123) 456-7890')

if __name__ == '__main__':
    main()
