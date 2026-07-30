import streamlit as st

st.set_page_config(page_title="Advanced Quality & CAPA Assistant", layout="wide")

st.title("🛠️ Advanced Quality Management & CAPA Assistant")
st.write("Professional CAPA, Outflow Action, aur Fishbone Analysis ke liye AI Tool.")

tab1, tab2 = st.tabs(["📋 Complaint & CAPA Generator", "🤖 Quality Q&A Assistant"])

with tab1:
    st.header("Customer Complaint to Advanced CAPA Generator")
    st.write("Defect description daalein aur Outflow, CAPA, aur Fishbone analysis prapt karein.")
    
    customer_name = st.text_input("Customer Name / Company")
    product_name = st.text_input("Product / Part Name / Part Code")
    defect_desc = st.text_area("Defect / Problem Description (Detail mein likhein)")
    
    if st.button("Generate Professional CAPA"):
        if defect_desc.strip() == "":
            st.warning("Kripya pehle defect description darj karein!")
        else:
            with st.spinner("Advanced CAPA aur Fishbone Analysis taiyar ho raha hai..."):
                st.success("Professional CAPA Generated Successfully!")
                
                # 1. Immediate Outflow Action
                st.markdown("### 🚨 1. Immediate Outflow / Containment Action")
                st.write(f"- *Stock Quarantine:* {customer_name} ya warehouse mein available is batch/lot ke saare products ka dispatch turant rokein aur stock ko quarantine area mein move karein.")
                st.write("- *Line Inspection:* Agar production line par ye issue active hai, toh line ko turant rok kar 100% sorting karwayein.")
                
                # 2. Root Cause Analysis & Fishbone (4M1E)
                st.markdown("### 🦴 2. Root Cause Analysis (Fishbone / Ishikawa Diagram - 4M1E)")
                st.write("Defect ke mukhya karan in categories ke antargat analysis kiye gaye hain:")
                
                st.markdown("""
                * *👨‍🔧 Man (Operator):* 
                  * Operator ki proper training ka abhav ya shift change ke dauran communication gap.
                * *⚙️ Machine (Equipment):* 
                  * Tool wear and tear, machine calibration mein error, ya sensor ki kharabi.
                * *📦 Material (Raw Material):* 
                  * Raw material ki property mein variation ya supplier ki taraf se sub-standard batch.
                * *📋 Method (Process):* 
                  * SOP (Standard Operating Procedure) ka theek se palan na hona ya parameters mein deviation.
                * *🌡️ Environment:* 
                  * Shop floor par temperature, humidity ya lighting ka asar.
                """)
                
                # 3. Corrective Action
                st.markdown("### ⚡ 3. Corrective Action (Permanent Fix)")
                st.write(f"1. Defective parts ({product_name}) ko rework ya scrap karein.")
                st.write("2. Machine ke us specific component ko replace ya recalibrate karein jisse defect utpann hua.")
                
                # 4. Preventive Action
                st.markdown("### 🛡️ 4. Preventive Action (Future Proofing)")
                st.write("1. Poka-Yoke (Error-proofing) mechanism implement karein taaki operator dobara ye galti na kar sake.")
                st.write("2. SOP ko update karke sabhi operators ki retraining karwayi jaye.")

with tab2:
    st.header("Quality & Manufacturing Q&A Assistant")
    st.write("Quality standards aur manufacturing se juda koi bhi sawal puchein.")
    
    user_query = st.text_input("Apna sawal yahan type karein:")
    
    if st.button("Get Answer"):
        if user_query.strip() == "":
            st.warning("Kripya koi sawal puchein!")
        else:
            with st.spinner("Jawab dhoondha ja raha hai..."):
                st.success("Expert Recommendation:")
                st.write(f"Aapke sawal ('{user_query}') ke sandarbh mein, quality standards (jaise ISO/IATF) ke mutabiq 5-Why analysis aur cross-functional team review karna sabse uchit rahega.")
