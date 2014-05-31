import markdown
from markdown.inlinepatterns import Pattern
from markdown.util import etree

RE_PULLQ=r"\[([^\]]+)\]\(\+\)"

class PullQuotePattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element('span')
        el.text = m.group(2)
        el.attrib["data-pullquote"] = m.group(2)
        return el

class PullQuoteExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('pullquote', PullQuotePattern(RE_PULLQ), '<link')

def makeExtension(configs=None):
    return PullQuoteExtension(configs=configs)
