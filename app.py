import streamlit as st

# App ka Title
st.set_page_config(page_title="Quality & CAPA Assistant", layout="wide")

st.title("🛠️ Quality Management & CAPA Assistant")
st.write("Aapka AI-powered assistant customer complaints, CAPA generation aur quality queries ke liye.")

# Tabs banana (Do sections ke liye)
tab1, tab2 = st.tabs(["📋 Complaint & CAPA Generator", "🤖 Quality Q&A Assistant"])

# --- TAB 1: CAPA & Complaint Generator ---
with tab1:
    st.header("Customer Complaint to CAPA Generator")
    st.write("Yahan customer ki complaint aur defect description daalein taaki instant CAPA generate ho sake.")
    
    # Input fields
    customer_name = st.text_input("Customer Name / Company")
    product_name = st.text_input("Product / Part Name")
    defect_desc = st.text_area("Defect / Problem Description (Detail mein likhein)")
    
    if st.button("Generate CAPA & Action Plan"):
        if defect_desc.strip() == "":
            st.warning("Kripya pehle defect description darj karein!")
        else:
            with st.spinner("AI CAPA generate kar raha hai..."):
                # Yahan hum AI logic jodenge. Filhal ke liye yeh ek sample output dega:
                st.success("CAPA Successfully Generated!")
                
                st.markdown("### 🔍 Root Cause Analysis (RCA)")
                st.info("Potential Cause: Process parameters (Temperature/Pressure) mein deviation hone ki sambhavna hai ya operator training ki kami.")
                
                st.markdown("### ⚡ Corrective Action (Immediate Fix)")
                st.write(f"1. {customer_name} ke is batch ke saare products ko quarantine karein.\n2. Defective pieces ko re-work ya scrap karein.")
                
                st.markdown("### 🛡️ Preventive Action (Future Fix)")
                st.write("1. Machine calibration ki frequency ko badhaya jaye.\n2. Standard Operating Procedure (SOP) ka strict palan karwaya jaye.")

# --- TAB 2: Quality Q&A Assistant ---
with tab2:
    st.header("Quality & Manufacturing Q&A Assistant")
    st.write("Quality standards (ISO, 5S, Six Sigma) ya manufacturing se juda koi bhi sawal puchein.")
    
    user_query = st.text_input("Apna sawal yahan type karein (Jaise: 'Welding porosity ko kaise theek karein?')")
    
    if st.button("Get Answer"):
        if user_query.strip() == "":
            st.warning("Kripya koi sawal puchein!")
        else:
            with st.spinner("Jawab dhoondha ja raha hai..."):
                st.success("Jawab:")
                st.write(f"Aapke sawal ('{user_query}') ke liye expert recommendation yeh hai ki root cause ko identify karke standard quality parameters follow kiye jaane chahiye.")
