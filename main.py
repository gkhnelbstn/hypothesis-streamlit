import streamlit as st
from sections import introduction, one_way_anova, two_way_anova

# Sayfa Başlığı
st.title("ANOVA Analizi")
st.write("""
Bu rehber, ANOVA'nın ne olduğunu, nasıl çalıştığını ve nasıl yorumlanacağını anlamak için tasarlanmıştır. 
Buna ek olarak, ANOVA'nın Python programlama dili kullanılarak nasıl uygulanacağını öğreneceksiniz.
""")

# Menü
menu = ["ANOVA Nedir?", "Tek Yönlü ANOVA", "İki Yönlü ANOVA"]

choice = st.sidebar.selectbox("Bölümler", menu)

if choice == "ANOVA Nedir?":
    introduction.show_introduction()
elif choice == "Tek Yönlü ANOVA":
    one_way_anova.one_way_anova()
elif choice == "İki Yönlü ANOVA":
    two_way_anova.two_way_anova()