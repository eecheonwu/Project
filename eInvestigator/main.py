import streamlit as st
from elawyer_engine import process_input, analyze_input
from setup import check_and_install_packages 


st.set_page_config(layout="centered")

def stream_print(text):
    """Prints text character by character with a delay."""
    horizontal_output = ""
    for i in range(len(text)):
        horizontal_output += text[i]
    # Print the entire string horizontally
    st.write(horizontal_output) 


def main():
    st.title("Nigerian Law AI Assistant")
    
    # Input fields based on chosen type
    input_data = st.text_area("Ask AI lawyer anything on the Nigerian Constitution and Criminal laws:", height=100)

    # Create a container for the buttons
    button_container = st.container()
    with button_container:
        col1, col2 = st.columns([4, 1])  # Divide the container into two columns
        with col1:
            # Analyze button
            if st.button("Provide Answer", key="default"):
                try:
                    processed_input = process_input("text", input_data)
                    # Analyze the processed input
                    relevant_documents = analyze_input(processed_input, input_data)

                    # Display results
                    st.subheader("Relevant Legal Submission:")

                    # Display the combined output in a text area
                    stream_print(relevant_documents)
                    
                except Exception as e:
                    st.error(f"Error: {e}")  
        with col2:
            def refresh_state():
                st.session_state.refresh += 1
                
                
            if 'refresh' not in st.session_state:
                st.session_state.refresh = 0
            st.button('Refresh', on_click=refresh_state)
                
                
    
if __name__ == "__main__":
    check_and_install_packages()
    main()