import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import *
import json
from PIL import Image

# %%
# Create a session to Snowflake with credentials
with open("creds.json") as f:
    connection_parameters = json.load(f)
session = Session.builder.configs(connection_parameters).create()

# %%
# Header
head1, head2 = st.columns([8, 1])

with head1:
    st.header("Mail Marketing Spend Prediction Model")
with head2:
    st.markdown(
        f' <img src="https://api.nuget.org/v3-flatcontainer/snowflake.data/0.1.0/icon" width="50" height="50"> ',
        unsafe_allow_html=True)

img =  Image.open("MailMkt.png")
st.image(img)
st.markdown('##')
st.markdown('##')

# %%
# Customer Spend Slider Column
col1, col2, col3 = st.columns([4, 1, 10])

# Connect Snowflake
customer_df = session.table('PREDICTED_CUSTOMER_SPENDING')

# Read Data: Salary, catalogs, location, children, history
# minhi, maxhi, 
# mintow, maxtow,
# minasl, maxasl, mintoa, maxtoa, 
minlom, maxlom, minsa, maxsa, minch, maxch, minca, maxca = customer_df.select(
    # floor(min(col("AGE"))),
    # ceil(max(col("AGE"))),
    # floor(min(col("GENDER"))),
    # ceil(max(col("GENDER"))),
    # floor(min(col("OWNHOME"))),
    # ceil(max(col("OWNHOME"))),
    floor(min(col("LOCATION"))),
    ceil(max(col("LOCATION"))),
    floor(min(col("SALARY"))),
    ceil(max(col("SALARY"))),
    floor(min(col("CHILDREN"))),
    ceil(max(col("CHILDREN"))),
    # floor(min(col("HISTORY"))),
    # ceil(max(col("HISTORY"))),
    floor(min(col("CATALOGS"))),
    ceil(max(col("CATALOGS")))
).toPandas().iloc[0, ]

# minasl = int(minasl)
# maxasl = int(maxasl)
# mintoa = int(mintoa)
# maxtoa = int(maxtoa)
# mintow = int(mintow)
# maxtow = int(maxtow)
minlom = int(minlom)
maxlom = int(maxlom)
minsa  = int(minsa)
maxsa = int(maxsa)
minch = int(minch)
maxch = int(maxch)
# minhi = int(minhi)
# maxhi = int(maxhi)
minca = int(minca)
maxca = int(maxca)

# Column 1
with col1:
    st.markdown("#### Search Criteria")
    st.markdown('##')
    #asl = st.slider("Age Group (1: Young 2: Middle 3: Old)", minasl, maxasl, (minasl, minasl+2), 1)
    #st.write("Session Length ", asl)
    #toa = st.slider("Gender (1: Female 2: Male)", mintoa, maxtoa, (mintoa, mintoa+1), 1)
    #st.write("Time on App ", toa)
    #tow = st.slider("Ownhome (1: Own 2: Non-Own)", mintow, maxtow, (mintow, mintow+1), 1)
    #st.write("Time on Website ", tow)
    lom = st.slider("Far from the store (1: close 2: far)", minlom,
                    maxlom, (minlom, minlom+2), 1)
    #st.write("Length of Membership ", lom)
    #SALARY
    sa = st.slider("Salary)", minsa,
                     maxsa, (minsa, minsa+1), 1)
    ch = st.slider("How many children", minch,
                    maxch, (minch, minch+3), 1)
    # hi = st.slider("History (1: close 2: far)", minhi,
    #                  maxhi, (minhi, minlhi+4), 1)
    ca = st.slider("Catalogs", minca,
                    maxca, (minca, minca+5), 1)

    hi = st.radio(
    "The Frequency of History:0:never,1:high,2:low",
    (0, 1, 2))

# Column 2 (3)
with col3:
    #avg_sess_len = st.slider("Avg. Session Length", min_sess_len, max_sess_len, (min_sess_len,min_sess_len+1), 1)
    st.markdown("#### Mail Marketing Customer Predicted Spending")
    st.markdown('##')

    minspend, maxspend = customer_df.filter(
        # (col("AGE") <= asl[1]) & (
        #     col("AGE") > asl[0])
        # & (col("GENDER") <= toa[1]) & (col("GENDER") > toa[0])
        # & (col("OWNHOME") <= tow[1]) & (col("OWNHOME") > tow[0])
          (col("LOCATION") <= lom[1]) & (col("LOCATION") > lom[0])
        & (col("SALARY") <= sa[1]) & (col("SALARY") > sa[0])
        & (col("CHILDREN") <= ch[1]) & (col("CHILDREN") > ch[0])
        # & (col("HISTORY") <= hi[1]) & (col("HISTORY") > hi[0])
        & (col("HISTORY") == hi) 
        & (col("CATALOGS") <= ca[1]) & (col("CATALOGS") > ca[0])
    ).select(trunc(min(col('PREDICTED_SPEND'))), trunc(max(col('PREDICTED_SPEND')))).toPandas().iloc[0, ]

    st.write(f'This customer is likely to spend between ')
    st.metric(label="", value=f"${minspend}")
    #st.write("and")
    st.metric(label="and", value=f"${maxspend}")
    #st.write(f'This customer is likely to spend between ')

    st.markdown("---")
    st.write("\nThe biggest drivers of customer spend are:")
    st.markdown('* **Distance to store** \n * **Salary** \n * **The number of children** \n * **Catalogs** \n * **Purchase History**')
    st.write("You can see spend range change much more when one of these variables is changed.")