from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import config as config
from pinterest import Pinterest
import time 
import random

# Log in to Pinterest
pinterest = Pinterest(username_or_email='bryanmorganoverbey@gmail.com', password=config.ebay['pinPass'])
logged_in = pinterest.login()
print('Successfully logged in to Pinterest... \n')
# Create Ebay Constructor
api = Finding(config_file='ebay.yaml', siteid="EBAY-US", )
print('Successfully logged in to Ebay API... \n')
# Define a list of keywords for a search
infile = open('keywords.txt', 'r')
# For item in keyword list:
for line in infile:
	# Do a search
    try:
        products = api.execute('findItemsAdvanced', {'keywords': line, 'affiliate': {'trackingId':config.ebay['trackingid'], 'networkId':'9'}})
        print('Successfully Generated Product list based on search term: \'' + line + '\'... \n')
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        print("got here 1")
        pass
	# For item in search return list
    try:
        print('Generating ads from search results... \n')
        for product in products.reply.searchResult.item:
			print("Title: " + product.title + " , Price: " + product.sellingStatus.currentPrice.value)
			try:
				# Make Add
				pin = pinterest.pin(
					board_id='460282093105823109',   # need to change this to be a new ebay board
					image_url = product.galleryURL,
					description = product.sellingStatus.currentPrice.value + ' | ' + product.title,
					link = product.viewItemURL)  # need to change this to be my affiliate link
				# print(product.detail_page_url)
				time.sleep(random.randint(60,120))
			except:
				print("got here 2")
				pass
    except:
		print("got here 3: " + line)
		pass



# 'itemId': '401445354806', 'isMultiVariationListing': 'true', 'topRatedListing': 'false', 'globalId': 'EBAY-US', 
# 'title': "Fashion Lord of the Rings The One Ring Lotr Stainless Steel Men's Ring Size 6-12", 'country': 'US', 
# 'shippingInfo': {'expeditedShipping': 'true', 'shipToLocations': 'Worldwide', 'shippingServiceCost': {'_currencyId': 'USD', 'value': '0.0'}, 
# 'oneDayShippingAvailable': 'true', 'handlingTime': '1', 'shippingType': 'Free'}, 'secondaryCategory': {'categoryId': '137856', 'categoryName': 'Rings'},
#  'autoPay': 'false', 'sellingStatus': {'currentPrice': {'_currencyId': 'USD', 'value': '4.99'}, 'timeLeft': 'P18DT7H56M27S',
#  'convertedCurrentPrice': {'_currencyId': 'USD', 'value': '4.99'}, 'sellingState': 'Active'}, 'location': 'Norcross,GA,USA', 'postalCode': '300**', 
# 'returnsAccepted': 'true', 'viewItemURL': 'https://www.ebay.com/itm/Fashion-Lord-Rings-One-Ring-Lotr-Stainless-Steel-Mens-Ring-Size-6-12-/401445354806?var=671098959182', 
# 'galleryURL': 'https://thumbs3.ebaystatic.com/pict/401445354806404000000001_2.jpg', 'paymentMethod': 'PayPal', 'primaryCategory': {'categoryId': '67681', 'categoryName': 'Rings'},
#  'condition': {'conditionId': '1500', 'conditionDisplayName': 'New without tags'}, 
# 'listingInfo': {'listingType': 'FixedPrice', 'gift': 'false', 'bestOfferEnabled': 'false', 'watchCount': '8',
#  'startTime': datetime.datetime(2017, 11, 20, 8, 30, 55), 'buyItNowAvailable': 'false', 
# 'endTime': datetime.datetime(2019, 12, 20, 8, 30, 55)}}], '_count': '100'}, 'version': '1.13.0'}