import streamlit as st
import pandas as pd

def show_introduction():
    # Section 1: Introduction of ANOVA Analysis
    st.header("📊 Anova Analizi")
    st.write(
    """
    ANOVA (Analysis of Variance), istatistikte kullanılan bir analiz yöntemidir ve iki veya daha fazla grup arasındaki ortalama farklarını incelemek için kullanılır.
    ANOVA, veri setindeki grup ortalamalarının birbirinden anlamlı derecede farklı olup olmadığını belirlemek için kullanılır ve bu sayede hipotez testlerine olanak tanır.
    """)  
    st.subheader("Temelde ikiye ayrılır:")
    st.write(
    """
    ANOVA'nın temel prensibi, toplam varyansı iki bileşene ayırmaktır:

    1. Grup İçi Varyans: Her grubun kendi içinde bulunan varyans.
    2. Gruplar Arası Varyans: Farklı gruplar arasındaki ortalama farklardan kaynaklanan varyans.
    
    Bu iki varyans bileşeni, F-istatistiği adı verilen bir test istatistiği kullanılarak karşılaştırılır. 
    F-istatistiği, gruplar arası varyansın grup içi varyansa oranıdır ve bu oran belirli bir eşik değeri aştığında, gruplar arasındaki farkların istatistiksel olarak anlamlı olduğu sonucuna varılır.        
    """)
    

    st.subheader("Anova'nın Türleri:")
    st.write(
    """
    1. Tek Yönlü Anova (One-Way ANOVA): Tek bir bağımsız değişkenin gruplar arasındaki farklılıkları açıklamak için kullanıldığı durumlarda kullanılır.
    2. İki Yönlü Anova (Two-Way ANOVA): İki bağımsız değişkenin gruplar arasındaki farklılıkları açıklamak için kullanıldığı durumlarda kullanılır.
    """)


    st.subheader("ANOVA'nın Uygulama Alanları:")
    st.write(
    """
    - Tıp araştırmaları: Farklı tedavi yöntemlerinin etkilerini karşılaştırmak.
    - Eğitim araştırmaları: Farklı öğretim stratejilerinin öğrenci başarıları üzerindeki etkisini değerlendirmek.
    - Sosyal bilimler: Farklı demografik grupların davranışlarının analizini yapmak. 
     """)
    