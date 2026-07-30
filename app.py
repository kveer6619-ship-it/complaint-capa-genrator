import streamlit as st

st.set_page_config(page_title="Advanced Quality & CAPA Assistant", layout="wide")

st.title("🛠️ Advanced Quality Management & CAPA Assistant")
st.write("Professional CAPA, Outflow Action, aur Fishbone Analysis ke liye AI Tool.")

tab1, tab2 = st.tabs(["📋 Complaint & CAPA Generator", "🤖 Quality Q&A Assistant"])

with tab1:
    st.header("Customer Complaint to Advanced CAPA Generator")
    st.write("Defect description daalein aur photo upload karein.")
    
    # NAYA FEATURE: Photo Upload
    uploaded_file = st.file_uploader("📸 Defect ki photo upload karein (Optional)", type=["jpg", "png", "jpeg"])
    
    customer_name = st.text_input("Customer Name / Company")
    product_name = st.text_input("Product / Part Name / Part Code")
    defect_desc = st.text_area("Defect / Problem Description (Detail mein likhein)")
    
    if st.button("Generate Professional CAPA"):
        if defect_desc.strip() == "":
            st.warning("Kripya pehle defect description darj karein!")
        else:
            with st.spinner("Advanced CAPA aur Fishbone Analysis taiyar ho raha hai..."):
                st.success("Professional CAPA Generated Successfully!")
                
                # Agar photo upload ki gayi hai toh yahan dikhayega
                if uploaded_file is not None:
                    st.image(uploaded_file, caption="Defect ki Image", use_container_width=True)
                
                # Download ke liye Report ka Data taiyar karna
                report_content = f"--- CAPA REPORT ---\n\nCustomer: {customer_name}\nProduct: {product_name}\nDefect Description: {defect_desc}\n\n"
                
                # 1. Immediate Outflow Action
                st.markdown("### 🚨 1. Immediate Outflow / Containment Action")
                outflow_text = f"- Stock Quarantine: {customer_name} ya warehouse mein available is batch/lot ke saare products ka dispatch turant rokein.\n- Line Inspection: Agar production line par ye issue active hai, toh line ko turant rok kar 100% sorting karwayein."
                st.write(outflow_text)
                report_content += "1. IMMEDIATE OUTFLOW ACTION\n" + outflow_text + "\n\n"
                
                # 2. Root Cause Analysis (Fishbone)
                st.markdown("### 🦴 2. Root Cause Analysis (Fishbone / Ishikawa - 4M1E)")
                st.write("- *Man:* Operator ki training ka abhav.\n- *Machine:* Tool wear/tear ya calibration error.\n- *Material:* Raw material variation.\n- *Method:* SOP deviation.\n- *Environment:* Temperature/Humidity impact.")
                fishbone_text = "Man: Operator training abhav.\nMachine: Tool wear/tear ya calibration error.\nMaterial: Raw material variation.\nMethod: SOP deviation.\nEnvironment: Temperature/Humidity impact."
                report_content += "2. ROOT CAUSE ANALYSIS (4M1E)\n" + fishbone_text + "\n\n"
                
                # 3. Corrective Action
                st.markdown("### ⚡ 3. Corrective Action (Permanent Fix)")
                ca_text = f"1. Defective parts ({product_name}) ko rework ya scrap karein.\n2. Machine ke component ko replace ya recalibrate karein."
                st.write(ca_text)
                report_content += "3. CORRECTIVE ACTION\n" + ca_text + "\n\n"
                
                # 4. Preventive Action
                st.markdown("### 🛡️ 4. Preventive Action (Future Proofing)")
                pa_text = "1. Poka-Yoke implement karein.\n2. SOP ko update karke retraining karwayein."
                st.write(pa_text)
                report_content += "4. PREVENTIVE ACTION\n" + pa_text + "\n\n"
                
                st.markdown("---")
                
                # NAYA FEATURE: Download Button
                st.download_button(
                    label="📥 Download CAPA Report (Text File)",
                    data=report_content,
                    file_name=f"CAPA_Report_{customer_name}.txt",
                    mime="text/plain"
                )

with tab2:
    st.header("Quality & Manufacturing Q&A Assistant")
    user_query = st.text_input("Apna sawal yahan type karein:")
    
    if st.button("Get Answer"):
        if user_query.strip() == "":
            st.warning("Kripya koi sawal puchein!")
        else:
            with st.spinner("Jawab dhoondha ja raha hai..."):
                st.success("Expert Recommendation:")
                st.write(f"Aapke sawal ('{user_query}') ke sandarbh mein, quality standards (jaise ISO/IATF) ke mutabiq 5-Why analysis aur cross-functional team review karna sabse uchit rahega.")
