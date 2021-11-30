
##### Data Initialization
Menu = ['1. Report Data Siswa',
        '2. Menambahkan Data Siswa',
        '3. Mengubah Data Siswa',
        '4. Menghapus Data Siswa',
        '5. Exit']

student = [{'NIM' : '12A', 'Nama' : 'Mike', 'Gender' : 'Pria', 'Kota' : 'Jakarta'},
{'NIM' : '12B', 'Nama' : 'Kay', 'Gender' : 'Wanita', 'Kota' : 'Bandung'}]

##### Sub Menu Function
def Sub_Main_Menu(x):
    stop = True
    while stop:
        print('='*50)
        print('1. Kembali Mengakses Sub Menu')
        print('2. Kembali Ke Menu Utama')
        sub = input('Silakan Pilih Sub Menu [1-2] : ')
        if sub == '1':
            x()
            stop = False
        elif sub == '2':
            Main_Menu()
            stop = False


###### Read Data Function
def Read_Data():
    read = True
    while read != '3':
        print("\n+++++++Report Data Siswa+++++++\n")    
        print("1. Report Seluruh Data")
        print("2. Report Data tertentu")
        print("3. Kembali Ke Menu Utama")                                                                     
        read = input("Silakan Pilih Sub Menu Read Data [1-3] : ")
        if read == '1':
            if len(student) != 0 :                                                                      
                print('Daftar Siswa :')                                                    
                for j, i in enumerate(student):                                                                       
                    print(f"{j+1}. NIM : {i['NIM']}, Nama : {i['Nama']}, Gender : {i['Gender']}, Kota : {i['Kota']}")                                                           
            else:                                                                                   
                print('\n****Tidak ada Data Siswa****')   
            Sub_Main_Menu(Read_Data)                                            
        elif read == '2':
            if len(student) != 0 :                                                                      
                std = input("Masukkan NIM : ").upper() 
                print(f"Data Siswa dg NIM : {std}")                                                 
                for j, i in enumerate(student):                                                                       
                    if i['NIM'] == std:
                        print(f"{j+1}. NIM : {i['NIM']}, Nama : {i['Nama']}, Gender : {i['Gender']}, Kota : {i['Kota']}")  
                        break
                else:
                    print("\n****Tidak ada Data Siswa*****")                                                       
            else:                                                                                   
                print('\n****Tidak ada Data Siswa****')  
            Sub_Main_Menu(Read_Data)
        elif read == '3':
            Main_Menu() 


#### Create Data Function
def Create_Data():
    create = True 
    while create != '2':
        print("++++++++Menambah Data Siswa++++++++++++")
        print('1. Tambah Data Siswa')
        print('2. Kembali Ke Menu Utama')
        create = input('Silakan Pilih Sub Menu Create Data [1-2] : ')
        if create == '1':
            nim = input('Masukkan NIM : ').upper()
            for i in student:
                if i['NIM'] == nim:
                    print("Data Sudah Ada")
                    break
                else:
                    nama = input("Masukkan Nama : ")
                    gender = input("Masukkan Gender : ")
                    kota = input("Masukkan Kota : ")
                    save = True
                    while save:
                        simpan = input("Apakah Data akan disimpan? (Y/N) : ").upper()
                        if simpan == 'Y':
                            data = {'NIM' : nim, 'Nama' : nama, 'Gender' : gender, 'Kota' : kota}
                            student.append(data)
                            print('Data Tersimpan')
                            save = False
                            break
                        elif simpan == 'N':
                            save = False
                            break
                break
            Sub_Main_Menu(Create_Data)
        elif create == '2':
            Main_Menu()



###### Update Data Function
def Update_Data():
    Update = True 
    while Update != '2':
        print("==================Mengubah Data Siswa==============")
        print('1. Ubah Data Siswa')
        print('2. Kembali Ke Menu Utama')
        Update = input('Silakan Pilih Sub Menu Update Data [1-2] : ')
        if Update == '1':
            nim = input('Masukkan NIM : ').upper()
            for i in student:
                if i['NIM'] == nim:
                    nama = input("Masukkan Nama Baru : ")
                    save = True
                    while save:
                        simpan = input("Apakah Data akan diUpdate? (Y/N) : ").upper()
                        if simpan == 'Y':
                            i['Nama'] = nama
                            print('Data Updated')
                            save = False
                            break
                        elif simpan == 'N':
                            print("Data Tidak TerUpdate")
                            save = False
                            break
                    break
                else:
                    continue
            else:
                print("Data Tidak Ada")
            Sub_Main_Menu(Update_Data)
        elif Update == '2':
            Main_Menu()


######## Delete Data Function
def Delete_Data():
    Delete = True 
    while Delete != '2':
        print("==================Menghapus Data Siswa==================")
        print('1. Hapus Data Siswa')
        print('2. Kembali Ke Menu Utama')
        Update = input('Silakan Pilih Sub Menu Hapus Data [1-2] : ')
        if Update == '1':
            nim = input('Masukkan NIM : ').upper()
            for i in student:
                if i['NIM'] == nim:
                    Hapus = True
                    while Hapus:
                        Hapus = input("Apakah Data akan diHapus? (Y/N) : ").upper()
                        if Hapus == 'Y':
                            ind = student.index(i)
                            student.pop(ind)
                            print('Data Deleted')
                            Hapus = False
                            break
                        elif Hapus == 'N':
                            print("Data Tidak TerHapus")
                            Hapus = False
                            break
                    break
                else:
                    continue
            else:
                print("Data Tidak Ada")
            Sub_Main_Menu(Delete_Data)
        elif Update == '2':
            Main_Menu()

#### Main Menu Function
def Main_Menu():
    Opsi = 5
    Run_App = True

    while (Opsi != '5' or Run_App):
        print("\n==========Data Record Siswa Purwadhika=============\n")
        for i in Menu:
            print(i)
        Opsi = input("Silakan Pilih Main_Menu [1-5] : ")
        if Opsi == '1':
            Read_Data()
        elif Opsi == '2':
            Create_Data()
        elif Opsi == '3':
            Update_Data()
        elif Opsi == '4':
            Delete_Data()
        elif Opsi == '5':
            print('Thank you and Good Bye!!!')
            quit()
        else:
            print("*****Pilihan yang anda Masukkan Salah************** \n")


###### Run the Application
Main_Menu()