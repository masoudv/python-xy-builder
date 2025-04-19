import pandas as pd
from datetime import datetime

# مقادیر ورودی را اینجا مشخص کنید
A = 8.0  # مقدار A
B = 21.0  # مقدار B
C = 32.0  # مقدار C

# محاسبه مقادیر M برای T از 0 تا 400
data = {'T': [], 'M': []}
for T in range(1, 401):  # شامل 400
    M = A + B * (T / 300) ** C
    data['T'].append(T)
    data['M'].append(M)

# تولید نام منحصربه‌فرد برای فایل CSV
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = f'/workspaces/python-xy-builder/output_{timestamp}.csv'

# ذخیره داده‌ها در فایل CSV
df = pd.DataFrame(data)
df.to_csv(csv_file, index=False)

print(f"✅ Calculate is DONE!\nThe CSV saved in this route:\n{csv_file}")