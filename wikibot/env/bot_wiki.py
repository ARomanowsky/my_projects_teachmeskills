from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
import wikipedia

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def test(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🇬🇧 English language", callback_data='en')
    button2 = types.InlineKeyboardButton("🇮🇹 Lingua italiana", callback_data='it')
    button3 = types.InlineKeyboardButton("🇷🇺 Русский язык", callback_data='ru')
    markup.row(button1, button2, button3)
    await message.answer('Choose language ● Scegli la lingua ● Bыберите язык', reply_markup=markup)

@dp.callback_query_handler(text='it')
async def lang_it(call: types.CallbackQuery):
    wikipedia.set_lang('it') 
    markup_lang_it = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_lang_it = types.KeyboardButton("❓ Coma usare")
    markup_lang_it.add(button_lang_it)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, call.from_user.first_name + ", ciao! Inserisci una parola o una frase e te ne darò una breve descrizione, oltre a collegamenti a risorse di terze parti se desideri maggiori dettagli")
    await bot.send_message(call.message.chat.id, text="Per visualizzare le istruzioni per l'utilizzo del bot, fare clic sul pulsante 'Come usare'".format(call.message.from_user), reply_markup=markup_lang_it)

    @dp.message_handler()
    async def term_send_it(message: types.Message):
        if(message.text == "❓ Coma usare"):
            await bot.send_message(message.chat.id, text="1. Per iniziare, seleziona la lingua desiderata; "'\n'
                                                            "2. Quindi inserisci la parola o la frase di cui vuoi conoscere il significato; "'\n'
                                                            "3. Se la richiesta inserita non è corretta, specificarla secondo le opzioni proposte e reinserire la richiesta; "'\n'
                                                            "4. Se hai bisogno di saperne di più su una parola o una frase, puoi leggere un articolo su Wikipedia, guardare un video su YouTube o guardare una foto su Shutterstock. Per fare ciò, fare clic sul pulsante appropriato; "'\n'
                                                            "5. Per cercare una nuova parola o frase, inserisci semplicemente una nuova query")
        
        else:
            await message.answer(wikipedia.summary(message.text, sentences=2))
            markup_term_send_it = types.InlineKeyboardMarkup()
            button1_term_send_it = types.InlineKeyboardButton(f"{(message.text).capitalize()} su Wikipedia", url=wikipedia.page(message.text).url)
            markup_term_send_it.add(button1_term_send_it)
            button2_term_send_it = types.InlineKeyboardButton(f"{(message.text).capitalize()} su Youtube", url=f"https://www.youtube.com/results?search_query={message.text}&sp=CAA%253D")
            markup_term_send_it.add(button2_term_send_it)
            button3_term_send_it = types.InlineKeyboardButton(f"{(message.text).capitalize()} su Shutterstock", url=f"https://www.shutterstock.com/ru/search/{message.text}")
            markup_term_send_it.add(button3_term_send_it)
            await bot.send_message(message.chat.id, text="⬇️Scopri di più⬇️".format(message.from_user), reply_markup=markup_term_send_it)
            await bot.send_message(message.chat.id, text=f"Inserisci una delle opzioni per perfezionare la tua richiesta - {str(wikipedia.search(message.text))[ 1 : - 1 ]}")


@dp.callback_query_handler(text='en')
async def lang_en(call: types.CallbackQuery):
    wikipedia.set_lang('en') 
    markup_lang_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_lang_en = types.KeyboardButton("❓ Terms of use")
    markup_lang_en.add(button_lang_en)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, call.from_user.first_name + ", hi! Enter a word or phrase and I will give you a brief description of it, as well as links to third-party resources if you want more details")
    await bot.send_message(call.message.chat.id, text="To view instructions for using the bot, click the button 'Terms of use'".format(call.message.from_user), reply_markup=markup_lang_en)

    @dp.message_handler()
    async def term_send_en(message: types.Message):
        if(message.text == "❓ Terms of use"):
            await bot.send_message(message.chat.id, text="1. To get started, select the desired language;"'\n'
                                                            "2. Then enter the word or phrase whose meaning you want to know;"'\n'
                                                            "3. If the entered request is not accurate, specify it in accordance with the proposed options and enter the request again;"'\n'
                                                            "4. If you need to learn more about a word or phrase, you can read an article on Wikipedia, watch a video on YouTube, or look at a photo on Shutterstock. To do this, click the appropriate button;"'\n'
                                                            "5. To search for a new word or phrase, simply enter a new query")
        
        else:
            await message.answer(wikipedia.summary(message.text, sentences=2))
            markup_term_send_en = types.InlineKeyboardMarkup()
            button1_term_send_en = types.InlineKeyboardButton(f"{(message.text).capitalize()} on Wikipedia", url=wikipedia.page(message.text).url)
            markup_term_send_en.add(button1_term_send_en)
            button2_term_send_en = types.InlineKeyboardButton(f"{(message.text).capitalize()} on Youtube", url=f"https://www.youtube.com/results?search_query={message.text}&sp=CAA%253D")
            markup_term_send_en.add(button2_term_send_en)
            button3_term_send_en = types.InlineKeyboardButton(f"{(message.text).capitalize()} on Shutterstock", url=f"https://www.shutterstock.com/ru/search/{message.text}")
            markup_term_send_en.add(button3_term_send_en)
            await bot.send_message(message.chat.id, text="⬇️Сhoose the required resource⬇️".format(message.from_user), reply_markup=markup_term_send_en)
            await bot.send_message(message.chat.id, text=f"Enter one of the options to refine your request - {str(wikipedia.search(message.text))[ 1 : - 1 ]}")


