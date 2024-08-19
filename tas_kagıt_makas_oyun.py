import random

def tas_kagit_makas_ECE_ALMIRA_KAYA():
    print("""Merhaba! Taş-Kağıt-Makas oyununa hoş geldiniz! Bu klasik oyunun kuralları çok basit:
            Taş: Makası yener ama kağıda yenilir.
            Kağıt: Taşı yener ama makasa yenilir. 
            Makas: Kağıdı yener ama taşa yenilir. 
            Oyunda, her iki oyuncu da aynı anda bir hamle yapar. Puanı ilk önce 2 olan oyuncu oyunu kazanır.
        Hamle sırasında Taş için 1, kağıt için 2, makas için 3 yazınız.
        Oyunu oynamak istemiyorsanız sorusu sorulduğunda 'hayır' yazınız.
        Oyunun başlayabilmesi için iki oyuncunun da 'evet' demesi gerekmektedir.""")
    while True:
        while True:
            play_game = input("Oynamak istiyor musunuz(Evet/Hayır): ").lower().strip()
            if play_game == "evet" or play_game == "hayır":
                break
            else:
                print("Sadece 'evet' ya da 'hayır' yazınız" )
        
        computer_game_choice = random.randint(0,100)
        if computer_game_choice < 20:
            computer_game_choice = "hayır"
        else:
            computer_game_choice = "evet"
        print(f"Bilgisayar istiyor mu? {computer_game_choice}\n")

        if play_game == "evet" and computer_game_choice == "evet":
            game_options = ["taş", "kağıt", "makas"]
            user_point = 0
            computer_point = 0
            round = 0
            while user_point < 2 and computer_point < 2:
                round += 1
                print(f"--------------Tur {round}--------------")
                while True:
                    user_input = int(input("Hamlenizi seçiniz (Taş(1)/Kağıt(2)/Makas(3)): "))
                    if user_input <= 3 and user_input > 0:
                        break
                    else:
                        print("1, 2 ya da 3 seçiniz.")
                
                computer_input = random.randint(1, 3)
                print(f"Bilgisayarın hamlesi: {game_options[computer_input - 1]}")
                
                if computer_input == user_input:
                    print("Berabere!")
                elif (computer_input == 1 and user_input == 3) or \
                    (computer_input == 2 and user_input == 1) or \
                    (computer_input == 3 and user_input == 2):
                    computer_point += 1
                    print("Bilgisayar kazandı!")
                else:
                    user_point += 1
                    print("Kazandınız!")

                print(f"Oyuncu puanı: {user_point}, Bilgisayar puanı: {computer_point}\n")
            
            if user_point > computer_point:
                print("---------OYUNU KAZANDINIZ---------")
            else:
                print("---------KAYBETTİNİZ---------")

        elif computer_game_choice == "hayır" and play_game== "evet":
            print("İstekleriniz karşılıksız.\nGörüşmek üzere!")
            break
        else:
            print("Görüşürüz!")
            break


tas_kagit_makas_ECE_ALMIRA_KAYA()
