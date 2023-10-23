import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd
import numpy as np


# constants
IMG_ADDRESS = "https://drzinph.com/wp-content/uploads/2020/05/image-6.png"


# functions
def extract_descriptors(smile: str) -> dict:
    descriptors = {}
    processed_smile = Chem.MolFromSmiles(smile)

    for descriptor_name, descriptor_function in Descriptors._descList:
        try:
            get_descriptor = descriptor_function(processed_smile)
            descriptors[descriptor_name] = get_descriptor
        except Exception as error:
            print(str(error))
            descriptors[descriptor_name] = np.nan

    return descriptors

# web app

# title
st.title("Predictions through Chem Descriptor")
# set an image
st.image(IMG_ADDRESS, caption = "Molecular Descriptors")

# text input 
smile = st.text_input("Enter the Canonical Smile Notation")

if smile:
    with st.spinner("Extracting Descriptors.."):
        descriptor_dict = extract_descriptors(smile)
        #st.dataframe(pd.DataFrame(descriptor_dict, index=[0]))
        with st.sidebar:
            # set header
            st.header("Extracted Descriptors")
            # set descriptors
            st.json(descriptor_dict)

tab1, tab2 = st.tabs(["Explanation", "Prediction"])

with tab1:
    st.subheader("Explanation on Descriptors...")
    with st.expander("What are Descriptors?"):
        st.write("Molecular descriptors, also known as chemical descriptors or molecular fingerprints, are numerical or binary representations of the chemical and structural characteristics of molecules. These descriptors are used in cheminformatics and computational chemistry to quantitatively describe various properties of chemical compounds. Molecular descriptors can provide valuable information for tasks such as compound screening, drug design, property prediction, and similarity analysis.")
    

