class Registry:
    plugins = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

class MyPlugin(Registry): pass
print(Registry.plugins) # [<class '__main__.MyPlugin'>]