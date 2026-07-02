import streamlit as st
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Happy Birthday! 🎂",
    page_icon="🎉",
    layout="centered"
)

# --- FUNGSI ANIMASI KONFETI ---
def perayaan():
    st.balloons()
    st.snow()

# --- HEADER & JUDUL ---
st.title("🎉 Happy Birthday, Sahabat! 🎂")
st.write("Ciee... ada yang nambah tua nih! Buka kado digital kamu di bawah ya~")

st.markdown("---")

# --- BAGIAN 1: INPUT NAMA & VALIDASI ---
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
        st.subheader(f"Selamat Ulang Tahun yang ke-19, {nama_teman}! 🥳")
        st.write(
            """
            Semoga di umur yang baru ini, kamu makin sukses, sehat selalu, 
            dan semua cita-cita kamu tercapai. Makasih udah jadi teman yang luar biasa 
            selama ini. Tetap jadi orang yang asyik dan random ya! 🌟
            """
        )
        st.caption("~ Dari sahabat terbaikmu 😎")

    # 2. Galeri Foto / Memori
    st.markdown("### 📸 Kilas Balik Kebersamaan")
    col1, col2 = st.columns(2)
    with col1:
        # Perbaikan: Menambahkan huruf 'r' di depan path agar tidak error unicode
        st.image(r"c:\Users\asust\Downloads\Fotbar.jpeg",
                 caption="Waktu kita Foto bareng")
    with col2:
        # Perbaikan: Menambahkan huruf 'r' di depan path agar tidak error unicode
        st.image(r"c:\Users\asust\Downloads\Tukar Kado.jpeg", 
                 caption="Waktu tukar kado ultah bareng :)!")

    # 3. Kuis Interaktif Mini
    st.markdown("### 🧩 Kuis Singkat: Seberapa Kenal Kita?")
    
    # Perbaikan: Menggunakan st.form agar saat tombol diklik, state tidak berantakan
    with st.form(key='kuis_form'):
        pertanyaan = st.radio(
            "Apa makanan / minuman favorit kita kalau lagi nongkrong bareng?",
            ["Seblak", "Es Teh", "Nasi Goreng", "Es Campur", "Siomay", "Es Jeruk"]
        )
        submit_button = st.form_submit_button(label="Kirim Jawaban")
        
        if submit_button:
            if "Es Teh" in pertanyaan or "Seblak" in pertanyaan:
                st.balloons()
                st.success("Wkwk bener banget! Emang sefrekuensi kita 🍜😂")
            else:
                st.warning("Eits, salah! Masa lupa sih? Coba tebak lagi 😜")

    # 4. Pemutar Musik / Audio
    st.markdown("### 🎵 Backsound Biar Meriah")
    st.info("💡 Kamu bisa putar lagu favorit kalian lewat Spotify sambil buka halaman ini!")