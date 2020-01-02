from app.models import NewsItem, Text


def common(request):
    context = {
                'news': NewsItem.objects.filter(published=True).order_by('created')[:3],
               }
    for t in Text.objects.all():
        context['text_'+t.key] = t.text
    return context