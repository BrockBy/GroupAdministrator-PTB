from telegram import *
from telegram.ext import *
import random
import json

CHAT_ID = [-1001640668090]
usuarios = {"pepito": "pepito"}

def chat(update, context):
	update.message.reply_text(f"{update.effective_chat.id}")

def start(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        update.message.reply_text(
            f"""usa /comandos para saber mas sobre mi.""", parse_mode="HTML")
    else:
        pass


def new_member(update, context):
    captcha_letters = ["a", "B", "c", "d", "F", "g", "H", "i", "j",
                       "k", "L", "m", "D", "R", "1", "2", "3", "4", "6", "8", "9"]
    p1 = random.choice(captcha_letters)
    p2 = random.choice(captcha_letters)
    p3 = random.choice(captcha_letters)
    p4 = random.choice(captcha_letters)
    p5 = random.choice(captcha_letters)
    p6 = random.choice(captcha_letters)
    captcha = [p1, p2, p3, p4, p5, p6]
    choice = "".join(captcha)
    id = update.message.new_chat_members[0].id
    chat_id = update.effective_chat.id
    if chat_id in CHAT_ID:
        usuarios[id] = choice
        update.message.reply_text(
            f"""Hola <a href="tg://user?id={update.message.new_chat_members[0].id}">{update.message.new_chat_members[0].first_name}</a>.
Puede usar el comando /comandos para saber cuales son mis comandos. Te invitamos a que si no estas en el <a href="https://t.me/PyScriptDevs">canal</a> vayas y le des un poco de amor :3


<b>Para terminar hemos puesto un captcha para evitar bots no deseados por favor escriba en el chat:</b>
{choice}""", parse_mode="HTML")


def filtros(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        text = update.message.text
        id = update.message.from_user.id
        if id in usuarios:
            if text == usuarios[id]:
                update.message.reply_text("Captcha resuelto.")
                usuarios.pop(id)
            else:
                a = update.message.message_id
                context.bot.deleteMessage(chat, a)


def ban(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        chat_id = update.message.reply_to_message.chat.id
        cause_name = update.message.from_user.first_name
        cause_id = update.message.from_user.id
        user_id = update.message.reply_to_message.from_user.id
        user_name = update.message.reply_to_message.from_user.first_name
        member = context.bot.get_chat_member(chat_id, cause_id)
        if member.status in ("administrator", "left", "creator"):
            context.bot.ban_chat_member(chat_id, user_id)
            update.message.reply_text(
                f"""El usuario <a href="tg://user?id={cause_id}">{cause_name}</a> ha expulsado a <a href="tg://user?id={user_id}">{user_name}</a>.. espero que te sientas bien donde quiera que estes...""", parse_mode="HTML")
        else:
            update.message.reply_text(
                f"""Mejor no lo intentes de nuevo, si no quieres que el expulsado seas tu...""")


def unban(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        chat_id = update.message.reply_to_message.chat.id
        cause_name = update.message.from_user.first_name
        cause_id = update.message.from_user.id
        user_id = update.message.reply_to_message.from_user.id
        user_name = update.message.reply_to_message.from_user.first_name
        member = context.bot.get_chat_member(chat_id, cause_id)
        if member.status in ("administrator", "left", "creator"):
            context.bot.unban_chat_member(chat_id, user_id)
            update.message.reply_text(
                f"""El usuario <a href="tg://user?id={cause_id}">{cause_name}</a> ha desbaneado a <a href="tg://user?id={user_id}">{user_name}</a>.. puede volver al chat...""", parse_mode="HTML")
        else:
            update.message.reply_text(
                f"""No eres administrador.. beibe..""")


def silenciar(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        permisos = ChatPermissions(can_send_messages=False, can_send_media_messages=False,
                                   can_send_other_messages=False, can_add_web_page_previews=False)
        chat_id = update.effective_chat.id
        id = update.message.reply_to_message.from_user.id
        cause_id = update.message.from_user.id
        member = context.bot.get_chat_member(chat_id, cause_id)
        if member.status in ('administrator', 'left', 'creator'):
            context.bot.restrict_chat_member(chat_id, id, permissions=permisos)
            update.message.reply_text("Ok.. ¡callado!")


def permh(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        permisos = ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                                   can_send_other_messages=True, can_add_web_page_previews=True)
        chat_id = update.effective_chat.id
        id = update.message.reply_to_message.from_user.id
        cause_id = update.message.from_user.id
        member = context.bot.get_chat_member(chat_id, cause_id)
        if member.status in ('administrator', 'left', 'creator'):
            context.bot.restrict_chat_member(chat_id, id, permissions=permisos)
            update.message.reply_text(
                "Puede volver a hablar... bah... que poco duro...")


def create_link(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        text = update.message.text
        chat = update.effective_chat.id
        creator = update.message.from_user.id
        member = context.bot.get_chat_member(chat, creator)
        if member.status in ('administrator', 'left', 'creator'):
            a = text.split()
            try:
                context.bot.create_chat_invite_link(chat, member_limit=a[1])
                context.bot.send_message(
                    chat_id=chat, text=f"Link creado.. {a[1]} miembros disponibles para la entrada..")
            except:
                context.bot.send_message(
                    chat_id=chat, text=f"Link creado.. 1 miembro disponible..")
                context.bot.create_chat_invite_link(chat, member_limit=1)


def borrar(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        message_id = update.message.reply_to_message.message_id
        cause_id = update.message.message_id
        chat_id = update.message.reply_to_message.chat.id
        id = update.message.from_user.id
        member = context.bot.get_chat_member(chat_id, id)
        if member.status in ("administrator", "left", "creator"):
            context.bot.deleteMessage(chat_id, message_id)
            context.bot.deleteMessage(chat_id, cause_id)
        else:
            update.message.reply_text(
                "Creo que lo mejor seria borrarte a ti... =)")


def fijar(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        id = update.message.from_user.id
        objetivo1 = update.message.reply_to_message.from_user.id
        objetivo2 = update.message.reply_to_message.from_user.first_name
        message_id = update.message.reply_to_message.message_id
        chat_id = update.message.reply_to_message.chat.id
        member = context.bot.get_chat_member(chat_id, id)
        if member.status in ("administrator", "left", "creator"):
            context.bot.pin_chat_message(chat_id, message_id)
            update.message.reply_text(
                f"""Oh... creia que lo ibamos a borrar.. como sea.. el mensaje de <a href="tg://user?id={objetivo1}">{objetivo2}</a> ha sido fijado""", parse_mode="HTML")
        else:
            update.message.reply_text(
                """No me mereces...""", parse_mode="HTML")


def desfijar(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        id = update.message.from_user.id
        objetivo1 = update.message.reply_to_message.from_user.id
        objetivo2 = update.message.reply_to_message.from_user.first_name
        message_id = update.message.reply_to_message.message_id
        chat_id = update.message.reply_to_message.chat.id
        member = context.bot.get_chat_member(chat_id, id)
        if member.status in ('administrator', 'left', 'creator'):
            context.bot.unpin_chat_message(chat_id, message_id)
            update.message.reply_text(
                f"""Genial.. algo mas para desechar... Mensaje de <a href="tg://user?id={objetivo1}">{objetivo2}</a> desfijado""", parse_mode="HTML")
        else:
            update.message.reply_text(
                """Shhh... me molestas...""", parse_mode="HTML")


def warn(update, context):
    id_2 = update.message.from_user.id
    permisos = ChatPermissions(can_send_messages=False, can_send_media_messages=False,
                               can_send_other_messages=False, can_add_web_page_previews=False)
    chat_id = update.effective_chat.id
    id = update.message.reply_to_message.from_user.id
    member = context.bot.get_chat_member(chat_id, id_2)
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        if member.status in ("administrator", "creator", "left"):
            with open("archivo.json", "r") as file:
                warns = json.load(file)
            if str(id) in warns:
                warns[str(id)] += 1
                update.message.reply_text(f"Total de warns: {warns[str(id)]}")
                with open("archivo.json", "w") as file:
                    json.dump(warns, file)
                    if warns[str(id)] == 3:
                        warns[str(id)] = 0
                        update.message.reply_text(
                            f"Advertencias 3/3. Para apelar contacte a @CasperDeveloper")
                        context.bot.restrict_chat_member(
                            chat_id, id, permissions=permisos)
            else:
                warns[str(id)] = 1
                update.message.reply_text(f"Total de warns: {warns[str(id)]}")
                with open("archivo.json", "w") as file:
                    json.dump(warns, file)


def dwarn(update, context):
    id_2 = update.message.from_user.id
    msg_id = update.message.reply_to_message.message_id
    permisos = ChatPermissions(can_send_messages=False, can_send_media_messages=False,
                               can_send_other_messages=False, can_add_web_page_previews=False)
    chat_id = update.effective_chat.id
    id = update.message.reply_to_message.from_user.id
    member = context.bot.get_chat_member(chat_id, id_2)
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        if member.status in ("administrator", "creator", "left"):
            with open("archivo.json", "r") as file:
                warns = json.load(file)
            if str(id) in warns:
                warns[str(id)] += 1
                update.message.reply_text(f"Total de warns: {warns[str(id)]}")
                context.bot.deleteMessage(chat_id, msg_id)
                with open("archivo.json", "w") as file:
                    json.dump(warns, file)
                    if warns[str(id)] == 3:
                        warns[str(id)] = 0
                        update.message.reply_text(
                            f"Advertencias 3/3. Para apelar contacte a @CasperDeveloper")
                        context.bot.restrict_chat_member(
                            chat_id, id, permissions=permisos)
                        context.bot.deleteMessage(chat_id, msg_id)
            else:
                warns[str(id)] = 1
                update.message.reply_text(f"Total de warns: {warns[str(id)]}")
                context.bot.deleteMessage(chat_id, msg_id)
                with open("archivo.json", "w") as file:
                    json.dump(warns, file)


def unwarn(update, context):
    id_2 = update.message.from_user.id
    permisos = ChatPermissions(can_send_messages=False, can_send_media_messages=False,
                               can_send_other_messages=False, can_add_web_page_previews=False)
    chat_id = update.effective_chat.id
    id = update.message.reply_to_message.from_user.id
    member = context.bot.get_chat_member(chat_id, id_2)
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        if member.status in ("administrator", "creator", "left"):
            with open("archivo.json", "r") as file:
                warns = json.load(file)
            if warns[str(id)] == 0:
                update.message.reply_text(
                    "El usuario no tiene advertencias.")
            else:
                if str(id) in warns:
                    warns[str(id)] -= 1
                    update.message.reply_text(
                        f"Total de warns: {warns[str(id)]}")
                    with open("archivo.json", "w") as file:
                        json.dump(warns, file)
                    with open("archivo.json", "r") as file:
                        warns = json.load(file)




def comandos(update, context):
    chat = update.effective_chat.id
    if chat in CHAT_ID:
        update.message.reply_text("""👮🏻 Comandos administrador 👮🏻
/pin - Fija un mensaje.
/unpin - Desfija un mensaje.
/ban - Expulsa a un usuario.
/unban - Permite entrar a un usuario expulsado.
/delete - Elimina un mensaje
/create - Crea un link de entrada para usuarios [X] es la cantidad por defecto 1.
/mute - Silencia a un usuario.
/unmute - Permite hablar a un usuario.
/warn - Da una advertencia a un usuario.
/dwarn - Da una advertencia y elimina el mensaje de un usuario.
/unwarn - Le retira una advertencia a un usuario.

🧔🏻Comandos usuarios-administrador👮🏻
/start - Inicia el bot.
/comandos""")


updater = Updater("TOKEN")
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(
    filters=Filters.status_update.new_chat_members, callback=new_member))
dp.add_handler(CommandHandler("ban", ban))
dp.add_handler(CommandHandler("unban", unban))
dp.add_handler(CommandHandler("pin", fijar))
dp.add_handler(CommandHandler("unpin", desfijar))
dp.add_handler(CommandHandler("delete", borrar))
dp.add_handler(CommandHandler("create", create_link))
dp.add_handler(CommandHandler("mute", silenciar))
dp.add_handler(CommandHandler("unmute", permh))
dp.add_handler(CommandHandler("comandos", comandos))
dp.add_handler(CommandHandler("warn", warn))
dp.add_handler(CommandHandler("dwarn", dwarn))
dp.add_handler(CommandHandler("unwarn", unwarn))
dp.add_handler(CommandHandler("chat", chat))
#====#
dp.add_handler(MessageHandler(Filters.text, filtros))
#===#

print("polling...")
updater.start_polling(allowed_updates=Update.ALL_TYPES)
updater.idle()
