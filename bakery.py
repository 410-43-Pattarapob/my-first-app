<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>แสนอร่อย เบเกอรี่ — ระบบคำนวณราคา</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Work+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --crust: #F6EDE0;
    --dough: #FFFBF5;
    --choc: #4A2E23;
    --choc-soft: #7A5648;
    --jam: #B5495B;
    --wheat: #D9A441;
    --line: #E4D5C0;
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    background: var(--crust);
    color: var(--choc);
    font-family: 'Work Sans', sans-serif;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  .wrap {
    max-width: 640px;
    margin: 0 auto;
    padding: 48px 20px 80px;
  }

  header {
    text-align: center;
    margin-bottom: 36px;
  }

  .eyebrow {
    font-size: 14px;
    color: var(--jam);
    letter-spacing: 0.02em;
  }

  h1 {
    font-family: 'Fraunces', serif;
    font-weight: 700;
    font-size: clamp(32px, 6vw, 46px);
    margin: 6px 0 10px;
  }

  .tagline {
    color: var(--choc-soft);
    font-size: 16px;
    max-width: 420px;
    margin: 0 auto;
  }

  .card {
    background: var(--dough);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 28px 24px;
    margin-bottom: 24px;
  }

  .card h2 {
    font-family: 'Fraunces', serif;
    font-size: 20px;
    font-weight: 600;
    margin: 0 0 18px;
  }

  .item-row {
    display: grid;
    grid-template-columns: 1fr auto auto;
    align-items: center;
    gap: 14px;
    padding: 12px 0;
    border-bottom: 1px solid var(--line);
  }

  .item-row:last-child { border-bottom: none; }

  .item-name { font-size: 15px; }
  .item-price { font-size: 14px; color: var(--choc-soft); white-space: nowrap; }

  .qty-input {
    width: 56px;
    padding: 8px 6px;
    text-align: center;
    border: 1px solid var(--line);
    border-radius: 8px;
    font-family: 'Work Sans', sans-serif;
    font-size: 15px;
    background: var(--crust);
    color: var(--choc);
  }

  .qty-input:focus {
    outline: 2px solid var(--wheat);
    outline-offset: 1px;
  }

  .member-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 6px;
    font-size: 15px;
  }

  .member-row input { width: 18px; height: 18px; accent-color: var(--jam); }

  .discount-note {
    font-size: 13px;
    color: var(--choc-soft);
    margin-top: 14px;
    line-height: 1.6;
  }

  .discount-note li { margin-bottom: 2px; }

  button {
    width: 100%;
    padding: 14px;
    border: none;
    border-radius: 10px;
    font-family: 'Work Sans', sans-serif;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.08s ease, opacity 0.15s ease;
  }

  button:active { transform: scale(0.98); }

  .btn-primary {
    background: var(--jam);
    color: var(--dough);
  }

  .btn-secondary {
    background: var(--wheat);
    color: var(--choc);
    margin-top: 10px;
  }

  .btn-ghost {
    background: transparent;
    color: var(--choc-soft);
    border: 1px solid var(--line);
    margin-top: 14px;
  }

  .summary {
    display: grid;
    gap: 8px;
    font-size: 15px;
    margin-bottom: 18px;
  }

  .summary-row {
    display: flex;
    justify-content: space-between;
  }

  .summary-row.total {
    font-family: 'Fraunces', serif;
    font-size: 20px;
    font-weight: 600;
    border-top: 1px solid var(--line);
    padding-top: 10px;
    margin-top: 4px;
  }

  .pay-row {
    display: flex;
    gap: 10px;
    margin: 18px 0;
  }

  .pay-row input {
    flex: 1;
    padding: 12px;
    border: 1px solid var(--line);
    border-radius: 8px;
    font-size: 15px;
    font-family: 'Work Sans', sans-serif;
    background: var(--crust);
    color: var(--choc);
  }

  .pay-row input:focus {
    outline: 2px solid var(--wheat);
    outline-offset: 1px;
  }

  #result-box {
    display: none;
    border-radius: 14px;
    padding: 18px 20px;
    font-size: 15px;
  }

  #result-box.ok {
    background: #EAF3E5;
    border: 1px solid #BFDCB0;
    color: #3A5C2C;
  }

  #result-box.error {
    background: #FBE9E7;
    border: 1px solid #F1B4AC;
    color: #8C3A2E;
  }

  #result-box strong { display: block; margin-bottom: 4px; font-size: 16px; }

  footer {
    text-align: center;
    font-size: 13px;
    color: var(--choc-soft);
    margin-top: 30px;
  }

  @media (prefers-reduced-motion: reduce) {
    button { transition: none; }
  }
