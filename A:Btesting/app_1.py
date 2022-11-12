import streamlit as st
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
from PIL import Image
import datetime as dt
import squarify
import altair as alt

def judge_type(x):
    if x in ['111']:
        a='Best Customers'
    elif x in ['211','212']:
        a='Loyal Customers'
    elif x in ['121','122','221','222','214','213','144','132']:
        a='Potential Loyalists'
    elif x in ['221','231','241','141','131','133','134','142','242','232']:
        a='Big Spenders'
    elif x in ['311','321','312','313','322','323','333','332']:
        a='At Risk Customers'
    elif x in ['411','421','422','431','413','432','423','413','431','414','412','244','314'
               ,'441','442','341','342','331']:
        a='Can’t Lose Them'
    elif x in ['112','113','114','124','123','223','223','224','234','233','244','243','143']:
        a='Recent Customers'
    elif x in ['433','444','434','443','343','334','433','424','344','442','324']:
        a='Lost Cheap Customers'
    else:
        a='others'
    return a

orders = pd.read_csv('sample-orders.csv',sep=',')
NOW = dt.datetime(2014,12,31)

# Make the date_placed column datetime
orders['order_date'] = pd.to_datetime(orders['order_date'])

rfmTable = orders.groupby('customer').agg({'order_date': lambda x: (NOW - x.max()).days, # Recency
                                        'order_id': lambda x: len(x),      # Frequency
                                        'grand_total': lambda x: x.sum()}) # Monetary Value

rfmTable['order_date'] = rfmTable['order_date'].astype(int)
rfmTable.rename(columns={'order_date': 'recency', 
                         'order_id': 'frequency', 
                         'grand_total': 'monetary_value'}, inplace=True)

quantiles = rfmTable.quantile(q=[0.25,0.5,0.75])
rfmSegmentation = rfmTable

# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)
def RClass(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4
    
# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)
def FMClass(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1

rfmSegmentation['R_Quartile'] = rfmSegmentation['recency'].apply(RClass, args=('recency',quantiles,))
rfmSegmentation['F_Quartile'] = rfmSegmentation['frequency'].apply(FMClass, args=('frequency',quantiles,))
rfmSegmentation['M_Quartile'] = rfmSegmentation['monetary_value'].apply(FMClass, args=('monetary_value',quantiles,))

rfmSegmentation['RFMClass'] = rfmSegmentation.R_Quartile.map(str) \
                            + rfmSegmentation.F_Quartile.map(str) \
                            + rfmSegmentation.M_Quartile.map(str)


st.title('RFM Analysis Report')
    
st.header('Dataset')
st.write(rfmTable)
        
st.header('RFM Customer Quantile')
if st.button('Generate Quantile Plot.'):
    st.write(quantiles)
    #st.box_chart(quantiles.T)
    
st.header('RFM Customer Classification')
st.write(rfmSegmentation)
    
st.header('RFM Customer Type')

st.warning('1. Best Customers:')
"Highest frequency as well as monetary value with least recency"

st.warning('2. Loyal Customers:')
"   High frequency as well as monetary value with good recency"

st.warning('3. Potential Loyalists:')
"High recency and monetary value, average frequency"

st.warning('4. Big Spenders:')
"High monetary value but good recency and frequency values"

st.error('5. At Risk Customers:')
"Customer's shopping less often now who used to shop a lot"

st.error('6. Can’t Lose Them:')
"Customer's shopped long ago who used to shop a lot."

st.info('7. Recent Customers:')
"Customer's who recently started shopping a lot but with less monetary value"

st.error('8. Lost Cheap Customers:')
"shopped long ago but with less frequency and monetary value"
    
st.header('RFM Customer Segmentation Analysis')



if st.button('Segmentation RFM Plot.'):
    st.subheader('TOP 5 Customers')
    rfmSegmentation['Segment']=rfmSegmentation['RFMClass'].apply(lambda x :judge_type(x))
    top5_frame = rfmSegmentation[rfmSegmentation['RFMClass']=='111'].sort_values('monetary_value', ascending=False).head(5)
    st.write(top5_frame)

    # img =  Image.open("images/RFM.PNG")
    # st.image(img)
    rfm_segments = rfmSegmentation[rfmSegmentation.Segment!='Others'].reset_index().groupby('Segment')['customer'].count().reset_index(name='counts')
    st.subheader("The numbser of 8 type customers")
    #seg_frame = pd.DataFrame(rfm_segments)
    #seg_frame = rfm_segments[['Segment','counts']]
    c = alt.Chart(rfm_segments.iloc[:8]).mark_bar().encode(
    x='Segment',
    y='counts')
    st.altair_chart(c, use_container_width=True)

    st.subheader("The percentage of 8 type customers ")
    segment = list(rfm_segments.iloc[:8].Segment)
    score = list(rfm_segments.iloc[:8].counts)
    color_list = ["#248af1", "#eb5d50", "#8bc4f6", "#8c5c94", "#a170e8", "#fba521", "#75bc3f"]
    fig = plt.figure(figsize=(12,8))
    plt.title('Customer Segments distribution')
    squarify.plot(sizes=score, label=segment,color=color_list, alpha=0.7)
    st.pyplot(fig)

st.header("RFM Recommendation")
img =  Image.open("RFM_Recommendation.png")
st.image(img)

    