@dp.callback_query_handler(text='ru')
async def lang_ru(call: types.CallbackQuery):
    wikipedia.set_lang('ru') 
    markup_lang_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_lang_ru = types.KeyboardButton("❓ Правила пользования")
    markup_lang_ru.add(button_lang_ru)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, call.from_user.first_name + ", привет! Введи слово или словосочетание и я выведу тебе его краткое описание, а также ссылки на сторонние ресурсы, если захочешь больше подробностей")
    await bot.send_message(call.message.chat.id, text="Для просмотра инструкции по пользованию ботом нажмите кнопку 'Правила пользования'".format(call.message.from_user), reply_markup=markup_lang_ru)

    @dp.message_handler()
    async def term_send_ru(message: types.Message):
        if(message.text == "❓ Правила пользования"):
            await bot.send_message(message.chat.id, text="1. Для начала работы выбери нужный язык;"'\n'
                                                            "2. Затем введи слово или словосочетание, смысл которого ты хочешь узнать;"'\n'
                                                            "3. Если введеный запрос не точен, уточни его в соответствии с предложенными вариантами и введи запрос повторно;"'\n'
                                                            "4. При необходимости узнать о слове или словосочетании подробнее ты можешь прочитать статью в Википедии, посмотреть видео на Youtube или посмотреть фото на Shutterstock. Для этого нажми соответствующую кнопку;"'\n'
                                                            "5. Для поиска нового слова или словочетания просто введи новый запрос")
        
        
        elif(message.text == "Телевизор"):
            await bot.send_message(message.chat.id, text=f"{(wikipedia.summary(message.text, sentences=5)).capitalize()}" '\n' 
                                                            "***ПОКУПАЙ ТЕЛЕВИЗОРЫ ПО САМЫМ ВЫГОДНЫМ ЦЕНАМ В ГУМЕ***")
            markup_term_send_ru = types.InlineKeyboardMarkup()
            button1_term_send_ru = types.InlineKeyboardButton(f"{(message.text).capitalize()} в Википедии", url=wikipedia.page(message.text).url)
            markup_term_send_ru.add(button1_term_send_ru)
            button2_term_send_ru = types.InlineKeyboardButton(f"{(message.text).capitalize()} на Youtube", url=f"https://www.youtube.com/results?search_query={message.text}&sp=CAA%253D")
            markup_term_send_ru.add(button2_term_send_ru)
            button3_term_send_ru = types.InlineKeyboardButton(f"{(message.text).capitalize()} на Shutterstock", url=f"https://www.shutterstock.com/ru/search/{message.text}")
            markup_term_send_ru.add(button3_term_send_ru)
            await bot.send_message(message.chat.id, text="⬇️Выбери необходимый ресурс⬇️".format(message.from_user), reply_markup=markup_term_send_ru)
            await bot.send_message(message.chat.id, text=f"Введи один из вариантов, чтобы уточнить запрос - {str(wikipedia.search(message.text))[ 1 : - 1 ]}")
        
        else:
            await message.answer(wikipedia.summary(message.text, sentences=2))
            markup_term_send_ru = types.InlineKeyboardMarkup()
            button1_term_send_ru = types.InlineKeyboardButton(f"{(message.text).capitalize()} в Википедии", url=wikipedia.page(message.text).url)
            markup_term_send_ru.add(button1_term_send_ru)
            button2_term_send_ru = types.InlineKeyboardButton(f"{(message.text).capitalize()} на Youtube", url=f"https://www.youtube.com/results?search_query={message.text}&sp=CAA%253D")
            markup_term_send_ru.add(button2_term_send_ru)
            button3_term_send_ru = types.InlineKeyboardButton(f"{(message.text).capitalize()} на Shutterstock", url=f"https://www.shutterstock.com/ru/search/{message.text}")
            markup_term_send_ru.add(button3_term_send_ru)
            await bot.send_message(message.chat.id, text="⬇️Выбери необходимый ресурс⬇️".format(message.from_user), reply_markup=markup_term_send_ru)
            await bot.send_message(message.chat.id, text=f"Введи один из вариантов, чтобы уточнить запрос - {str(wikipedia.search(message.text))[ 1 : - 1 ]}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)