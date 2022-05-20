def user_can_add_aula(user):
    return user.has_perm('aula.add_aula')
