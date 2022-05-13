from django.contrib import messages

# def logged_in_message(sender, user, request, **kwargs):
#     """
#         Mostra mensagem de sucesso ao fazer login
#     """
#     messages.success(request, "Login realizado com sucesso, {}".format(user.get_full_name()))

def login_failed_message(sender, credentials, request, **kwargs):
    """
        Mostra mensagem de warning ao falhar o login
    """
    messages.warning(request, 'Usuário ou Senha incorretos.')

def logout_message(sender, request, user, **kwargs):
    """
        Mostra mensagem sucesso ao fazer logout
    """
    messages.info(request, 'Você fez logout, {}.'.format(user.get_short_name()))
