import streamlit as st
from PIL import Image
import numpy as np 
import pandas as pd

import seaborn as sns 
import matplotlib.pyplot as plt
# Plotly Libraris
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

#header
st.header("Data Analysis for Mail Marketing")

#Intro for the project 
st.markdown("---")
st.write("Currently, there are lots of marketers who still insist on selling") 
st.write("their products directly via the mail. They send catalogs with product") 
st.write("characteristics to customers who then directly from the catalogs." )
st.write("Therefore, we want to learn that marketers have developed customer records to learn") 
st.write("what makes some customers spend more than others and predict their spending.")

st.markdown('##')
img =  Image.open("MailMkt.png")
st.image(img)
st.markdown('##')
st.markdown('##')

# Intro the feagures
st.markdown("#### Data analysis for each features ")
st.write('For the Analysis, we would analyze the features as follows:')
st.markdown('* **Age** \n * **Amount Spend** \n * **Salary** \n * **Gender** \n * **Ownhome** \n * **Location** \n * **Children** \n')

#load data
df = pd.read_csv('DirectMarketing.csv')

# Age
st.markdown("#### Age")
st.write("Age we divide the into three group:  Young(<=35),Middle(35-50),old(>50)")
st.write("1. Age Distribution For All")

col1, col2, col3 = st.columns([10,1,10])

df_age = df['Age'].value_counts().to_frame().reset_index().rename(columns={'index':'Age','Age':'count'})
fig = go.Figure(go.Bar(
    x=df_age['Age'],y=df_age['count'],
    marker={'color': df_age['count'], 
    'colorscale': 'Viridis'},  
    text=df_age['count'],
    textposition = "outside",
))

with col1:  
    fig_age = fig.update_layout(title_text='Age Distribution',xaxis_title="Age",yaxis_title="Count ",title_x=0.5)
    #fig.show()
    st.plotly_chart(fig_age, use_container_width=True)

with col3:
    fig = go.Figure([go.Pie(labels=df_age['Age'], values=df_age['count'], pull=[0.2,0,0],hole=0.4)])

    fig.update_traces(hoverinfo='percent', textinfo='value+percent', textfont_size=12,insidetextorientation='radial')

    fig_pie = fig.update_layout(title="Age Distribution",title_x=0.5)
    #fig.show()
    st.plotly_chart(fig_pie, use_container_width=True)

# Avg Salary group by Age
st.write("2. Average Salary group by Age")

df_age_salary = df.groupby(by = ['Age'])['Salary'].mean().to_frame().reset_index().rename(columns = {
                    'Salary':'AVG_Salary'})
df_age_amountSpent=df.groupby(by =['Age'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'Age':'Age1','AmountSpent':'AVG_AmountSpent'})
result = pd.concat([df_age_salary,df_age_amountSpent], axis=1)
result.drop(['Age1'],inplace = True,axis = 1)
result["AVG_Salary"]=result["AVG_Salary"].map(lambda x:round(x,2))
result["AVG_AmountSpent"]=result["AVG_AmountSpent"].map(lambda x:round(x,2))

fig = make_subplots(rows=2, cols=1,
                   subplot_titles=("Age AVG Salary ",
                                   "Age AVG Amount Spent " ))  # Subplot titles
# plot Avg Salary group by Age
fig.add_trace(go.Bar(
    x=result['Age'],y=result['AVG_Salary'],
    name="Mean Salary",
    marker={'color': result['AVG_Salary'], 
    'colorscale': 'fall'},  
    text=result['AVG_Salary'],
    textposition = "inside"),
    row=1, col=1         
)

fig.add_trace(go.Bar(
    x=result['Age'],y=result['AVG_AmountSpent'],
    name="Mean Amount Spent",
    marker={'color': result['AVG_AmountSpent'], 
    'colorscale': 'fall'},  
    text=result['AVG_AmountSpent'],
    textposition = "inside"),
    row=2, col=1         
)


