import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота из переменной окружения (для безопасности)
BOT_TOKEN = os.getenv('BOT_TOKEN', '7250905524:AAGYAFlTIAOV2wxAnUqxdaWCSelNB-N2X94')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start - главный экран приветствия"""
    
    welcome_text = """Добро пожаловать! 👋

Это премиальный VPN клиент, который обеспечивает конфиденциальность и защиту ваших данных, пока вы онлайн.

🚀Безграничная скорость
🌐Передовой протокол  
🔒Безопасность

Наше приложение:
appstore.com/kaifuvpn
Скачали → вставили ключ → пользуетесь"""

    # Создаем клавиатуру с кнопками
    keyboard = [
        [InlineKeyboardButton("Купить подписку", callback_data='buy_subscription')],
        [InlineKeyboardButton("Личный кабинет", callback_data='personal_cabinet')],
        [InlineKeyboardButton("Помощь", callback_data='help')],
        [InlineKeyboardButton("Как настроить?", callback_data='how_to_setup')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def buy_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Экран покупки подписки"""
    
    subscription_text = """📅 <b>1 Месяц</b>
💰 <s>249р</s>/199р
💎Полный функционал
🎰x1 Шанс к выигрышу

📅 <b>6 месяцев</b>
💰 <s>1494р</s>/999р (-15%)
💎Полный функционал
🎰x6 Шанс к выигрышу

📅 <b>12 месяцев</b>
💰 <s>2988р</s>/1799р (-25%)
💎Полный функционал
🎰x12 Шанс к выигрышу"""

    # Кнопки для выбора тарифа
    keyboard = [
        [InlineKeyboardButton("1 месяц - 199р", callback_data='plan_1_month')],
        [InlineKeyboardButton("6 месяцев - 999р (-15%)", callback_data='plan_6_months')],
        [InlineKeyboardButton("12 месяцев - 1799р (-25%)", callback_data='plan_12_months')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        subscription_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def personal_cabinet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Личный кабинет пользователя"""
    
    cabinet_text = """<b>Личный кабинет</b> 👤

📊 <b>Статус подписки:</b> Активна
📅 <b>Действует до:</b> 15.02.2024
🔑 <b>Ваш ключ:</b> <code>kaif-vpn-key-123456</code>

📈 <b>Статистика:</b>
• Трафик за месяц: 15.2 ГБ
• Серверов доступно: 25
• Текущий сервер: Нидерланды

⚙️ <b>Настройки:</b>
• Автопродление: Включено
• Уведомления: Включены"""

    keyboard = [
        [InlineKeyboardButton("🔄 Обновить ключ", callback_data='update_key')],
        [InlineKeyboardButton("📱 Скачать приложение", callback_data='download_app')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        cabinet_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def help_section(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Раздел помощи"""
    
    help_text = """<b>Помощь</b> 🆘

<b>Часто задаваемые вопросы:</b>

❓ <b>Как активировать VPN?</b>
1. Скачайте приложение по ссылке
2. Скопируйте ваш ключ из личного кабинета
3. Вставьте ключ в приложение
4. Нажмите "Подключиться"

❓ <b>Не работает подключение?</b>
• Проверьте интернет-соединение
• Попробуйте другой сервер
• Обновите ключ в личном кабинете

❓ <b>Как изменить сервер?</b>
В приложении выберите нужную страну из списка

📞 <b>Техподдержка:</b> @kaif_vpn_support"""

    keyboard = [
        [InlineKeyboardButton("📞 Связаться с поддержкой", callback_data='contact_support')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        help_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def how_to_setup(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Инструкция по настройке"""
    
    setup_text = """<b>Как настроить?</b> ⚙️

<b>Пошаговая инструкция:</b>

<b>1️⃣ Скачайте приложение</b>
• iOS: App Store → "KAIF VPN"
• Android: Google Play → "KAIF VPN"

<b>2️⃣ Получите ключ</b>
• Купите подписку в боте
• Скопируйте ключ из личного кабинета

<b>3️⃣ Активируйте VPN</b>
• Откройте приложение
• Нажмите "Добавить конфигурацию"
• Вставьте ваш ключ
• Нажмите "Подключиться"

<b>4️⃣ Выберите сервер</b>
• В списке стран выберите нужную
• Дождитесь подключения (зеленый значок)

✅ <b>Готово!</b> Теперь ваш трафик защищен"""

    keyboard = [
        [InlineKeyboardButton("📱 Скачать приложение", callback_data='download_app')],
        [InlineKeyboardButton("🎥 Видео-инструкция", callback_data='video_guide')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_to_main')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        setup_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def handle_plan_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка выбора тарифного плана"""
    
    query = update.callback_query
    plan = query.data
    
    plans = {
        'plan_1_month': {'name': '1 месяц', 'price': '199р', 'original': '249р'},
        'plan_6_months': {'name': '6 месяцев', 'price': '999р', 'original': '1494р', 'discount': '15%'},
        'plan_12_months': {'name': '12 месяцев', 'price': '1799р', 'original': '2988р', 'discount': '25%'}
    }
    
    selected_plan = plans.get(plan.replace('plan_', '').replace('_', '_'))
    
    if selected_plan:
        payment_text = f"""<b>Оплата подписки</b> 💳

<b>Выбранный тариф:</b> {selected_plan['name']}
<b>Цена:</b> {selected_plan['price']}
{f"<s>{selected_plan['original']}</s> скидка {selected_plan.get('discount', '')}" if 'discount' in selected_plan else ''}

💎 Полный функционал VPN
🚀 Безлимитная скорость
🔒 Максимальная защита
🎰 Участие в розыгрышах

<b>Выберите способ оплаты:</b>"""

        keyboard = [
            [InlineKeyboardButton("💳 Банковская карта", callback_data=f'pay_card_{plan}')],
            [InlineKeyboardButton("📱 СБП", callback_data=f'pay_sbp_{plan}')],
            [InlineKeyboardButton("🥝 QIWI", callback_data=f'pay_qiwi_{plan}')],
            [InlineKeyboardButton("⬅️ Назад к тарифам", callback_data='buy_subscription')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.answer()
        await query.edit_message_text(
            payment_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик всех callback запросов"""
    
    query = update.callback_query
    
    if query.data == 'buy_subscription':
        await buy_subscription(update, context)
    elif query.data == 'personal_cabinet':
        await personal_cabinet(update, context)
    elif query.data == 'help':
        await help_section(update, context)
    elif query.data == 'how_to_setup':
        await how_to_setup(update, context)
    elif query.data.startswith('plan_'):
        await handle_plan_selection(update, context)
    elif query.data == 'back_to_main':
        # Возвращаемся к главному экрану
        await start_from_callback(update, context)
    elif query.data == 'download_app':
        await query.answer("Ссылка на приложение: appstore.com/kaifuvpn", show_alert=True)
    elif query.data == 'contact_support':
        await query.answer("Напишите в поддержку: @kaif_vpn_support", show_alert=True)
    elif query.data.startswith('pay_'):
        await query.answer("Функция оплаты в разработке", show_alert=True)
    else:
        await query.answer("Функция в разработке", show_alert=True)

async def start_from_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Возврат к главному экрану из callback"""
    
    welcome_text = """Добро пожаловать! 👋

Это премиальный VPN клиент, который обеспечивает конфиденциальность и защиту ваших данных, пока вы онлайн.

🚀Безграничная скорость
🌐Передовой протокол  
🔒Безопасность

Наше приложение:
appstore.com/kaifuvpn
Скачали → вставили ключ → пользуетесь"""

    keyboard = [
        [InlineKeyboardButton("Купить подписку", callback_data='buy_subscription')],
        [InlineKeyboardButton("Личный кабинет", callback_data='personal_cabinet')],
        [InlineKeyboardButton("Помощь", callback_data='help')],
        [InlineKeyboardButton("Как настроить?", callback_data='how_to_setup')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

def main() -> None:
    """Запуск бота"""
    
    # Проверяем наличие токена
    if not BOT_TOKEN or BOT_TOKEN == 'your_token_here':
        logger.error("❌ BOT_TOKEN не найден! Установите переменную окружения BOT_TOKEN")
        return
    
    logger.info("🚀 Запуск KAIF VPN бота...")
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(callback_handler))
    
    # Запускаем бота
    logger.info("✅ Бот запущен и готов к работе!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 
