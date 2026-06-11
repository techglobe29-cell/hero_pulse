import streamlit as st
from database import conn, cursor
from equipment import add_equipment
from maintenance import add_maintenance
from downtime import log_downtime
from reports import (
    get_downtime_report,
    get_maintenance_report,
    get_equipment_report,
    get_department_report,
    get_technician_report,
    get_failure_report,
    get_action_report
)
from department import add_department, get_departments
from technician import add_technician, get_technicians
from failure_reason import add_failure_reason, get_failure_reasons
from corrective_action import add_corrective_action, get_corrective_actions

st.set_page_config(
    page_title="Hero LinePulse",
    page_icon="🏭",
    layout="wide"
)

st.markdown("""
<style>

/* Main Page */
.main {
    padding-top: 1rem;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    background-color: #005BAC;
    color: white;
    border: none;
}

.stButton > button:hover {
    background-color: #0077E6;
    color: white;
}

.stButton > button:active {
    background-color: #003D73 !important;
    color: white !important;
}

.stButton > button:focus {
    box-shadow: none;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background-color: rgba(128,128,128,0.12);
    border-radius: 12px;
    padding: 15px;
    border: 1px solid rgba(128,128,128,0.25);
}

/* Inputs */
.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid #005BAC !important;
    box-shadow: none !important;
    outline: none !important;
}

.stNumberInput [data-baseweb="input"]:focus-within,
.stNumberInput [data-baseweb="base-input"]:focus-within,
div[data-baseweb="input"]:focus-within {
    border-color: #005BAC !important;
    box-shadow: none !important;
    outline: none !important;
}

.stNumberInput > div:focus-within,
.stNumberInput > div > div:focus-within {
    border-color: #005BAC !important;
    box-shadow: none !important;
    outline: none !important;
}

.stTextArea [data-baseweb="textarea"]:focus-within,
div[data-baseweb="textarea"]:focus-within {
    border-color: #005BAC !important;
    box-shadow: none !important;
    outline: none !important;
}

.stTextArea > div:focus-within,
.stTextArea > div > div:focus-within {
    border-color: #005BAC !important;
    box-shadow: none !important;
    outline: none !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128,128,128,0.2);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
# 🏭 Hero LinePulse
### Preventive Maintenance & Equipment Downtime Tracker
---
""")

