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
RANDOM_STATUS = ["GamersPro™ | !ajuda"]

user_timer = {}
user_spam_count = {}


@client.event
async def on_ready():
    print("Iniciado com sucesso!")
    print(client.user.name)
    print(client.user.id)
    print("versão 1.0")
    print("GamersPro™")
    try:
        choice = random.choice(RANDOM_STATUS)
        await client.change_presence(game=discord.Game(name=choice, type=1))
        await client.send_message(client, "Online!")
    except Exception as e:
        print("Todos direitos {}.".format("reservados"))
    print("Copyright ©")

@client.event
async def on_member_join(member):
  canal = client.get_channel("415675317550841887")
  embed = discord.Embed(
      title="Olá {}".format(member.name),
      color=COR,
      description="Bem-vindo ao discord da rede {} esperamos que seja educado e que leia as regras.".format(member.server.name)
  )
  embed.set_thumbnail(
      url=member.author.avatar_url
  )
  await client.send_message(canal, embed=embed)


@client.event
async def on_message(message):
    url = "https://discord.gg/ZUzGVzj"
    if message.content.startswith('!ajuda'):
        embed = discord.Embed(
            title="SUPORTE",
            color=COR,
            description="Encaminhei uma mensagem com todos os meus comandos!"
        )
        embed.set_thumbnail(
            url=message.server.icon_url
        )
        embed.set_footer(
            text="GamersPro™ © 2018",
            icon_url=message.server.icon_url
        )
        await client.send_message(message.channel, embed=embed)
        embed = discord.Embed(
            title="COMANDOS",
            color=COR,
            description="Segue a lista abaixo com todos os meus comandos."
        )
        embed.set_author(
            name=message.server.name,
            icon_url=message.server.icon_url
        )
        embed.add_field(
            name="",
            value="",
            inline=False
        )
        embed.set_footer(
            text="GamersPro™ © 2018",
            icon_url=message.server.icon_url
        )
        await client.send_message(message.author, embed=embed)

    if message.content.lower().startswith('!usuario'):
        try:
            tmp1 = datetime.datetime.now()

            utcnow = datetime.time(hour=tmp1.hour, minute=tmp1.minute, second=tmp1.second)
            del tmp1
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Nome de usuário:",
                description=user.name,
                color=COR
            )
            userembed.set_author(
                name="Informações do usuário"
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
                text="GamersPro™ © 2018",
                icon_url=message.server.icon_url
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
            description='[Click Here](' + user.avatar_url + ') para acessar o avatar do {}'.format(user.name)
        )
        embed.set_image(
            url=user.avatar_url
        )
        embed.set_footer(
            text="GamersPro™ © 2018",
            icon_url=message.server.icon_url
        )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith('!serverinfo'):
        embed = discord.Embed(
            title='Informações do Servidor',
            color=0x03c3f5,
            descripition='Essas são as informações\n')
        embedserver = discord.Embed(name="{} Server ".format(message.server.name), color=0x551A8B)
        embedserver.add_field(name="Nome:", value=message.server.name, inline=True)
        embedserver.add_field(name=":crown: Dono:", value=message.server.owner.mention)
        embedserver.add_field(name="<:Id:437244194113716235> ID:", value=message.server.id, inline=True)
        embedserver.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embedserver.add_field(name=":family: Membros:", value=len(message.server.members), inline=True)
        embedserver.add_field(name=":date: Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embedserver.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embedserver.add_field(name=":flag_eu: Região:", value=str(message.server.region).title())
        embedserver.set_thumbnail(url=message.server.icon_url)
        embedserver.set_footer(
            text="GamersPro™ © 2018",
            icon_url=message.server.icon_url
        )
        await client.send_message(message.channel, embed=embedserver)

    if message.content.startswith('!sugestão'):
        try:
            await client.delete_message(message)
            remover_sugestao = message.content.replace("!sugestão ", "")
            separar = remover_sugestao.split("|", 1)
            embed = discord.Embed(
                title="%s" % "".join(separar[0]),
                color=COR,
                description="%s" % "".join(separar[1]),
                url=""
            )
            embed.set_author(
                name="{}".format(message.author.name),
                icon_url=message.author.avatar_url
            )
            embed.set_thumbnail(
                url=message.server.icon_url
            )
            await client.send_message(message.author, "Sua sugestão foi enviada!")
            time.sleep(3)
            botmsg = await client.send_message(message.channel, embed=embed)
            await client.add_reaction(botmsg, "👍")
            await client.add_reaction(botmsg, "👎")
        except IndexError:
            await client.send_message(message.author, "Uso correto do comando: !sugestão <sugestão> | <motivo para adicionarmos>")
            time.sleep(3)
        except:
            await client.send_message(message.author,"Uso correto do comando: !sugestão <sugestão> | <motivo para adicionarmos>")
            time.sleep(3)
        finally:
            pass

    if message.content.startswith('!ban'):
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel,
                                             "Só o administrador do servidor pode usar essa comando bobinho(a)🌈!")
        try:
            user = message.mentions[0]
            await client.ban(user, delete_message_days=1)
            await client.send_message(message.channel,
                                      "Membro {} foi banido com sucesso do servidor!".format(user.name))
        except discord.errors.Forbidden:
            await client.send_message(message.channel, "Não tenho permissões para banir esse usuário!")
        except:
            await client.send_message(message.channel, "Especifique um membro!")

    if message.content.startswith('!say'):
        args = message.content.split(" ")
        await client.send_message(message.channel, (" ".join(args[1:])))
        asyncio.sleep(1)
        await client.delete_message(message)
        asyncio.sleep(1)

    if message.content.startswith('!central'):
        msg = "Ei {}, acabei de enviar o convite da minha central no seu privado.".format(message.author.mention)
        await client.send_message(message.channel, msg)
        msg = "Segue abaixo o link do discord\n__https://discord.gg/ZUzGVzj__"
        await client.send_message(message.author, msg)

    if message.content.startswith('!anunciar'):
        args = message.content.split(" ")
        embed = discord.Embed(
            title="",
            color=COR,
            description=(" ".join(args[1:]))
        )
        embed.set_author(
            name="📢 Anúncio"
        )
        embed.set_footer(
            text="GamersPro™ © 2018",
            icon_url=message.server.icon_url
        )
        await client.send_message(message.channel, "@here")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
        asyncio.sleep(1)

    if message.content.startswith('!limpar'):
        tmp = await client.send_message(message.channel, 'Limpando mensagens...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)

    if message.content.startswith('!cantadas'):
        messages = ["Você: Seu pai é sapateiro? \nEla: Não, porquê? \nVocê: Porque você é uma graxinha! Rs", "Você: Nossa moça, desculpa, você se machucou? \nEla: Não! \nVocê: Nossa, mas como um anjo como você cai do céu e não se machuca?", "Você: Oi, por acaso você tem um lápis? \nEla: Não, porquê? \nVocê: Porque quero começar a escrever nossa linda história de amor!", "Você: Por acaso o seu pai é ladrão? \nEla: Claro que não! \nVocê: Então como que ele conseguiu o brilho das estrelas e colocou no seu olhar?"]
        await client.send_message(message.channel, random.choice(messages))
        await asyncio.sleep(21600)

client.run(os.environ.get("BOT_TOKEN"))
