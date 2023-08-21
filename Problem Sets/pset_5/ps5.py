# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Jatin Jindal
# Collaborators: None
# Time: About 2 hours

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.pubdate = pubdate
        self.description = description
        self.title = title
        self.link = link
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_pubdate(self):
        return self.pubdate
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story : NewsStory):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase.lower()
        
    def is_phrase_in(self, text):
        cleaned_phrase = ''.join(' ' if char in string.punctuation else char for char in self.phrase)
        phrase_list = cleaned_phrase.split()
        print(phrase_list)
        
        final_text = text.lower()
        print(final_text)
        cleaned_text = ''.join(' ' if char in string.punctuation else char for char in final_text)
        print(cleaned_text)
        text_list = cleaned_text.split() 
        print(text_list)
        
        i = 0
        j = 0

        while i < len(phrase_list) and j < len(text_list):
            if text_list[j] == phrase_list[i]:
                i += 1
            j += 1
    
        first_index = text_list.index(phrase_list[0])
        last_index = text_list.index(phrase_list[-1])
        return last_index - first_index == len(phrase_list) - 1
            
        
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story : NewsStory):
        return PhraseTrigger.is_phrase_in(self, story.title)

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story : NewsStory):
        return PhraseTrigger.is_phrase_in(self, story.description)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, date):
        Trigger.__init__(self)
        self.date = datetime.strptime(date, '%d %b %Y %H:%M:%S').replace(tzinfo=pytz.timezone('EST'))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __init__(self, date):
        TimeTrigger.__init__(self, date)
        
    def evaluate(self, story: NewsStory):
        return self.date > story.get_pubdate().replace(tzinfo=pytz.timezone('EST'))
    
class AfterTrigger(TimeTrigger):
    def __init__(self, date):
        TimeTrigger.__init__(self, date)
        
    def evaluate(self, story: NewsStory):
        return self.date < story.get_pubdate().replace(tzinfo=pytz.timezone('EST'))
       
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger : Trigger):
        Trigger.__init__(self)
        self.trigger = trigger
        
    def evaluate(self, story: NewsStory):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger_1 : Trigger, trigger_2 : Trigger):
        Trigger.__init__(self)
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
        
    def evaluate(self, story: NewsStory):
        return self.trigger_2.evaluate(story) and self.trigger_1.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger_1 : Trigger, trigger_2 : Trigger):
        Trigger.__init__(self)
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
        
    def evaluate(self, story: NewsStory):
        return self.trigger_2.evaluate(story) or self.trigger_1.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                filtered_stories.append(story)
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_dict = {}
    triggerlist = []
    for line in lines:
        args = line.split(',')
        if (args[0] == 'ADD'):
            for trigger_name in args[1 : ]:
                triggerlist.append(trigger_dict[trigger_name])
        else:
            trigger_name = args[0]
            trigger_type = args[1]
            
        if trigger_type == 'TITLE':
            trigger_dict[trigger_name] = TitleTrigger(args[2])
            
        if trigger_type == 'DESCRIPTION':
            trigger_dict[trigger_name] = DescriptionTrigger(args[2])
            
        if trigger_type == 'AFTER':
            trigger_dict[trigger_name] = AfterTrigger(args[2])
            
        if trigger_type == 'AND':
            t1 = trigger_dict[args[2]]
            t2 = trigger_dict[args[3]]
            trigger_dict[trigger_name] = AndTrigger(t1, t2)
            
        if trigger_type == 'OR':
            t1 = trigger_dict[args[2]]
            t2 = trigger_dict[args[3]]
            trigger_dict[trigger_name] = OrTrigger(t1, t2)
        
        if trigger_type == 'NOT':
            t = trigger_dict[args[2]]
            trigger_dict[trigger_name] = NotTrigger(t)
            
        if trigger_type == 'BEFORE':
            trigger_dict[trigger_name] = BeforeTrigger(args[2])

    return triggerlist
    
filename = 'Problem Sets\\pset_5\\triggers.txt'

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config(filename)
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

