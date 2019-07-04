# 可以传参数的装饰器
# def html_tags(tag_name):
def html_tags(tag_name):
    # def wrapper_(func):
    def wrapper_(func):
        # def wrapper(*args, **kwargs):
        def wrapper(*args, **kwargs):
            # content = func(*args, **kwargs)
            content = func(*args, **kwargs)
            # return "{tag} {content} {tag}".format(tag=tag_name, content=content)
            return "{tag}{content}{tag}".format(tag=tag_name, content=content)
        # return wrapper
        return wrapper
    # return wrapper_
    return wrapper_

# @html_tags('bbb')  # 先执行html_tags('bbb')，然后和 @+返回的函数体(wrapper_)
@html_tags('bbb') #
# def hello(name='Toby'):
def hello(name='Toby'):
    # return 'Hello {}!'.format(name)
    return 'Hello {}！'.format(name)

# 被装饰器装饰的函数，已经不是它本身了。例如 上边的hello 已经代表wrapper
# 被装饰器装饰的函数，已经不是它本身了。例如 上边的hello 已经代表wrapper


# print(hello.__name__)
print(hello.__name__)
# print(hello(name='tom'))
print(hello(name='tom'))