fig_salary_age = fig.update_layout(title = "Age ",title_x=0.5)
#fig.show()
st.plotly_chart(fig_salary_age, use_container_width=True)
st.write("So from here, we can see that middle age group earns more and spend more")

fig = px.scatter(df, x='Salary', y='AmountSpent',trendline="ols",
                 color='Age') # Added color to basic scatter
fig_agesalart_spent = fig.update_layout(title='Age With Salary Vs Amount Spent ',xaxis_title="Salary",yaxis_title="Amount Spent",title_x=0.5)
# fig.show()
st.plotly_chart(fig_agesalart_spent, use_container_width=True)
st.markdown('Conclusion:\n * *Most of the customers are in the middle age group* \n * *Middle age group earns more and spends more* \n')




#AmountSpent
st.markdown("#### AmountSpent Distribution")
st.write("Now let's start to analyze AmountSpend")

col1, col2 = st.columns([10,10])

with col1:
    fig = go.Figure(data=[go.Histogram(x=df['AmountSpent'],  # To get Horizontal plot ,change axis - 
                                  marker_color="Crimson",
                       xbins=dict(
                      start=0, #start range of bin
                      end=6000,  #end range of bin
                      size=200   #size of bin
                      ))])
    fig_amount = fig.update_layout(title="Distribution Of Amount Spent",xaxis_title="Amount Spent ",yaxis_title="Counts",title_x=0.5)

    st.plotly_chart(fig_amount, use_container_width=True)

with col2:
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=df["AmountSpent"],
        name='Amount Spent',
        marker_color='royalblue',
        boxmean='sd' # represent mean and standard deviation
    ))
    fig_spend_dis = fig.update_layout(title = "Amount Spent Distribution ",title_x=0.5,
                 )
    st.plotly_chart(fig_spend_dis, use_container_width=True)
#fig.show()
st.markdown('Conclusion:\n Amountspend \n * *max:6217 * \n * *mean: 1216* \n * *median: 962* \n * *min: 348* \n')


# Salary
st.markdown("#### Salary")
col1, col2 = st.columns([10,10])

with col1:
    fig = go.Figure(data=[go.Histogram(x=df['Salary'],  # To get Horizontal plot ,change axis - 
                                  marker_color="Crimson",
                       xbins=dict(
                      start=0, #start range of bin
                      end=150000,  #end range of bin
                      size=5000   #size of bin
                      ))])
    fig_salary = fig.update_layout(title="Distribution Of Salary",xaxis_title="Salary ",yaxis_title="Counts",title_x=0.5)
    st.plotly_chart(fig_salary, use_container_width=True)

with col2:
    fig = go.Figure()
    fig.add_trace(go.Box(
        y=df["Salary"],
        name='Salary',
        marker_color='royalblue',
        boxmean='sd' # represent mean and standard deviation
    ))
    fig_salary_box = fig.update_layout(title = "Salary Distribution ",title_x=0.5,
                 )
    st.plotly_chart(fig_salary_box, use_container_width=True)

st.markdown('Conclusion:\n Salary \n * *max: 168.8k* \n * *mean: 56.1k* \n * *median: 53.7k* \n * *min: 10.1k* \n')



#gender
st.markdown("#### Gender")

df_Gender=df['Gender'].value_counts().to_frame().reset_index().rename(columns={'index':'Gender','Gender':'count'})

fig = go.Figure(go.Bar(
    x = df_Gender['Gender'], y=df_Gender['count'],
    marker = {'color':df_Gender['count'],
             'colorscale':'emrld'},
    text = df_Gender['count'],
    textposition = 'outside',
))
fig_gender = fig.update_layout(title_text = 'Gender Distribution',xaxis_title = 'Gender',
                 yaxis_title = 'Count',title_x = 0.5)
#fig.show()
st.plotly_chart(fig_gender, use_container_width=True)

