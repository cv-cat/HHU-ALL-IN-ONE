# 将ck_str转换为ck_dict
def trans_cookies(cookies_str):
    return {i.split('=')[0]: '='.join(i.split('=')[1:]) for i in cookies_str.split('; ')}


# 将ck_dict转换为ck_str
def str_cookies(cookies_dict):
    cookies = '; '.join([f'{k}={v}' for k, v in cookies_dict.items()])
    return cookies


