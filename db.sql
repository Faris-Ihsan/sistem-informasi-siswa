PGDMP                          {            sistem_informasi_siswa    15.1    15.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    sistem_informasi_siswa    DATABASE     �   CREATE DATABASE sistem_informasi_siswa WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
 &   DROP DATABASE sistem_informasi_siswa;
                postgres    false            �            1259    32893 
   data_siswa    TABLE       CREATE TABLE public.data_siswa (
    id integer NOT NULL,
    nisn character varying(15) NOT NULL,
    niss character varying(20) NOT NULL,
    nama character varying(100),
    tanggal_lahir date,
    tempat_lahir character varying(100),
    alamat character varying(100),
    jenis_kelamin character varying(15),
    nama_orangtua character varying(100),
    asal_sekolah character varying(100),
    tahun_ijazah integer,
    riwayat_pelayanan character varying(100),
    data_assesment character varying(100)
);
    DROP TABLE public.data_siswa;
       public         heap    postgres    false            �            1259    32892    data_siswa_id_seq    SEQUENCE     �   CREATE SEQUENCE public.data_siswa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.data_siswa_id_seq;
       public          postgres    false    215            �           0    0    data_siswa_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.data_siswa_id_seq OWNED BY public.data_siswa.id;
          public          postgres    false    214            e           2604    32896    data_siswa id    DEFAULT     n   ALTER TABLE ONLY public.data_siswa ALTER COLUMN id SET DEFAULT nextval('public.data_siswa_id_seq'::regclass);
 <   ALTER TABLE public.data_siswa ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            �          0    32893 
   data_siswa 
   TABLE DATA           �   COPY public.data_siswa (id, nisn, niss, nama, tanggal_lahir, tempat_lahir, alamat, jenis_kelamin, nama_orangtua, asal_sekolah, tahun_ijazah, riwayat_pelayanan, data_assesment) FROM stdin;
    public          postgres    false    215   �                   0    0    data_siswa_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.data_siswa_id_seq', 74, true);
          public          postgres    false    214            h           2606    32900    data_siswa pk_data_siswa 
   CONSTRAINT     \   ALTER TABLE ONLY public.data_siswa
    ADD CONSTRAINT pk_data_siswa PRIMARY KEY (id, nisn);
 B   ALTER TABLE ONLY public.data_siswa DROP CONSTRAINT pk_data_siswa;
       public            postgres    false    215    215            f           1259    32901    data_siswa_pk    INDEX     O   CREATE UNIQUE INDEX data_siswa_pk ON public.data_siswa USING btree (id, nisn);
 !   DROP INDEX public.data_siswa_pk;
       public            postgres    false    215    215            �   �  x��Z�r�F}��o٭��0 �Dqcp1�.�0+��ؖ\�U���==�BS�%K �/�Ow�-\ד��rW.B���]_z���X�X��Ng�V���k7���"W�*V����I�|��Uq��mZ�eU^9�Z%�*��NŕΜ;ը��ηN���J;������c�?�8��~�>�������rF�D��ˮ��8�����`*�WES�q�Y�L�{�H�Ciq�s�}>(�NǪ*u�;�x�\�@�����'���0���|;<�|?�x <e�U�#۔i����t	�nT�lU�4β���c��3X��Y�V��c���U[w �k���KUmJzDFM<�L�xb���$�|7�#�d8�`�
