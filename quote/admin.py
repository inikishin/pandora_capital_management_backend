from django.contrib import admin
from .models import Quote, Market, Ticker, MarketType, Timeframe, StockExchange, BondAdditionalInfo, ShareAdditionalInfo, Currency

admin.site.register(Quote)
admin.site.register(Market)
admin.site.register(Ticker)
admin.site.register(MarketType)
admin.site.register(Timeframe)
admin.site.register(StockExchange)
admin.site.register(BondAdditionalInfo)
admin.site.register(ShareAdditionalInfo)
admin.site.register(Currency)
