PGDMP         4                 {            sistem_informasi_siswa    14.0    14.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    41055    sistem_informasi_siswa    DATABASE     v   CREATE DATABASE sistem_informasi_siswa WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_Indonesia.1252';
 &   DROP DATABASE sistem_informasi_siswa;
                postgres    false            �            1259    41056    tabel_siswa    TABLE     �  CREATE TABLE public.tabel_siswa (
    nisn numeric(10,0) NOT NULL,
    niss numeric(13,0) NOT NULL,
    nama character varying(100) NOT NULL,
    tanggal_lahir date NOT NULL,
    tempat_lahir character varying(50) NOT NULL,
    alamat character varying(100) NOT NULL,
    jenis_kelamin character varying(10) NOT NULL,
    nama_orangtua character varying(100) NOT NULL,
    asal_sekolah character varying(100) NOT NULL,
    tahun_ijazah numeric(4,0) NOT NULL
);
    DROP TABLE public.tabel_siswa;
       public         heap    postgres    false            �          0    41056    tabel_siswa 
   TABLE DATA           �   COPY public.tabel_siswa (nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah) FROM stdin;
    public          postgres    false    209   C       \           2606    41060    tabel_siswa tabel_siswa_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.tabel_siswa
    ADD CONSTRAINT tabel_siswa_pkey PRIMARY KEY (nisn);
 F   ALTER TABLE ONLY public.tabel_siswa DROP CONSTRAINT tabel_siswa_pkey;
       public            postgres    false    209            �   �   x�]���0���)��m���ă�b��K����F���O�B������O�����ʽ5��dz�>{-�ʥΕ�ƿB�XŖ�3�i��.����Li�E'��)x�6ݫ2����rYX�ɴJ�*��P��G�̙�R>`b
D0V�~z�"v���N�Y���M2a&�NU������?��*˲/��S�     