page = st.sidebar.radio(
    "📋 Navigation",
    [
        "Dashboard",
        "Department",
        "Technician",
        "Failure Reason",
        "Corrective Action",
        "Equipment",
        "Maintenance",
        "Downtime",
        "Reports"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Hero MotoCorp")

# =====================
# Dashboard
# =====================

if page == "Dashboard":

    st.header("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Equipment", 0)
    with col2:
        st.metric("Maintenance Due", 0)
    with col3:
        st.metric("Downtime Hours", 0)
    with col4:
        st.metric("Technicians", 0)

    st.divider()
    st.info("Monitor equipment health, preventive maintenance schedules, and downtime records.")

# =====================
# Department
# =====================

elif page == "Department":

    st.header("🏢 Department Management")

    col1, col2 = st.columns(2)

    with col1:
        dept_name = st.text_input("Department Name")
    with col2:
        dept_location = st.text_input("Location")

    if st.button("💾 Save Department"):
        try:
            add_department(dept_name, dept_location)
            st.success("✅ Department saved successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

    st.divider()
    st.subheader("Existing Departments")
    try:
        depts = get_departments()
        if depts:
            st.dataframe({
                "ID": [d[0] for d in depts],
                "Department Name": [d[1] for d in depts]
            })
        else:
            st.info("No departments added yet.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# =====================
# Technician
# =====================

elif page == "Technician":

    st.header("👷 Technician Management")

    col1, col2 = st.columns(2)

    with col1:
        tech_name = st.text_input("Technician Name")
        tech_phone = st.text_input("Phone")
    with col2:
        tech_email = st.text_input("Email")
        tech_skill = st.selectbox("Skill Level", ["Junior", "Mid", "Senior", "Expert"])

    if st.button("💾 Save Technician"):
        try:
            add_technician(tech_name, tech_phone, tech_email, tech_skill)
            st.success("✅ Technician saved successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

    st.divider()
    st.subheader("Existing Technicians")
    try:
        techs = get_technicians()
        if techs:
            st.dataframe({
                "ID": [t[0] for t in techs],
                "Name": [t[1] for t in techs]
            })
        else:
            st.info("No technicians added yet.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# =====================
# Failure Reason
# =====================

elif page == "Failure Reason":

    st.header("⚠️ Failure Reason Management")

    col1, col2 = st.columns(2)

    with col1:
        failure_category = st.text_input("Failure Category")
    with col2:
        failure_desc = st.text_area("Description")

    if st.button("💾 Save Failure Reason"):
        try:
            add_failure_reason(failure_category, failure_desc)
            st.success("✅ Failure reason saved successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

    st.divider()
    st.subheader("Existing Failure Reasons")
    try:
        failures = get_failure_reasons()
        if failures:
            st.dataframe({
                "ID": [f[0] for f in failures],
                "Category": [f[1] for f in failures]
            })
        else:
            st.info("No failure reasons added yet.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# =====================
# Corrective Action
# =====================

elif page == "Corrective Action":

    st.header("🛠️ Corrective Action Management")

    col1, col2 = st.columns(2)

    with col1:
        action_name = st.text_input("Action Name")
    with col2:
        action_desc = st.text_area("Description")

    if st.button("💾 Save Corrective Action"):
        try:
            add_corrective_action(action_name, action_desc)
            st.success("✅ Corrective action saved successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

    st.divider()
    st.subheader("Existing Corrective Actions")
    try:
        actions = get_corrective_actions()
        if actions:
            st.dataframe({
                "ID": [a[0] for a in actions],
                "Action Name": [a[1] for a in actions]
            })
        else:
            st.info("No corrective actions added yet.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# =====================
# Equipment
# =====================

elif page == "Equipment":

    st.header("⚙️ Equipment Management")

    departments = get_departments()
    dept_options = {d[1]: d[0] for d in departments} if departments else {}

    col1, col2 = st.columns(2)

    with col1:
        equipment_name = st.text_input("Equipment Name")
        equipment_type = st.text_input("Equipment Type")
        manufacturer = st.text_input("Manufacturer")
        model_number = st.text_input("Model Number")

    with col2:
        serial_number = st.text_input("Serial Number")
        installation_date = st.date_input("Installation Date")
        purchase_date = st.date_input("Purchase Date")
        dept_selected = st.selectbox("Department", list(dept_options.keys()) if dept_options else ["No departments yet"])
        status = st.selectbox("Status", ["Active", "Inactive"])

    if st.button("💾 Save Equipment"):
        try:
            dept_id = dept_options[dept_selected]
            add_equipment(
                equipment_name, equipment_type, manufacturer,
                model_number, serial_number, installation_date,
                purchase_date, dept_id, status
            )
            st.success("✅ Equipment saved successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# =====================
# Maintenance
# =====================

elif page == "Maintenance":

    st.header("🔧 Maintenance Management")

    technicians = get_technicians()
    tech_options = {t[1]: t[0] for t in technicians} if technicians else {}

    equipments = []
    cursor.execute("SELECT Equipment_ID, Equipment_Name FROM Equipment")
    equipments = cursor.fetchall()
    equip_options = {e[1]: e[0] for e in equipments} if equipments else {}

    col1, col2 = st.columns(2)

    with col1:
        equip_selected = st.selectbox("Equipment", list(equip_options.keys()) if equip_options else ["No equipment yet"])
        tech_selected = st.selectbox("Technician", list(tech_options.keys()) if tech_options else ["No technicians yet"])

    with col2:
        maintenance_type = st.selectbox("Maintenance Type", ["Preventive", "Corrective"])
        scheduled_date = st.date_input("Scheduled Date")

    remarks = st.text_area("Remarks")

    if st.button("📅 Schedule Maintenance"):
        try:
            equip_id = equip_options[equip_selected]
            tech_id = tech_options[tech_selected]
            add_maintenance(equip_id, tech_id, maintenance_type, scheduled_date, remarks)
            st.success("✅ Maintenance scheduled successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# =====================
# Downtime
# =====================

elif page == "Downtime":

    st.header("⏱️ Downtime Tracking")

    cursor.execute("SELECT Equipment_ID, Equipment_Name FROM Equipment")
    equipments = cursor.fetchall()
    equip_options = {e[1]: e[0] for e in equipments} if equipments else {}

    failures = get_failure_reasons()
    failure_options = {f[1]: f[0] for f in failures} if failures else {}

    actions = get_corrective_actions()
    action_options = {a[1]: a[0] for a in actions} if actions else {}

    col1, col2 = st.columns(2)

    with col1:
        equip_selected = st.selectbox("Equipment", list(equip_options.keys()) if equip_options else ["No equipment yet"])
        start_time = st.text_input("Start Time (YYYY-MM-DD HH:MM:SS)")
        failure_selected = st.selectbox("Failure Reason", list(failure_options.keys()) if failure_options else ["No failure reasons yet"])

    with col2:
        end_time = st.text_input("End Time (YYYY-MM-DD HH:MM:SS)")
        duration = st.number_input("Duration (Hours)", min_value=0.0)
        action_selected = st.selectbox("Corrective Action", list(action_options.keys()) if action_options else ["No actions yet"])

    if st.button("📝 Log Downtime"):
        try:
            equip_id = equip_options[equip_selected]
            failure_id = failure_options[failure_selected]
            action_id = action_options[action_selected]
            log_downtime(equip_id, start_time, end_time, duration, failure_id, action_id)
            st.success("✅ Downtime logged successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# =====================
# Reports
# =====================

elif page == "Reports":

    import pandas as pd
    import io

    st.header("📈 Reports")

    # ── Equipment Summary ──────────────────────────
    st.subheader("⚙️ Equipment Summary")
    try:
        equip_data = get_equipment_report()
        if equip_data:
            df_equip = pd.DataFrame(equip_data, columns=[
                "Equipment Name", "Type", "Manufacturer", "Status", "Department"
            ])
            st.dataframe(df_equip, use_container_width=True)
        else:
            st.info("No equipment records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Department Summary ─────────────────────────
    st.subheader("🏢 Department Summary")
    try:
        dept_data = get_department_report()
        if dept_data:
            df_dept = pd.DataFrame(dept_data, columns=[
                "Department Name", "Location"
            ])
            st.dataframe(df_dept, use_container_width=True)
        else:
            st.info("No department records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Technician Summary ─────────────────────────
    st.subheader("👷 Technician Summary")
    try:
        tech_data = get_technician_report()
        if tech_data:
            df_tech = pd.DataFrame(tech_data, columns=[
                "Name", "Phone", "Email", "Skill Level"
            ])
            st.dataframe(df_tech, use_container_width=True)
        else:
            st.info("No technician records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Maintenance Summary ────────────────────────
    st.subheader("🔧 Maintenance Summary")
    try:
        maint_data = get_maintenance_report()
        if maint_data:
            df_maint = pd.DataFrame(maint_data, columns=[
                "Equipment", "Type", "Scheduled Date", "Status"
            ])
            st.dataframe(df_maint, use_container_width=True)
        else:
            st.info("No maintenance records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Downtime Summary ───────────────────────────
    st.subheader("⏱️ Downtime Summary")
    try:
        down_data = get_downtime_report()
        if down_data:
            df_down = pd.DataFrame(down_data, columns=[
                "Equipment", "Total Downtime (Hours)"
            ])
            st.dataframe(df_down, use_container_width=True)
        else:
            st.info("No downtime records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Failure Reason Summary ─────────────────────
    st.subheader("⚠️ Failure Reason Summary")
    try:
        fail_data = get_failure_report()
        if fail_data:
            df_fail = pd.DataFrame(fail_data, columns=[
                "Failure Category", "Occurrences"
            ])
            st.dataframe(df_fail, use_container_width=True)
        else:
            st.info("No failure records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Corrective Action Summary ──────────────────
    st.subheader("🛠️ Corrective Action Summary")
    try:
        action_data = get_action_report()
        if action_data:
            df_action = pd.DataFrame(action_data, columns=[
                "Action Name", "Times Used"
            ])
            st.dataframe(df_action, use_container_width=True)
        else:
            st.info("No corrective action records found.")
    except Exception as e:
        st.error(f"❌ Error: {e}")

    st.divider()

    # ── Export All as CSV ──────────────────────────
    st.subheader("📥 Export Report")

    if st.button("📥 Export All Data as CSV"):
        try:
            output = io.BytesIO()

            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                if equip_data:
                    df_equip.to_excel(writer, sheet_name="Equipment", index=False)
                if dept_data:
                    df_dept.to_excel(writer, sheet_name="Departments", index=False)
                if tech_data:
                    df_tech.to_excel(writer, sheet_name="Technicians", index=False)
                if maint_data:
                    df_maint.to_excel(writer, sheet_name="Maintenance", index=False)
                if down_data:
                    df_down.to_excel(writer, sheet_name="Downtime", index=False)
                if fail_data:
                    df_fail.to_excel(writer, sheet_name="Failure Reasons", index=False)
                if action_data:
                    df_action.to_excel(writer, sheet_name="Corrective Actions", index=False)

            st.download_button(
                label="📂 Click here to Download",
                data=output.getvalue(),
                file_name="hero_linepulse_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"❌ Export Error: {e}")