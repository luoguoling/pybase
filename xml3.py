__author__ = 'Administrator'
#__*__ coding=utf-8 __*__
from  xml.etree import ElementTree
text1 = "werwe"
filepath = './movies.xml'
tree = ElementTree.parse('./movies.xml')
nodelist = tree.findall("movie/type")
def write_xml(tree,out_path):
    '''将xml文件写出
    tree:xml树
    out_path:写出路径'''
#    tree = ElementTree()
    tree.write(out_path,encoding="utf-8",xml_declaration=True)
def change_node_text(nodelist,text,is_add=False,is_delete=False):
    '''改变/增加/删除一个节点的文本
    nodelist:节点列表
    text:更新后的文本
    '''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
change_node_text(nodelist,text1)
write_xml(tree,"./movies.xml")