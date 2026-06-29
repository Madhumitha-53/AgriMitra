import streamlit as st

from ai.llm import get_response



def chatbot_ui(language="en"):


    st.markdown(
    """
    <div class="card">

    <h2 style="color:inherit;">
    💬 AgriMitra Chatbot
    </h2>

    <p style="color:inherit;">
    Ask your farming questions here
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



    if "messages" not in st.session_state:

        st.session_state.messages = []





    for message in st.session_state.messages:


        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )






    question = st.chat_input(
        "🌱 Ask farming question..."
    )



    if question:


        st.session_state.messages.append(

            {
            "role":"user",
            "content":question
            }

        )



        with st.chat_message("user"):

            st.markdown(question)





        with st.chat_message("assistant"):


            answer = "Sorry, I could not answer."

            with st.spinner(
                "🌾 Thinking..."
            ):


                try:

                    answer = get_response(
                        question
                    )

                except Exception as e:

                    answer = (
                        "Sorry, I could not answer. "
                        f"({e})"
                    )



            st.markdown(answer)




        st.session_state.messages.append(

            {
            "role":"assistant",
            "content":answer
            }

        )