�Y� {�t~�Ino
���������'�j`��90Lz�/���������q�ç��b�vI�
���Xu�%O�z
��v]�uB�(0�-	zd�gN�?��mR�}ζm*5�i���x�l3xa�d��}Y�S�uc0aAi���kQ�N��/�S���i����7�����("V�f�)�<��LH`�0�������T�*�u����D��^V��E��G3�*0���x&"0a�n������j�Ȋ:�M���NwP�k�.�9���]f�ʹ�3�WN���n Kz��VI���F �j�I)(��K(�EQ�?4>^�]Ո���v9ΨߨņR����w��1�KӦz_�[��AHPbd-�b��;����]U��i���1O����=]9KU�f|z�+u��t��h���q_�Mt\���S)���Ŀ�_s6�J}���-V���e�_)ӓ�K.����`!�1�)#	Y�"V���AL`��������a��Mۻ�G�8ٖ颃9s<9������^�\"n�ļ�e�eO�GvbC��<}��
ĕ���&�s�KUޜ����	�f��,���9����'u�-ذOgv�柇/�/�u�V�6�u���2i]�&L��	W���@�Vm=6��zP�V�X`��B70'���[��kG�[�	XN�Z����5�f��Ʃ�_��x�|�<�$;�9����1�H��o��5d�X�Nez��8�����.���[P�������=p1gȻ��+'o�T�2��Z-����b�����s���L�J�W��sC���� �-i&H�-o�(��AN�	��8���J
#��4Hnq�X���U?�����ņ��)wQlh)��-��$`"��rz���|��ϑş��!-T�%�E�pb\/��8Ō ���1c�G�vlON#�dgښ|31�����Q�S����rf��I�6F&���QJ�����|z����tRnχ���cS�u[��5\4��������ħ��S���n%]P�NvJg�E6�]9'L�%�yY2�B�
)�%�#(D����;��B��EK�]�t�	�MR��>2E����O�+��]f�FtF�H�8hG��
�pl�p�W8�������X��vj�oO�?���	6C���@��MG�[R�Y�ʼ׵F��r�L���O?k�Ҷ���4�lyh�D(&��#�A)���.p�
��N�&L� ��]�\0�v�51�vuƸg|E��D}�F�Q�jGGަ�	�?��Ils�8��N�n�V����C��A�����#��h��<R/U�f�Zw)d�n���?��:�7/��9sf�B.=�
G$Y�K��n�D�l`�����i��1o��7ˏ0JUzR�u�fdy�N����}=T�X����T֮�zw"��>�ߚj��ׅѢ�/(<��Hvp@�����i�Ȁ\�!�l�	��B2O�(Rp.
 AY]�h��[���r@pu|<��m��ѝײن[�}W�� D����54��ӷ*��k�e�T����k�KM���|�K:�B�ֽs��o']�0r4�uր"���T�j�3|iA��QĠI��8L�~ƛu&�1���	ly<0t��Eҵ�iJ�tnAĽ�@S��>�kn
���<53��+����`	��Jmz�jMÜ�&٨�;����ϳ�a.�O�V�(��W��� !"�)uE��
��f�N�+Ե��/�f����ث����|p!�<�8�Kq"N�%$�8�*���`F�xF�E��}�S?ν��(֗Kcw��Q�4��=M_l@&G4��Pe��jf��4I
��lj{������O&e$������h��ڌ��HNy��5H�+�6��	��M��0�[��z���?#������=�&�mb���a�	����ݛ���I��?\L�2H��	����jy2��eA:h���N����(������>�@��̱�^��J�m��o�>����u������S��a�n�+���M�u��6N{�����MF�˃F	�$�O�dey4K��n͈� w���Gf�T�w��������������9�\���|)�N��,��%�YN󍺃lm�}D����Z���z�m�Ь�K:a�^$�r�{>Q/�ԛ�����#��hv�O��#�a^?=|�8��_��(�*4T�ͪ�k+�шN�m 1��M&n^d�n�L��c3�!_Ӥɱ���9z�-�_�--�h]�n���`}^��F�z��G�$17D��C e�&�v����b�Tņ��<�74�hW-�.]S�]Ȝ�`w�74�YY�dj��:	��ķ��£b#�0o�L��O����؁���z���;fz���-9}��v�P�X黋�sV"��6D�c~H]�����)�X�!�nO����k��&|SX�
�J*LNϻ3�s�ڬ+�fӄ+6�~����[V�À��!Vg��uSޡ�w˾v3���'��|=��4�px�W5}���F�q����g�ާ���������PM�U�d���(ą1��̈��9�D0����x�:��C%�f��t�D������p>�C%��_���Q�a�w���÷����@������v��E�4j����[���@�g��OXz�^��io�|���px�uf6�s{Q;o`�ё�d"rn��J>t;���r*��W���������L+��L���	���%���%ҢSrK����Ω�f�����k6BU�:���]�����9b��ΐ͎"��*��n��d9k�>B^Z�J.:�Ķ�0v�~��11�p�4s
_"0z����[­J�x����6L�hd1�տ~<��8�/������C~%�$7���ěci�)��ؚH����@��Z#���|�lS�)״П��̧.�i��@83��֞�[����P!�r���?gs�����ev�Y��!��-�Џ��̦u�䖍;q]����VI�bӦ���=��/�y��3Pջ_�fi>�Շؖ֞�[��<���R�n[��nhDg%aa>h�f���?�{��Wn��~��4���?�4�n�B�O�|������������&Y�b����*K*����Q�)��4 �"�rU.�_���_R�y�/�i�5
<.Lr�
K���-H�Y�ڡ�;[����s2��_��~FG�����'�.��<"C�,,��i�)�%؝�bb��PF
+-���fH��_;��Mq'�V}1;���Ğ��]9��S
˞4�oL]qڕp������`�q�7)�����	�
��1���M�^`kJL]�S݇����������� ܊F����TX���=?���~$��~��ĕ�6?+���y�����74(     