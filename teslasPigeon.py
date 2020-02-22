import streamlit as st
import utility as ut
#import detection
import explore
import detection_simplified

########################################################################################################################
# main function
def main():
    st.sidebar.title("Navigation")
    select_operationMode()


########################################################################################################################
def select_operationMode():
    operationMode = st.sidebar.radio( "Please select the operation mode:",
                                      ("Camera", "Badges", "My Collection", "Explore", "Alternative"))

    if operationMode == "Camera":
        pass
        #detection.run()
    elif operationMode == "Badges":
        pass
    elif operationMode == "My Collection":
        pass
    elif operationMode == "Explore":
        explore.run()
    elif operationMode == "Alternative":
        detection_simplified.run()


########################################################################################################################
if __name__ == "__main__":
    # TODO for the final version this is supposed to be set to FALSE!!!
    menuFlag = False
    ut.show_menu( menuFlag )

    main()


