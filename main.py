import random
import catalog
import docs 
import discord
from discord.ext import commands
import datetime
import pandas as pd
import numpy as np




#Note to self: Write something to handle formatting episodes with longer titles. 

#Note: Variables named with only a single character are simply boolean variables to control loops. 

client = commands.Bot(command_prefix = "?")

pd.set_option('display.max_rows', 1000)

players = {}

@client.event
async def on_ready():
  log = pd.read_csv('archive.csv', index_col='label')
  print(log)
  print("")
  print("The bot is ready.")
  await client.change_presence(activity=discord.Game(name=str(log.Episode[len(log) - 1]) + " | Type ?docx for help"))



@client.command(aliases=["random", "randomepisode", "episode"], pass_context=True)
async def weekly(ctx):
  x = False
  while x == False:
    log = pd.read_csv('archive.csv', index_col='label')
    index = random.randrange(len(catalog.Gumball))
    episode = catalog.Gumball[index]
    id = index + 1
    temp = np.count_nonzero(log.ID == id)
    print(temp)
    if temp == 1:
      if len(log) == len(catalog.Gumball):
        print("All episodes have been discussed.")
        await ctx.send("All episodes have been discussed.")
        x = True
      else:
        x = False

    else:
      if id <= 36:
        season = 1
        number = id
      elif id >= 37 and id <= 76:
        season = 2
        number = id - 36
      elif id >= 77 and id <= 116:
        season = 3
        number = id - 76
      elif id >= 117 and id <=156:
        season = 4
        number = id - 116
      elif id >= 157 and id <=196:
        season = 5
        number = id - 156
      else:
        season = 6
        number = id - 196

      x = True


  if len(log) != len(catalog.Gumball):
    sentence = "Season " + str(season) + ", Episode " + str(number) + ": " + episode

    print(sentence)
    print("")



    idx = pd.Index([log.shape[0]], name='label')
    df = pd.DataFrame({'Episode': [episode], 'Season': [season], 'ID': [id], 'Date': [datetime.date.today()]}, index=idx)
    print(df)
    print("")

    concat = pd.concat([log, df], names=['label', 'Episode', 'Season', 'ID', 'Date'])
    concat.to_csv('archive.csv')
    print(concat)
    await ctx.send(f"The episode is:\n**{sentence}**\n@everyone")
    await client.change_presence(activity=discord.Game(name=episode + " | Type ?docx for help"))
  
@client.command(aliases=["count"])
async def counter(ctx):
  log = pd.read_csv('archive.csv', index_col='label')
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  for j in range(len(log)):
    if log.Season[j] == 1:
      one = one + 1
    elif log.Season[j] == 2:
      two = two + 1
    elif log.Season[j] == 3:
      three = three + 1
    elif log.Season[j] == 4:
      four = four + 1
    elif log.Season[j] == 5:
      five = five + 1
    elif log.Season[j] == 6:
      six = six + 1
  print(f"Season 1: {one}\nSeason 2: {two}\nSeason 3: {three}\nSeason 4: {four}\nSeason 5: {five}\nSeason 6: {six}")
  print("Total: " + str(len(log)))
  await ctx.send(f"Season 1: {one}\nSeason 2: {two}\nSeason 3: {three}\nSeason 4: {four}\nSeason 5: {five}\nSeason 6: {six}\nTotal: {str(len(log))}")


@client.command(aliases=["deleterecent"])
async def removerecent(ctx):
    log = pd.read_csv('archive.csv', index_col='label')
    b = len(log) - 1
    episode = log.Episode[b]
    log = log.drop([b])
    log.to_csv('archive.csv')
    print("")
    print(log)
    print("")
    print(episode + " has been removed from the log.")
    await ctx.send(f'"{episode}" has been removed from the log.')
    await client.change_presence(activity=discord.Game(name=str(log.Episode[len(log) - 1]) + " | Type ?docx for help"))

