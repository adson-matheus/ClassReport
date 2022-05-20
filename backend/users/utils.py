from django.contrib.auth.models import Group

def is_admin(request):
    group = Group.objects.get(name='grp_administradores')
    if group in request.user.groups.all():
        return {'is_admin':True}
    else: return {'is_admin':False}
