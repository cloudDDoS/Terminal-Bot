import os
import re

id_pattern = re.compile(r'^.\d+$')


token = os.environ.get("5614158736:AAGFS3oL-lcELu7AkFvdrm21ZlPEobTC-n0")
app_id = int(os.environ.get("12981185"))
app_hash = os.environ.get("66d4471698f94ec48d1c0a3347bda212")
allowed = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]

help_text = """

🔹 /st - speed test
🔹 /ip - ip details
🔹 /stats - disk space
🔹 /cd - change working dir
🔹 /my_files - file manager
🔹 And All System Commands...

"""
