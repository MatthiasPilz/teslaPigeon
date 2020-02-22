import streamlit as st
import glob
import streamlit.ReportThread as ReportThread

from state import get_state
from streamlit.ScriptRequestQueue import RerunData
from streamlit.ScriptRunner import RerunException
from streamlit.server.Server import Server


def rerun():
    """Rerun a Streamlit app from the top!"""
    widget_states = _get_widget_states()
    raise RerunException(RerunData(widget_states))


def _get_widget_states():
    ctx = ReportThread.get_report_ctx()

    session = None
    session_infos = Server.get_current()._session_infos.values()

    for session_info in session_infos:
        s = session_info.session
        if (
                (hasattr(s, '_main_dg') and s._main_dg == ctx.main_dg)
                or
                (not hasattr(s, '_main_dg') and s.enqueue == ctx.enqueue)
        ):
            session = s

    if session is None:
        raise RuntimeError("ERROR: while working with SessionState of streamlit")

    return session._widget_states


from dataclasses import dataclass

########################################################################################################################
@dataclass
class MyState:
    flag_todo: bool

def setup() -> MyState:
    return MyState( flag_todo = False )

state = get_state(setup)


########################################################################################################################
def button_resetAllStates(k, place):
    if place.button("reset", key=k):
        reset_allStates()
        rerun()


########################################################################################################################
def reset_allStates():
    state.flag_todo = False


########################################################################################################################
# print title on the screen (center aligned)
def show_title( text ):
    s = "<h1 style='text-align: center; '>" + text + "</h1>"
    st.markdown(s, unsafe_allow_html=True)


########################################################################################################################
# print subtitle on the screen (center aligned)
def show_subtitle( text ):
    s = "<h3 style='text-align: center; '>" + text + "</h3>"
    st.markdown(s, unsafe_allow_html=True)


########################################################################################################################
# Download a single file and make its content available as a string.
@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    with open(path, "r") as myfile:
        data = myfile.read()
        return data


########################################################################################################################
def select_file( ):
    fileNames = [f for f_ in [glob.glob(e) for e in ("*.png", "*.jpg", ".jpeg")] for f in f_]
    fileNames.insert(0, 'none')
    selectedFileName = st.selectbox("", fileNames)
    return selectedFileName


########################################################################################################################
def show_menu( flag ):
    if not flag:
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)


