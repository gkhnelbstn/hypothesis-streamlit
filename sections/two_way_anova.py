import streamlit as st
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

def two_way_anova():
    def calculate_two_way_anova(df, factor1, factor2, value_column):
        """
        Calculate the two-way ANOVA for given factors and value column in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        factor1 (str): The name of the first factor column.
        factor2 (str): The name of the second factor column.
        value_column (str): The name of the value column.

        Returns:
        pd.DataFrame: The ANOVA table.
        """
        formula = f'{value_column} ~ C({factor1}) + C({factor2}) + C({factor1}):C({factor2})'
        model = ols(formula, data=df).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        return anova_table

    # Streamlit UI
    st.title("Two-Way ANOVA Analysis")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded DataFrame:")
        st.dataframe(df.head())

        # Select columns for analysis
        factor1 = st.selectbox("Select first factor column:", df.columns)
        factor2 = st.selectbox("Select second factor column:", df.columns)
        value_column = st.selectbox("Select value column:", df.columns)

        if st.button("Perform Two-Way ANOVA"):
            # Perform Two-Way ANOVA analysis
            anova_results = calculate_two_way_anova(df, factor1, factor2, value_column)
            st.write("Two-Way ANOVA Table:")
            st.dataframe(anova_results)

            # Create interaction plot
            sns.set_style("whitegrid")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.pointplot(x=factor1, y=value_column, hue=factor2, data=df, dodge=True, markers=["o", "s", "D"], capsize=0.1, ax=ax)
            ax.set_title("Interaction Plot")
            plt.tight_layout()
            st.pyplot(fig)

if __name__ == "__main__":
    two_way_anova()
