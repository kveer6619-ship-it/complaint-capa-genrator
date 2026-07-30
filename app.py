import streamlit as st
import random

st.set_page_config(page_title="Advanced Quality & CAPA Assistant", layout="wide")

st.title("🛠️ Advanced Quality Management & CAPA Assistant")
st.write("Professional CAPA, Outflow Action, aur Fishbone Analysis ke liye AI Tool.")

tab1, tab2 = st.tabs(["📋 Complaint & CAPA Generator", "🤖 Quality Q&A Assistant"])

with tab1:
    st.header("Customer Complaint to Advanced CAPA Generator")
    st.write("Defect description daalein aur photo upload karein.")
    
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
                
                if uploaded_file is not None:
                    st.image(uploaded_file, caption="Defect ki Image", use_container_width=True)
                
                report_content = f"--- CAPA REPORT ---\n\nCustomer: {customer_name}\nProduct: {product_name}\nDefect Description: {defect_desc}\n\n"
                
                st.markdown("### 🚨 1. Immediate Outflow / Containment Action")
                outflow_text = f"- Stock Quarantine: {customer_name} ya warehouse mein available is batch/lot ke saare products ka dispatch turant rokein.\n- Line Inspection: Agar production line par ye issue active hai, toh line ko turant rok kar 100% sorting karwayein."
                st.write(outflow_text)
                report_content += "1. IMMEDIATE OUTFLOW ACTION\n" + outflow_text + "\n\n"
                
                st.markdown("### 🦴 2. Root Cause Analysis (Fishbone / Ishikawa - 4M1E)")
                st.write("- *Man:* Operator ki training ka abhav.\n- *Machine:* Tool wear/tear ya calibration error.\n- *Material:* Raw material variation.\n- *Method:* SOP deviation.\n- *Environment:* Temperature/Humidity impact.")
                fishbone_text = "Man: Operator training abhav.\nMachine: Tool wear/tear ya calibration error.\nMaterial: Raw material variation.\nMethod: SOP deviation.\nEnvironment: Temperature/Humidity impact."
                report_content += "2. ROOT CAUSE ANALYSIS (4M1E)\n" + fishbone_text + "\n\n"
                
                st.markdown("### ⚡ 3. Corrective Action (Permanent Fix)")
                ca_text = f"1. Defective parts ({product_name}) ko rework ya scrap karein.\n2. Machine ke component ko replace ya recalibrate karein."
                st.write(ca_text)
                report_content += "3. CORRECTIVE ACTION\n" + ca_text + "\n\n"
                
                st.markdown("### 🛡️ 4. Preventive Action (Future Proofing)")
                pa_text = "1. Poka-Yoke implement karein.\n2. SOP ko update karke retraining karwayein."
                st.write(pa_text)
                report_content += "4. PREVENTIVE ACTION\n" + pa_text + "\n\n"
                
                st.markdown("---")
                
                st.download_button(
                    label="📥 Download CAPA Report (Text File)",
                    data=report_content,
                    file_name=f"CAPA_Report_{customer_name}.txt",
                    mime="text/plain"
                )

with tab2:
    st.header("Quality & Manufacturing Q&A Assistant")
    st.write("Quality standards (5S, ISO, Welding, Poka-Yoke) ke baare mein sawal puchein.")
    
    user_query = st.text_input("Apna sawal yahan type karein:")
    
    if st.button("Get Answer"):
        if user_query.strip() == "":
            st.warning("Kripya koi sawal puchein!")
        else:
            with st.spinner("Jawab dhoondha ja raha hai..."):
                query_lower = user_query.lower()
                
                # Smart Keyword Logic for Dynamic Answers
                if "welding" in query_lower or "porosity" in query_lower:
                    reply = "🛠️ *Welding Issue:* Welding mein porosity aam taur par moisture, gandi surface, ya galat shielding gas ki wajah se hoti hai. Turant pre-heating check karein aur surface cleaning SOP ko follow karein."
                elif "5s" in query_lower:
                    reply = "🧹 *5S Standard:* 5S ke 5 steps hain: Sort (Seiri), Set in order (Seiton), Shine (Seiso), Standardize (Seiketsu), aur Sustain (Shitsuke). Yeh factory floor par safety aur efficiency badhane ke liye sabse zaroori tool hai."
                elif "iso" in query_lower or "audit" in query_lower:
                    reply = "📄 *ISO & Audit:* ISO standard ke tahat har process ka documented information aur continuous improvement zaroori hai. Ensure karein ki aapke operators ki training matrix updated ho aur internal audit schedule par ho."
                elif "poka" in query_lower or "yoke" in query_lower or "mistake" in query_lower:
                    reply = "🛡️ *Poka-Yoke:* Poka-Yoke ek mistake-proofing technique hai. Iska maqsad aisi design ya sensor lagana hai jisse operator chah kar bhi galti na kar sake (jaise 3-pin plug)."
                elif "rejection" in query_lower or "scrap" in query_lower:
                    reply = "📉 *Rejection Control:* High rejection rate ko kam karne ke liye 8D methodology ya DMAIC (Define, Measure, Analyze, Improve, Control) process ka istemal karein."
                else:
                    # Agar koi random sawal ho toh alag-alag general jawab dega
                    replies = [
                        "🔍 Is samasya ke liye 5-Why analysis karke root cause nikalna sabse behtar rahega.",
                        "👥 Quality standards ke anusar, is condition mein Cross-Functional Team (CFT) ke sath review meeting karni chahiye.",
                        "📋 Kripya process ke Standard Operating Procedure (SOP) aur Control Plan ko refer karein, wahin iska permanent solution milega."
                    ]
                    reply = random.choice(replies)

                st.success("Expert Recommendation:")
                st.write(reply)
                
                st.info("💡 Note: Abhi yeh app keywords par kaam kar rahi hai. Duniya ke kisi bhi ajeeb ya naye sawal ka ekdum perfect jawab paane ke liye, humein future mein isme OpenAI (ChatGPT) ya Gemini ki 'API Key' jodni hogi.")
