import json
import random
import getpass

user = []

def play():
	print("\n==========Mulai Kuis==========")
	score = 0
	with open("assets/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(10):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {j[ch]["question"]}\n')
			for option in j[ch]["options"]:
				print(option)
			answer = input("\nMasukan Jawaban: ")
			if j[ch]["answer"][0] == answer[0].upper():
				print("\nJawaban Benar!")
				score+=1
			else:
				print("\nJawaban Kurang Tepat!")
			del j[ch]
		print(f'\nSCORE Akhir: {score}')

def quizQuestions():
	if len(user) == 0:
		print("Kamu Harus Login Sebelum Menambahkan Pertanyaan")
	elif len(user) == 2:
		if user[1] == "ADMIN":
			print('\n==========Tambah Pertanyaan==========\n')
			ques = input("Masukan Pertanyaan yang ingin ditambahkan:\n")
			opt = []
			print("Masukkan 4 opsi dengan inisial karakter (A, B, C, D)")
			for _ in range(4):
				opt.append(input())
			ans = input("Masukan Jawaban:\n")
			with open("assets/questions.json", 'r+') as f:
				questions = json.load(f)
				dic = {"question": ques, "options": opt, "answer": ans}
				questions.append(dic)
				f.seek(0)
				json.dump(questions, f)
				f.truncate()
				print("Pertanyaan Berhasil ditambahkan.")		
		else:
			print("Anda tidak memiliki akses untuk menambahkan pertanyaan. Hanya admin yang diizinkan untuk menambahkan pertanyaan.")


def createAccount():
	print("\n==========Buat Akun==========")
	username = input("Masukan USERNAME: ")
	password = getpass.getpass(prompt= 'Masukan PASSWORD: ')
	with open('assets/user_accounts.json', 'r+') as user_accounts:
		users = json.load(user_accounts)
		if username in users.keys():
			print("Akun Nama Pengguna ini sudah ada.nSilakan masuk ke panel login.")
		else:
			users[username] = [password, "PLAYER"]
			user_accounts.seek(0)
			json.dump(users, user_accounts)
			user_accounts.truncate()
			print("Akun Berhasil di Buat!")

def loginAccount():
	print('\n==========LOGIN PANEL==========')
	username = input("USERNAME: ")
	password = getpass.getpass(prompt= 'PASSWORD: ')
	with open('assets/user_accounts.json', 'r') as user_accounts:
		users = json.load(user_accounts)
	if username not in users.keys():
		print("Akun dengan nama itu tidak ada.\nSilakan buat akun terlebih dahulu.")
	elif username in users.keys():
		if users[username][0] != password:
			print("Kata sandi Anda salah.\nSilakan masukkan kata sandi yang benar dan coba lagi.")
		elif users[username][0] == password:
			print("Log in Berhasil.\n")
			user.append(username)
			user.append(users[username][1])

def logout():
	global user
	if len(user) == 0:
		print("Anda sudah keluar")
	else:
		user = []
		print("Anda telah berhasil keluar.")

def rules():
	print('''\n==========Peraturan==========
1. Setiap putaran terdiri dari 10 pertanyaan acak. Untuk menjawabnya, Anda harus menekan A/B/C/D (case-insensitive).
Skor akhir Anda akan diberikan di akhir.
2. Setiap pertanyaan terdiri dari 1 poin. Tidak ada poin negatif untuk jawaban yang salah.
3. Anda dapat membuat akun dari panel PEMBUATAN AKUN.
4. Anda dapat login menggunakan PANEL LOGIN. Saat ini, program hanya dapat masuk dan tidak melakukan apa-apa lagi.
	''')

def about():
	print('''\n==========Tentang Kami==========
Projeck ini dibuat oleh wahyung dan fadhil,
sebagai tugas akhir Mata Kulia AI Programming.''')

if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n=========Selamat Datang di MAster Quiz==========')
		print('------------------------------------------------')
		print('1. Mulai Quiz')
		print('2. Tambah Pertanyaan Quiz')
		print('3. Buat Akun')
		print('4. Login')
		print('5. Logout')
		print('6. Lihat Instruksi Permainan')
		print('7. Keluar')
		print('8. Tentang Kami')
		choice = int(input('Masukan Pilihan: '))
		if choice == 1:
			play()
		elif choice == 2:
			quizQuestions()
		elif choice == 3:
			createAccount()
		elif choice == 4:
			loginAccount()
		elif choice == 5:
			logout()
		elif choice == 6:
			rules()
		elif choice == 7:
			break
		elif choice == 8:
			about()
		else:
			print('MASUKAN YANG SALAH. MASUKKAN PILIHAN LAGI')
