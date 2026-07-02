import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN (Wajib di bagian paling atas) ---
st.set_page_config(
    page_title="Happy Birthday! 🎂",
    page_icon="🎉",
    layout="centered"
)

# --- FUNGSI ANIMASI KONFETI ---
def perayaan():
    st.balloons()
    st.snow()

# --- INSTALASI SESSION STATE ---
if 'buka_kado' not in st.session_state:
    st.session_state.buka_kado = False
if 'nama_terkonfirmasi' not in st.session_state:
    st.session_state.nama_terkonfirmasi = ""

# --- HEADER & JUDUL ---
st.title("🎉 Happy Birthday, Sahabat! 🎂")
st.write("Ciee... ada yang nambah tua nih! Buka kado digital kamu di bawah ya~")

st.markdown("---")

# --- BAGIAN 1: INPUT NAMA & VALIDASI (Dengan Tombol Oke) ---
with st.form(key="form_nama"):
    nama_input = st.text_input("Masukkan nama kamu dulu dong buat konfirmasi:", placeholder="Contoh: Budi")
    tombol_oke = st.form_submit_button(label="Oke")

# Logika ketika tombol Oke diklik
if tombol_oke:
    if nama_input.strip():
        st.session_state.nama_terkonfirmasi = nama_input.strip()
    else:
        st.error("Nama tidak boleh kosong yaa!")

# Jika nama sudah terkonfirmasi, tampilkan tombol kejutan
if st.session_state.nama_terkonfirmasi:
    st.success(f"Yess, bener ini buat kamu, {st.session_state.nama_terkonfirmasi}! ✨")
    
    # Tombol Utama Kejutan
    if st.button("KLIK UNTUK LIHAT KEJUTAN! 🎁"):
        st.session_state.buka_kado = True
        perayaan()

# --- BAGIAN 2: KONTEN KEJUTAN ---
if st.session_state.buka_kado:
    
    # 1. Kartu Ucapan Digital
    st.markdown("### 💌 Ucapan Spesial Buat Kamu")
    with st.container(border=True):
        st.subheader(f"Selamat Ulang Tahun yang ke-19, {st.session_state.nama_terkonfirmasi}! 🥳")
        st.write(
            """
            Semoga di umur yang baru ini, kamu makin sukses, sehat selalu, 
            doa-doa mu dikabulkan dan semua cita-cita kamu tercapai. Makasih udah jadi teman yang luar biasa 
            selama ini. Tetap jadi orang yang asyik dan seru ya! 🌟
            """
        )
        st.caption(f"~ Dari sahabat terbaikmu untuk {st.session_state.nama_terkonfirmasi} ❤️")

    # 2. Galeri Foto / Memori (Versi Ringkas Tanpa Else)
    st.markdown("### 📸 Kilas Balik Kebersamaan")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("Fotbar.jpeg", caption="Waktu kita Foto bareng", use_container_width=True)

    with col2:
        st.image("Tukar Kado.jpeg", caption="Waktu tukar kado ultah", use_container_width=True)

    # 3. Kuis Interaktif Mini
    st.markdown("### 🧩 Kuis Singkat: Seberapa Kenal Kita?")
    with st.form(key="form_kuis"):
        pertanyaan = st.radio(
            "Apa makanan / minuman favorit kita kalau lagi nongkrong bareng?",
            ["Seblak", "Es Teh", "Nasi Goreng", "Es Campur", "Siomay", "Es Jeruk"]
        )
        tombol_kuis = st.form_submit_button("Kirim Jawaban")
        
        if tombol_kuis:
            if pertanyaan in ["Es Teh", "Seblak"]:
                st.balloons()
                st.success("Wkwk bener banget! Emang sefrekuensi kita 🍜😂")
            else:
                st.warning("Eits, salah! Masa lupa sih? Coba tebak lagi 😜")

    # 4. Pemutar Musik / Audio 
    st.markdown("### 🎵 Backsound Biar Meriah")
    if os.path.exists("happy_birthday.mp3"):
        st.audio("happy_birthday.mp3", autoplay=True) # Ditambahkan autoplay agar otomatis berputar saat kado dibuka
    else:
        st.info("💡 Hubungkan file musikmu dengan memberi nama 'happy_birthday.mp3' di folder yang sama agar lagu otomatis berputar!")