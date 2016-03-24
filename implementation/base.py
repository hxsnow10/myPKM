# encoding=utf-8
'''
一方面，现在应用太多了，无论是输入的，处理的，还是输出的；
另外，人工智能处理技术的发展, 推动重构知识的管理；
所以我建了这个项目，作为新型知识管理的尝试

常见的信息源：
个人evernote,可以写
google，搜索引擎
一个格式化的输出源rss
一个非格式化的网站
arxiv:论文数据库
本地数据库
'''
'''
TODO:另外，很多知识不是文章的粒度的，比如说deeplearning相关的一个
mailing list是xxxxx@.com. 这个信息可以添加几个标签，但它不好用文章来形容。
信息提取与表示是很重要的一环。有意思的是，现在的NLP对信息提取已经很有力量了。

所以说知识库如果要搜索maillist,那么你最好提前把那个信息提取好，至少定位好
'''

from abc import ABCMeta

class knowledge_system(ABCMeta):
    '''
    a abstract class for knowlege system.
    '''
    def __init__(self, name='', url='', ):
        self.name=name
        self.url=url
        self.author=author
        self.description=description
        self.updated_time=updated_time
        self.rights=['read']
        self.knowlege_base=self.get_knowlege_base(url)
    

    def get_knowlege_base(url):
        pass

    def write_to():
        
class knowledge_base():
    '''
    knowledge_base有很多不同的表达形式。
    '''
    def __init__():
        # 组织文章与tag的关系
        # 将里面的信息映射到数据库中。

    def answer(query):

    def find_faults(content):

    def report_faults():

    def write():

    def uodate_article()

class article():
    '''
    base class for article.
    '''
    def __init__(title='', author=, build_time, update_time, tags=[], 
            description, ):


#----------------------------------------------------------------
# 标签+文章
# 我记得我做过一个NLP项目：新闻专题生成，和这个很类似。
# DCKMS也能在语义上组织，即一堆数据可以在多个维度上观察组织。
# 标签形成一棵树，所谓标签就是最概括的语义。
# 文章会对应一些标签

class tag_based_knowledge_base(knowledge_base):
    
    def __init__(self, tags, articles):
        self.tags=tags
        self.articles=articles
    
class Systems_Manage_Interface(knowledge_system):
    '''
    将个人关注的许多信息源集中在一起,这其实不改变原本的knowledge_system性质
    就是作为一个一致的界面，需要一些多出来的方法。
    有个问题在于：是把每个源单独作为knowledge_system形成一个List，还是融合成一个新的？
    '''
    
    def __init__():
        
    def update()

    def search()
    
    def write_to()

        
class tag():
    '''
    '''
    def __init__(name='',description='', children, parents, brothers, syms, similar):

class tag_system():
    '''
    may not general tree.
    init through:
        1. extraction from wikipedia: general knowledge tah_tree
        2. biuld from url: node_specific tag_tree
    tag may be different types, include topic, location, time...
    tag_system be may represent by 不同粒度
    tag_system 可以直接类似wikipedia, 也可以按向量表示
    '''
    def __init__():
        pass

    def add()

    def plot()
    
        


        
# 
 

###这版本计划