df_Gender_Salary=df.groupby(by =['Gender'])['Salary'].mean().to_frame().reset_index().rename(columns={'Salary':'AVG_Salary'})
df_Gender_AmountSpent=df.groupby(by =['Gender'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'Gender':'Gender1','AmountSpent':'AVG_AmountSpent'})
result = pd.concat([df_Gender_Salary,df_Gender_AmountSpent], axis=1)
result.drop(['Gender1'],inplace=True,axis=1)
result["AVG_Salary"]=result["AVG_Salary"].map(lambda x:round(x,2))
result["AVG_AmountSpent"]=result["AVG_AmountSpent"].map(lambda x:round(x,2))

fig = make_subplots(rows=2, cols=1,
                   subplot_titles=("Gender AVG Salary ",
                                   "Gender AVG Amount Spent " ))  # Subplot titles
                                  

fig.add_trace(go.Bar(
    x=result['Gender'],y=result['AVG_Salary'],
    name="Mean Salary",
    marker={'color': result['AVG_Salary'], 
    'colorscale': 'fall'},  
    text=result['AVG_Salary'],
    textposition = "inside"),
    row=1, col=1         
)
fig.add_trace(go.Bar(
    x=result['Gender'],y=result['AVG_AmountSpent'],
    name="Mean Amount Spent",
    marker={'color': result['AVG_AmountSpent'], 
    'colorscale': 'fall'},  
    text=result['AVG_AmountSpent'],
    textposition = "inside"),
    row=2, col=1         
)

fig_avg_sa_group = fig.update_layout(title = "Gender ",title_x=0.5)
st.plotly_chart(fig_avg_sa_group, use_container_width=True)
#fig.show()
st.write("we can see men's salary is higher and spend more too.")

fig = px.scatter(df, x='Salary', y='AmountSpent',trendline="ols",
                 color='Gender') # Added color to basic scatter
fig_trend_for_gender = fig.update_layout(title='Gender With Salary Vs Amount Spent ',xaxis_title="Salary",yaxis_title="Amount Spent",title_x=0.5)
st.plotly_chart(fig_trend_for_gender, use_container_width=True)

#Age distribution by gender
st.write("1. Age distribution by gender")

df_G_and_A=df.groupby(by =['Gender','Age'])['Married'].count().to_frame().reset_index().rename(columns={'Gender':'Gender','Age':'Age','Married':'count'})

df_G_and_A=df.groupby(by =['Gender','Age'])['Married'].count().to_frame().reset_index().rename(columns={'Gender':'Gender','Age':'Age','Married':'count'})

fig = px.bar(df_G_and_A, x="Age", y="count",color="Gender",barmode="group",
             
             )
fig_G_A = fig.update_layout(title_text='Age Count With Gender',title_x=0.5,yaxis_title="Count",
                 )
st.plotly_chart(fig_G_A, use_container_width=True)
st.markdown('Conclusion:\n * *male middle group is main cusumption group* \n * *older men is the lowest* \n')



## Average amount distribution by gender and age group

st.markdown("#### Average amount distribution by gender and age group")
df_G_and_A=df.groupby(by =['Gender','Age'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'AmountSpent':'AVG_AmountSpent'})
df_G_and_A["AVG_AmountSpent"]=df_G_and_A["AVG_AmountSpent"].map(lambda x:round(x,2))

df_G_and_A=df.groupby(by =['Gender','Age'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'AmountSpent':'AVG_AmountSpent'})
df_G_and_A["AVG_AmountSpent"]=df_G_and_A["AVG_AmountSpent"].map(lambda x:round(x,2))

fig = px.bar(df_G_and_A, x="Age", y="AVG_AmountSpent",color="Gender",barmode="group",
             
             )
fig_amount_age_gender = fig.update_layout(title_text='Age Amount Spent With Gender,Age',title_x=0.5,yaxis_title="Amount Spent",
                 )
st.plotly_chart(fig_amount_age_gender, use_container_width=True)
st.markdown('Conclusion:\n * *Highest average spending:Male Old 1691* \n * *Lowest average spending: Female Young 501* \n')




