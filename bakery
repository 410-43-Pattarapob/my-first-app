"""
โปรเจกต์: Smart Shop & Discount
หัวข้อ: ร้านเบเกอรี่ "แสนอร่อย เบเกอรี่" (Saen-Aroi Bakery)
รายละเอียด:
 - มีสินค้า 5 รายการ ให้ลูกค้ากรอกจำนวนที่ต้องการซื้อ (ช่องรับข้อมูลตัวเลข)
 - คำนวณราคารวมทั้งหมด
 - เช็คเงื่อนไขส่วนลด (If-Else) อย่างน้อย 2 เงื่อนไข:
     1) ซื้อครบ 300 บาทขึ้นไป ลด 10%
     2) เป็นสมาชิก (ติ๊กช่อง) ลดเพิ่มอีก 50 บาท
 - รับเงินจากลูกค้า และคำนวณเงินทอน พร้อมแจ้งผลผ่าน MessageBox
"""

import tkinter as tk
from tkinter import messagebox

# ---------------------- ข้อมูลสินค้าและราคา (แก้ไข/เพิ่มเติมได้ตามต้องการ) ----------------------
SHOP_NAME = "แสนอร่อย เบเกอรี่ (Saen-Aroi Bakery)"

MENU = [
    {"name": "ครัวซองต์เนยสด", "price": 45},
    {"name": "เค้กช็อกโกแลต (ชิ้น)", "price": 120},
    {"name": "ขนมปังโฮลวีท", "price": 55},
    {"name": "มัฟฟินบลูเบอร์รี่", "price": 40},
    {"name": "ทาร์ตผลไม้รวม", "price": 65},
]

MEMBER_DISCOUNT = 50        # ส่วนลดเพิ่มสำหรับสมาชิก (บาท)
BIG_ORDER_THRESHOLD = 300   # ยอดขั้นต่ำที่จะได้ส่วนลดเปอร์เซ็นต์
BIG_ORDER_DISCOUNT_RATE = 0.10   # ลด 10%


class BakeryShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"🍞 ระบบคำนวณราคา - {SHOP_NAME}")
        self.root.geometry("560x600")
        self.root.configure(bg="#FFF3E0")

        # ---------- หัวร้าน ----------
        tk.Label(
            root, text=f"🥐 {SHOP_NAME} 🧁",
            font=("TH Sarabun New", 22, "bold"), bg="#FFF3E0", fg="#8D5524"
        ).pack(pady=10)

        # ---------- กรอบรายการสินค้า ----------
        menu_frame = tk.Frame(root, bg="#FFF3E0")
        menu_frame.pack(pady=10)

        tk.Label(menu_frame, text="สินค้า", font=("TH Sarabun New", 14, "bold"),
                 bg="#FFF3E0", width=22, anchor="w").grid(row=0, column=0, padx=5)
        tk.Label(menu_frame, text="ราคา/ชิ้น", font=("TH Sarabun New", 14, "bold"),
                 bg="#FFF3E0", width=10).grid(row=0, column=1)
        tk.Label(menu_frame, text="จำนวน", font=("TH Sarabun New", 14, "bold"),
                 bg="#FFF3E0", width=10).grid(row=0, column=2)

        # เก็บ Entry ของแต่ละสินค้าไว้ใน list เพื่อดึงค่าภายหลัง
        self.qty_entries = []
        for i, item in enumerate(MENU, start=1):
            tk.Label(menu_frame, text=item["name"], font=("TH Sarabun New", 13),
                     bg="#FFF3E0", width=22, anchor="w").grid(row=i, column=0, padx=5, pady=4)
            tk.Label(menu_frame, text=f"{item['price']} บาท", font=("TH Sarabun New", 13),
                     bg="#FFF3E0", width=10).grid(row=i, column=1)

            qty_entry = tk.Entry(menu_frame, font=("TH Sarabun New", 13), width=8, justify="center")
            qty_entry.insert(0, "0")
            qty_entry.grid(row=i, column=2, pady=4)
            self.qty_entries.append(qty_entry)

        # ---------- ช่องติ๊กสมาชิก ----------
        self.member_var = tk.BooleanVar()
        tk.Checkbutton(
            root, text="เป็นสมาชิกร้าน (ลดเพิ่ม 50 บาท)", variable=self.member_var,
            font=("TH Sarabun New", 13), bg="#FFF3E0"
        ).pack(pady=8)

        # ---------- ปุ่มคำนวณราคารวม ----------
        tk.Button(
            root, text="🧮 คำนวณราคารวม", font=("TH Sarabun New", 14, "bold"),
            bg="#FF9800", fg="white", width=20, command=self.calculate_total
        ).pack(pady=8)

        # ---------- แสดงผลราคา ----------
        self.result_label = tk.Label(
            root, text="ราคารวม: 0.00 บาท\nส่วนลด: 0.00 บาท\nยอดที่ต้องจ่าย: 0.00 บาท",
            font=("TH Sarabun New", 14), bg="#FFF3E0", fg="#333333", justify="left"
        )
        self.result_label.pack(pady=10)

        # ---------- รับเงินจากลูกค้า ----------
        pay_frame = tk.Frame(root, bg="#FFF3E0")
        pay_frame.pack(pady=10)

        tk.Label(pay_frame, text="เงินที่รับจากลูกค้า:", font=("TH Sarabun New", 13),
                 bg="#FFF3E0").grid(row=0, column=0, padx=5)
        self.paid_entry = tk.Entry(pay_frame, font=("TH Sarabun New", 13), width=12, justify="center")
        self.paid_entry.grid(row=0, column=1, padx=5)

        tk.Button(
            root, text="💰 คำนวณเงินทอน", font=("TH Sarabun New", 14, "bold"),
            bg="#4CAF50", fg="white", width=20, command=self.calculate_change
        ).pack(pady=10)

        # ---------- ปุ่มเริ่มออเดอร์ใหม่ ----------
        tk.Button(
            root, text="🔄 เริ่มออเดอร์ใหม่", font=("TH Sarabun New", 12, "bold"),
            bg="#9E9E9E", fg="white", width=20, command=self.reset_order
        ).pack(pady=5)

        # ตัวแปรเก็บยอดที่ต้องจ่ายจริง (คำนวณล่าสุด)
        self.final_total = 0.0

    # -------------------- คำนวณราคารวม + ส่วนลด --------------------
    def calculate_total(self):
        total = 0.0
        try:
            for item, qty_entry in zip(MENU, self.qty_entries):
                qty = int(qty_entry.get())
                if qty < 0:
                    raise ValueError
                total += item["price"] * qty
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกจำนวนสินค้าเป็นตัวเลขจำนวนเต็มไม่ติดลบ")
            return

        discount = 0.0

        # ---------- เงื่อนไขส่วนลด (If-Else) ----------
        # เงื่อนไขที่ 1: ซื้อครบ 300 บาทขึ้นไป ลด 10%
        if total >= BIG_ORDER_THRESHOLD:
            discount += total * BIG_ORDER_DISCOUNT_RATE

        # เงื่อนไขที่ 2: เป็นสมาชิก ลดเพิ่มอีก 50 บาท
        if self.member_var.get():
            discount += MEMBER_DISCOUNT

        final_total = max(total - discount, 0)
        self.final_total = final_total

        self.result_label.config(
            text=(
                f"ราคารวม: {total:,.2f} บาท\n"
                f"ส่วนลดทั้งหมด: {discount:,.2f} บาท\n"
                f"ยอดที่ต้องจ่ายจริง: {final_total:,.2f} บาท"
            )
        )

        if total == 0:
            messagebox.showinfo("แจ้งเตือน", "กรุณาเลือกจำนวนสินค้าอย่างน้อย 1 รายการ")

    # -------------------- คำนวณเงินทอน --------------------
    def calculate_change(self):
        if self.final_total == 0:
            messagebox.showwarning("แจ้งเตือน", "กรุณากดคำนวณราคารวมก่อน")
            return

        try:
            paid = float(self.paid_entry.get())
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกจำนวนเงินเป็นตัวเลข")
            return

        # ---------- เงื่อนไขตรวจสอบเงินที่รับมา (If-Else) ----------
        if paid < self.final_total:
            messagebox.showerror(
                "เงินไม่พอ",
                f"ลูกค้าจ่ายเงินไม่พอ!\nยอดที่ต้องจ่าย: {self.final_total:,.2f} บาท\n"
                f"จ่ายมา: {paid:,.2f} บาท\nขาดอีก: {self.final_total - paid:,.2f} บาท"
            )
        else:
            change = paid - self.final_total
            messagebox.showinfo(
                "สรุปการชำระเงิน",
                f"ยอดที่ต้องจ่าย: {self.final_total:,.2f} บาท\n"
                f"รับเงินมา: {paid:,.2f} บาท\n"
                f"เงินทอน: {change:,.2f} บาท\n\n"
                f"ขอบคุณที่อุดหนุน {SHOP_NAME} ค่ะ/ครับ 🍞"
            )

    # -------------------- เริ่มออเดอร์ใหม่ --------------------
    def reset_order(self):
        for qty_entry in self.qty_entries:
            qty_entry.delete(0, tk.END)
            qty_entry.insert(0, "0")
        self.member_var.set(False)
        self.paid_entry.delete(0, tk.END)
        self.final_total = 0.0
        self.result_label.config(
            text="ราคารวม: 0.00 บาท\nส่วนลด: 0.00 บาท\nยอดที่ต้องจ่าย: 0.00 บาท"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = BakeryShopApp(root)
    root.mainloop()
