{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import warnings\n",
    "import matplotlib.pyplot as plt\n",
    "warnings.filterwarnings('ignore')\n",
    "from PIL import Image\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "orders = pd.read_csv('sample-orders.csv',sep=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "NOW = dt.datetime(2014,12,31)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Make the date_placed column datetime\n",
    "orders['order_date'] = pd.to_datetime(orders['order_date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "rfmTable = orders.groupby('customer').agg({'order_date': lambda x: (NOW - x.max()).days, # Recency\n",
    "                                        'order_id': lambda x: len(x),      # Frequency\n",
    "                                        'grand_total': lambda x: x.sum()}) # Monetary Value\n",
    "\n",
    "rfmTable['order_date'] = rfmTable['order_date'].astype(int)\n",
    "rfmTable.rename(columns={'order_date': 'recency', \n",
    "                         'order_id': 'frequency', \n",
    "                         'grand_total': 'monetary_value'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "quantiles = rfmTable.quantile(q=[0.25,0.5,0.75])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "rfmSegmentation = rfmTable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)\n",
    "def RClass(x,p,d):\n",
    "    if x <= d[p][0.25]:\n",
    "        return 1\n",
    "    elif x <= d[p][0.50]:\n",
    "        return 2\n",
    "    elif x <= d[p][0.75]: \n",
    "        return 3\n",
    "    else:\n",
    "        return 4\n",
    "    \n",
    "# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)\n",
    "def FMClass(x,p,d):\n",
    "    if x <= d[p][0.25]:\n",
    "        return 4\n",
    "    elif x <= d[p][0.50]:\n",
    "        return 3\n",
    "    elif x <= d[p][0.75]: \n",
    "        return 2\n",
    "    else:\n",
    "        return 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "rfmSegmentation['R_Quartile'] = rfmSegmentation['recency'].apply(RClass, args=('recency',quantiles,))\n",
    "rfmSegmentation['F_Quartile'] = rfmSegmentation['frequency'].apply(FMClass, args=('frequency',quantiles,))\n",
    "rfmSegmentation['M_Quartile'] = rfmSegmentation['monetary_value'].apply(FMClass, args=('monetary_value',quantiles,))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "rfmSegmentation['RFMClass'] = rfmSegmentation.R_Quartile.map(str) \\\n",
    "                            + rfmSegmentation.F_Quartile.map(str) \\\n",
    "                            + rfmSegmentation.M_Quartile.map(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def app():\n",
    "    st.title('RFM Analysis Report')\n",
    "    \n",
    "    st.title('Dataset')\n",
    "    st.write(rfmTable)\n",
    "        \n",
    "    st.title('RFM Customer Quantile')\n",
    "    if st.button('Generate RFM Plot.'):\n",
    "        st.write(quantiles)\n",
    "    \n",
    "    st.title('RFM Customer Classification')\n",
    "    st.write(rfmSegmentation)\n",
    "    \n",
    "    st.title('RFM Customer Type')\n",
    "    st.write('Best Customers')\n",
    "    st.write('Loyal Customers')\n",
    "    st.write('Potential Loyalists')\n",
    "    st.write('Big Spenders')\n",
    "    st.write('At Risk Customers')\n",
    "    st.write('Can’t Lose Them')\n",
    "    st.write('Recent Customers')\n",
    "    st.write('Lost Cheap Customers')\n",
    "    \n",
    "    st.title('RFM Customer Segmentation Analysis')\n",
    "    if st.button('Generate RFM Plot.'):\n",
    "        img =  Image.open(\"images/RFM.PNG\")\n",
    "        st.image(img)\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
