#!/usr/bin/env python
#coding:gbk
from lucene import \
    QueryParser, IndexSearcher, StandardAnalyzer, SimpleFSDirectory, File, \
    VERSION, initVM, Version, BooleanQuery, BooleanClause
import lucene
import jieba


"""
This script is loosely based on the Lucene (java implementation) demo class
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""

def run(command,searcher, analyzer):
    #while True:
        #print
        #print "Hit enter with no input to quit."
        #command = raw_input("Query:")
        #command = unicode(command,'gbk')
        command = command.decode('utf-8')
        if command == '':
            return

        #print
        #print "Searching for:",
        querys = BooleanQuery()
        for i in jieba.cut(command):
            #print i,
            query = QueryParser(Version.LUCENE_CURRENT, "contents",
                            analyzer).parse(i)
            querys.add(query, BooleanClause.Occur.MUST)
        scoreDocs = searcher.search(querys, 50).scoreDocs

        #print "\n%s total matching documents." % len(scoreDocs)
        list1 = []
        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            list1.append(doc)
        return list1
        #    print 'path:', doc.get("path"),'title:',doc.get('title'),\
        #    'url:',doc.get('url'),'name:', doc.get("name")

vm_env = 0
#if __name__ == '__main__':
def begining(command):
    STORE_DIR = "index"
    global vm_env
    vm_env = initVM()
    vm_env.attachCurrentThread()
    #print 'lucene', VERSION
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(directory, True)
    analyzer = lucene.WhitespaceAnalyzer(Version.LUCENE_CURRENT)
    a = run(command, searcher, analyzer)
    searcher.close()
    return a
