# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from linkedin.spreadsheet import updatevalues

if __name__ == '__main__':
    main()

class LinkedinPipeline(object):


    def open_spider(self, spider):
        self.file = open('profile_details_1.json', 'w')

    def close_spider(self, spider):
        self.file.close()    

    def process_item(self, item, spider):

        itemdict = dict(item)
        name = itemdict["name"]
        url = itemdict["url"]
        title = itemdict["title"]
        email = itemdict["email"]

        mylist = [name, url, title, email]
        
        #add data to google spreadsheet.
        updatevalues(mylist)
        line = json.dumps(dict(item)) + "\n"
        
        #Add data to file.
        self.file.write(line)
        return item
