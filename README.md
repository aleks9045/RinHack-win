# Регистрация с помощью jwt токена
Сайт доступен по адресу
# 85.192.41.43
# Все пути:</br>
admin/ </br>
auth/ ^users/$</br>
auth/ ^users\.(?P<format>[a-z0-9]+)/?$ </br>
auth/ ^users/activation/$</br>
auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/me/$</br>
auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/resend_activation/$</br>
auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/reset_password/$</br>
auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/reset_password_confirm/$</br>
auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/reset_username/$</br>
auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/reset_username_confirm/$</br>
auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/set_password/$</br>
auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/set_username/$</br>
auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^users/(?P<id>[^/.]+)/$</br>
auth/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^$</br>
auth/ ^\.(?P<format>[a-z0-9]+)/?$</br>
auth/ ^jwt/create/?</br>
auth/ ^jwt/refresh/?</br>
auth/ ^jwt/verify/?</br>
</br>

# Разрешения
'activation': AllowAny</br>
'password_reset': AllowAny</br>
'password_reset_confirm': AllowAny</br>
'set_password': CurrentUserOrAdmin</br>
'username_reset': AllowAny</br>
'username_reset_confirm': AllowAny</br>
'set_username': CurrentUserOrAdmin</br>
'user_create': AllowAny</br>
'user_delete': CurrentUserOrAdmin</br>
'user': CurrentUserOrAdmin</br>
'user_list': CurrentUserOrAdmin</br>
'token_create': AllowAny</br>
'token_destroy': IsAuthenticated</br>
</br>
# RinHack
