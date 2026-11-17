import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. العنوان والوصف
st.title("لوحة تحكم بيانات القروض")
st.write("لوحة تفاعلية لاستعراض بيانات طلبات القروض حسب المنطقة والتعليم والدخل.")

# قراءة البيانات مع التخزين المؤقت (باستخدام المسار الكامل لضمان عدم حدوث خطأ الفراغ)
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\05312\Downloads\loan_clean.csv")

df = load_data()

# 2. الفلاتر في الـ Sidebar
st.sidebar.header("الفلاتر")

areas = sorted(df["Property_Area"].dropna().unique())
selected_areas = st.sidebar.multiselect("المنطقة", areas, default=areas)

education = st.sidebar.radio(
    "التعليم", ["الكل"] + sorted(df["Education"].dropna().unique())
)

min_income = int(df["ApplicantIncome"].min())
max_income = int(df["ApplicantIncome"].max())
income_range = st.sidebar.slider(
    "دخل المتقدم", min_income, max_income, (min_income, max_income)
)

# تطبيق الفلاتر
filtered = df[df["Property_Area"].isin(selected_areas)]
filtered = filtered[filtered["ApplicantIncome"].between(income_range[0], income_range[1])]
if education != "الكل":
    filtered = filtered[filtered["Education"] == education]

# 7. الحالة الخاصة: لا توجد صفوف
if len(filtered) == 0:
    st.warning("لا توجد بيانات تطابق الفلاتر المختارة، جرّبي تغيير الفلاتر.")
    st.stop()

# 3. الأرقام الرئيسية
total = len(filtered)
approval_rate = (filtered["Loan_Status"] == "Y").mean() * 100
median_loan = filtered["LoanAmount"].median()

st.subheader("المؤشرات الرئيسية")
col1, col2, col3 = st.columns(3)
col1.metric("عدد الطلبات", total)
col2.metric("نسبة الموافقة", f"{approval_rate:.1f}%")
col3.metric("وسيط مبلغ القرض", f"{median_loan:.0f}")

# 4. رسمتان بـ Seaborn في عمودين
st.subheader("الرسومات البيانية")
left, right = st.columns(2)

with left:
    st.write("توزيع مبالغ القروض")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.histplot(data=filtered, x="LoanAmount", bins=20, kde=True, ax=ax1)
    st.pyplot(fig1)

with right:
    st.write("العلاقة بين الدخل ومبلغ القرض")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=filtered, x="ApplicantIncome", y="LoanAmount",
                    hue="Loan_Status", ax=ax2)
    st.pyplot(fig2)

# 5. selectbox لاختيار عمود رقمي وعرض توزيعه
st.subheader("توزيع عمود رقمي مختار")
numeric_cols = filtered.select_dtypes(include="number").columns.tolist()
selected_col = st.selectbox("اختاري عمودًا رقميًا", numeric_cols)

fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.histplot(data=filtered, x=selected_col, bins=20, ax=ax3)
st.pyplot(fig3)

# 6. الجدول داخل expander
with st.expander("عرض البيانات المفلترة"):
    st.dataframe(filtered)