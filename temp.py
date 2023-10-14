from gtts import gTTS
import random
import platform
from pydub import AudioSegment
import pyglet
import os

database = [
    {"word": "apple", "word_tr": "elma", "sentences_en": ["I have an apple.", "She likes apples."]},
    {"word": "banana", "word_tr": "muz", "sentences_en": ["He ate a banana.", "Bananas are yellow."]},
    {"word": "computer", "word_tr": "bilgisayar", "sentences_en": ["I use a computer.", "The computer is fast."]},
    {"word": "dog", "word_tr": "köpek", "sentences_en": ["I have a dog.", "The dog is brown."]},
    {"word": "cat", "word_tr": "kedi", "sentences_en": ["She has a cat.", "Cats like to play."]},
    {"word": "book", "word_tr": "kitap", "sentences_en": ["I love reading books.", "The book is on the table."]},
    {"word": "house", "word_tr": "ev", "sentences_en": ["I live in a house.", "The house is big."]},
    {"word": "car", "word_tr": "araba", "sentences_en": ["I drive a car.", "The car is fast."]},
    {"word": "tree", "word_tr": "ağaç", "sentences_en": ["I like climbing trees.", "The tree has green leaves."]},
    {"word": "river", "word_tr": "nehir", "sentences_en": ["I swam in the river.", "The river is wide."]},
    {"word": "mountain", "word_tr": "dağ", "sentences_en": ["I climbed a mountain.", "The mountain is high."]},
    {"word": "flower", "word_tr": "çiçek", "sentences_en": ["I picked a flower.", "The flower is red."]},
    {"word": "bird", "word_tr": "kuş", "sentences_en": ["I saw a bird.", "The bird can fly."]},
    {"word": "friend", "word_tr": "arkadaş", "sentences_en": ["I have a friend.", "My friend is nice."]},
    {"word": "family", "word_tr": "aile", "sentences_en": ["I love my family.", "My family is big."]},
    {"word": "school", "word_tr": "okul", "sentences_en": ["I go to school.", "The school is far."]},
    {"word": "food", "word_tr": "yiyecek", "sentences_en": ["I like Italian food.", "The food is delicious."]},
    {"word": "movie", "word_tr": "film", "sentences_en": ["I watched a movie.", "The movie was interesting."]},
    {"word": "music", "word_tr": "müzik", "sentences_en": ["I listen to music.", "The music is loud."]},
    {"word": "city", "word_tr": "şehir", "sentences_en": ["I live in a city.", "The city is busy."]},
    {"word": "beach", "word_tr": "plaj", "sentences_en": ["I went to the beach.", "The beach is sandy."]},
    {"word": "computer", "word_tr": "bilgisayar", "sentences_en": ["I use a computer.", "The computer is fast."]},
    {"word": "phone", "word_tr": "telefon", "sentences_en": ["I have a phone.", "The phone is new."]},
    {"word": "game", "word_tr": "oyun", "sentences_en": ["I played a game.", "The game was fun."]},
    {"word": "weather", "word_tr": "hava", "sentences_en": ["The weather is nice.", "I like sunny weather."]},
    {"word": "garden", "word_tr": "bahçe", "sentences_en": ["I have a garden.", "The garden has flowers."]}
    
]

used_words = []


def text_to_speech(text):
    
    if os.path.exists("ses.mp3"):
        os.remove("ses.mp3")
    
    tts = gTTS(text=text, lang='en')
    tts.save("ses.mp3")
    
    play_audio("ses.mp3")

def play_audio(file_path):
    music=pyglet.resource.media("ses.mp3")
    music.play()

def learn_word():
    while True:
        word_entry = random.choice(database)
        if word_entry["word"] not in used_words:
            break
    
    used_words.append(word_entry["word"])
    correct_answer = word_entry["word_tr"]
    sentence = random.choice(word_entry["sentences_en"])
    
    text_to_speech(f"{word_entry['word']}. For example: {sentence}")
    
    answer = input("Lütfen duyduğunuz kelimenin Türkçe karşılığını yazın:")
    
    answer = answer.strip().lower()
    
    if answer == correct_answer:
        print("Tebrikler! Yanıt doğru.")
        learn_next_word()
    elif answer == "exit":
        print("Uygulama sonlandırılıyor...")
    else:
        print(f"Üzgünüm. Kelime yanlış. Doğrusu '{correct_answer}' olacaktı.")
    
    

def learn_next_word():
    print("Bir sonraki kelime yükleniyor.")
    learn_word()
    

def main():
    while True:
        print("\n1. Kelime Öğrenme")
        print("2. Çıkış")
        
        choice = input("Lütfen bir seçenek girin (1/2): ").strip()
        
        if choice == "1":
            learn_word()
        elif choice == "2":
            print("Uygulamadan çıkılıyor.")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()