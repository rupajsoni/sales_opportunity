#read the sentiments, counts, twitter sentiments, counts
# find their headers

sentiments_csv = open('/home/vivek/Desktop/sales_opportunity/code/sentiments.csv', 'r')
twitter_sentiments_csv = open('/home/vivek/Desktop/sales_opportunity/code/twitter_sentiments.csv', 'r')
counts_csv = open('/home/vivek/Desktop/sales_opportunity/code/counts.csv', 'r')
twitter_counts_csv = open('/home/vivek/Desktop/sales_opportunity/code/twitter_counts.csv', 'r')


def extract_dictionaries(inputfile):
	lineno = 0
	features = set()
	feature_s = []
	sentiment = {}
	phone = None
	for line in inputfile :
		if len(line) > 0: 
			fs = line.split("\n")[0].split(",")
			if lineno == 0 :
				for f in fs:
					if f != "phones" :
						features.add(f)
						feature_s.append(f)
			else :
				l = 0
				for f in fs:
					if l == 0:
						sentiment[f] = {}
						phone = f
					else :
						sentiment[phone][feature_s[l-1]] = f
					l += 1
			lineno += 1
	print sentiment
	return features, sentiment

def get_values(exp_price, features_input) :
	print "A"
	ln_f, ln_sentiments = extract_dictionaries(sentiments_csv)
	ln_f1, ln_counts = extract_dictionaries(counts_csv)

	t_f, t_sentiments = extract_dictionaries(twitter_sentiments_csv)
	t_f1, t_counts = extract_dictionaries(twitter_counts_csv)

	features = ln_f
	for f in ln_f1 :
		features.add(f)
	for f in t_f :
		features.add(f)
	for f in t_f1 :
		features.add(f)

	phones = ln_sentiments.keys()
	return ln_f
	'''
	unwanted_phones = []
	for phone in phones :
		print phone['price']
		phone_price = int(phone['price'])
		if phone_price > exp_price + 50 or phone_price < exp_price - 50 :
			unwanted_phones.append(phone)
	
	for p in unwanted_phones :
		phones.remove(p)
		
	feature_phones = {}
	#for each feature, find the max sentiment for each phone
	for feature in features_input :
		max_sentiment = 0
		max_senti_phone = None
		for phone in phones :
			if max_senti_phone is None :
				max_senti_phone = phone
				max_sentiment = features[phone][feature]
			elif features[phone][feature] > max_sentiment :
				max_sentiment = features[phone][feature]
				max_senti_phone = phone
		feature_phones[feature] = max_senti_phone
	
	print feature_phones
	'''
