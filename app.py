import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="UMKM Tahu Sumedang",
    page_icon="🌱",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
produksi = pd.read_csv("data_produksi.csv")
limbah = pd.read_csv("data_limbah.csv")

# =========================
# PERHITUNGAN DATA
# =========================
produksi["Waste"] = produksi["Produksi_kg"] * 0.1

limbah["Pendapatan_Limbah"] = limbah["Ampas_kg"] * 2000
limbah["Sisa_Limbah"] = limbah["Ampas_kg"] * 0.2

# =========================
# SIDEBAR MENU (URUTAN BARU)
# =========================
st.sidebar.title("📌 Menu")

menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "Beranda",
        "Tentang Kami",
        "Dashboard Produksi",
        "Dashboard Limbah",
        "Sustainability",
        "Kontak Kami"
    ]
)

# =========================
# 1. BERANDA
# =========================
if menu == "Beranda":

    st.title("🟨 UMKM Tahu Sumedang")

    st.subheader("Cita Rasa Tradisional dengan Sentuhan Modern")

    st.write(
        """
        UMKM Tahu Sumedang berbasis digital untuk meningkatkan
        efisiensi produksi, mengurangi waste, dan memanfaatkan
        limbah ampas tahu sebagai pakan ternak.
        """
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Produksi", f"{produksi['Produksi_kg'].sum()} Kg")
    col2.metric("Total Waste", f"{produksi['Waste'].sum():.1f} Kg")
    col3.metric("Profit Limbah", f"Rp {limbah['Pendapatan_Limbah'].sum():,.0f}")

# =========================
# 2. TENTANG KAMI
# =========================
elif menu == "Tentang Kami":

    st.title("🏪 Tentang Kami")

    st.write(
        """
        Berawal dari usaha rumahan, kami menghadirkan Tahu Sumedang
        dengan cita rasa khas yang dipadukan dengan pendekatan modern
        dalam pemasaran dan pengelolaan usaha.

        Kami percaya bahwa UMKM tradisional juga mampu berkembang
        melalui transformasi digital, inovasi produk, dan pelayanan
        yang lebih baik kepada pelanggan.

        Dengan komitmen terhadap kualitas, kebersihan, dan
        keberlanjutan, kami terus berupaya menghadirkan produk
        terbaik untuk masyarakat.
        """
    )

# =========================
# 3. DASHBOARD PRODUKSI
# =========================
elif menu == "Dashboard Produksi":

    st.title("📊 Dashboard Produksi")

    st.dataframe(produksi)

    fig, ax = plt.subplots()

    ax.plot(produksi["Hari"], produksi["Produksi_kg"], marker='o', label="Produksi")
    ax.set_title("Produksi Tahu")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Kg")
    ax.legend()

    st.pyplot(fig)

    st.warning(f"Total Waste: {produksi['Waste'].sum():.1f} Kg")

# =========================
# 4. DASHBOARD LIMBAH
# =========================
elif menu == "Dashboard Limbah":

    st.title("🌱 Dashboard Limbah Ampas Tahu")

    st.dataframe(limbah)

    fig2, ax2 = plt.subplots()

    ax2.bar(limbah["Hari"], limbah["Pendapatan_Limbah"])
    ax2.set_title("Pendapatan Limbah")

    st.pyplot(fig2)

    st.success(f"Total Pendapatan: Rp {limbah['Pendapatan_Limbah'].sum():,.0f}")

# =========================
# 5. SUSTAINABILITY
# =========================
elif menu == "Sustainability":

    st.title("♻️ Sustainability")

    st.write(
        """
        Kami percaya bahwa usaha yang baik tidak hanya menghasilkan
        keuntungan, tetapi juga memperhatikan lingkungan.

        Limbah ampas tahu kami manfaatkan kembali menjadi produk
        bernilai tambah seperti pakan ternak dan inovasi makanan
        berbasis serat.

        Melalui pengelolaan limbah yang lebih baik, kami berupaya
        mengurangi waste produksi dan menciptakan usaha yang lebih
        berkelanjutan.
        """
    )

    st.info(
        "Digitalisasi membantu UMKM mengambil keputusan lebih efisien dan berkelanjutan."
    )

# =========================
# 6. KONTAK KAMI
# =========================
elif menu == "Kontak Kami":

    st.title("📞 Kontak Kami")

    st.write(
        """
        Kami siap melayani pemesanan, kerja sama, maupun pertanyaan
        seputar produk kami.
        """
    )

    st.markdown("### 📱 WhatsApp")
    st.write("0812-3456-7890")

    st.markdown("### 📧 Email")
    st.write("umkmtahusumedang@gmail.com")
