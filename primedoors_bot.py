from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "7895178842:AAEKH25qO9xc0y5y1e0_ZmH0uVMr-x9-VaE"

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        x = float(update.message.text)
        result = ((x * 1.05) + 4000) * 1.6
        await update.message.reply_text(f"Ամբողջական արժեք: {result}")
    except:
        await update.message.reply_text("Խնդրում եմ մուտագրել միայն թվեր")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

app.run_polling()