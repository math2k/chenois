from app.models import NewsItem


def common(request):
    context = {'news': NewsItem.objects.filter(published=True).order_by('-created')[:3]}
    return context