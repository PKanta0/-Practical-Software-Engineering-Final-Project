import json
import os

FILENAME = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as f:
        return json.load(f)

def save_tasks(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)


def add_task(tasks):
    name = input("🔹 ชื่องาน: ").strip()
    if not name:
        print("❌ ห้ามเว้นชื่อว่าง")
        return
    description = input("🔹 คำอธิบาย: ").strip()
    due_date = input("🔹 วันที่ครบกำหนด (YYYY-MM-DD): ").strip()

    task_id = max([t['id'] for t in tasks], default=0) + 1
    task = {
        'id': task_id,
        'name': name,
        'description': description,
        'due_date': due_date,
        'completed': False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ เพิ่มงานเรียบร้อย")