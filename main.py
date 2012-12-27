from Bible import Bible
from simplediff import html_diff

# open our two bibles 
kjv = Bible('bibles/kjv.xml')
nkjv = Bible('bibles/nkjv.xml')

extension = '.mdown'
directory = './kjv_vs_nkjv/'

# go in order through all books, chapters, verses
for book in kjv.bible:
    print 'opening %s%s.html for writing' % (directory, book)
    f = open('%s%s%s' % (directory, book, extension), 'w')
    for chapter in kjv.bible[book]:
        for verse in kjv.bible[book][chapter]:
            kjv_body = kjv.bible[book][chapter][verse]
            nkjv_body = nkjv.bible[book][chapter][verse]
            
            # Only print is something is differnt
            if kjv_body != nkjv_body:
                data = '<p><b>[%s %s:%s]</b> %s</p>' % \
                    (book, chapter, verse, html_diff(kjv_body, nkjv_body))
                f.write(data)
    f.close()
