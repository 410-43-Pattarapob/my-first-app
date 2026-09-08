import time
import streamlit as st

st.title("Bakero Bakery — ระบบคำนวณราคา")

# ---------------------- ข้อมูลสินค้า (แก้ไข/เพิ่มเติมได้ตามต้องการ) ----------------------
MENU = [
    {"name": "ครัวซองต์เนยสด", "price": 45},
    {"name": "เค้กช็อกโกแลต (ชิ้น)", "price": 120},
    {"name": "ขนมปังโฮลวีท", "price": 55},
    {"name": "มัฟฟินบลูเบอร์รี่", "price": 40},
    {"name": "ทาร์ตผลไม้รวม", "price": 65},
]

MEMBER_DISCOUNT = 50            # ส่วนลดเพิ่มสำหรับสมาชิก (บาท)
BIG_ORDER_THRESHOLD = 300       # ยอดขั้นต่ำที่จะได้ส่วนลดเปอร์เซ็นต์
BIG_ORDER_DISCOUNT_RATE = 0.10  # ลด 10%

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
for i in range(len(MENU)):
    key = f"qty_{i}_val"
    if key not in st.session_state:
        st.session_state[key] = 0
if "member_val" not in st.session_state:
    st.session_state.member_val = False
if "paid_val" not in st.session_state:
    st.session_state.paid_val = 0.0

# * ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มออเดอร์ใหม่
def reset_order():
    for i in range(len(MENU)):
        st.session_state[f"qty_{i}_val"] = 0
    st.session_state.member_val = False
    st.session_state.paid_val = 0.0
    st.session_state.is_ended = False

# ฟังก์ชัน MessageBox (Dialog) สรุปราคาและส่วนลด
@st.dialog("สรุปยอดและส่วนลด")
def show_summary_dialog(total, discount, final_total):
    st.write(f"ราคารวม: **{total:,.2f} บาท**")
    st.write(f"ส่วนลดทั้งหมด: **{discount:,.2f} บาท**")
    st.success(f"ยอดที่ต้องจ่ายจริง: **{final_total:,.2f} บาท**")

# ฟังก์ชัน MessageBox (Dialog) แสดงผลเงินทอน
@st.dialog("ผลการชำระเงิน")
def show_payment_dialog(paid, final_total):
    if paid < final_total:
        missing = final_total - paid
        st.error(f"เงินไม่พอ! ขาดอีก {missing:,.2f} บาท")
    else:
        change = paid - final_total
        st.balloons()
        st.success(f"เงินทอน: {change:,.2f} บาท\n\nขอบคุณที่อุดหนุนแสนอร่อย เบเกอรี่ 🍞")

# ---------------------- แสดงรายการสินค้า ----------------------
st.subheader("รายการสินค้า")
for i, item in enumerate(MENU):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"{item['name']} — {item['price']} บาท")
    with col2:
        st.session_state[f"qty_{i}_val"] = st.number_input(
            "จำนวน",
            min_value=0,
            step=1,
            value=st.session_state[f"qty_{i}_val"],
            key=f"qty_input_{i}",
            label_visibility="collapsed",
        )

st.session_state.member_val = st.checkbox(
    "เป็นสมาชิกร้าน (ลดเพิ่ม 50 บาท)", value=st.session_state.member_val
)

st.caption("เงื่อนไขส่วนลด: ซื้อครบ 300 บาทขึ้นไป ลด 10% และสมาชิกลดเพิ่มอีก 50 บาท (ใช้ร่วมกันได้)")

# 1. ปุ่มคำนวณราคารวม
if st.button("🧮 คำนวณราคารวม"):
    total = sum(item["price"] * st.session_state[f"qty_{i}_val"] for i, item in enumerate(MENU))

    discount = 0
    # ---------- เงื่อนไขส่วนลด (If-Else) ----------
    # เงื่อนไขที่ 1: ซื้อครบ 300 บาทขึ้นไป ลด 10%
    if total >= BIG_ORDER_THRESHOLD:
        discount += total * BIG_ORDER_DISCOUNT_RATE

    # เงื่อนไขที่ 2: เป็นสมาชิก ลดเพิ่มอีก 50 บาท
    if st.session_state.member_val:
        discount += MEMBER_DISCOUNT

    final_total = max(total - discount, 0)
    st.session_state.final_total = final_total

    if total == 0:
        st.warning("กรุณาเลือกจำนวนสินค้าอย่างน้อย 1 รายการ")
    else:
        show_summary_dialog(total, discount, final_total)

st.divider()

# ---------------------- รับเงินและคำนวณเงินทอน ----------------------
st.subheader("รับเงินจากลูกค้า")
st.session_state.paid_val = st.number_input(
    "เงินที่รับจากลูกค้า (บาท)", min_value=0.0, step=1.0, value=st.session_state.paid_val
)

# 2. ปุ่มคำนวณเงินทอน
if st.button("💰 คำนวณเงินทอน"):
    if "final_total" not in st.session_state or st.session_state.final_total == 0:
        st.warning("กรุณากดคำนวณราคารวมก่อน")
    else:
        show_payment_dialog(st.session_state.paid_val, st.session_state.final_total)

st.divider()

# 3. ปุ่มเริ่มออเดอร์ใหม่
st.button("🔄 เริ่มออเดอร์ใหม่", on_click=reset_order)

st.divider()
st.write("ชื่อนายภัทรภพ เวียงบรรพต เลขที่ 43 ม.4/10")
