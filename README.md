Random-Episode-Bot

This is a Discord chat bot. Every week or so, a Discord server that I take part it choose one Gumball episode at random to watch and discuss. Keeping track of it all by hand became unmangable, so this bot was designed to automate the process.

The primary function of the bot is to automatically select one of 240 episodes and make a note of that so that it is taken out of the rotation. Alternatively, one can prompt the bot to choose a specific episode of their choosing provided it exists and that it hasn't already been selected.

Additional functionality of the bot includes the ability to view which episodes have been watched, count how many episodes have been watched and from what seasons, and pull up a list of instructions detailing how to use the bot. 

The bot uses the Pandas, NumPy, and Discord libraries to function. Since the episodes that have already been watched are written to a csv file, Pandas and NumPy are used as means of manipulating said csv file. The Discord library is what gives the bot functionaltiy with Discord.

Currently, the bot can only write to one csv file, meaning that it can only keep track of one specific rotation of episodes. If multiple servers were to use the bot, then their rotations would overlap with one another. In the feature, I would like to design it so that each server has its own designated csv file. 
