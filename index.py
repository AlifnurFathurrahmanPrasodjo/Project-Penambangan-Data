# import libary 
import streamlit as st
import norm
import time

# pige title
st.set_page_config(
    page_title="Prediksi Depresi",
    page_icon="https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2022/06/19/336133550.jpg",
)

    # 0 = Anda Tidak Depresi
    # 1 = Anda Depresi

# hide menu
hide_streamlit_style = """

<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# insialisasi web
kolom = st.columns((2, 0.48, 2.7))
home = kolom[1].button('Home')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Depresi</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>Harap Diisi Semua Kolom</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Masukkan Nama",placeholder='Nama')
    with col2:
        Age = st.number_input("Masukkan Umur",max_value=100)
    sex = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
    col3,col4,col5 = st.columns(3)
    with col3:
        Number_children = st.number_input("Jumlah anak yang dimiliki",min_value=0,max_value=999999999999)
    with col4:
        education_level = st.number_input("Level edukasi (1-19)",min_value=0,max_value=999999999999)
    with col3:
        total_members = st.number_input("Jumlah anggota keluarga",min_value=0,max_value=999999999999)
    incoming_salary = st.selectbox("Apakah memiliki pendapatan?",('Ya','Tidak'))
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    sumbit = columns[1].button("Submit")
    if sumbit and nama != '' and sex != '' and Number_children != 0 and education_level != 0 and Age != 0 and total_members != 0 and incoming_salary != '':
        # cek jenis kelamin
        #0 = laki-laki
        #1 = perempuan
        if sex == 'Laki-laki':
            sex = 0
        else:
            sex = 1
        
        if incoming_salary == 'Ya':
            incoming_salary = 0
        else:
            incoming_salary = 1
        # normalisasi data
        data = norm.normalisasi([sex,Age,Number_children,education_level,total_members,incoming_salary])
        # prediksi data
        prediksi = norm.knn(data)
        # cek prediksi
        with st.spinner("Tunggu Sebentar Masih Proses..."):
            if prediksi[-1] == 0:
                time.sleep(1)
                st.success("Hasil Prediksi : "+nama+", anda tidak depresi")
            else:
                time.sleep(1)
                st.warning("Hasil Prediksi : "+nama+", anda depresi")

# about page
if about==True and home==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h1>", unsafe_allow_html=True)
    st.write('Sistem Predeksi Depresi adalah sebuah sistem yang bertujuan untuk memprediksi apakah seseorang dalam keadaan depresi atau tidak. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 6</b> . Dataset yang digunakan memiliki <b>8 fitur</b> termasuk kelas.</p>", unsafe_allow_html=True)
    st.write('Alasan menggunakan model KNN dengan parameter k = 6 adalah karena memiliki akurasi yang terbesar dari model lainnya pada dataset ini, sehingga diputuskan untuk menggunakan model tersebut. Sebelumnya sudah dilakukan dua analisa dan percobaan untuk model lainnya, lebih lengkapnya pada link dibawah.')
    st.markdown("<p> <a class='text-warning' target='_blank' href=''>Percobaan model pertama</a> | <a target='_blank' class='text-warning' href=''>Percobaan model kedua</a></p>", unsafe_allow_html=True)
    

        

            





