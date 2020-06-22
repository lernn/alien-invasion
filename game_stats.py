class GameStats():
    def __init__(self, ai_settings):
        self.ai_setting = ai_settings
        self.reset_stats()   #为什么是self.   在构造函数中调用方法
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.ai_setting.ship_limt
