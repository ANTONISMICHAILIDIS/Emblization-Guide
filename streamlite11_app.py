import streamlit as st
import pandas as pd

# App title and subtitle
st.title("Embolization Guide")
st.markdown("<p style='font-size:12px'>Created by Michailidis A. for free use</p>", unsafe_allow_html=True)

# Sidebar: Let the user choose the organ, pathology, and emergency status.
st.sidebar.header("Embolization Parameters")
organ = st.sidebar.selectbox("Select the organ:", 
                             ["Liver", "Kidney", "Lung", "Prostate", "Uterus", "Bone/MSK", "Cerebrovascular"])
pathology = st.sidebar.selectbox("Select the pathology:", 
                                 ["Tumor (Malignant)", "Tumor (Benign)", "Hemorrhage", "Other"])
emergency = st.sidebar.checkbox("Emergency Case?")

st.header("Embolization Instructions")

def get_instructions(organ, pathology, emergency):
    instructions = ""
    if organ == "Liver":
        if pathology == "Tumor (Malignant)":
            instructions += (
                "Protocol: Use Microwave Ablation (MWA) or Radiofrequency Ablation (RFA) depending on lesion size.\n\n"
                "• **MWA Example:** 40 watt for 5 minutes to produce an ablation zone of approximately 3.6 x 2.9 x 2.0 cm, "
                "ensuring a 1-cm safety margin.\n\n"
                "• **Embolic Material:** Consider using drug-eluting beads for combined chemoembolization or PVA particles "
                "when applicable.\n\n"
                "• **Vessel Variations:** Be aware of hepatic arterial variants (e.g., replaced right hepatic artery) and "
                "perform superselective catheterization.\n"
            )
        elif pathology == "Hemorrhage":
            instructions += (
                "Protocol: For hepatic hemorrhage, prioritize rapid temporary occlusion.\n\n"
                "• **Embolic Material:** Gelfoam slurry (temporary) combined with PVA particles or coils for proximal occlusion.\n\n"
                "• **Vessel Variations:** Confirm hepatic arterial anatomy using angiography to account for variations.\n"
            )
        else:
            instructions += (
                "For benign or other liver lesions, tailor the approach with lower energy settings and minimal safety margins.\n"
            )
    elif organ == "Kidney":
        if pathology == "Tumor (Malignant)":
            instructions += (
                "Protocol: Consider RFA or MWA ensuring a 1-cm safety margin.\n\n"
                "• **Embolic Material:** When used as part of a combined therapy, drug-eluting beads or PVA particles may be added.\n\n"
                "• **Vessel Variations:** Check for accessory renal arteries; superselective catheterization is advised.\n"
            )
        elif pathology == "Hemorrhage":
            instructions += (
                "Protocol: For renal hemorrhage, use a combination of coil embolization for proximal control and particles for distal occlusion.\n\n"
                "• **Embolic Material:** Coils combined with PVA particles are recommended.\n\n"
                "• **Vessel Variations:** Renal vascular anatomy is variable; thorough angiographic evaluation is essential.\n"
            )
        else:
            instructions += (
                "For benign renal lesions (e.g., angiomyolipoma), consider cryoablation protocols if indicated or use a tailored embolization approach.\n"
            )
    elif organ == "Lung":
        if pathology == "Tumor (Malignant)":
            instructions += (
                "Protocol: Use MWA or RFA under CT guidance to ablate the lesion.\n\n"
                "• **Embolic Material:** Although primary treatment is ablation, adjunct particle embolization may be considered in select cases.\n\n"
                "• **Vessel Variations:** Evaluate both pulmonary and bronchial arteries; note that bronchial arterial supply can vary.\n"
            )
        elif pathology == "Hemorrhage":
            instructions += (
                "Protocol: In pulmonary hemorrhage, rapid embolization is critical.\n\n"
                "• **Embolic Material:** Fast-acting liquid agents such as n-Butyl Cyanoacrylate (nBCA) glue or Onyx® are options, "
                "often in combination with coils.\n\n"
                "• **Vessel Variations:** Assess both pulmonary and bronchial vascular contributions via high-resolution CT angiography.\n"
            )
        else:
            instructions += (
                "For benign lung lesions, treatment is highly case-specific. Consult multidisciplinary guidelines for detailed protocol.\n"
            )
    elif organ == "Prostate":
        if pathology == "Tumor (Malignant)":
            instructions += (
                "Protocol: For prostate cancer, consider non-embolization modalities such as HIFU, cryoablation, or transurethral RFA.\n\n"
                "• **Embolic Material:** Embolization is less common; focus on ablation for tumor control.\n\n"
                "• **Vessel Variations:** Detailed mapping of prostatic arterial supply is required; microcatheters may be necessary.\n"
            )
        else:
            instructions += (
                "Protocol: For benign prostatic hyperplasia (BPH), perform prostatic artery embolization.\n\n"
                "• **Embolic Material:** Use calibrated microspheres (100–300 microns) or PVA particles.\n\n"
                "• **Vessel Variations:** Carefully identify prostatic arterial branches and their anastomoses with rectal or bladder arteries.\n"
            )
    elif organ == "Uterus":
        instructions += (
            "Protocol: For uterine embolization (either for fibroids or postpartum hemorrhage), perform superselective catheterization "
            "of the uterine arteries.\n\n"
        )
        if pathology == "Tumor (Benign)":
            instructions += (
                "• **Embolic Material:** Typically, tris-acryl gelatin microspheres (355–500 microns) or PVA particles are used.\n\n"
            )
        elif pathology == "Hemorrhage":
            instructions += (
                "• **Embolic Material:** For postpartum hemorrhage, temporary agents such as Gelfoam® are often preferred.\n\n"
            )
        instructions += (
            "• **Vessel Variations:** Be mindful of uterine artery variants and possible ovarian artery collaterals; "
            "pre-procedural imaging is essential.\n"
        )
    elif organ == "Bone/MSK":
        instructions += (
            "Protocol: For hypervascular bone tumors or chronic musculoskeletal pain, perform superselective embolization.\n\n"
        )
        if pathology == "Tumor (Malignant)":
            instructions += (
                "• **Embolic Material:** Consider using PVA particles or calibrated microspheres (100–300 microns), and add coils for larger feeding vessels if needed.\n\n"
            )
        else:
            instructions += (
                "• **Embolic Material:** For pain management, smaller particles (100–300 microns) are typically used to reduce blood flow to the area.\n\n"
            )
        instructions += (
            "• **Vessel Variations:** Evaluate the arterial supply to the affected bone and surrounding soft tissues via pre-procedural imaging.\n"
        )
    elif organ == "Cerebrovascular":
        instructions += (
            "Protocol: For cerebrovascular lesions such as aneurysms, arteriovenous malformations (AVMs), or dural fistulas, "
            "a combination of coils and liquid embolic agents is commonly used.\n\n"
        )
        if pathology == "Hemorrhage":
            instructions += (
                "• **Embolic Material:** Coils, Onyx®, or nBCA glue are options based on lesion complexity.\n\n"
            )
        else:
            instructions += (
                "• **Embolic Material:** For AVMs, Onyx® or Squid® is frequently used; coils may be added for proximal flow control.\n\n"
            )
        instructions += (
            "• **Vessel Variations:** Given the highly variable cerebral vasculature, high-resolution angiography is mandatory to map the target vessels.\n"
        )
    else:
        instructions += "Organ not recognized. Please select a valid option from the sidebar.\n"
        
    if emergency:
        instructions += "\n**Emergency Protocol Adjustments:**\n"
        instructions += (
            "- Prioritize rapid hemostasis.\n"
            "- Consider fast-acting liquid embolics (e.g., nBCA glue) or coils for immediate vessel occlusion.\n"
            "- Streamline the procedure by reducing imaging delays and ensuring quick access to required embolic materials.\n"
        )
    
    return instructions

# Generate and display instructions based on the user's selections.
instructions_text = get_instructions(organ, pathology, emergency)
st.text_area("Instructions", value=instructions_text, height=400)
