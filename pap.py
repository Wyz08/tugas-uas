import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- Fungsi untuk memuat data ----
def load_data():
    # Ganti dengan path ke file CSV Anda
    data = pd.read_csv('data_harga.csv')
    data['Tanggal'] = pd.to_datetime(data['Tanggal'])
    data.set_index('Tanggal', inplace=True)
    return data

# ---- Fungsi untuk menggambar grafik ----
def plot_harga(data):
    plt.clf()  # Clear previous plot
    window_size = 12  # Rata-rata 12 jam

    data['Moving_Average'] = data['Harga'].rolling(window=window_size).mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data.index, data['Harga'], label='Harga Emas (per jam)', color='blue')
    ax.plot(data.index, data['Moving_Average'], label=f'{window_size}-Jam Moving Average', color='orange', linestyle='--')
    ax.set_title('Harga Emas dan Moving Average (Per Jam)')
    ax.set_xlabel('Tanggal & Jam')
    ax.set_ylabel('Harga (IDR)')
    ax.legend()
    ax.grid(alpha=0.3)
    fig.autofmt_xdate()  # Agar label tanggal miring dan tidak bertumpuk

    st.pyplot(fig)


# ---- Fungsi untuk menampilkan berita ----
def display_news():
    st.subheader("Berita Terbaru tentang Emas")
    news_items = [
        {
            "title": "Harga Emas Mengalami Kenaikan Drastis di Tahun 2024",
            "date": "2024-05-15",
            "source": "Reuters",
            "link": "https://www.reuters.com/article/gold-price-increase-2024"
        },
        {
            "title": "Prediksi Harga Emas menyentuh level tertinggi dalam 5 tahun",
            "date": "2024-04-10",
            "source": "Bloomberg",
            "link": "https://www.bloomberg.com/news/articles/2024-04-10/gold-price-prediction"
        },
        {
            "title": "Faktor global yang mempengaruhi harga emas Indonesia",
            "date": "2024-03-25",
            "source": "Jakarta Post",
            "link": "https://www.thejakartapost.com/news/2024/03/25/gold-price-factors-id"
        }
    ]
    
    for item in news_items:
        st.markdown(f"**[{item['title']}]({item['link']})**")
        st.markdown(f"_Tanggal: {item['date']} | Sumber: {item['source']}_")
        st.markdown("---")

# ---- Fungsi utama ----
def main():
    st.set_page_config(page_title="Dashboard Harga Emas Indonesia", layout="wide")

    if "page" not in st.session_state:
        st.session_state.page = "Dashboard Utama"

    if st.session_state.page == "emas":
        menu = "Harga Emas"
        st.session_state.page = "Dashboard Utama"
    else:
        st.sidebar.title("Navigasi")
        menu = st.sidebar.radio("Pilih halaman", ["Dashboard Utama", "Harga Emas"])

    if menu == "Dashboard Utama":
        st.title("Selamat Datang di Dashboard Harga Emas Indonesia")
        st.markdown("Pilih salah satu topik berikut untuk melihat detailnya:")
        if st.button("📈 Emas"):
            st.session_state.page = "emas"
            st.rerun() 

    elif menu == "Harga Emas":
        st.title("Analisis Harga Emas di Indonesia")
        data = load_data()
        st.write("Contoh Data:")
        st.dataframe(data.head())

        plot_harga(data)
        display_news()

    


if __name__ == '__main__':
    main()
