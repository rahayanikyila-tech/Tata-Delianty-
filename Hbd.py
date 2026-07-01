import streamlit as pd
import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Happy Birthday! 🎂",
    page_icon="🎉",
    layout="centered"
)

# --- FUNGSI ANIMASI KONFETI ---
# Menggunakan komponen bawaan jika ada, atau trik balon/salju dari Streamlit
def perayaan():
    st.balloons()
    st.snow()

# --- HEADER & JUDUL ---
st.title("🎉 Happy Birthday, Sahabat! 🎂")
st.write("Ciee... ada yang nambah tua nih! Buka kado digital kamu di bawah ya~")

st.markdown("---")

# --- BAGIAN 1: INPUT NAMA & VALIDASI ---
# Menggunakan session state agar kejutan tidak hilang saat di-klik
if 'buka_kado' not in st.session_state:
    st.session_state.buka_kado = False

nama_teman = st.text_input("Masukkan nama kamu dulu dong buat konfirmasi:", placeholder="Contoh: Budi")

if nama_teman:
    st.success(f"Yess, bener ini buat kamu, {nama_teman}! ✨")
    
    # Tombol Utama Kejutan
    if st.button("KLIK UNTUK LIHAT KEJUTAN! 🎁"):
        st.session_state.buka_kado = True
        perayaan()

# --- BAGIAN 2: KONTEN KEJUTAN ---
if st.session_state.buka_kado:
    
    # 1. Kartu Ucapan Digital
    st.markdown("### 💌 Ucapan Spesial Buat Kamu")
    with st.container(border=True):
        st.subheader(f"Selamat Ulang Tahun yang ke-X, {nama_teman}! 🥳")
        st.write(
            """
            Semoga di umur yang baru ini, kamu makin sukses, sehat selalu, 
            dan semua cita-cita kamu tercapai. Makasih udah jadi teman yang luar biasa 
            selama ini. Tetap jadi orang yang asyik dan random ya! 🌟
            """
        )
        st.caption("~ Dari sahabat terbaikmu 😎")

    # 2. Galeri Foto / Memori (Opsional)
    st.markdown("### 📸 Kilas Balik Kebersamaan")
    col1, col2 = st.columns(2)
    with col1:
        # Ganti dengan url foto asli atau file lokal kamu
        st.image("https://images.unsplash.com/photo-1513151233558-d860c5398176?w=500", 
                 caption="Waktu kita seru-seruan bareng")
    with col2:
        st.image("https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?w=500", 
                 caption="Satu tahun ke depan harus lebih banyak petualangan!")

    # 3. Kuis Interaktif Mini
    st.markdown("### 🧩 Kuis Singkat: Seberapa Kenal Kita?")
    pertanyaan = st.radio(
        "Apa makanan favorit kita kalau lagi nongkrong bareng?",
        ["Seblak level 5 (sampe nangis)", "Indomie Warmindo", "Nasi Goreng pinggir jalan", "Diet, ga makan apa-apa"]
    )
    
    if st.button("Kirim Jawaban"):
        if "Warmindo" in pertanyaan or "Seblak" in pertanyaan: # Sesuaikan dengan jawaban asli kalian
            st.balloons()
            st.success("Wkwk bener banget! Emang sefrekuensi kita 🍜😂")
        else:
            st.warning("Eits, salah! Masa lupa sih? Coba tebak lagi 😜")

    # 4. Pemutar Musik / Audio (Opsional)
    st.markdown("### 🎵 Backsound Biar Meriah")
    # Kamu bisa masukkan file audio ulang tahun berformat .mp3 di sini
    # st.audio("happy_birthday.mp3", start_time=0)
    st.info("💡 Kamu bisa putar lagu favorit kalian lewat Spotify sambil buka halaman ini!")