import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

GRAVITY = {"Mercury": 0.38, "Venus": 0.90, "Earth": 1.00, "Moon": 0.17, "Mars": 0.38,
           "Jupiter": 2.53, "Saturn": 1.07, "Uranus": 0.89, "Neptune": 1.14}

st.title("ميزان الفضاء")

weight = st.number_input("وزنك على الأرض (كجم)", min_value=1.0, value=50.0)
planet = st.selectbox("اختاري الكوكب", list(GRAVITY.keys()))

new_weight = weight * GRAVITY[planet]
difference = new_weight - weight

st.metric(f"وزنك على {planet}", f"{new_weight:.1f} كجم", delta=f"{difference:.1f} كجم")

if GRAVITY[planet] < 1:
    st.success(f"جاذبيتك أخف، وتقدرين تقفزين أعلى بحوالي {1 / GRAVITY[planet]:.1f} مرة.")
elif GRAVITY[planet] > 1:
    st.warning("جاذبية هذا الكوكب أقوى من الأرض، ستشعرين بثقل أكبر.")
else:
    st.info("هذه هي الأرض، وزنك كما هو.")

all_weights = pd.Series({name: weight * g for name, g in GRAVITY.items()})
st.bar_chart(all_weights)