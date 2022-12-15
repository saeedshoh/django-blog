from django import template
from blog.models import Post, Tag

register = template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def popular_posts(cnt = 3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}

@register.inclusion_tag('blog/tags_tpl.html')
def tags(cnt = 10):
    tags = Tag.objects.all()
    return {"tags": tags}