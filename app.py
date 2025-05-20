import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Fungsi untuk memuat data
def load_data():
    data = pd.read_csv('data_harga.csv')
    data['Tanggal'] = pd.to_datetime(data['Tanggal'])
    data.set_index('Tanggal', inplace=True)
    return data

# Fungsi untuk menggambar grafik
def plot_harga(data):
    plt.clf()
    window_size = 12
    data['Moving_Average'] = data['Harga'].rolling(window=window_size).mean()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data.index, data['Harga'], label='Harga Emas (per jam)', color='blue')
    ax.plot(data.index, data['Moving_Average'], label=f'{window_size}-Jam Moving Average', color='orange', linestyle='--')
    ax.set_title('Harga Emas dan Moving Average (Per Jam)')
    ax.set_xlabel('Tanggal & Jam')
    ax.set_ylabel('Harga (IDR)')
    ax.legend()
    ax.grid(alpha=0.3)
    fig.autofmt_xdate()
    st.pyplot(fig)

#Fungsi untuk menampilkan berita
def display_news():
    st.subheader("Berita Terbaru tentang Emas")
    news_items = [
        {
            "title": "10 Faktor yang Mempengaruhi Harga Emas di Pasar Global",
            "date": "2025-04-08",
            "source": "Young On Top",
            "link": "https://youngontop.com/10-faktor-yang-mempengaruhi-harga-emas-di-pasar-global/#:~:text=Faktor%20yang%20Mempengaruhi%20Harga%20Emas%20di%20Pasar%20Global,8.%20Permintaan%20Industri%20dan%20Perhiasan%20...%20More%20items",
            "image": "https://youngontop.com/wp-content/uploads/2025/04/gold-bars-stacks-of-cash-sit-on-a-table-at-night-2025-02-15-19-18-59-utc-1500x1000.jpg"
        },
        {
            "title": "Harga Emas Baru Melonjak Lagi, Ada yang Berani Ramal Tembus US$3.700",
            "date": "2025-05-20",
            "source": "CNBC INDONESIA",
            "link": "https://www.cnbcindonesia.com/research/20250520061512-128-634506/harga-emas-baru-melonjak-lagi-ada-yang-berani-ramal-tembus-us-3700",
            "image": "https://awsimages.detik.net.id/visual/2025/05/13/emas-gold-bar-1747107954719_169.jpeg?w=900&q=80"
        },
        {
            "title": "Harga Emas Antam Logam Mulia Naik Rp 23.000, Dekati Rp 1,9 Juta",
            "date": "2025-05-19",
            "source": "CNBC INDONESIA",
            "link": "https://www.cnbcindonesia.com/research/20250519091627-128-634242/harga-emas-antam-logam-mulia-naik-rp-23000-dekati-rp-19-juta",
            "image": "https://awsimages.detik.net.id/visual/2024/07/16/karyawati-menunjukkan-emas-pt-aneka-tambang-tbk-antam-di-salah-satu-gallery-penjualan-emas-di-jakarta-selasa-1672024-9_169.jpeg?w=900&q=80"
        },
        
    ]
    
    for item in news_items:
        st.markdown(f"**[{item['title']}]({item['link']})**")
        st.markdown(f"_Tanggal: {item['date']} | Sumber: {item['source']}_")
        st.image(item['image'], width=300)  # Menampilkan gambar
        st.markdown("---")

#Fungsi untuk menampilkan statistik
def display_statistics(data):
    st.subheader("Statistik Harga Emas")
    st.write("Statistik Deskriptif:")
    st.write(data.describe())

# Fungsi utama
def main():
    st.set_page_config(page_title="Dashboard Harga Emas di Indonesia", layout="wide")
    
    if "page" not in st.session_state:
        st.session_state.page = "Dashboard Utama"
    
    if st.session_state.page == "emas":
        menu = "Harga Emas"
        st.session_state.page = "Dashboard Utama"
    else:
        st.sidebar.title("Navigasi")
        menu = st.sidebar.radio("Pilih Dashboard", ["Dashboard Utama", "Harga Emas"])
    if menu == "Dashboard Utama":
        st.title("Selamat Datang di Dashboard Harga Emas  di Indonesia")
        st.markdown("Pilih salah satu topik berikut untuk melihat detailnya:")
        if st.button("📈 Emas"):
            st.session_state.page = "Emas"
            st.rerun() 
    elif menu == "Harga Emas":
        st.title("Analisis Harga Emas di Indonesia")
        data = load_data()
        st.write("Contoh Data:")
        st.dataframe(data.head())
        # Menambahkan slider untuk memilih rentang tanggal
        start_date, end_date = st.slider(
            "Pilih rentang tanggal:",
            min_value=data.index.min().date(),
            max_value=data.index.max().date(),
            value=(data.index.min().date(), data.index.max().date())
        )
        # Menyaring data berdasarkan rentang tanggal yang dipilih
        filtered_data = data.loc[start_date:end_date]

        # Menampilkan grafik dan statistik untuk data yang telah difilter
        plot_harga(filtered_data)
        display_statistics(filtered_data)
        display_news()

        # Menambahkan tombol untuk mengunduh data
        csv = filtered_data.to_csv().encode('utf-8')
        st.download_button(
            label="Unduh Data (CSV)",
            data=csv,
            file_name='data_harga_emas.csv',
            mime='text/csv',
        )
        
if __name__ == '__main__':
    main()