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
    nama_input = st.text_input("Masukkan nama kamu dulu dong buat konfirmasi:")
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
            """
            Maaf ya atas terlambat ngucapin nya..
            """
        )
        st.caption(f"~ Dari sahabat terbaikmu untuk {st.session_state.nama_terkonfirmasi} ❤️")

    # 2. Galeri Foto / Memori (BAGIAN YANG SUDAH DIPERBAIKI)
    st.markdown("### 📸 Kilas Balik Kebersamaan")
    
    # Menggunakan container agar tampilan foto rapi dan berjarak bagus
    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            # TIPS: Ganti "Fotbar 1.jpg" dengan URL Link Foto internet (Imgur/Postimages) jika file di GitHub masih tidak terbaca
            foto_1 = "Fotbar 1.jpg" 
            try:
                st.image(foto_1, caption="Waktu kita Foto bareng saat nunggu jemputan pulang sekolah ♡", use_container_width=True)
            except Exception:
                st.error("❌ Gagal memuat 'Fotbar 1.jpg'. Pastikan nama file di GitHub sama persis (perhatikan huruf besar/kecil)!")

        with col2:
            foto_2 = "Tukar Kado 1.jpg"
            try:
                st.image(foto_2, caption="Waktu tukar kado ultah bareng ♡", use_container_width=True)
            except Exception:
                st.error("❌ Gagal memuat 'Tukar Kado 1.jpg'. Pastikan file sudah diunggah ke GitHub!")

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
    
    # Nama file musik kamu di GitHub
    nama_audio = "Happy_Birthday Music.mpeg"
    
    if os.path.exists(nama_audio):
        # Format diatur ke audio/mpeg agar browser mengenali tipenya dengan baik
        st.audio(nama_audio, format="audio/mpeg", autoplay=True)
    else:
        st.info(f"💡 Hubungkan file musikmu dengan memberi nama '{nama_audio}' di folder GitHub yang sama agar lagu otomatis berputar!")