class MsgTemplate:
    def __init__(self, template):
        self.template = template

    def create(self, *arg):
        return self.template.format(*arg)

if __name__ == '__main__':
    t = MsgTemplate('{0}時の{1}は{2}')
    msg = t.create(12, '気温', 22.4)

    print(msg)