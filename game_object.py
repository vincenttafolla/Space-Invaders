class GameObject():
    def __init__(self, image, xcor, ycor, initial_direction, initial_speed):
        self.image = image
        self.xcor = xcor
        self.ycor = ycor
        self.direction = initial_direction
        self.speed = initial_speed
        self.is_alive = True
    def show(self, game_display):
        game_display.blit(self.image,(self.xcor, self.ycor))
    def collides_with(self, foreigm_object):
        if self.xcor + self.image.get_width() > foreigm_object.xcor and \
            self.xcor < foreigm_object.xcor + foreigm_object.image.get_width() and \
            self.ycor + self.image.get_height() > foreigm_object.ycor and \
            self.ycor < foreigm_object.ycor + foreigm_object.image.get_height():
            return True
        else:
            return False

