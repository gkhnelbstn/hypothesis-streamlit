import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

def one_way_anova():
    def calculate_anova_table(groups):
        means = [np.mean(group) for group in groups]
        overall_mean = np.mean(np.concatenate(groups))
        ss_between = sum([len(group) * (mean - overall_mean) ** 2 for group, mean in zip(groups, means)])
        ss_within = sum([sum((x - mean) ** 2 for x in group) for group, mean in zip(groups, means)])
        df_between = len(groups) - 1
        df_within = sum(len(group) for group in groups) - len(groups)
        ms_between = ss_between / df_between
        ms_within = ss_within / df_within
        f_value = ms_between / ms_within
        p_value = 1 - stats.f.cdf(f_value, df_between, df_within)
        eta_squared = ss_between / sum([sum((x - overall_mean) ** 2 for x in group) for group in groups])
        return pd.DataFrame({
            "Source": ["Between", "Within", "Total"],
            "Sum of Squares": [ss_between, ss_within, ss_between + ss_within],
            "df": [df_between, df_within, df_between + df_within],
            "Mean Square": [ms_between, ms_within, np.nan],
            "F": [f_value, np.nan, np.nan],
            "P": [p_value, np.nan, np.nan],
            "η²": [eta_squared, np.nan, np.nan],
        })
    
    def calculate_f_value(groups):
        means = [np.mean(group) for group in groups]
        overall_mean = np.mean(np.concatenate(groups))
        ss_between = sum([len(group) * (mean - overall_mean) ** 2 for group, mean in zip(groups, means)])
        ss_within = sum([sum((x - mean) ** 2 for x in group) for group, mean in zip(groups, means)])
        df_between = len(groups) - 1
        df_within = sum(len(group) for group in groups) - len(groups)
        f_value = (ss_between / df_between) / (ss_within / df_within)
        return f_value, df_between, df_within
    
    def post_hoc(groups, labels, alpha=0.05):
        post_hoc_results = []
        try:
            if len(groups) < 3:
                st.write("Tukey's HSD test cannot be performed with less than 3 groups.")
                return []
            tukey_results = pairwise_tukeyhsd(np.concatenate(groups), np.concatenate([np.repeat(i, len(group)) for i, group in enumerate(groups)]), alpha=alpha)
            for result in tukey_results.summary().data[1:]:
                group1 = labels[int(result[0])]
                group2 = labels[int(result[1])]
                p_value = result[5]
                if result[4] < alpha:
                    post_hoc_results.append({'group1': group1, 'group2': group2, 'p_value': p_value})
        except (ValueError, TypeError) as e:
            st.error(f"Error performing post-hoc analysis: {e}")
        return post_hoc_results

    st.title("ANOVA Analysis")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded DataFrame:")
        st.data_editor(df.head())

        group_column = st.selectbox("Select grouping column:", df.columns)
        value_column = st.selectbox("Select value column:", df.columns)

        if st.button("Perform One-Way ANOVA"):
            groups = [group[value_column].dropna().tolist() for name, group in df.groupby(group_column)]
            labels = df[group_column].unique().tolist()

            anova_results = calculate_anova_table(groups)
            st.write("ANOVA Table:")
            st.dataframe(anova_results)

            f_value, df_between, df_within = calculate_f_value(groups)

            post_hoc_results = post_hoc(groups, labels, alpha=0.05)
            if post_hoc_results:
                st.write("Post-Hoc Comparisons (Tukey's HSD):")
                st.write(pd.DataFrame(post_hoc_results))

            result = "Reject H0 (Statistically Significant Difference)" if anova_results.loc[0, "P"] < 0.05 else "Fail to Reject H0 (Not Statistically Significant Difference)"
            st.write(result)

            sns.set_style("whitegrid")
            
            # Create box plot
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            bp = ax1.boxplot(
                [group[value_column] for name, group in df.groupby(group_column)],
                vert=False,
                patch_artist=True,
                showmeans=True,
            )
            for box, median in zip(bp["boxes"], bp["medians"]):
                box.set_facecolor("lightblue")
                median.set_color("black")
                median.set_linewidth(2)
            ax1.set_xlabel(value_column)
            ax1.set_ylabel("Groups")
            ax1.set_title("Distribution of Values Across Groups")
            plt.tight_layout()
            st.pyplot(fig1)

            # Create density plot
            fig2, ax2 = plt.subplots(figsize=(8, 4))
            for name, group in df.groupby(group_column):
                sns.kdeplot(group[value_column], ax=ax2, label=name)
            ax2.set_xlabel(value_column)
            ax2.set_ylabel("Density")
            ax2.set_title("Density Plot of Values Across Groups")
            plt.tight_layout()
            st.pyplot(fig2)

one_way_anova()