# Plot gender age with amount spent
df_G_and_A_AVG=df.groupby(by =['Gender','Age'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'Gender':'Gender','Age':'Age','AmountSpent':'AVG_AmountSpent'})
df_G_and_A_Max=df.groupby(by =['Gender','Age'])['AmountSpent'].max().to_frame().reset_index().rename(columns={'Gender':'Gender1','Age':'Age1','AmountSpent':'Max_AmountSpent'})
df_G_and_A_Min=df.groupby(by =['Gender','Age'])['AmountSpent'].min().to_frame().reset_index().rename(columns={'Gender':'Gender2','Age':'Age2','AmountSpent':'Min_AmountSpent'})
df_G_and_A_Count=df.groupby(by =['Gender','Age'])['AmountSpent'].count().to_frame().reset_index().rename(columns={'Gender':'Gender3','Age':'Age3','AmountSpent':'Count'})
result = pd.concat([df_G_and_A_AVG, df_G_and_A_Max,df_G_and_A_Min,df_G_and_A_Count], axis=1)
result.drop(['Gender1','Gender2','Gender3','Age1','Age2','Age3'],inplace=True,axis=1)
result["AVG_AmountSpent"]=result["AVG_AmountSpent"].map(lambda x:round(x,2))
result["Gender_Age"]=result["Gender"]+" "+result["Age"]
result.drop(['Gender','Age'],inplace=True,axis=1)

fig = make_subplots(rows=4, cols=1,
                   subplot_titles=(" Mean Amount Spent",
                                   " Min Amount Spent",
                                   " Max Amount Spent",
                                   " Count "))  # Subplot titles

fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['AVG_AmountSpent'],
    name="Mean",
    marker={'color': result['AVG_AmountSpent'], 
    'colorscale': 'fall'},  
    text=result['AVG_AmountSpent'],
    textposition = "inside"),
    row=1, col=1         
)
fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['Min_AmountSpent'],
    name="Min",
    marker={'color': result['Min_AmountSpent'], 
    'colorscale': 'fall'},  
    text=result['Min_AmountSpent'],
    textposition = "inside"),
    row=2, col=1         
)
fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['Max_AmountSpent'],
    name="Max",
    marker={'color': result['Max_AmountSpent'], 
    'colorscale': 'fall'},  
    text=result['Max_AmountSpent'],
    textposition = "inside"),
    row=3, col=1           
)
fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['Count'],
    name="Count",
    marker={'color': result['Count'], 
    'colorscale': 'fall'},  
    text=result['Count'],
    textposition = "inside"),
    row=4, col=1           
)
fig.update_layout(title = "Gender Age With Amount Spent",title_x=0.5)
fig_g_a_amount = fig.update_xaxes(
        tickangle = 0,
        )

st.plotly_chart(fig_g_a_amount, use_container_width=True)
#st.markdown('Conclusion:\n * *Highest average spending:Male Old 1691* \n * *Lowest average spending: Female Young 501* \n')



## Average salary by gender and age


df_G_and_A_AVG=df.groupby(by =['Gender','Age'])['Salary'].mean().to_frame().reset_index().rename(columns={'Gender':'Gender','Age':'Age','Salary':'AVG_Salary'})
df_G_and_A_Max=df.groupby(by =['Gender','Age'])['Salary'].max().to_frame().reset_index().rename(columns={'Gender':'Gender1','Age':'Age1','Salary':'Max_Salary'})
df_G_and_A_Min=df.groupby(by =['Gender','Age'])['Salary'].min().to_frame().reset_index().rename(columns={'Gender':'Gender2','Age':'Age2','Salary':'Min_Salary'})
df_G_and_A_Count=df.groupby(by =['Gender','Age'])['Salary'].count().to_frame().reset_index().rename(columns={'Gender':'Gender3','Age':'Age3','Salary':'Count'})
result = pd.concat([df_G_and_A_AVG, df_G_and_A_Max,df_G_and_A_Min,df_G_and_A_Count], axis=1)
result.drop(['Gender1','Gender2','Gender3','Age1','Age2','Age3'],inplace=True,axis=1)
result["AVG_Salary"]=result["AVG_Salary"].map(lambda x:round(x,2))
result["Gender_Age"]=result["Gender"]+" "+result["Age"]
result.drop(['Gender','Age'],inplace=True,axis=1)