</style>
</head>
<body>
<div class="wrap">

  <header>
    <div class="eyebrow">ระบบคำนวณราคาและส่วนลด</div>
    <h1>แสนอร่อย เบเกอรี่</h1>
    <p class="tagline">เลือกจำนวนขนมที่ต้องการ ระบบจะคำนวณราคารวม ส่วนลด และเงินทอนให้อัตโนมัติ</p>
  </header>

  <div class="card">
    <h2>รายการสินค้า</h2>
    <div id="menu-list"></div>

    <label class="member-row">
      <input type="checkbox" id="member-check">
      เป็นสมาชิกร้าน (ลดเพิ่ม 50 บาท)
    </label>

    <ul class="discount-note">
      <li>ซื้อครบ 300 บาทขึ้นไป รับส่วนลด 10%</li>
      <li>สมาชิกร้าน รับส่วนลดเพิ่มอีก 50 บาท (ใช้ร่วมกันได้)</li>
    </ul>

    <button class="btn-primary" onclick="calculateTotal()" style="margin-top:20px;">คำนวณราคารวม</button>
  </div>

  <div class="card">
    <h2>สรุปยอด</h2>
    <div class="summary">
      <div class="summary-row"><span>ราคารวม</span><span id="sum-total">0.00 บาท</span></div>
      <div class="summary-row"><span>ส่วนลดทั้งหมด</span><span id="sum-discount">0.00 บาท</span></div>
      <div class="summary-row total"><span>ยอดที่ต้องจ่าย</span><span id="sum-final">0.00 บาท</span></div>
    </div>

    <div class="pay-row">
      <input type="number" id="paid-input" placeholder="เงินที่รับจากลูกค้า (บาท)" min="0">
    </div>
    <button class="btn-secondary" onclick="calculateChange()">คำนวณเงินทอน</button>

    <div id="result-box"></div>

    <button class="btn-ghost" onclick="resetOrder()">เริ่มออเดอร์ใหม่</button>
  </div>

  <footer>ทำขึ้นเพื่อโปรเจกต์เรียนเขียนโปรแกรม — หัวข้อ Smart Shop &amp; Discount</footer>
</div>

