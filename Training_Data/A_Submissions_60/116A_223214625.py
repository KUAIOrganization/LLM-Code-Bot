n = int(input())  # عدد محطات الترام
min_capacity = 0  # السعة الأدنى المسجلة حتى الآن
current_capacity = 0  # عدد الركاب في الترام حالياً

for _ in range(n):
    a, b = map(int, input().split())  # عدد الركاب الخارجين والداخلين في المحطة الحالية
    current_capacity = current_capacity - a + b  # حساب عدد الركاب الجديد في الترام
    min_capacity = max(min_capacity, current_capacity)  # تحديث السعة الأدنى

print(min_capacity)