#plot Average salary by gender and age

fig = make_subplots(rows=4, cols=1,
                   subplot_titles=(" Mean Salary",
                                   " Min Salary",
                                   " Max Salary",
                                   " Count "))  # Subplot titles

fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['AVG_Salary'],
    name="Mean",
    marker={'color': result['AVG_Salary'], 
    'colorscale': 'fall'},  
    text=result['AVG_Salary'],
    textposition = "inside"),
    row=1, col=1         
)
fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['Min_Salary'],
    name="Min",
    marker={'color': result['Min_Salary'], 
    'colorscale': 'fall'},  
    text=result['Min_Salary'],
    textposition = "inside"),
    row=2, col=1         
)
fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['Max_Salary'],
    name="Max",
    marker={'color': result['Max_Salary'], 
    'colorscale': 'fall'},  
    text=result['Max_Salary'],
    textposition = "inside"),
    row=3, col=1           
)
fig.add_trace(go.Bar(
    x=result['Gender_Age'],y=result['Count'],
    name="Count",
    marker={'color': result['Count'], 
    'colorscale': 'fall'},  
    text=result['Count'],
    textposition = "inside"),
    row=4, col=1           
)
fig.update_layout(title = "Gender Age With Salary",title_x=0.5)
fig_g_a_salary = fig.update_xaxes(
        tickangle = 0,
        )
st.plotly_chart(fig_g_a_salary, use_container_width=True)
st.markdown('Conclusion:\n * *Middle age men is the mainly cosumption group* \n * *highest average spending is male old group, about 1691* \n')
st.markdown('* *lowest average spending is female young. about 501* \n * *highest average salary is male middle: 76.3k* \n * *lowest avaerage salary is femal young: 25.5k*\n')


# whether own home
st.markdown("#### whether own home")

col1, col2 = st.columns([10,10])

