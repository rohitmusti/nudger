# Nudger: The Confusion Engine

original idea: [@charlottemcclintock](https://github.com/charlottemcclintock)

developer: [@rohitmusti](https://rohitmusti.dev)

googler utility author: [@jarun](https://github.com/jarun)

## What is it?

Charlotte has been doing research for her work and noticed that as she searched for information about climate change, she found that her ads from various search engines and social media platforms began to show her ads about companies doing work to better the planet. 
This has nudged her to adopt more environmentally friendly habits, think about her environmental impact, and be more appreciative of nature. 

We then realized that we had an incredibly powerful idea.
Most companies try to nudge potential customers to buy their products through search result ads.
However, if we intentionally searched about certain topics, then we would receive ads about organizations doing work around those topics.
Thus, if we search about topics like climate change, we will begin nudging ourselves towards greener habits.

## How does it work?

Obviously, we can't spend all day googling terms to nudge our behavior, however, we can use our computers to search for us.
So, we wrote a little tool to do it for us, any time we use our computers, we make sure we run our tool.
The way it works is that it uses a library to make google searches in the background.
Google has methods of tracking your searches using your computer's IP address and we are exploiting them to make searches about topics that we want to be advertised about.

Currently, we only have implemented the sustainable company search queries.
We hope to add more queries to this set and create more sets.

## Set up process

1. Install selenium: `pip3 install selenium`
1. Install the chrome driver: `brew cask install chromedriver`
1. Download this github repository.

## Want to contribute?

We have a few next steps in mind.

1. Add in more categories and implement CLI args to make it simpler to switch between different categories.
1. Create a Mac status bar app with a nice GUI to make this more user friendly.
1. Create a Windows application.
1. Create a Linux application.
1. Add in Facebook and Amazon capabilities to increase sites that we search.

## Suggestions?

Please make git issues with any suggestions you have to make this project better! Guide to issues [here](https://guides.github.com/features/issues/)
