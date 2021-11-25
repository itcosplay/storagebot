from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType

from loader import dp, bot
from data import yookassa_test_token


@dp.message_handler(Command(commands='pay'))
async def get_pay(message: types.Message):
    """send payment invoice"""
    await bot.delete_message(message.from_user.id, message.message_id)
    await bot.send_invoice(chat_id=message.from_user.id,
                           title='Оплатить услугу',
                           description='Описание заказа',
                           payload='storage-invoice',
                           provider_token=yookassa_test_token,
                           currency="RUB",
                           start_parameter='unique-deep-linking-parameter',
                           prices=[{"label": "руб", "amount": 100000}])


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkput_query: types.PreCheckoutQuery):
    """Do final confirmation to complete payment process."""
    await bot.answer_pre_checkout_query(pre_checkput_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_afterpayment(message: types.Message):
    """Process successful payment."""
    if message.successful_payment.invoice_payload == 'storage-invoice':
        state = dp.current_state(user=message.from_user.id)
        await bot.send_message(message.from_user.id, "Заказ оформлен. QR-Code для доступа формируется...")
