import streamlit as st
import pandas as pd

def daily_compound_interest_annual_gain_report(principal, years, annual_rate):
    days_per_year = 365
    daily_rate = (1 + annual_rate) ** (1 / days_per_year) - 1
    current_amount = principal
    results = []

    for year in range(1, years + 1):
        previous_amount = current_amount
        current_amount *= (1 + daily_rate) ** days_per_year
        annual_gain = current_amount - previous_amount
        results.append((year, current_amount, annual_gain))
    
    # 创建 DataFrame 并将数值字段四舍五入到两位小数
    df = pd.DataFrame(results, columns=['第x年', '总资产', '年收入'])
    df['总资产'] = df['总资产'].round(2)
    df['年收入'] = df['年收入'].round(2)
    return df

def main():
    st.title("日复利计算器")
    st.write("请输入本金、年数和年利率，计算每年的总金额及年度收益，并显示图表。")

    principal = st.number_input("请输入本金（元）", min_value=0.0, value=1000.0, step=100.0)
    years = st.number_input("请输入年数", min_value=1, value=10, step=1)
    annual_rate = st.number_input("请输入年利率（如5%请输入0.05）", min_value=0.0, value=0.05, step=0.01)

    if st.button("计算"):
        results_df = daily_compound_interest_annual_gain_report(principal, years, annual_rate)
        st.write("年度总金额变化")
        st.bar_chart(results_df.set_index('第x年')['总资产'])
        st.write("每年收益变化")
        st.bar_chart(results_df.set_index('第x年')['年收入'])

if __name__ == "__main__":
    main()