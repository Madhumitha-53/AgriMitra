schemes = {


"rice":
"PM Kisan and crop insurance scheme",

"tomato":
"State horticulture subsidy",

"wheat":
"Farmer support scheme"


}



def get_scheme(crop):

    return schemes.get(
        crop.lower(),
        "Check local agriculture office schemes"
    )