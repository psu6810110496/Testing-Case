# HackerRank Algorithms & Unit Testing

โปรเจกต์นี้เป็นการแก้โจทย์ Algorithm จาก HackerRank จำนวน 5 ข้อ พร้อมทั้งเขียน Unit Test เพื่อทดสอบการทำงานของฟังก์ชัน และมีการประยุกต์ใช้ **Stub** ในการจำลองระบบภายนอก

## โครงสร้างโปรเจกต์
- `app/algorithms.py`: โค้ด Production ที่ประกอบไปด้วยฟังก์ชันแก้ปัญหา Algorithm ทั้ง 5 ข้อ และคลาสจำลองสำหรับส่งผลลัพธ์
- `tests/test_algorithms.py`: โค้ดสำหรับทดสอบ (Unit Test) ครอบคลุมเคสปกติ, เคส Defect และการใช้งาน Stub เพื่อจำลองการส่งข้อมูล

## รายชื่อโจทย์ HackerRank
- Funny String
- Alternating Characters
- Caesar Cipher
- Two Characters
- Grid Challenge

## วิธีรัน Unit Test
เปิด Terminal ในโฟลเดอร์หลักของโปรเจกต์แล้วรันคำสั่ง:
```bash
python -m unittest discover tests