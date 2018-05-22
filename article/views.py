#  -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage,PageNotAnInteger

# Create your views here.

#实现全局变量
def globl_init(request):
    # 取新闻分类
    category_list = Category.objects.all()
    # 取热门新闻
    hot_articles = Article.objects.filter(is_active=True)[0:5]
    # 取广告数据
    ad_list = Ad.objects.all()

    return locals() #返回字典
#根据一级栏目类型取新闻列表
def index(request):
    # #实现首页 去新闻分类 导航栏 取新闻分类
    # category_list = Category.objects.all()   #将表中数据全部取出，生成一个object赋值给一个对象
    #取新闻列表
    article_list =Article.objects.all()
    # # #取热门新闻
    # hot_articles = Article.objects.filter(is_active=True)[0:5] #取热点新闻5条
    # #
    # # #取广告数据
    # ad_list = Ad.objects.all()
    # context={
    #     'category_list':category_list,
    #     'article_list': article_list,
    #     'hot_articles': hot_articles,
    #     'ad_list': ad_list,
    # }
    # return  render(request,'index.html',context)
    return render(request, 'index.html', locals())


def category(request):
    categoryid = request.GET.get('cid')
    # 取二级栏目
    items_list = Item.objects.filter(article_category=categoryid)
    # 取新闻
    article_list = Article.objects.filter(item__article_category=categoryid)
    article_list = get_page(request,article_list)   #实现分页
    curr_url= request.get_full_path()[0:16]
    return render(request,'category.html',locals())

#根据二级栏目类型取新闻列表
def item(request):
    categoryid = request.GET.get('cid')
    itemid=request.GET.get('itemid')
    # 取二级栏目
    items_list = Item.objects.filter(article_category=categoryid)
    # 取新闻
    article_list = Article.objects.filter(item=itemid)
    article_list = get_page(request, article_list)
    curr_url = request.get_full_path()[0:21]
    return render(request, 'category.html', locals())
# 按标签查询对应的文章列表
def tag(request):
    tagid = request.GET.get('tagid')        #取出标签ID
    article_list = Article.objects.filter(tags=tagid)   #
    article_list = get_page(request, article_list)
    curr_url=request.get_full_path()[0:13]
    return render(request,'tag.html',locals())

def article(request):
    id = request.GET.get('id')
    article = Article.objects.get(id=id)

    # # 取新闻分类
    # category_list = Category.objects.all()
    # # 取热门新闻
    # hot_articles = Article.objects.filter(is_active=True)[0:5]
    #
    # # 取广告数据
    # ad_list = Ad.objects.all()

    # context = {
    #     'article':article,
    #     'category_list': category_list,
    #     'hot_articles': hot_articles,
    #     'ad_list': ad_list,
    # }
    # return render(request, 'index.html', context)
    return render(request,'article.html',locals())

def search(request):
    strquery = request.GET.get('query')     #查询条件 字符串  使用get方法获取来
    article_list=Article.objects.filter(title__contains=strquery)   #标题包含文字搜索内容
    # # print article_list.query
    # # 取新闻分类
    # category_list = Category.objects.all()
    # # 取热门新闻
    # hot_articles = Article.objects.filter(is_active=True)[0:5]
    # context={
    #     'category_list': category_list,
    #     'article_list': article_list,
    #     'hot_articles': hot_articles,
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html', locals())

def get_page(request,object_list):

    '''
       Paginator是如何工作的：
       我们使用希望在每页中显示的对象的数量来实例化Paginator类。
       我们获取到page GET参数来指明页数
       我们通过调用Paginator的 page()方法在期望的页面中获得了对象。
       如果page参数不是一个整数，我们就返回第一页的结果。如果这个参数数字超出了最大的页数，我们就展示最后一页的结果。
       我们传递页数并且获取对象给这个模板（template）。
       :param request:
       :param object_list:
       :return: object_list
       '''
    pagesize = 1    #每页显示的页数
    paginator = Paginator(object_list, pagesize)
    try:
        page = int(request.GET.get('page', 1))
        object_list = paginator.page(page)
        # print article_list
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        object_list = paginator.page(1)
    return object_list


