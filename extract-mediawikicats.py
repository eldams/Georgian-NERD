from mediawiki import MediaWiki;
wikipedia=MediaWiki(lang='ka');

catprefix = 'კატეგორია:'
entitycats = {
	'loc.cities': 'ქალაქები_ქვეყნების_მიხედვით',
	'loc.countries.africa' : 'აფრიკის ქვეყნები',
	'loc.countries.asia' : 'აზიის ქვეყნები',
	'loc.countries.europe' : 'ევროპის ქვეყნები',
	'loc.countries.america.north' : 'ჩრდილოეთ ამერიკის ქვეყნები',
	'loc.countries.oceania' : 'ოკეანეთის ქვეყნები',
	'loc.countries.america.south' : 'სამხრეთ ამერიკის ქვეყნები',
}

for entitycat in entitycats:
	catnames = [catprefix+entitycats[entitycat]]
	while catnames:
		allsubcats = []
		for catname in catnames:
			catname = catname[len(catprefix):]
			entitypages, subcats=wikipedia.categorymembers(catname, subcategories=True);
			allsubcats.extend(subcats)
			for entitypage in entitypages:
				print(entitypage+','+catname)
		catnames = allsubcats
