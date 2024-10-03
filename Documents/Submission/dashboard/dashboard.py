import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_total_rentals_by_date(df, selected_date):
    filtered_data = df[df['dteday'] == pd.to_datetime(selected_date)]
    total_rentals = filtered_data['cnt'].sum()
    return total_rentals, filtered_data

def plot_hourly_rentals(filtered_data, selected_date):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=filtered_data, x='hr', y='cnt', ax=ax, palette='viridis')
    ax.set_title(f'Penyewaan Sepeda Berdasarkan Jam pada {selected_date.strftime("%Y-%m-%d")}')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Jumlah Sepeda yang Disewa')
    return fig

def plot_total_year(filtered_data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='mnth', y='cnt', ax=ax, palette='viridis')
    ax.set_title(f'Penyewaan Sepeda Tahun 2011 dan 2012')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Sepeda yang Disewa')
    return fig

def get_total_rentals_by_quarter(df, year, quarter):
    if quarter == 1:
        return df[(df['yr'] == year) & (df['mnth'].between(1, 3))]['cnt'].sum()
    elif quarter == 2:
        return df[(df['yr'] == year) & (df['mnth'].between(4, 6))]['cnt'].sum()
    elif quarter == 3:
        return df[(df['yr'] == year) & (df['mnth'].between(7, 9))]['cnt'].sum()
    elif quarter == 4:
        return df[(df['yr'] == year) & (df['mnth'].between(10, 12))]['cnt'].sum()
    
def plot_monthly_user_type_trend(df):
    monthly_rents = df.groupby(by='mnth')[['casual', 'registered']].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_rents.plot(kind='line', marker='o', ax=ax)
    ax.set_title('Tren Penyewaan Sepeda oleh Pengguna Kasual dan Terdaftar')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Sepeda yang Disewa')
    plt.xticks(rotation=0)
    plt.legend(title='Tipe Pengguna')
    plt.grid(axis='y')
    return fig


def main():
    st.title("Dashboard Analisis Bike Sharing Dataset")


    hour_df = pd.read_csv('hour.csv')
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday']) 
    
    selected_date = st.date_input("Pilih Tanggal:", value=pd.to_datetime("2011-01-01"), 
                                  min_value=hour_df['dteday'].min(), max_value=hour_df['dteday'].max())

    total_rentals, filtered_data = get_total_rentals_by_date(hour_df, selected_date)
    st.write(f"**Total penyewaan sepeda pada {selected_date.strftime('%Y-%m-%d')}: {total_rentals} sepeda.**")

    if not filtered_data.empty:
        fig = plot_hourly_rentals(filtered_data, selected_date)
        st.pyplot(fig)
    else:
        st.warning("Tidak ada data penyewaan sepeda pada tanggal ini.")
    
    st.subheader("Jumlah Penyewaan Sepeda per Kuartal")
    st.markdown("Silahkan pilih kuartal untuk melihat total penyewaan sepeda")

    col_q1, col_q2, col_q3, col_q4 = st.columns(4)
    
    if col_q1.button("Kuartal 1"):
        total_q1_2011 = get_total_rentals_by_quarter(hour_df, 0, 1)
        total_q1_2012 = get_total_rentals_by_quarter(hour_df, 1, 1)
        st.metric("Total Penyewaan pada Kuartal 1 (2011)", f"{total_q1_2011} sepeda")
        st.metric("Total Penyewaan pada Kuartal 1 (2012)", f"{total_q1_2012} sepeda")

    if col_q2.button("Kuartal 2"):
        total_q2_2011 = get_total_rentals_by_quarter(hour_df, 0, 2)
        total_q2_2012 = get_total_rentals_by_quarter(hour_df, 1, 2)
        st.metric("Total Penyewaan pada Kuartal 2 (2011)", f"{total_q2_2011} sepeda")
        st.metric("Total Penyewaan pada Kuartal 2 (2012)", f"{total_q2_2012} sepeda")

    if col_q3.button("Kuartal 3"):
        total_q3_2011 = get_total_rentals_by_quarter(hour_df, 0, 3)
        total_q3_2012 = get_total_rentals_by_quarter(hour_df, 1, 3)
        st.metric("Total Penyewaan pada Kuartal 3 (2011)", f"{total_q3_2011} sepeda")
        st.metric("Total Penyewaan pada Kuartal 3 (2012)", f"{total_q3_2012} sepeda")

    if col_q4.button("Kuartal 4"):
        total_q4_2011 = get_total_rentals_by_quarter(hour_df, 0, 4)
        total_q4_2012 = get_total_rentals_by_quarter(hour_df, 1, 4)
        st.metric("Total Penyewaan pada Kuartal 4 (2011)", f"{total_q4_2011} sepeda")
        st.metric("Total Penyewaan pada Kuartal 4 (2012)", f"{total_q4_2012} sepeda")

    st.subheader("Tren Penyewaan Sepeda ")
    st.markdown("Tren penyewaan sepeda per bulan untuk tahun 2011 dan 2012.")
    
    fig = plot_total_year(hour_df)
    st.pyplot(fig)
    
    st.markdown("Grafik tren penyewaan sepeda diatas menunjukkan kenaikan dimulai dari bulan Januari hingga Juni. Namun, terdapat perlambatan hingga penurunan tren penyewaan dari bulan Juli hingga Desember .")
    
    st.subheader("Tren Penyewaan Sepeda antara Pengguna Kasual dan Terdaftar")

    fig_user_trend = plot_monthly_user_type_trend(hour_df)
    st.pyplot(fig_user_trend)
    
    st.markdown("Grafik diatas menunjukkan bahwa pengguna terdaftar lebih banyak menyewa sepeda dibandingkan pengguna kasual. Namun, tren penyewaan sepeda oleh pengguna kasual mengalami peningkatan yang lebih signifikan dibandingkan pengguna terdaftar.")


if __name__ == '__main__':
    main()
