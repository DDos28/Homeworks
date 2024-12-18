from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = '****************************'
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

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer(text='Введите свой возраст:', reply_markup=kb)
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(a=message)
    await message.answer(text='Введите свой рост:', reply_markup=kb)
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(g=message)
    await message.answer(text='Введите свой вес:', reply_markup=kb)
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
