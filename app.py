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
produksi["Waste"] = produksi["Produksi"] - produksi["Terjual"]
produksi["Pendapatan"] = produksi["Terjual"] * produksi["Harga"]

limbah["Pendapatan_Limbah"] = limbah["Dijual_kg"] * limbah["Harga_kg"]
limbah["Sisa_Limbah"] = limbah["Ampas_kg"] - limbah["Dijual_kg"]

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Pilih Halaman",
    [
        "Beranda",
        "Dashboard Produksi",
        "Dashboard Limbah",
        "Sustainability"
    ]
)

# =========================
# HALAMAN BERANDA
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

    total_produksi = produksi["Produksi"].sum()
    total_terjual = produksi["Terjual"].sum()
    total_limbah = limbah["Pendapatan_Limbah"].sum()

    col1.metric("Total Produksi", f"{total_produksi} pcs")
    col2.metric("Total Terjual", f"{total_terjual} pcs")
    col3.metric("Profit Limbah", f"Rp {total_limbah:,.0f}")

# =========================
# DASHBOARD PRODUKSI
# =========================
elif menu == "Dashboard Produksi":

    st.title("📊 Dashboard Produksi")

    st.dataframe(produksi)

    st.subheader("Grafik Produksi vs Penjualan")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        produksi["Tanggal"],
        produksi["Produksi"],
        marker='o',
        label='Produksi'
    )

    ax.plot(
        produksi["Tanggal"],
        produksi["Terjual"],
        marker='o',
        label='Terjual'
    )

    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah")
    ax.legend()

    st.pyplot(fig)

    st.subheader("Analisis Waste")

    waste_total = produksi["Waste"].sum()

    st.warning(f"Total Waste Produksi: {waste_total} pcs")

# =========================
# DASHBOARD LIMBAH
# =========================
elif menu == "Dashboard Limbah":

    st.title("🌱 Dashboard Limbah Ampas Tahu")

    st.dataframe(limbah)

    st.subheader("Pendapatan Limbah")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    ax2.bar(
        limbah["Tanggal"],
        limbah["Pendapatan_Limbah"]
    )

    ax2.set_xlabel("Tanggal")
    ax2.set_ylabel("Pendapatan")

    st.pyplot(fig2)

    total_profit_limbah = limbah["Pendapatan_Limbah"].sum()

    st.success(
        f"Total Pendapatan Limbah: Rp {total_profit_limbah:,.0f}"
    )

# =========================
# HALAMAN SUSTAINABILITY
# =========================
elif menu == "Sustainability":

    st.title("♻️ Sustainability")

    st.write(
        """
        Limbah ampas tahu dimanfaatkan sebagai pakan ternak
        untuk mengurangi waste produksi sekaligus menciptakan
        nilai ekonomi tambahan bagi UMKM.
        """
    )

    st.info(
        "Digitalisasi data produksi dan limbah membantu UMKM "
        "mengambil keputusan berbasis data untuk meningkatkan "
        "efisiensi operasional."
    )

    st.markdown("---")

    st.subheader("Alur Pengelolaan Limbah")

    st.code(
        """
Produksi Tahu
      ↓
Ampas Tahu
      ↓
Pencatatan Digital
      ↓
Distribusi Pakan Ternak
      ↓
Profit Tambahan
        """
    )