@client.command(aliases=["add", "choice", "pick"])
async def choose(ctx, *, arg):
  log = pd.read_csv('archive.csv', index_col='label')
  b = 0
  d = True
  id = 0
  index = 0


  while b < len(log):
    if log.Episode[b] == str(arg):
      b = len(log) + 3
      d = True
      if len(log) == len(catalog.Gumball):
        print("All epidoes have been discussed.")
        await ctx.send("All episodes have been discussed.")
      else:
        print("This episode has been discussed.")
        await ctx.send("This episode has been discussed.")
    else:
      b = b + 1
      d = False

  if d == False:
    b = 0
    while b < len(catalog.Gumball):
      if catalog.Gumball[b] == str(arg):
        index = b
        id = index + 1
        episode = str(arg)

        if id <= 36:
          season = 1
          number = id
        elif id >= 37 and id <= 76:
          season = 2
          number = id - 36
        elif id >= 77 and id <= 116:
          season = 3
          number = id - 76
        elif id >= 117 and id <=156:
          season = 4
          number = id - 116
        elif id >= 157 and id <=196:
          season = 5
          number = id - 156
        else:
          season = 6
          number = id - 196
        
        sentence = "Season " + str(season) + ", Episode " + str(number) + ": " + episode

        print(sentence)
        print("")



        idx = pd.Index([log.shape[0]], name='label')
        df = pd.DataFrame({'Episode': [episode], 'Season': [season], 'ID': [id], 'Date': [datetime.date.today()]}, index=idx)
        print(df)
        print("")

        concat = pd.concat([log, df], names=['label', 'Episode', 'Season', 'ID', 'Date'])
        concat.to_csv('archive.csv')
        print(concat)
        await ctx.send(f"The episode is:\n**{sentence}**\n@everyone")
        await client.change_presence(activity=discord.Game(name=episode + " | Type ?docx for help"))

        b = len(catalog.Gumball) + 3
        d = True

      else:
        b = b + 1
  
  if d == False:
    print("Episode not found.")
    await ctx.send("Episode not found.")


@client.command(aliases=["delete"])
async def remove (ctx, *, arg):
  log = pd.read_csv('archive.csv', index_col='label')
  b = 0
  d = False

  while b < len(log):
    if log.Episode[b] == str(arg):
      episode = log.Episode[b]
      log = log.drop([b])
      log.index = range(len(log))
      log = log.rename_axis('label')
      print("")
      print(log)
      print("")
      log.to_csv('archive.csv')
      await ctx.send(f'"{episode}" has been removed from the log.')
      await client.change_presence(activity=discord.Game(name=str(log.Episode[len(log) - 1]) + " | Type ?docx for help"))
      b = len(log) + 3
      d = True

    else:
      b = b + 1
  
  if d == False:
    print("")
    print("Episode not found.")
    await ctx.send("This episode has not been logged and discussed yet.")

@client.command(aliases=["archivedate", "logbydate", "archivebydate"])
async def logdate(ctx):
  log = pd.read_csv('archive.csv', index_col='label')
  log = log.reset_index()
  log = log.drop(columns=['label'])
  print(log)

  b = 1

  while b < len(log):
    if b % 37 == 0:
      df1 = log.iloc[b-37:b]
      print(df1)
      await ctx.send(f"``................................................\n{df1}``")
      b = b + 1
    else:
      b = b + 1
      if b == len(log):
        df1 = log.iloc[b - (b%37):b]
        await ctx.send(f"``................................................\n{df1}``")







@client.command(aliases=["archiveepisode", "logbyepisode", "archivebyepisode", "logseason", "archiveseason", "logbyseason", "archivebyseason"])
async def logepisode(ctx):
  log = pd.read_csv('archive.csv', index_col='label')
  log = log.sort_values(by=['ID'])
  log = log.reset_index()
  log = log.drop(columns=['label'])
  print(log)

  b = 1

  while b < len(log):
    if b % 37 == 0:
      df1 = log.iloc[b-37:b]
      print(df1)
      await ctx.send(f"``................................................\n{df1}``")
      b = b + 1
    else:
      b = b + 1
      if b == len(log):
        df1 = log.iloc[b - (b%37):b]
        await ctx.send(f"``................................................\n{df1}``")


@client.command(aliases=["archivename", "logbyname", "archivebyname"])
async def logname(ctx):
  log = pd.read_csv('archive.csv', index_col='label')
  log = log.sort_values(by=['Episode'])
  log = log.reset_index()
  log = log.drop(columns=['label'])
  print(log)

  b = 1

  while b < len(log):
    if b % 37 == 0:
      df1 = log.iloc[b-37:b]
      print(df1)
      await ctx.send(f"``................................................\n{df1}``")
      b = b + 1
    else:
      b = b + 1
      if b == len(log):
        df1 = log.iloc[b - (b%37):b]
        await ctx.send(f"``................................................\n{df1}``")

@client.command()
async def docx(ctx):
  await ctx.send(f"{docs.help}")


      

      
      



  


client.run('NTk3NTA5MDE0Mzc2NDE1MjQy.XSJ0RQ.E5JIoBdTAbWLRzwbWmD3KDAVyA4')   


