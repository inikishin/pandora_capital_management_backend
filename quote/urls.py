from rest_framework import routers
from .views import CurrencyViewSet, QuoteViewSet, TickerViewSet, StockExchangeViewSet, TimeframeViewSet, MarketViewSet, MarketTypeViewSet, BondAdditionalInfoViewSet, ShareAdditionalInfoViewSet

router = routers.DefaultRouter()
router.register(r'currency', CurrencyViewSet)
router.register(r'quotes', QuoteViewSet)
router.register(r'tickers', TickerViewSet)
router.register(r'stock-exchanges', StockExchangeViewSet)
router.register(r'timeframes', TimeframeViewSet)
router.register(r'markets', MarketViewSet)
router.register(r'market-types', MarketTypeViewSet)
router.register(r'bonds-additional-info', BondAdditionalInfoViewSet)
router.register(r'shares-additional-info', ShareAdditionalInfoViewSet)
