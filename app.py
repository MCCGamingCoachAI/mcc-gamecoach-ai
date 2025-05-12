import streamlit as st

st.set_page_config(page_title="MCC GameCoach AI", layout="centered")

st.title("MCC GameCoach AI")
st.markdown("### Smart Coaching for Raid: Shadow Legends")

st.write("Enter your battle details below, and let the AI coach give you real feedback.")

# Input form
with st.form("battle_form"):
    battle_type = st.text_input("Battle Type (e.g., Dragon 20, Arena, Clan Boss)")
    team = st.text_area("Your Team (Champion name + Role, one per line)")
    enemy = st.text_input("Enemy or Boss Faced")
    outcome = st.selectbox("Battle Outcome", ["Win", "Loss"])
    issues = st.text_area("What You Think Went Wrong (optional)")

    submitted = st.form_submit_button("Analyze My Match")

if submitted:
    st.markdown("### Coaching Feedback")
    feedback = ""

    if outcome == "Loss":
        if "support" in team.lower() and not any(dps in team.lower() for dps in ["dps", "damage", "kael", "athel", "bellower"]):
            feedback = "Your team is support-heavy. Add at least one strong DPS champion to speed up fights and secure kills."
        elif "speed" not in team.lower():
            feedback = "Speed tuning might be an issue. Consider increasing your lead champion's speed to control the turn order."
        else:
            feedback = "Check gear synergy and cooldown timing. Sometimes losses come from poor skill timing or lack of debuff coverage."
    else:
        feedback = "Nice win! Still consider reviewing your team balance for better efficiency and faster clears."

    st.success(feedback)
