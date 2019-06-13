from mediawiki import MediaWiki;
wikipedia=MediaWiki(lang='ka');

citysubcats = ['კატეგორია:ქალაქები_ქვეყნების_მიხედვით']
while citysubcats:
	subsubcats = []
	for subcat in citysubcats:
		subcat = subcat[len('კატეგორია:'):]
		#print('SUBCAT', subcat)
		citypages, ssc=wikipedia.categorymembers(subcat, subcategories=True);
		subsubcats.extend(ssc)
		for citypage in citypages:
			print(citypage)
	citysubcats = subsubcats