<script>
  // ---------------------- ข้อมูลสินค้า (แก้ไข/เพิ่มเติมได้ตามต้องการ) ----------------------
  const MENU = [
    { name: "ครัวซองต์เนยสด", price: 45 },
    { name: "เค้กช็อกโกแลต (ชิ้น)", price: 120 },
    { name: "ขนมปังโฮลวีท", price: 55 },
    { name: "มัฟฟินบลูเบอร์รี่", price: 40 },
    { name: "ทาร์ตผลไม้รวม", price: 65 },
  ];

  const MEMBER_DISCOUNT = 50;          // ส่วนลดเพิ่มสำหรับสมาชิก (บาท)
  const BIG_ORDER_THRESHOLD = 300;     // ยอดขั้นต่ำที่จะได้ส่วนลดเปอร์เซ็นต์
  const BIG_ORDER_DISCOUNT_RATE = 0.10; // ลด 10%

  let finalTotal = 0;

  // ---------------------- สร้างรายการสินค้าในหน้าเว็บ ----------------------
  function renderMenu() {
    const list = document.getElementById("menu-list");
    MENU.forEach((item, i) => {
      const row = document.createElement("div");
      row.className = "item-row";
      row.innerHTML = `
        <span class="item-name">${item.name}</span>
        <span class="item-price">${item.price} บาท</span>
        <input type="number" class="qty-input" id="qty-${i}" value="0" min="0">
      `;
      list.appendChild(row);
    });
  }
  renderMenu();

  // ---------------------- คำนวณราคารวมและส่วนลด ----------------------
  function calculateTotal() {
    let total = 0;

    for (let i = 0; i < MENU.length; i++) {
      const qtyInput = document.getElementById(`qty-${i}`);
      const qty = parseInt(qtyInput.value, 10);

      if (isNaN(qty) || qty < 0) {
        showResult("error", "ข้อผิดพลาด", "กรุณากรอกจำนวนสินค้าเป็นตัวเลขจำนวนเต็มไม่ติดลบ");
        return;
      }
      total += MENU[i].price * qty;
    }

    let discount = 0;

    // ---------- เงื่อนไขส่วนลด (If-Else) ----------
    // เงื่อนไขที่ 1: ซื้อครบ 300 บาทขึ้นไป ลด 10%
    if (total >= BIG_ORDER_THRESHOLD) {
      discount += total * BIG_ORDER_DISCOUNT_RATE;
    }

    // เงื่อนไขที่ 2: เป็นสมาชิก ลดเพิ่มอีก 50 บาท
    const isMember = document.getElementById("member-check").checked;
    if (isMember) {
      discount += MEMBER_DISCOUNT;
    }

    finalTotal = Math.max(total - discount, 0);

    document.getElementById("sum-total").textContent = `${total.toFixed(2)} บาท`;
    document.getElementById("sum-discount").textContent = `${discount.toFixed(2)} บาท`;
    document.getElementById("sum-final").textContent = `${finalTotal.toFixed(2)} บาท`;

    if (total === 0) {
      showResult("error", "แจ้งเตือน", "กรุณาเลือกจำนวนสินค้าอย่างน้อย 1 รายการ");
    } else {
      hideResult();
    }
  }

  // ---------------------- คำนวณเงินทอน ----------------------
  function calculateChange() {
    if (finalTotal === 0) {
      showResult("error", "แจ้งเตือน", "กรุณากดคำนวณราคารวมก่อน");
      return;
    }

    const paidInput = document.getElementById("paid-input");
    const paid = parseFloat(paidInput.value);

    if (isNaN(paid)) {
      showResult("error", "ข้อผิดพลาด", "กรุณากรอกจำนวนเงินเป็นตัวเลข");
      return;
    }

    // ---------- เงื่อนไขตรวจสอบเงินที่รับมา (If-Else) ----------
    if (paid < finalTotal) {
      const missing = (finalTotal - paid).toFixed(2);
      showResult(
        "error",
        "เงินไม่พอ",
        `ยอดที่ต้องจ่าย ${finalTotal.toFixed(2)} บาท จ่ายมา ${paid.toFixed(2)} บาท ขาดอีก ${missing} บาท`
      );
    } else {
      const change = (paid - finalTotal).toFixed(2);
      showResult(
        "ok",
        "ชำระเงินสำเร็จ",
        `รับเงินมา ${paid.toFixed(2)} บาท เงินทอน ${change} บาท ขอบคุณที่อุดหนุนแสนอร่อย เบเกอรี่ 🍞`
      );
    }
  }

  // ---------------------- แสดง/ซ่อนกล่องผลลัพธ์ ----------------------
  function showResult(type, title, message) {
    const box = document.getElementById("result-box");
    box.className = type;
    box.style.display = "block";
    box.innerHTML = `<strong>${title}</strong>${message}`;
  }

  function hideResult() {
    const box = document.getElementById("result-box");
    box.style.display = "none";
  }

  // ---------------------- เริ่มออเดอร์ใหม่ ----------------------
  function resetOrder() {
    MENU.forEach((_, i) => {
      document.getElementById(`qty-${i}`).value = 0;
    });
    document.getElementById("member-check").checked = false;
    document.getElementById("paid-input").value = "";
    finalTotal = 0;
    document.getElementById("sum-total").textContent = "0.00 บาท";
    document.getElementById("sum-discount").textContent = "0.00 บาท";
    document.getElementById("sum-final").textContent = "0.00 บาท";
    hideResult();
  }
</script>
</body>
</html>
