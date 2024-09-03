import streamlit as st


st.set_page_config(page_title="Nathaniel Tampus", page_icon="🌊", layout="wide")

tab1, tab2 = st.tabs(["Home", "Contact"])

with tab1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="https://nize.foo/images/nize.png" style="background-color: #fbf1c7; border-radius: 100%;" width="144" height="144" />
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<h1 style="text-align: center;">Nathaniel "nize" Tampus</h1>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h5 style="text-align: center;">Web Developer | BSIT-4 Student</h5>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; margin-top: 2rem;">
            <p style="text-align: justify; max-width: 80ch; font-size: 1.25rem; text-indent: 2rem;">I'm Nathaniel, also known online as nize, and I'm a self-taught web developer and currently in my 4th year pursuing my Bachelor of Science in Information Technology degree at CIT University.</p>
            <p style="text-align: justify; max-width: 80ch; font-size: 1.25rem; text-indent: 2rem;">I started my programming journey in high school when I discovered game scripting and modding in online video games. I fell in love with the idea of problem solving mixed with creativity in programming and since then I explored various fields such as game development, graphics programming, and finally - web development.</p>
            <p style="text-align: justify; max-width: 80ch; font-size: 1.25rem; text-indent: 2rem;">Nowadays, I build freelance projects for my clients from simple websites to interactive web applications with various tech stacks such as TypeScript, Python, and Go. I'm also trying to get in the world of technopreneurship by building my own SaaS products and services. Business is nice and all, but I'm still a software engineer at heart.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h2 style="text-align: center; margin-top: 2rem;">Featured Projects</h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 1rem; flex-direction: column;">
        <div style="display: flex; gap: 1rem; justify-content: space-between; max-width: 820px;">
        <div style="display: flex; flex: 1; flex-direction: column; align-items: center; background-color: #32302f; border-radius: 1rem; padding: 1rem;">
            <h3 style="text-align: center;">Venur</h3>
            <p style="text-align: center;">An upcoming personalized ecommerce platform for freelancers and MSMEs.</p>
            <a href="https://venur.me" target="_blank" style="text-align: center; color: #8ec07c;">venur.me</a>
        </div>
        <div style="display: flex; flex: 1; flex-direction: column; align-items: center; background-color: #32302f; border-radius: 1rem; padding: 1rem;">
            <h3 style="text-align: center;">Mugnavo</h3>
            <p style="text-align: center;">A developer collective and agency building software solutions and open-source products.</p>
            <a href="https://mugnavo.com" target="_blank" style="text-align: center; color: #8ec07c;">mugnavo.com</a>
        </div>
        </div>

        <div style="display: flex; gap: 1rem; justify-content: space-between; max-width: 820px;">
        <div style="display: flex; flex: 1; flex-direction: column; align-items: center; background-color: #32302f; border-radius: 1rem; padding: 1rem;">
            <h3 style="text-align: center;">chessu</h3>
            <p style="text-align: center;">Open-source multiplayer chess for playing and watching games with friends online.</p>
            <a href="https://github.com/dotnize/chessu" target="_blank" style="text-align: center; color: #8ec07c;">github.com/dotnize/chessu</a>
        </div>
        <div style="display: flex; flex: 1; flex-direction: column; align-items: center; background-color: #32302f; border-radius: 1rem; padding: 1rem;">
            <h3 style="text-align: center;">StartUpSphere</h3>
            <p style="text-align: center;">Our capstone project - 3D mapping for startup ecosystems.</p>
            <a href="https://startupsphere.mugnavo.com" target="_blank" style="text-align: center; color: #8ec07c;">startupsphere.mugnavo.com</a>
        </div>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with tab2:
    st.markdown(
        """
        <h2 style="text-align: center; margin-top: 2rem;">Contact</h2>

        <p style="text-align: center; font-size: 1.25rem;">You can email me at <a href="mailto:nate@mugnavo.com" style="color: #8ec07c;">nate@mugnavo.com</a></p>
        <p style="text-align: center; font-size: 1.25rem; margin-top: 3rem;">You can also reach me through the following platforms:</p>

        <div style="display: flex; flex-direction: column; align-items: center; gap: 1rem">
            <a href="https://nize.foo" target="_blank" style="font-size: 1.25rem; color: #8ec07c;">nize.foo</a>
            <a href="https://github.com/dotnize" target="_blank" style="font-size: 1.25rem; color: #8ec07c;">github.com/dotnize</a>
            <a href="https://linkedin.com/in/nize" target="_blank" style="font-size: 1.25rem; color: #8ec07c;">linkedin.com/in/nize</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

css = """
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.25rem;
    }
    section.main > div {max-width:960px}
</style>
"""

st.markdown(css, unsafe_allow_html=True)
