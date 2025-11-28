import streamlit as st
import json
from translate import get_generator
from check import round_trip_similarity, sanity_checks

st.set_page_config(page_title="TrustCheck", layout="wide")
st.title("TrustCheck — LLM Intent Reliability")
nl = st.text_area("Requirement", value="Allow HTTPS from dev VLAN to web servers.")
if st.button("Check"):
    with st.spinner("Running checks..."):
        gen = get_generator()
        sim, intent_str, back = round_trip_similarity(nl, gen)
        st.subheader("LLM Generated Intent")
        st.code(intent_str)
        st.subheader("Back-translated NL")
        st.write(back)
        st.subheader("Round-trip similarity")
        st.write(f"{sim:.2f}")
        try:
            parsed = json.loads(intent_str)
            issues = sanity_checks(parsed)
            if issues:
                st.warning("Sanity issues: " + "; ".join(issues))
            else:
                st.success("No obvious sanity issues")
        except Exception as e:
            st.error(f"Could not parse intent JSON: {e}")
