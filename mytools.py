from langchain_core.tools import tool 


@tool
def get_user_Details()-> dict[str, any]:
    """
    strictly return users name
    """
    users = {
       "name": "alex",
       "age" : 23
    }
    return users