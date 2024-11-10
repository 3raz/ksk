
class MainController:
    def __init__(self, screen, gui, event_manager):
        self.screen = screen
        self.gui = gui
        self.event_manager = event_manager

    def simulatsioon(self):
        while True:
            self.event_manager.process_events()
            self.screen.update()
            self.gui.update()
            self.screen.draw()
            self.gui.draw()
            

if __name__ == "__main__":
    main_controller = MainController()
    main_controller.simulatsioon()