import discord
import random
import asyncio
import time
import datetime
import sys
import io
import os

client = discord.Client()
testmsgid = None
testmsguser = None

COR =0x3498DB
msg_id = None
msg_user = None
RANDOM_STATUS = ["Euro Truck Simulator 2"]

user_timer = {}
user_spam_count = {}


@client.event
async def on_ready():
    print("Iniciado com sucesso!")
    print(client.user.name)
    print(client.user.id)
    print("versão 1.0")
    print("AmazonExpress™")
    try:
        choice = random.choice(RANDOM_STATUS)
        await client.change_presence(game=discord.Game(name=choice, type=1))
        await client.send_message(client, "Online!")
    except Exception as e:
        print("Todos direitos {}.".format("reservados"))
    print("Copyright ©")

@client.event
async def on_member_join(member):
    canal = client.get_channel("397166274855305226")
    embed = discord.Embed(
        title="",
        color=COR,
        description="Bem vindo ao discord da empresa {}!".format(member.server.name))
    embed.set_author(name="Olá {}!".format(member.name))
    embed.set_thumbnail(url="https://i.imgur.com/yJey64O.png")
    await client.send_message(canal, embed=embed)

    role = discord.utils.get(member.server.roles, name="Visitante")
    await client.add_roles(member, role)
    print("Adicionado o cargo '" + role.name + "' para " + member.name)

@client.event
async def on_message(message):
    if message.content.lower().startswith('!usuario'):
        try:
            tmp1 = datetime.datetime.now()

            utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
            del tmp1
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Informações do usuário",
                description="\n",
                color=COR
            )
            userembed.set_author(
                name=user.server.name,
                icon_url=user.server.icon_url
            )
            userembed.add_field(
                name="Nome de usuário:",
                value=user.name
            )
            userembed.add_field(
                name="Juntou-se ao servidor em:",
                value=userjoinedat
            )
            userembed.add_field(
                name="Usuário criado em:",
                value=usercreatedat
            )
            userembed.add_field(
                name="Identificação:",
                value=user.discriminator
            )
            userembed.add_field(
                name="ID de Usuário:",
                value=user.id
            )
            userembed.set_thumbnail(
                url=user.avatar_url
            )
            userembed.set_footer(
                text="Copyright © 2018.",
                icon_url="https://i.imgur.com/9euTj6A.png"
            )
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Usuário não encontrado.")
        except:
            await client.send_message(message.channel, "Desculpe pelo erro.")
        finally:
            pass

    if message.content.startswith('!avatar'):
        user = message.mentions[0]
        embed = discord.Embed(
            title="",
            color=COR,
            description='[Clique aqui](' + user.avatar_url + ') para acessar o avatar do {}'.format(user.name)
        )
        embed.set_author(
            name=message.server.name,
            icon_url=message.server.icon_url
        )
        embed.set_image(
            url=user.avatar_url
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!serverinfo'):
        embed = discord.Embed(
            title='Informações do Servidor',
            color=0x03c3f5,
            descripition='Essas são as informações\n')
        embed.set_author(name=message.server.name, icon_url=message.server.icon_url)
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name=":crown: Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embed.add_field(name=":family: Membros:", value=len(message.server.members), inline=True)
        embed.add_field(name=":date: Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embed.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embed.add_field(name=":flag_eu: Região:", value=str(message.server.region).title())
        embed.set_thumbnail(url=message.server.icon_url)
        embed.set_footer(text="Copyright © 2018.", icon_url="https://i.imgur.com/9euTj6A.png")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!say'):
        args = message.content.split(" ")
        await client.send_message(message.channel, (" ".join(args[1:])))
        asyncio.sleep(1)
        await client.delete_message(message)
        asyncio.sleep(1)

    if message.content.startswith('!anunciar'):
        args = message.content.split(" ")
        embed = discord.Embed(
            title="📢 Amazon Express 📢",
            color=COR,
            description=" ".join(args[1:])
        )
        embed.set_footer(
            text="Enviado por: {}".format(message.author.name),
            icon_url=message.author.avatar_url
        )
        embed.set_thumbnail(
            url=message.server.icon_url
        )
        await client.send_message(message.channel, "@everyone")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)

    if message.content.startswith('!limpar'):
        await client.send_message(message.channel, 'Limpando mensagens...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)


    if message.content.startswith('!comandofuturo'):
        try:
            await client.delete_message(message)
            remover_sugestao = message.content.replace("!sugestão ", "")
            separar = remover_sugestao.split("|", 1)
            embed = discord.Embed(
                title="💡 SUGESTÃO 💡",
                color=COR,
                description="Nova sugestão recebida. \nEnviada por: {}".format(message.author.mention)
            )
            embed.add_field(
                name="Sugestão:",
                value="```%s```" % "".join(separar[0]),
                inline=False
            )
            embed.add_field(
                name="Por quê?",
                value="```%s```" % "".join(separar[1]),
                inline=False
            )
            embed.set_footer(
                text="Sugestão postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(message.author, "Sua sugestão foi enviada!")
            time.sleep(3)
            botmsg = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(botmsg, "👍")
            await client.add_reaction(botmsg, "👎")


        except IndexError:
            await client.send_message(message.author, "Uso correto do comando: !sugestão <sugestão> | <por quê adicionariamos?>")
            time.sleep(3)
        except:
            await client.send_message(message.author,"Desculpe pelo erro.")
            time.sleep(3)
        finally:
            pass


    if message.content.startswith('!comandofuturo2'):
        try:
            remover_reportar = message.content.replace("!reportar ", "")
            separar = remover_reportar.split("|", 1)
            tmp1 = datetime.datetime.now()

            utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
            del tmp1

            embed = discord.Embed(
                title="🔔 DENÚNCIA 🔔",
                color=COR,
                description="Novo reporte recebido. \nEnviada por: {}".format(message.author.mention)
            )
            embed.add_field(
                name="Suspeito:",
                value="```%s```" % "".join(separar[0]),
                inline=False
            )
            embed.add_field(
                name="Motivo:",
                value="```%s```" % "".join(separar[1]),
                inline=False
            )
            embed.set_footer(
                text="Denúncia postada com sucesso.",
                icon_url=message.author.avatar_url
            )
            await client.send_message(message.channel, embed=embed)
            await client.delete_message(message)
        except IndexError:
            await client.send_message(message.author, "{}, use !reportar <Suspeito> | <Motivo>".format(message.author.mention))
            await client.delete_message(message)
        except:
            await client.send_message(message.author, "Desculpe pelo erro.".format(message.author.mention))
            await client.delete_message(message)
        finally:
            pass

client.run(os.environ.get("BOT_TOKEN"))
