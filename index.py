import streamlit as st

st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white; margin:0 ; padding:0;'>SEMUA KOLOM WAJIB DIISI</h5>", unsafe_allow_html=True)

st.text_input("Masukkan Nama",placeholder='Masukkan Nama')
st.number_input("Masukkan Umur",max_value=100)
st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
st.number_input("Tekanan Darah",min_value=0,max_value=1000)
st.number_input("Kadar Kolesterol",min_value=0,max_value=1000)

columns = st.columns((2, 0.6, 2))
sumbit = columns[1].button("Submit")
