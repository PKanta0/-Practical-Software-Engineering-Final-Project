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

def add_task():
    tasks = load_tasks()
    task = {
        "id": 1,
        "name": "งานตัวอย่าง",
        "description": "ยังไม่รับค่าจากผู้ใช้",
        "due_date": "2025-05-01",
        "completed": False
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print("✅ เพิ่มงานสำเร็จ (ทดสอบ)")