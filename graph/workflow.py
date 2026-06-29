from langgraph.graph import StateGraph, END



class FarmerState(dict):
    pass




def check_information(state):


    query = state.get(
        "query",
        ""
    )


    if not query:


        return {

            "query":"",

            "response":
            "Please repeat your farming question"

        }



    return {


        "query":query,

        "response":query

    }





workflow = StateGraph(
    FarmerState
)



workflow.add_node(

    "check",

    check_information

)



workflow.set_entry_point(
    "check"
)



workflow.add_edge(
    "check",
    END
)



workflow = workflow.compile()




def process_query(text):


    if not text:

        return ""



    result = workflow.invoke(

        {
            "query":text
        }

    )


    if result is None:

        return text



    return result.get(

        "response",

        text

    )