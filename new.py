import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
import keyboard as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


# --- /dynamic ---
@dp.message(Command("dynamic"))
async def dynamic(message: Message):
    await message.answer("Нажми кнопку 👇", reply_markup=kb.start_kb)


@dp.callback_query(F.data == "show_more")
async def show_more(callback: CallbackQuery):
    await callback.message.edit_text("Выбери опцию:", reply_markup=kb.options_kb)


@dp.callback_query(F.data.in_(["option_1", "option_2"]))
async def option_selected(callback: CallbackQuery):
    await callback.answer()



# ---------- Reply-клавиатура ----------
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

# ---------- Хендлеры ----------
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Выбери кнопку 👇",
        reply_markup=main_menu
    )

@dp.message(Command("links"))
async def show_links(message: Message):
    await message.answer(
        "Вот полезные ссылки 👇",
        reply_markup=kb.links_keyboard
    )


@dp.message(F.text == "Привет")
async def say_hello(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def say_bye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")


# ---------- Запуск ----------
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

