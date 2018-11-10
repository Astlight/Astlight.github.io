import os
import tkinter


class Hexo:
    def __init__(self, blog_path):
        self.path = blog_path
        self.root = tkinter.Tk()
        self.show()

    def show(self):
        self.root.geometry("200x170+400+300")  # 创建200×170大的窗口,并移动到屏幕400,300位置
        self.root.overrideredirect(True)  # 无边框启动

        label_1 = tkinter.Label(self.root, text='标题')  # 文本
        label_1.pack()
        title_text = tkinter.Entry(relief='flat')  # 输入框
        title_text.pack()

        label_2 = tkinter.Label(self.root, text='标签')
        label_2.pack()
        tags_text = tkinter.Entry(relief='flat')
        tags_text.pack()

        label_3 = tkinter.Label(self.root, text='分类')
        label_3.pack()
        cats_text = tkinter.Entry(relief='flat')
        cats_text.pack()

        fm = tkinter.Frame(self.root)
        create_btn = tkinter.Button(fm, text='创建', command=lambda: self.create_blog(title_text, tags_text,
                                                                                    cats_text))  # 按钮,绑定创建文章的激活函数
        create_btn.pack(side=tkinter.LEFT, padx=10)

        exit_btn = tkinter.Button(fm, text='退出', command=lambda: os._exit(0))
        exit_btn.pack(side=tkinter.RIGHT, padx=10)
        fm.pack()

        # 为窗口绑定无界面时可拖动的相关函数
        self.root.bind("<B1-Motion>", self.move)
        self.root.bind("<Button-1>", self.button_1)

        self.root.mainloop()

    def create_blog(self, title_text, tags_text, cats_text):
        title = title_text.get()
        tags = [tag for tag in tags_text.get().split(' ') if tag != '']
        cats = [cat for cat in cats_text.get().split(' ') if cat != '']

        # 创建文章
        os.chdir(self.path)
        os.system('hexo n %s ' % title)

        # 为文章加上标签和分类
        os.chdir('.\source\_posts')
        with open('./%s.md' % title, 'rb') as f:
            md = f.read().decode()

        md = md.replace('tags:', 'tags: %s' % tags)
        md = md.replace('categories:', 'categories: %s' % cats)

        with open('./' + title + '.md', 'wb') as f:
            f.write(md.encode())

        # 创建成功弹窗
        warn = tkinter.Toplevel()
        warn.geometry("260x110+650+300")
        tkinter.Label(warn, text='').pack()  # 来个空白好看

        warn_label = tkinter.Label(warn, text='新文章创建成功!')
        warn_label.pack()

        tkinter.Label(warn, text='').pack()  # 来个空白好看

        fm = tkinter.Frame(warn)

        tkinter.Button(fm, text='打开文件并退出', command=lambda: self.open_new(title)).pack(side=tkinter.LEFT, padx=10)
        tkinter.Button(fm, text='继续创建', command=lambda: warn.destroy()).pack(side=tkinter.LEFT, padx=10)
        tkinter.Button(fm, text='退出', command=lambda: os._exit(0)).pack(side=tkinter.LEFT, padx=10)
        fm.pack()

    def open_new(self, file_name):
        os.startfile(file_name + '.md')
        os._exit(0)

    def button_1(self, event):
        global x, y
        x, y = event.x, event.y

    def move(self, event):
        global x, y
        new_x = (event.x - x) + self.root.winfo_x()
        new_y = (event.y - y) + self.root.winfo_y()
        s = "200x170+" + str(new_x) + "+" + str(new_y)
        self.root.geometry(s)


if __name__ == '__main__':
    Hexo('E:\Hexo')  # 填上自己的博客文件夹路径,多个标签或分类以空格分隔即可
