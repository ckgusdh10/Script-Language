from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import urllib
from xml.sax import handler, parseString

xmlFD = -1
BooksDoc = None

def LoadXMLFile():
    fileName = str(input("please input file name to load :"))
    global xmlFD, BooksDoc
    try:
        xmlFD = open(fileName)
        #xmlFD = unicode(xmlFD, 'euc-kr').encode('utf-8')
    except IOError:
        print("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print("loading fail!!!")
        else:
            print("XML Document loading complete")
            BooksDoc = dom
            return dom
    return None

def PrintXML():
    if checkDocument():
        print(BooksDoc.toxml())

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()

def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True
