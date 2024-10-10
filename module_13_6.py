from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '******************************'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.add(button2)

kb_in = InlineKeyboardMarkup()
button_in1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_in2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.row(button_in1, button_in2)

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        "Упрощенная формула Миффлина-Сан Жеора: "
        "\n-для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5 "
        "\n-для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161"
    )
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(a=message)
    await message.answer('Введите свой рост:', reply_markup=kb)
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(g=message)
    await message.answer('Введите свой вес:', reply_markup=kb)
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(w=message)
    data = await state.get_data()
    age = int(data['a'])
    growth = int(data['g'])
    weight = int(data['w'])
    result = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма в сутки {result} ккал.')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)