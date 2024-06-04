from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value):
    return censor_bad_words(value)


def censor_bad_words(text):
    bad_word = "редиска"
    censored_text = text.replace(bad_word, bad_word[0] + "*" * (len(bad_word) - 1))
    return censored_text
