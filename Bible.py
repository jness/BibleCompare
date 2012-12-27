from xml.dom import minidom
from collections import OrderedDict

class Bible(object):
    
    def __init__(self, xml):
        self.dom = minidom.parse(xml)
        self.__build()
        
    def __build(self):
        '''Build a Bible Dict'''
        self.bible = OrderedDict()
        for book, book_object in self._getBooks():
            self.bible[book] = OrderedDict()
            for chapter, chapter_object in self._getChapters(book_object):
                self.bible[book][chapter] = OrderedDict()
                for verse, body in self._getVerses(chapter_object):
                    self.bible[book][chapter][verse] = body
        
    def _getBooks(self):
        '''Return a list of Books with Dict objects'''
        books = self.dom.getElementsByTagName('book')
        return [ (i.getAttribute('name'), i) for i in books ]
    
    def _getChapters(self, book):
        '''Get the chapters for a Book'''
        chapters = book.getElementsByTagName('chapter')
        return [ (i.getAttribute('name'), i) for i in chapters ]
    
    def _getVerses(self, chapter):
        '''Get the verses in a chapter'''
        verses = chapter.getElementsByTagName('verse')
        return [ (i.getAttribute('name'), i.firstChild.nodeValue) for i in verses ]