'''
	betsy: new web bot spider/crawler 
'''

'''some project TODO'''
import re

''' this extend regex class; we have to parse html page 
    for <a> tag links (basic version) 
'''
class betsy_bot(re): 

	
	'''this parse a html page and pick up any links related'''
	def get_links(self, url): 
		pass

	'''this implements a kind of dfs engine '''
	def crawl_deep(self, urls): 
		pass 
	
	
if __name__ == "___main__": 
	print "Betsy say you Hi!"
		
	print "[B] Gimme a url"
	
