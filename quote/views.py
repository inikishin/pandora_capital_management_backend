from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Market, MarketType, Timeframe, ShareAdditionalInfo, BondAdditionalInfo, Ticker, Quote, Currency, StockExchange
from .serializers import TickerSerializer, MarketSerializer, TimeframeSerializer, MarketTypeSerializer, CurrencySerializer, QuoteSerializer, StockExchangeSerializer, ShareAdditionalInfoSerializer, BondAdditionalInfoSerializer


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class MarketTypeViewSet(viewsets.ModelViewSet):
    queryset = MarketType.objects.all()
    serializer_class = MarketTypeSerializer


class TimeframeViewSet(viewsets.ModelViewSet):
    queryset = Timeframe.objects.all()
    serializer_class = TimeframeSerializer


class ShareAdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = ShareAdditionalInfo.objects.all()
    serializer_class = ShareAdditionalInfoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['ticker']


class BondAdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = BondAdditionalInfo.objects.all()
    serializer_class = BondAdditionalInfoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['ticker', 'short_name']


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['market']
    search_fields = ['code', 'fullname']


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['ticker', 'timeframe', 'datetime']


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class StockExchangeViewSet(viewsets.ModelViewSet):
    queryset = StockExchange.objects.all()
    serializer_class = StockExchangeSerializer
