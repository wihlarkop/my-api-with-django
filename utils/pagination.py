from django.conf import settings


def get_page_limit_offset_from_limit_page(request):
    limit = request.GET.get('limit')
    if limit and limit.isnumeric():
        limit = int(limit)
        if limit > settings.LIMIT:
            limit = settings.MAX_LIMIT
        elif limit < 1:
            limit = settings.DEFAULT_LIMIT
    else:
        limit = settings.DEFAULT_LIMIT

    page = request.GET.get('page')
    if page and page.isnumeric():
        page = int(page)
        if page < 1:
            page = 1
    else:
        page = 1

    offset = (page - 1) * limit

    return page, limit, offset
