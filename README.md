js-inspect.py
=============

this is really silly. it literally just pulls all(?) named functions out of a javascript file.

Example
-------

	rolands@kamaji:~/utils/js-inspect$ python js-inspect.py ../CommonMark-py/stmd.js
	js-inspect.py - ../CommonMark-py/stmd.js
	[functions]
	        unescape(s)
	        isBlank(s)
	        normalizeReference(s)
	        matchAt(re, s, offset)
	        detabLine(text)
	        match(re)
	        peek()
	        spnl()
	        parseBackticks(inlines)
	        parseEscaped(inlines)
	        parseAutolink(inlines)
	        parseHtmlTag(inlines)
	        scanDelims(c)
	        parseEmphasis(inlines)
	        parseLinkTitle()
	        parseLinkDestination()
	        parseLinkLabel()
	        parseRawLabel(s)
	        parseLink(inlines)
	        parseEntity(inlines)
	        parseString(inlines)
	        parseNewline(inlines)
	        parseImage(inlines)
	        parseReference(s, refmap)
	        parseInline(inlines)
	        parseInlines(s, refmap)
	        InlineParser()
	        makeBlock(tag, start_line, start_column)
	        canContain(parent_type, child_type)
	        acceptsLines(block_type)
	        endsWithBlankLine(block)
	        breakOutOfLists(block, line_number)
	        addLine(ln, offset)
	        addChild(tag, line_number, offset)
	        parseListMarker(ln, offset)
	        listsMatch(list_data, item_data)
	        incorporateLine(ln, line_number)
	        closeUnmatchedBlocks(mythis)
	        finalize(block, line_number)
	        processInlines(block)
	        parse(input)
	        DocParser()
	        inTags(tag, attribs, contents, selfclosing)
	        renderInline(inline)
	        renderInlines(inlines)
	        renderBlock(block, in_tight_list)
	        renderBlocks(blocks, in_tight_list)
	        HtmlRenderer()
	        escape(s, preserve_entities)

