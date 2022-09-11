from pyVinted import Vinted

import discord
import time
import re 
from discord.ext import commands
vinted = Vinted()
client = commands.Bot(command_prefix='!')
from table2ascii import table2ascii
import requests
import interactions
import pyshorteners

#!vintedstart 53 150 chaussures

@client.event
async def on_ready():

    print(f'{client.user.name} is ready!')

@client.command()
async def vintedstart(ctx, arg, arg2,arg3):
    words_pattern = '[0-9]+'
    price = re.findall(words_pattern, arg2)
    brand = re.findall(words_pattern, arg)
    brand = brand[0].replace('[','')
    price = price[0].replace('[','')
    key = "https://www.vinted.be/vetements?" + "price_to=" + price +"&currency=EUR&brand_id[]=" + brand +"&catalog[]=5&search_text=" + arg3 +"&order=newest_first"  
    headers = {"Content-Type": "application/json; charset=utf-8"}
    items = vinted.items.search(key, 10, 1)
    
    await ctx.channel.send("Début de recherche en cours : (5 secondes maxi.)")
    time.sleep(2.5)
    for item in items:
        vinted_id = item.id
        title = item.title
        photo = item.photo
        brand = item.brand_title
        price = item.price
        url = item.url
        type_tiny = pyshorteners.Shortener()
        url = type_tiny.tinyurl.short(url)
        output = table2ascii(
        header=["Noms :", title],
        body=[["Prix :", price+"€"], ["URL :",url]   ],
        footer=["Dev Note",vinted_id]   
        )
       

        time.sleep(1.5)
        await ctx.channel.send(output)
   
        
@vintedstart.error
async def vintedstart_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                await ctx.send("(One or + arguments is missing after !vintedstart), Merci de checker !commandes afin de remplir tous les arguments.")

client.run('MTAxNzQ2NzYxMTE5MTE5MzYzMA.GEH6kx.yk-h7I7l0vmIa4MHU8nxfLYwIn0bPqbWVq_5BI')
#https://www.vinted.be/vetements?" + "price_to" + price +"&currency=EUR&brand_id[]=" + brand +"&catalog[]=5&search_text=" + arg3 +"&order=newest_first

