from mediawiki import MediaWiki;
wikipedia=MediaWiki(lang='ka');
list_of_city_by_country=wikipedia.categorymembers('ქალაქები_ქვეყნების_მიხედვით');
#print ( list_of_city_by_country)
for subcat in list_of_city_by_country[1]:
    print (wikipedia.categorymembers(subcat.replace('კატეგორია:',''),results=30, subcategories=False));