with col1:
    df_OwnHome=df['OwnHome'].value_counts().to_frame().reset_index().rename(columns={'index':'OwnHome','OwnHome':'count'})

    colors=['darkblue',"darkcyan"]

    fig = go.Figure([go.Pie(labels=df_OwnHome['OwnHome'], values=df_OwnHome['count'])])
    fig.update_traces(hoverinfo='label+percent', textinfo='percent+value', textfont_size=15,
                 marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig_ownhome = fig.update_layout(title="Own Home  Count",title_x=0.5)
    st.plotly_chart(fig_ownhome, use_container_width=True)

with col2:
    df_OwnHome_Salary=df.groupby(by =['OwnHome'])['Salary'].mean().to_frame().reset_index().rename(columns={'Salary':'AVG_Salary'})
    df_OwnHome_AmountSpent=df.groupby(by =['OwnHome'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'OwnHome':'OwnHome1','AmountSpent':'AVG_AmountSpent'})
    result = pd.concat([df_OwnHome_Salary,df_OwnHome_AmountSpent], axis=1)
    result.drop(['OwnHome1'],inplace=True,axis=1)
    result["AVG_Salary"]=result["AVG_Salary"].map(lambda x:round(x,2))
    result["AVG_AmountSpent"]=result["AVG_AmountSpent"].map(lambda x:round(x,2))

    # Plot the avg distribution for own home 

    fig = make_subplots(rows=2, cols=1,
                   subplot_titles=("Own Home AVG Salary ",
                                   "Own Home AVG Amount Spent " ))  # Subplot titles
                                  

    fig.add_trace(go.Bar(
        x=result['OwnHome'],y=result['AVG_Salary'],
        name="Mean Salary",
        marker={'color': result['AVG_Salary'], 
        'colorscale': 'fall'},  
        text=result['AVG_Salary'],
        textposition = "inside"),
        row=1, col=1         
        )
    fig.add_trace(go.Bar(
        x=result['OwnHome'],y=result['AVG_AmountSpent'],
        name="Mean Amount Spent",
        marker={'color': result['AVG_AmountSpent'], 
        'colorscale': 'fall'},  
        text=result['AVG_AmountSpent'],
        textposition = "inside"),
        row=2, col=1         
    )

    fig_home_avg = fig.update_layout(title = "Own Home",title_x=0.5)
    st.plotly_chart(fig_home_avg, use_container_width=True)

fig = px.scatter(df, x='Salary', y='AmountSpent',trendline="ols",
                 color='OwnHome') # Added color to basic scatter
fig_home_trend = fig.update_layout(title='Own Home With Salary Vs Amount Spent ',xaxis_title="Salary",yaxis_title="Amount Spent",title_x=0.5)
st.plotly_chart(fig_home_trend, use_container_width=True)
st.markdown('Conclusion:\n * *OwnHome distribution is balanced* \n * *Homeowners earn more and spend more* \n')


# Location
st.markdown("#### Location")

col1, col2 = st.columns([10,10])

with col1:
    df_Location=df['Location'].value_counts().to_frame().reset_index().rename(columns={'index':'Location','Location':'count'})

    fig = go.Figure(go.Bar(
    x=df_Location['Location'],y=df_Location['count'],
    marker={'color': df_Location['count'], 
    'colorscale': 'Viridis'},  
    text=df_Location['count'],
    textposition = "outside",
    ))
    fig_location = fig.update_layout(title_text='Location Distribution',xaxis_title="Location",yaxis_title="Count ",title_x=0.5)
    st.plotly_chart(fig_location, use_container_width=True)

with col2:
    df_Location_Salary=df.groupby(by =['Location'])['Salary'].mean().to_frame().reset_index().rename(columns={'Salary':'AVG_Salary'})
    df_Location_AmountSpent=df.groupby(by =['Location'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'Location':'Location1','AmountSpent':'AVG_AmountSpent'})
    result = pd.concat([df_Location_Salary,df_Location_AmountSpent], axis=1)
    result.drop(['Location1'],inplace=True,axis=1)
    result["AVG_Salary"]=result["AVG_Salary"].map(lambda x:round(x,2))
    result["AVG_AmountSpent"]=result["AVG_AmountSpent"].map(lambda x:round(x,2))

    # Plot the avg distribution for location

    fig = make_subplots(rows=2, cols=1,
                   subplot_titles=("Location AVG Salary ",
                                   "Location AVG Amount Spent " ))  # Subplot titles
                                  
    fig.add_trace(go.Bar(
        x=result['Location'],y=result['AVG_Salary'],
        name="Mean Salary",
        marker={'color': result['AVG_Salary'], 
        'colorscale': 'fall'},  
        text=result['AVG_Salary'],
        textposition = "inside"),
        row=1, col=1         
    )
    fig.add_trace(go.Bar(
        x=result['Location'],y=result['AVG_AmountSpent'],
        name="Mean Amount Spent",
        marker={'color': result['AVG_AmountSpent'], 
        'colorscale': 'fall'},  
        text=result['AVG_AmountSpent'],
        textposition = "inside"),
        row=2, col=1         
    )

    fig_location_avg = fig.update_layout(title = "Location ",title_x=0.5)
    #fig.show()
    st.plotly_chart(fig_location_avg, use_container_width=True)


fig = px.scatter(df, x='Salary', y='AmountSpent',trendline="ols",
                 color='Location') # Added color to basic scatter
fig_loc_trend = fig.update_layout(title='Location With Salary Vs Amount Spent ',xaxis_title="Salary",yaxis_title="Amount Spent",title_x=0.5)
st.plotly_chart(fig_loc_trend, use_container_width=True)
st.markdown('Conclusion:\n * *Most customers are close to the nearest physical store that sells similar products* \n * *Customers who are close to the nearest physical store selling similar products have lower spend, although their income is higher* \n')


# children

st.markdown("#### Children")

col1, col2 = st.columns([10,10])

with col1:
    df_Children=df['Children'].value_counts().to_frame().reset_index().rename(columns={'index':'Children','Children':'count'})

    colors=['darkblue',"darkcyan","CadetBlue","DarkSeaGreen"]

    fig = go.Figure([go.Pie(labels=df_Children['Children'], values=df_Children['count'])])
    fig.update_traces(hoverinfo='label+percent', textinfo='percent+value', textfont_size=15,
                 marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig_children = fig.update_layout(title="Children  Count",title_x=0.5)

    st.plotly_chart(fig_children, use_container_width=True)

with col2:
    fig = go.Figure(data=[go.Scatter(
        x=df_Children['Children'], y=df_Children['count'],
        mode='markers',
        marker=dict(
            color=df_Children['count'],
            size=df_Children['count']*0.1, # Multiplying by 0.3 to reduce size and stay uniform accross all points
            showscale=True
        ))])

    fig_scatter_ch = fig.update_layout(title='Children Distribution ',xaxis_title="Children Count  ",yaxis_title="Number Of Customers ",title_x=0.5)
    st.plotly_chart(fig_scatter_ch, use_container_width=True)


df_Children_Salary=df.groupby(by =['Children'])['Salary'].mean().to_frame().reset_index().rename(columns={'Salary':'AVG_Salary'})
df_Children_AmountSpent=df.groupby(by =['Children'])['AmountSpent'].mean().to_frame().reset_index().rename(columns={'Children':'Children1','AmountSpent':'AVG_AmountSpent'})
result = pd.concat([df_Children_Salary,df_Children_AmountSpent], axis=1)
result.drop(['Children1'],inplace=True,axis=1)
result["AVG_Salary"]=result["AVG_Salary"].map(lambda x:round(x,2))
result["AVG_AmountSpent"]=result["AVG_AmountSpent"].map(lambda x:round(x,2))
result


fig = make_subplots(rows=2, cols=1,
                   subplot_titles=("Children AVG Salary ",
                                   "Children AVG Amount Spent " ))  # Subplot titles
                                  

fig.add_trace(go.Bar(
    x=result['Children'],y=result['AVG_Salary'],
    name="Mean Salary",
    marker={'color': result['AVG_Salary'], 
    'colorscale': 'fall'},  
    text=result['AVG_Salary'],
    textposition = "inside"),
    row=1, col=1         
)
fig.add_trace(go.Bar(
    x=result['Children'],y=result['AVG_AmountSpent'],
    name="Mean Amount Spent",
    marker={'color': result['AVG_AmountSpent'], 
    'colorscale': 'fall'},  
    text=result['AVG_AmountSpent'],
    textposition = "inside"),
    row=2, col=1         
)

fig_avg_children = fig.update_layout(title = "Children ",title_x=0.5)

st.plotly_chart(fig_avg_children, use_container_width=True)
st.markdown('Conclusion:\n* *46 percent of customers do not have Children* \n* *Although customers incomes were close, there was a decrease in spending as the number of children increased* \n')


# Final Conclusion
st.markdown("#### Final Conclusion")

st.markdown('* *The main consuming group is middle group* \n * *Middle age group earns more and spends more* \n * *Men, especaiily middle age men, earn more spend more and they are the main consuming group*')
st.markdown('* *Lowest number of customers older men* \n* *Homeowners earn more and spend more* \n* *Most customers are close to the nearest physical store that sells similar products*')
st.markdown('* *Customers who are close to the nearest physical store selling similar products have lower spend , although their income is higher* \n* *the family onws more children, it would spend less* \n* *46 percent of customers do not have Children*')






