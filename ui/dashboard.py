import streamlit as st



def show_dashboard(
    crop,
    fertilizer,
    water,
    risk,
    scheme,
    language="en"
):


    texts = {


    "en":{

    "title":"📊 Smart Farm Dashboard",
    "crop":"🌱 Crop",
    "fert":"🧪 Fertilizer",
    "water":"💧 Water",
    "risk":"🐛 Pest Risk",
    "scheme":"🏛 Government Scheme"

    },



    "ta":{

    "title":"📊 ஸ்மார்ட் பண்ணை டாஷ்போர்டு",
    "crop":"🌱 பயிர்",
    "fert":"🧪 உரம்",
    "water":"💧 நீர்",
    "risk":"🐛 பூச்சி அபாயம்",
    "scheme":"🏛 அரசு திட்டம்"

    },



    "hi":{

    "title":"📊 स्मार्ट फार्म डैशबोर्ड",
    "crop":"🌱 फसल",
    "fert":"🧪 खाद",
    "water":"💧 पानी",
    "risk":"🐛 कीट जोखिम",
    "scheme":"🏛 योजना"

    },


    "te":{

    "title":"📊 స్మార్ట్ ఫామ్ డ్యాష్‌బోర్డ్",
    "crop":"🌱 పంట",
    "fert":"🧪 ఎరువు",
    "water":"💧 నీరు",
    "risk":"🐛 పురుగు ప్రమాదం",
    "scheme":"🏛 పథకం"

    }

    }



    t = texts.get(
        language,
        texts["en"]
    )



    st.markdown(

    f"""

<h1 class="main-title">

{t['title']}

</h1>

""",

    unsafe_allow_html=True

    )





    cards=[


    ("🌱",t["crop"],crop),

    ("🧪",t["fert"],fertilizer),

    ("💧",t["water"],water),

    ("🐛",t["risk"],risk),

    ("🏛",t["scheme"],scheme)

    ]




    cols = st.columns(3)



    for i,(icon,title,value) in enumerate(cards):


        with cols[i % 3]:


            st.markdown(

            f"""

<div class="card dashboard-card">


<div class="dashboard-icon">

{icon}

</div>



<div class="dashboard-title">

{title}

</div>



<div class="dashboard-value">

{value}

</div>


</div>


""",

            unsafe_allow_html=True

            )