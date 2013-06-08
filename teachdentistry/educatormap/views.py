from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required


@login_required
@render_to('educatormap/map.html')
def interactive_map(request):
    return dict()
