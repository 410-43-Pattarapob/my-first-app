import streamlit as st

#ส่วนที่ 1 หัวข้อเว็ป (Title สีแดง)
st.markdown("# :red[🏋️ คำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
Weight = st.numbera_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.numbera_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

#ส่วนที่ 3 สร้างปุ่มกดคำนวณ
if st.button("คำนวณค่า BMI 🎯"):
    # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณ BMI
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    
st.write("---")
st.heafer(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

#ส่วนที่ 4 แปลผลค่า BMI ตามเกณฑ์
if bmi < 18.5:
    st.warning(" คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif bmi < 23.0:
    st.success = "สุขภาพดี"
elif bmi < 25.0:
    st.info = "ท้วม"
else:
    st.error = "อ้วน"

st.divider()
st.write("นายภัทรภพ เวียงบรรพต เลขที่ 43 ม.4/10")
