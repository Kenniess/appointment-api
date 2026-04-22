name: FastAPI Backend CI/CD

on:
  push:
    branches: ["main"] # หุ่นยนต์จะทำงานทุกครั้งที่มีการ push เข้า branch main

# สำคัญมาก: ปลดล็อกสิทธิ์ให้หุ่นยนต์สามารถแก้โค้ดและ push ไปยังสาขา release ได้
permissions:
  contents: write

jobs:
  test-and-release:
    runs-on: ubuntu-latest

    steps:
      - name: 1. Checkout Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # ดึงประวัติ Git ทั้งหมด เพื่อให้สามารถ push ข้าม branch ได้

      - name: 2. Run Robot Framework Tests
        run: |
          docker compose up --build --exit-code-from robot_tester
          # ถ้า Robot รันไม่ผ่าน ขั้นตอนถัดไปจะไม่ทำงาน

      - name: 3. Promote to Release Branch
        if: success() # จะทำงานก็ต่อเมื่อขั้นตอนรันทดสอบ "ผ่าน" เท่านั้น
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"

          # ดันโค้ดจาก commit ปัจจุบันไปยังสาขา release บน GitHub
          git push origin HEAD:release --force
