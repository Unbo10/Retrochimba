import pygame
from sys import exit
import math as m
from moviepy.editor import * 
import random
import datetime

def f1():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((600, 500))
    logo = pygame.image.load("images/logo-title-bar-FC.png").convert_alpha()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Fórmula Chimba")
    clock = pygame.time.Clock()
    Minfont = pygame.font.Font('Minecraft.ttf',40)
    video = VideoFileClip("images/This-is-Formula-One-Pixelated.mp4")
    lap_times = [["Last session", "0:00.000", "0:00.000", "0:00.000", "images/f1-mercedes-softs.png"], ["Best session", "0:00.000", "0:00.000", "0:00.000", "images/f1-ferrari-hards.png"]]

    def get_lap_time(time):
        if time != 0:
            return time
        else:
            return datetime.datetime.now()

    def play_sound(audio, time):
        if time > 0:
            audio.play()

    #Speed = acc + 25m/s
    def acceleration(x_increment, y_increment, acc, fw, rw, deg, angle):
        #  team_name, fw, rw, topspeed, acc, braking, deg, tyre_selected, team_color
        accel = 0
        accel_x = 0
        accel_y = 0
        accel_tuple = [0.0, 0.0]
        if (x_increment != 0):
            accel_x = x_increment * ((5*(fw + rw)) - deg + (10 * acc)) / 400
        if (y_increment > 0):
            accel_y = y_increment * ((5*(fw + rw)) + deg + (10 * acc)) / 400
        if (y_increment < 0):
            accel_y = y_increment * ((5*(fw + rw)) + deg + (10 * acc)) / 100
        accel = m.sqrt((accel_x*accel_x) + (accel_y*accel_y))
        accel_tuple[0] = m.sin(m.radians(angle)) * accel * 3
        accel_tuple[1] = m.cos(m.radians(angle)) * accel
        return accel_tuple

    def reverse(y_increment, aum_y, acc, fw, rw, deg, angle):
        if y_increment >= -7:
            return m.cos(m.radians(angle)) * aum_y * ((5*(fw + rw)) + deg + (10 * acc)) / 100
        else:
            return 0
        
    def menu(video, lap_times):
        current_time = 0

        # play("ferrari", 10, 10, 10, 10, 10, 10, "M", [0, 0, 0])
        car_size = (128, 326)
        pygame.mixer.music.load('audio/This-is-Formula-One-Pixelated-Audio.mp3')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play()
        frame_rate = 25
        current_time = 0
        Minfont_cars = pygame.font.Font('Minecraft.ttf', 16)
        Minfont_title = pygame.font.Font('Minecraft.ttf', 25)

        S_logo = pygame.image.load("images/logo-FC.png").convert_alpha()
        S_logo = pygame.transform.scale(S_logo, (308, 56))
        R_S_logo = S_logo.get_rect(midtop = (300, 13))

        transparent_surface = pygame.Surface((230, 40), pygame.SRCALPHA)
        pygame.draw.rect(transparent_surface, (255, 255, 255, 128), transparent_surface.get_rect())
        R_S_car_text = pygame.Rect(185, 80, 250, 40)
        S_car_text = Minfont_title.render("Choose your car:", None, "Black")

        S_Mercedes = pygame.image.load("images/Mercedes-FC-softs.png").convert_alpha()
        S_Mercedes = pygame.transform.scale(S_Mercedes,car_size)
        R_S_Mercedes = S_Mercedes.get_rect(topleft = (24, 127))
        R_S_text_Mercedes = pygame.Rect(R_S_Mercedes.left, R_S_Mercedes.bottom - 9, car_size[0], 30)
        Mercedes_text = Minfont_cars.render("Mercedes W14", None, "Black")

        S_Ferrari = pygame.image.load("images/Ferrari-FC-softs.png").convert_alpha()
        S_Ferrari = pygame.transform.scale(S_Ferrari, car_size)
        R_S_Ferrari = S_Ferrari.get_rect(midtop = (300, 127))
        R_S_text_Ferrari = pygame.Rect(R_S_Ferrari.left, R_S_Ferrari.bottom - 9, car_size[0], 30)
        Ferrari_text = Minfont_cars.render("Ferrari SF-23", None, "Black")

        S_Mclaren = pygame.image.load("images/McLaren-FC-softs.png").convert_alpha()
        S_Mclaren = pygame.transform.scale(S_Mclaren, car_size)
        R_S_Mclaren = S_Mclaren.get_rect(topright = (577, 127))
        R_S_text_Mclaren = pygame.Rect(R_S_Mclaren.left, R_S_Mclaren.bottom - 9, car_size[0], 30)
        Mclaren_text = Minfont_cars.render("McLaren MCL60", None, "Black")
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            screen.fill((0, 0, 0))
            time_counter = pygame.time.get_ticks()

            if current_time < video.duration:
                video_frame = video.get_frame(current_time)
                pygame_frame = pygame.image.fromstring(video_frame.tobytes(), video.size, "RGB")
                screen.blit(pygame_frame, (0, 0))
                current_time += 1 / frame_rate  # Increment time by 1 frame at the specified frame rate
            else:
                current_time = 0

            if time_counter > 5000:
                mouse_pos = pygame.mouse.get_pos()
                if R_S_Mercedes.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pygame.mixer.music.stop()
                            video.close()
                            car_set_up("mercedes", lap_times)
                if R_S_Ferrari.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pygame.mixer.music.stop()
                            video.close()
                            car_set_up("ferrari", lap_times)  
                if R_S_Mclaren.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pygame.mixer.music.stop()
                            video.close()
                            car_set_up("mclaren",  lap_times)  

                screen.blit(S_logo, R_S_logo)
                screen.blit(transparent_surface, (185, 80))        
                screen.blit(S_car_text, (R_S_car_text.left + 10, R_S_car_text.top + 10))
                pygame.draw.rect(screen, (12, 229, 192), R_S_text_Mercedes) #If you have time, design a curved botton
                screen.blit(Mercedes_text, (R_S_text_Mercedes.left + 12, R_S_text_Mercedes.top + 9))
                pygame.draw.rect(screen, (239, 26, 45), R_S_text_Ferrari) #If you have time, design a curved botton
                screen.blit(Ferrari_text, (R_S_text_Ferrari.left + 12, R_S_text_Ferrari.top + 11))
                pygame.draw.rect(screen, (255, 128, 0), R_S_text_Mclaren) #If you have time, design a curved botton
                screen.blit(Mclaren_text, (R_S_text_Mclaren.left + 2, R_S_text_Mclaren.top + 9))
                screen.blit(S_Mercedes, R_S_Mercedes)
                screen.blit(S_Ferrari, R_S_Ferrari)
                screen.blit(S_Mclaren, R_S_Mclaren)
                

            pygame.display.update()
            clock.tick(25)


    #################################################################################################################       

    # *** SET UP OF THE CAR ***

    def car_set_up (team_name, lap_times):

        screen.fill((0, 0, 0))

        team_color = 0
        team_image = ""
        tyre_size = (90, 54)
        downforce_big_size = (230, 65)
        downforce_small_size = (130, 65)
        increment_size = (35, 35)
        default_fw = 0
        default_rw = 0
        lows_corner = 0
        mids_corner = 0
        highs_corner = 0
        brakes = 0
        click_time = 0
        tyre_deg = 2
        tyre_acceleration = 9
        tyre_braking = 9
        tyre_topspeed = 10
        car_acceleration = 0
        car_deg = 0
        car_braking = 0
        car_topspeed = 0
        mclaren_softs = "images/f1-mclaren-softs.png"
        mclaren_mediums = "images/f1-mclaren-mediums.png"
        mclaren_hards = "images/f1-mclaren-hards.png"
        ferrari_softs = "images/f1-ferrari-softs.png"
        ferrari_mediums = "images/f1-ferrari-mediums.png"
        ferrari_hards = "images/f1-ferrari-hards.png"
        mercedes_softs = "images/f1-mercedes-softs.png"
        mercedes_mediums = "images/f1-mercedes-mediums.png"
        mercedes_hards = "images/f1-mercedes-hards.png"
        chosen_car = ""
        
        Minfont_cars = pygame.font.Font('Minecraft.ttf', 16)
        Minfont_title = pygame.font.Font('Minecraft.ttf', 25)
        Minfont_play = pygame.font.Font('Minecraft.ttf', 21)
        Minfont_play_2 = pygame.font.Font('Minecraft.ttf', 19)
        car_size = (128, 316)

        S_logo = pygame.image.load("images/logo-FC.png").convert_alpha()
        S_logo = pygame.transform.scale(S_logo, (308, 56))
        R_S_logo = S_logo.get_rect(midtop = (300, 13))

        S_back_button = pygame.image.load("images/back-button.png")
        S_back_button = pygame.transform.scale(S_back_button, (56, 56))
        R_S_back_button = S_back_button.get_rect(topleft = (24, R_S_logo.top))

        R_S_title = pygame.Rect(200, R_S_logo.bottom + 25, 250, 40)
        S_title = Minfont_title.render("Set up your car:", None, "White")
            
        if team_name == "mercedes":
            S_car = pygame.image.load("images/Mercedes-FC-softs.png").convert_alpha()
            S_car = pygame.transform.scale(S_car,car_size)
            R_S_car = S_car.get_rect(bottomleft = (24, 456))
            R_S_car_text = pygame.Rect(R_S_car.left, R_S_car.bottom - 9, car_size[0], 30)
            S_car_text = Minfont_cars.render("Mercedes W14", None, "Black")
            team_color = [12, 229, 192]
            team_image = "images/Mercedes-background.jpg"
            team_tyre_placer = "images/Mercedes-tyre-placer.png"
            team_play_button = "images/Mercedes-play-button.png"
            I_car_softs = "images/Mercedes-FC-softs.png"
            I_car_mediums = "images/Mercedes-FC-mediums.png"
            I_car_hards = "images/Mercedes-FC-hards.png"
            default_fw = 9
            default_rw = 7
            lows_corner = 10
            mids_corner = 8
            highs_corner = 7
            brakes = 9
            chosen_car = mercedes_softs

        elif team_name == "ferrari":
            S_car = pygame.image.load("images/Ferrari-FC-softs.png").convert_alpha()
            S_car = pygame.transform.scale(S_car, car_size)
            R_S_car = S_car.get_rect(bottomleft = (24, 456))
            R_S_car_text = pygame.Rect(R_S_car.left, R_S_car.bottom - 9, car_size[0], 30)
            S_car_text = Minfont_cars.render("Ferrari SF-23", None, "Black") 
            team_color = [239, 26, 45]
            team_image = "images/Ferrari-background.png"
            team_tyre_placer = "images/Ferrari-tyre-placer.png"
            team_play_button = "images/Ferrari-play-button.png"
            I_car_softs = "images/Ferrari-FC-softs.png"
            I_car_mediums = "images/Ferrari-FC-mediums.png"
            I_car_hards = "images/Ferrari-FC-hards.png"
            default_fw = 7
            default_rw = 7
            lows_corner = 9
            mids_corner = 8
            highs_corner = 9
            brakes = 8
            chosen_car = ferrari_softs

        elif team_name == "mclaren":
            S_car = pygame.image.load("images/McLaren-FC-softs.png").convert_alpha()
            S_car = pygame.transform.scale(S_car, car_size)
            R_S_car = S_car.get_rect(bottomleft = (24, 456))
            R_S_car_text = pygame.Rect(R_S_car.left, R_S_car.bottom - 9, car_size[0], 30)
            S_car_text = Minfont_cars.render("McLaren MCL60", None, "Black")
            team_color = [255, 128, 0]
            team_image = "images/Mclaren-background.jpg"
            team_tyre_placer = "images/Mclaren-tyre-placer.png"
            team_play_button = "images/Mclaren-play-button.png"
            I_car_softs = "images/McLaren-FC-softs.png"
            I_car_mediums = "images/McLaren-FC-mediums.png"
            I_car_hards = "images/McLaren-FC-hards.png"
            default_fw = 8
            default_rw = 7
            lows_corner = 9
            mids_corner = 10
            highs_corner = 9
            brakes = 7
            chosen_car = mclaren_softs
            
        # Tyre-compounds
        
        S_Tyre_placer = pygame.image.load(team_tyre_placer).convert_alpha()
        S_Tyre_placer = pygame.transform.scale(S_Tyre_placer, (98, car_size[1] + 21))
        R_S_Tyre_placer = S_Tyre_placer.get_rect(topleft = (R_S_car.right - 9, R_S_car.top))

        S_Soft_tyre = pygame.image.load("images/Soft-tyre.png").convert()
        S_Soft_tyre = pygame.transform.scale(S_Soft_tyre, tyre_size)
        S_Soft_tyre = pygame.transform.rotate(S_Soft_tyre, 90)
        R_S_Soft_tyre = S_Soft_tyre.get_rect(topleft = (R_S_car.right + 18, R_S_car.top + 17))

        S_Medium_tyre = pygame.image.load("images/Medium-tyre.png").convert()
        S_Medium_tyre = pygame.transform.scale(S_Medium_tyre, tyre_size)
        S_Medium_tyre = pygame.transform.rotate(S_Medium_tyre, 90)
        R_S_Medium_tyre = S_Soft_tyre.get_rect(topleft = (R_S_car.right + 18, R_S_Soft_tyre.bottom + 17))

        S_Hard_tyre = pygame.image.load("images/Hard-tyre.png").convert()
        S_Hard_tyre = pygame.transform.scale(S_Hard_tyre, tyre_size)
        S_Hard_tyre = pygame.transform.rotate(S_Hard_tyre, 90)
        R_S_Hard_tyre = S_Soft_tyre.get_rect(topleft = (R_S_car.right + 18, R_S_Medium_tyre.bottom + 17))

        S_background = pygame.image.load(team_image).convert_alpha()
        S_background = pygame.transform.scale(S_background, (900, 500))
        S_background.set_alpha(150)
        R_S_background = S_background.get_rect(topleft = (-50, 0))

        team_color_transparent = team_color + [200]
        transparent_surface = pygame.Surface((225, 40), pygame.SRCALPHA)
        
        transparent_surface.fill(team_color_transparent)
        hover_color_s = [120, 120, 120]
        hover_color_m = [180, 180, 180]
        hover_color_h = hover_color_s
        default_hover_color = [180, 180, 180]
        focus_hover_color = [120, 120, 120]
        tyre_selected = "S"

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            screen.fill((0, 0, 0))

            # Mouse position for hover effects
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()

            if (R_S_back_button.collidepoint(mouse_pos_x, mouse_pos_y)):
                if(mouse_buttons[0]):
                    menu(VideoFileClip("images/This-is-Formula-One-Pixelated.mp4"), lap_times)

            if (R_S_car.right + 12 < mouse_pos_x < R_S_Tyre_placer.right - 12):
                if (R_S_car.top + 12 < mouse_pos_y < R_S_Soft_tyre.bottom + 5):
                    hover_color_s = focus_hover_color
                    if (mouse_buttons[0]):
                        tyre_selected = "S"
                elif (R_S_Soft_tyre.bottom + 12 < mouse_pos_y < R_S_Medium_tyre.bottom + 5):
                    hover_color_m = focus_hover_color
                    if (mouse_buttons[0]):
                        tyre_selected = "M"
                elif (R_S_Medium_tyre.bottom + 12 < mouse_pos_y < R_S_Hard_tyre.bottom + 5):
                    hover_color_h = focus_hover_color
                    if (mouse_buttons[0]):
                        tyre_selected = "H"
            else:
                hover_color_s = default_hover_color
                hover_color_m = default_hover_color
                hover_color_h = default_hover_color
                        
            if (tyre_selected == "S"):
                hover_color_s = focus_hover_color
                S_car = pygame.image.load(I_car_softs).convert_alpha()
                S_car = pygame.transform.scale(S_car, car_size)
                tyre_deg = 2
                tyre_acceleration = 9
                tyre_braking = 9
                tyre_topspeed = 10
            elif (tyre_selected == "M"):
                hover_color_m = focus_hover_color
                S_car = pygame.image.load(I_car_mediums).convert_alpha()
                S_car = pygame.transform.scale(S_car, car_size)
                tyre_deg = 5
                tyre_acceleration = 7
                tyre_braking = 8
                tyre_topspeed = 8
            elif (tyre_selected == "H"):
                hover_color_h = focus_hover_color
                S_car = pygame.image.load(I_car_hards).convert_alpha()
                S_car = pygame.transform.scale(S_car, car_size)
                tyre_deg = 9
                tyre_acceleration = 5
                tyre_braking = 6
                tyre_topspeed = 6

            S_Soft_tyre_hover = pygame.Surface((64, 100))
            S_Soft_tyre_hover.fill(hover_color_s)
            R_S_Soft_tyre_hover = S_Soft_tyre_hover.get_rect(topleft = (R_S_Soft_tyre.left - 5, R_S_Soft_tyre.top - 5))

            S_Medium_tyre_hover = pygame.Surface((64, 100))
            S_Medium_tyre_hover.fill(hover_color_m)
            R_S_Medium_tyre_hover = S_Medium_tyre_hover.get_rect(topleft = (R_S_Medium_tyre.left - 5, R_S_Medium_tyre.top - 5))

            S_Hard_tyre_hover = pygame.Surface((64, 100))
            S_Hard_tyre_hover.fill(hover_color_h)
            R_S_Hard_tyre_hover = S_Hard_tyre_hover.get_rect(topleft = (R_S_Hard_tyre.left - 5, R_S_Hard_tyre.top - 5))

            #Car settings

            S_FW_level_placer = pygame.image.load("images/FW-level.png").convert_alpha()
            S_FW_level_placer = pygame.transform.scale(S_FW_level_placer, downforce_big_size)
            R_S_FW_level_placer = S_FW_level_placer.get_rect(midtop = (((R_S_Tyre_placer.right + ((600 - R_S_Tyre_placer.right - 12) / 2)), R_S_Tyre_placer.top)))

            S_FW_text = Minfont_cars.render("Front wing", None, (0, 0, 0))
            R_S_FW_text = S_FW_text.get_rect(topleft = (R_S_FW_level_placer.left + 18, R_S_FW_level_placer.top + 5))
            
            S_FW_level = pygame.Surface(((default_fw*21) + 1, 14))
            S_FW_level.fill(team_color)
            R_S_FW_level = S_FW_level.get_rect(bottomleft = (R_S_FW_level_placer.left + 10, R_S_FW_level_placer.bottom - 13))
            S_FW_level_background = pygame.Surface((210, 14))
            S_FW_level_background.fill((70, 70, 70))

            S_FW_increment = pygame.image.load("images/level-increment.png").convert_alpha()
            S_FW_increment = pygame.transform.scale(S_FW_increment, increment_size)
            R_S_FW_increment = S_FW_increment.get_rect(midleft = (R_S_FW_level_placer.right + 10, R_S_FW_level_placer.bottom - 20))
            S_FW_decrement = pygame.image.load("images/level-decrement.png").convert_alpha()
            S_FW_decrement = pygame.transform.scale(S_FW_decrement, (increment_size[0], 10))
            R_S_FW_decrement = S_FW_decrement.get_rect(midright = (R_S_FW_level_placer.left - 10, R_S_FW_level_placer.bottom - 20))

            S_RW_level_placer = pygame.image.load("images/FW-level.png").convert_alpha()
            S_RW_level_placer = pygame.transform.scale(S_RW_level_placer, downforce_big_size)
            R_S_RW_level_placer = S_RW_level_placer.get_rect(midtop = (R_S_FW_level_placer.centerx, R_S_FW_level_placer.bottom + 15))

            S_RW_text = Minfont_cars.render("Rear wing", None, (0, 0, 0))
            R_S_RW_text = S_RW_text.get_rect(topleft = (R_S_RW_level_placer.left + 19, R_S_RW_level_placer.top + 5))
            
            S_RW_level = pygame.Surface(((default_rw*21) + 1, 14))
            S_RW_level.fill(team_color)
            R_S_RW_level = S_RW_level.get_rect(bottomleft = (R_S_RW_level_placer.left + 10, R_S_RW_level_placer.bottom - 13))
            S_RW_level_background = pygame.Surface((210, 14))
            S_RW_level_background.fill((70, 70, 70))

            R_S_RW_increment = S_FW_increment.get_rect(midleft = (R_S_RW_level_placer.right + 10, R_S_RW_level_placer.bottom - 20))
            R_S_RW_decrement = S_FW_decrement.get_rect(midright = (R_S_RW_level_placer.left - 10, R_S_RW_level_placer.bottom - 20))

            S_settings = pygame.image.load("images/Settings-level.png").convert_alpha()
            S_settings = pygame.transform.scale(S_settings, downforce_small_size)

            R_S_acceleration = S_settings.get_rect(topleft = (R_S_RW_decrement.left, R_S_RW_level_placer.bottom + 10))
            car_acceleration = ((lows_corner/10) + (mids_corner/10) + (highs_corner/10) + (default_rw/10) + (tyre_acceleration/10))/5
            S_acceleration_level = pygame.Surface((107*car_acceleration, 14))
            S_acceleration_level.fill(team_color)
            R_S_acceleration_level = S_acceleration_level.get_rect(midleft = (R_S_acceleration.left + 11, R_S_acceleration.bottom - 20))
            S_acceleration_background = pygame.Surface((107, 14))
            S_acceleration_background.fill((70, 70, 70))
            S_acceleration_text = Minfont_cars.render("Acceleration", None, (0, 0, 0))
            R_S_acceleration_text = S_acceleration_text.get_rect(topleft = (R_S_acceleration.left + 15, R_S_acceleration.top + 6))

            R_S_braking = S_settings.get_rect(topleft = (R_S_acceleration.left, R_S_acceleration.bottom + 10))
            car_braking = ((default_fw/10) + (default_rw/15) + (brakes/10) + (tyre_braking/10))/4.5
            S_braking_level = pygame.Surface((107*car_braking, 14))
            S_braking_level.fill(team_color)
            R_S_braking_level = S_braking_level.get_rect(midleft = (R_S_braking.left + 11, R_S_braking.bottom - 20))
            S_braking_background = pygame.Surface((107, 14))
            S_braking_background.fill((70, 70, 70))
            S_braking_text = Minfont_cars.render("Braking", None, (0, 0, 0))
            R_S_braking_text = S_braking_text.get_rect(topleft = (R_S_braking.left + 33, R_S_braking.top + 6))

            R_S_degradation = S_settings.get_rect(topright = (R_S_RW_increment.right, R_S_acceleration.top))
            car_deg = (4.5 + 2/3 + 10/3 - (default_fw/10) - (default_rw/10) - (brakes/10) - (highs_corner/10) - (mids_corner/15) - (lows_corner/20) - (tyre_deg/3))/(4.5 + 2/3)
            S_degradation_level = pygame.Surface((107*car_deg, 14))
            S_degradation_level.fill(team_color)
            R_S_degradation_level = S_degradation_level.get_rect(midleft = (R_S_degradation.left + 11, R_S_degradation.bottom - 20))
            S_degradation_background = pygame.Surface((107, 14))
            S_degradation_background.fill((70, 70, 70))
            S_degradation_text = Minfont_cars.render("Degradation", None, (0, 0, 0))
            R_S_degradation_text = S_degradation_text.get_rect(topleft = (R_S_degradation.left + 19, R_S_degradation.top + 6))

            R_S_topspeed = S_settings.get_rect(topleft = (R_S_degradation.left, R_S_braking.top))
            car_topspeed = (2 - (default_fw/10) - (default_rw/10) + (tyre_topspeed/10))/3
            S_topspeed_level = pygame.Surface((107*car_topspeed, 14))
            S_topspeed_level.fill(team_color)
            R_S_topspeed_level = S_topspeed_level.get_rect(midleft = (R_S_topspeed.left + 11, R_S_topspeed.bottom - 20))
            S_topspeed_background = pygame.Surface((107, 14))
            S_topspeed_background.fill((70, 70, 70))
            S_topspeed_text = Minfont_cars.render("Top speed", None, (0, 0, 0))
            R_S_topspeed_text = S_topspeed_text.get_rect(topleft = (R_S_topspeed.left + 25, R_S_topspeed.top + 6))

            current_time = pygame.time.get_ticks()
            delay_time = 150

            if R_S_FW_decrement.collidepoint(mouse_pos_x, mouse_pos_y) and (0 < default_fw <= 10) and current_time - click_time > delay_time:
                if mouse_buttons[0]:
                    default_fw -= 1
                    click_time = current_time
            elif R_S_FW_increment.collidepoint(mouse_pos_x, mouse_pos_y) and  (0 <= default_fw < 10) and current_time - click_time > delay_time:
                if mouse_buttons[0]:
                    default_fw += 1
                    click_time = current_time
            elif R_S_RW_decrement.collidepoint(mouse_pos_x, mouse_pos_y) and (0 < default_rw <= 10) and current_time - click_time > delay_time:
                if mouse_buttons[0]:
                    default_rw -= 1
                    click_time = current_time
            elif R_S_RW_increment.collidepoint(mouse_pos_x, mouse_pos_y) and  (0 <= default_rw < 10) and current_time - click_time > delay_time:
                if mouse_buttons[0]:
                    default_rw += 1
                    click_time = current_time


            if team_name == "mclaren":
                if tyre_selected == "S":
                    chosen_car = mclaren_softs
                elif tyre_selected == "M":
                    chosen_car = mclaren_mediums
                elif tyre_selected == "H":
                    chosen_car = mclaren_hards

            elif team_name == "ferrari":
                if tyre_selected == "S":
                    chosen_car = ferrari_softs
                elif tyre_selected == "M":
                    chosen_car = ferrari_mediums
                elif tyre_selected == "H":
                    chosen_car = ferrari_hards

            elif team_name == "mercedes":
                if tyre_selected == "S":
                    chosen_car = mercedes_softs
                elif tyre_selected == "M":
                    chosen_car = mercedes_mediums
                elif tyre_selected == "H":
                    chosen_car = mercedes_hards

            S_play_button = pygame.image.load(team_play_button).convert_alpha()
            S_play_button = pygame.transform.scale(S_play_button, (240, 32))
            R_S_play_button = S_play_button.get_rect(midtop = (R_S_FW_level_placer.centerx, R_S_braking.bottom + 10))
            S_play_button_background = pygame.image.load("images/Play-button-background.png").convert()
            S_play_button_background = pygame.transform.scale(S_play_button_background, (217, 15))
            R_S_play_button_background = S_play_button_background.get_rect(center = (R_S_play_button.center))
            S_play_button_text = Minfont_play.render("", None, (0, 0, 0, 0))
            R_S_play_button_text = S_play_button_text.get_rect(center = R_S_play_button_background.center)
            if R_S_play_button.collidepoint(mouse_pos_x, mouse_pos_y):
                S_play_button_background = pygame.Surface((217, 14), pygame.SRCALPHA)
                S_play_button_background.fill(team_color_transparent)
                S_play_button_text = Minfont_play.render("LET'S GO RACING", None, (255, 255, 255))
                R_S_play_button_text = S_play_button_text.get_rect(center = (R_S_play_button_background.centerx, R_S_play_button_background.centery + 2))
                if(mouse_buttons[0]):
                    lap_times[0][4] = chosen_car
                    play(team_name, chosen_car, default_fw, default_rw, car_topspeed, car_acceleration, car_braking, car_deg, tyre_selected, team_color, lap_times)


            screen.blit(S_background, R_S_background)
            screen.blit(S_logo, R_S_logo)
            screen.blit(S_back_button, R_S_back_button)
            screen.blit(transparent_surface, (R_S_logo.left + 41, R_S_logo.bottom + 15))
            screen.blit(S_title, R_S_title)
            
            #Car and model
            screen.blit(S_Soft_tyre_hover, R_S_Soft_tyre_hover)
            screen.blit(S_Medium_tyre_hover, R_S_Medium_tyre_hover)
            screen.blit(S_Hard_tyre_hover, R_S_Hard_tyre_hover)
            screen.blit(S_Tyre_placer, R_S_Tyre_placer)
            screen.blit(S_car, R_S_car)
            pygame.draw.rect(screen, team_color, R_S_car_text)
            screen.blit(S_car_text, (R_S_car_text.left + 10, R_S_car_text.centery - 6))

            #Tyres
            screen.blit(S_Soft_tyre, R_S_Soft_tyre)
            screen.blit(S_Medium_tyre, R_S_Medium_tyre)
            screen.blit(S_Hard_tyre, R_S_Hard_tyre)

            #Car settings
            screen.blit(S_FW_level_background, R_S_FW_level)
            screen.blit(S_RW_level_background, R_S_RW_level)
            screen.blit(S_FW_level, R_S_FW_level)
            screen.blit(S_FW_level_placer, R_S_FW_level_placer)
            screen.blit(S_FW_text, R_S_FW_text)
            screen.blit(S_FW_increment, R_S_FW_increment)
            screen.blit(S_FW_decrement, R_S_FW_decrement)
            screen.blit(S_RW_level, R_S_RW_level)
            screen.blit(S_RW_level_placer, R_S_RW_level_placer)
            screen.blit(S_RW_text, R_S_RW_text)
            screen.blit(S_FW_increment, R_S_RW_increment)
            screen.blit(S_FW_decrement, R_S_RW_decrement)

            screen.blit(S_acceleration_background, R_S_acceleration_level)
            screen.blit(S_acceleration_level, R_S_acceleration_level)
            screen.blit(S_settings, R_S_acceleration)
            screen.blit(S_acceleration_text, R_S_acceleration_text)
            screen.blit(S_braking_background, R_S_braking_level)
            screen.blit(S_braking_level, R_S_braking_level)
            screen.blit(S_settings, R_S_braking)
            screen.blit(S_braking_text, R_S_braking_text)
            screen.blit(S_degradation_background, R_S_degradation_level)
            screen.blit(S_degradation_level, R_S_degradation_level)
            screen.blit(S_settings, R_S_degradation)
            screen.blit(S_degradation_text, R_S_degradation_text)
            screen.blit(S_topspeed_background, R_S_topspeed_level)
            screen.blit(S_topspeed_level, R_S_topspeed_level)
            screen.blit(S_settings, R_S_topspeed)
            screen.blit(S_topspeed_text, R_S_topspeed_text)

            screen.blit(S_play_button_background, R_S_play_button_background)
            screen.blit(S_play_button, R_S_play_button)
            screen.blit(S_play_button_text, R_S_play_button_text)
            

            pygame.display.update()
            clock.tick(30)

    ##################################################################################################################       

            
    def play (team_name, chosen_car, fw, rw, topspeed, acc, braking, deg, tyre_selected, team_color, lap_times):

        # Default sizes for images to scale them
        size_S = (225, 500)
        size_S_L= (245, 500)
        size_S_R = (246, 500)
        starting_position = [328, 1358]
        Minfont_times = pygame.font.Font('Minecraft.ttf', 16)
        Minfont_title = pygame.font.Font('Minecraft.ttf', 25)

        #BACKGROUND

        #Track
        S_start = pygame.image.load("images/i-S.png").convert_alpha()
        S_start = pygame.transform.scale(S_start, size_S)
        R_S_start = S_start.get_rect(center = (starting_position[0], 250 + starting_position[1]))
        S_grid = pygame.image.load("images/i-S-grid.png").convert_alpha()
        S_grid = pygame.transform.scale(S_grid, size_S)
        R_S_grid = S_grid.get_rect(midbottom = (R_S_start.midtop))
        S_finish_line = pygame.image.load("images/i-S-finish-line.png").convert_alpha()
        S_finish_line = pygame.transform.scale(S_finish_line, size_S)
        S_chicane_1 = pygame.image.load("images/i-S-chicane.png")
        S_chicane_1 = pygame.transform.scale(S_chicane_1, size_S)
        S_obstacle = pygame.image.load("images/i-obstacle.png")
        S_obstacle = pygame.transform.scale(S_obstacle, (101, 201))
        R_S_finish_line = S_finish_line.get_rect(midbottom = (R_S_grid.midtop))
        R_S_base2 = S_start.get_rect(midbottom = (R_S_finish_line.midtop))
        R_S_base3 = S_start.get_rect(midbottom = (R_S_base2.midtop))
        R_S_base4 = S_start.get_rect(midbottom = (R_S_base3.midtop))
        R_S_base5 = S_start.get_rect(midbottom = (R_S_base4.midtop))
        R_S_chicane_1 = S_chicane_1.get_rect(midbottom = (R_S_base5.midtop))
        R_S_base6 = S_start.get_rect(midbottom = (R_S_chicane_1.midtop))
        R_S_base7 = S_start.get_rect(midbottom = (R_S_base6.midtop))
        S_chicane_2 = pygame.transform.rotate(S_chicane_1, 180)
        R_S_chicane_2 = S_chicane_2.get_rect(midbottom = (R_S_base7.midtop))
        R_S_base_final = S_finish_line.get_rect(midbottom = (R_S_chicane_2.midtop))
        R_S_obstacle = S_obstacle.get_rect(bottomleft = ( R_S_chicane_1.left, R_S_chicane_1.bottom - 150))
        R_S_obstacle_2 = S_obstacle.get_rect(bottomleft = ( R_S_chicane_2.left, R_S_chicane_2.bottom - 150))
        R_S_obstacle_3 = S_obstacle.get_rect(center = (R_S_base6.center))
        R_S_obstacle_4 = S_obstacle.get_rect(midright = (R_S_base7.midright))
        R_S_obstacles = [R_S_obstacle, R_S_obstacle_2, R_S_obstacle_3, R_S_obstacle_4]
                                            
                            




        S_barriers_L = pygame.image.load("images/i-S-Lbarrier.png").convert_alpha()
        S_barriers_L = pygame.transform.scale(S_barriers_L, size_S_L)
        R_S_barriers_L1 = S_barriers_L.get_rect(midright = R_S_start.midleft)
        R_S_barriers_L2 = S_barriers_L.get_rect(midright = R_S_grid.midleft)
        R_S_barriers_L3 = S_barriers_L.get_rect(midright = R_S_finish_line.midleft)
        R_S_barriers_L4 = S_barriers_L.get_rect(midright = R_S_base2.midleft)
        R_S_barriers_L5 = S_barriers_L.get_rect(midright = R_S_base3.midleft)
        R_S_barriers_L6 = S_barriers_L.get_rect(midright = R_S_base4.midleft)
        R_S_barriers_L7 = S_barriers_L.get_rect(midright = R_S_base5.midleft)
        R_S_barriers_L8 = S_barriers_L.get_rect(midright = R_S_chicane_1.midleft)
        R_S_barriers_L9 = S_barriers_L.get_rect(midright = R_S_base6.midleft)
        R_S_barriers_L10 = S_barriers_L.get_rect(midright = R_S_base7.midleft)
        R_S_barriers_L11 = S_barriers_L.get_rect(midright = R_S_chicane_2.midleft)
        R_S_barriers_L12 = S_barriers_L.get_rect(midright = R_S_base_final.midleft)




        S_pits = pygame.image.load("images/i-S-pits-NOlogos.png").convert_alpha()
        S_pits = pygame.transform.scale(S_pits, size_S_R)
        R_S_pits1 = S_pits.get_rect(midleft = R_S_start.midright)
        S_pits_logos = pygame.image.load("images/i-S-pits-logos.png").convert_alpha()
        S_pits_logos = pygame.transform.scale(S_pits_logos, size_S_R)
        R_S_pits_logos = S_pits_logos.get_rect(midleft = R_S_grid.midright)
        R_S_pits_logos2 = S_pits_logos.get_rect(midleft = R_S_finish_line.midright)
        R_S_pits2 = S_pits.get_rect(midleft = R_S_base2.midright)
        R_S_pits3 = S_pits.get_rect(midleft = R_S_base3.midright)
        R_S_pits4 = S_pits.get_rect(midleft = R_S_base4.midright)
        S_pits_exit = pygame.image.load("images/i-S-pits-exit.png").convert_alpha()
        S_pits_exit = pygame.transform.scale(S_pits_exit, size_S_R)
        R_S_pits_exit = S_pits.get_rect(midleft = (R_S_base5.midright))
        S_barriers_R = pygame.transform.rotate(S_barriers_L, 180)
        R_S_barriers_R8 = S_barriers_R.get_rect(midleft = R_S_chicane_1.midright)
        R_S_barriers_R9 = S_barriers_R.get_rect(midleft = R_S_base6.midright)
        R_S_barriers_R10 = S_barriers_R.get_rect(midleft = R_S_base7.midright)
        R_S_barriers_R11 = S_barriers_R.get_rect(midleft = R_S_chicane_2.midright)
        R_S_barriers_R12 = S_barriers_R.get_rect(midleft = R_S_base_final.midright)


        #CAR AND OTHERS
        
        car = pygame.image.load(chosen_car).convert_alpha()
        car = pygame.transform.scale(car, (27, 95))
        R_car = car.get_rect(center = (300, 433))

        #Variables
        car_pos_y_increment = float(0)
        car_pos_x_increment = 0
        start_menu = 0
        game_active = False
        start_menu = True
        lights_out = False
        disappear_time = random.randint(1, 1500)
        lights_out_time = 0
        angle = 0
        laps = 0
        lap_counter = -1
        audio_braking =  ""
        audio_accelerating =  ""
        audio_cornering =  ""
        audio_soundtrack = pygame.mixer.Sound("audio/F1-soundtrack.mp3")
        audio_soundtrack.play(-1)
        start_time = 0
        start_time_condition = True
        end_time = 0
        end_time_condition = True
        Time = Minfont.render(lap_times[0][lap_counter + 1], False, "Black")
        condition = False



        S_lights_background = pygame.Surface((275, 80))
        S_lights_background.fill((245, 245, 245))
        S_lights = pygame.Surface((32, 32))
        S_lights.fill((0, 0, 0))
        audio = pygame.mixer.Sound("audio/light-out.mp3")
        if team_name == "mercedes":
            audio_braking =  pygame.mixer.Sound("audio/Mercedes-sound-braking1.mp3")
            audio_accelerating =  pygame.mixer.Sound("audio/Mercedes-sound-accelerating1.mp3")
            audio_cornering =  pygame.mixer.Sound("audio/Mercedes-sound-cornering1.mp3")
        elif team_name == "ferrari":
            audio_braking =  pygame.mixer.Sound("audio/Ferrari-sound-braking1.mp3")
            audio_accelerating =  pygame.mixer.Sound("audio/Ferrari-sound-accelerating1.mp3")
            audio_cornering =  pygame.mixer.Sound("audio/Ferrari-sound-cornering1.mp3")
        elif team_name == "mclaren":
            audio_braking =  pygame.mixer.Sound("audio/Mclaren-sound-braking1.mp3")
            audio_accelerating =  pygame.mixer.Sound("audio/Mclaren-sound-accelerating1.mp3")
            audio_cornering =  pygame.mixer.Sound("audio/Mclaren-sound-cornering1.mp3")
        
        audio_accelerating.set_volume(0.0)
        audio_braking.set_volume(0.0)
        audio_cornering.set_volume(0.0)

        audio_accelerating.play(-1)
        audio_braking.play(-1)
        audio_cornering.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            screen.fill((0, 0, 0))

            ########################################################################################################

            current_time = pygame.time.get_ticks()

            if start_menu == True:
                screen.blit(S_finish_line, R_S_finish_line)
                screen.blit(S_barriers_L, R_S_barriers_L3)
                screen.blit(S_pits_logos, R_S_pits_logos2)
                screen.blit(S_start, R_S_base2)
                screen.blit(S_barriers_L, R_S_barriers_L4)
                screen.blit(S_pits_logos, R_S_pits2)

                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                mouse_buttons = pygame.mouse.get_pressed()

                S_background = pygame.image.load("images/start-menu.png")
                S_background = pygame.transform.scale(S_background, (550, 450))
                R_S_background = S_background.get_rect(center = (300, 250))

                S_best_laps_background = pygame.Surface((150, 23))
                S_best_laps_background.fill(team_color)
                R_S_best_laps_background = S_best_laps_background.get_rect(topleft = (R_S_background.left + 350, R_S_background.top + 85))
                R_S_lights_background = S_lights_background.get_rect(bottomleft = (R_S_background.left + 45, R_S_background.bottom - 53))

                S_logo = pygame.image.load("images/logo-FC.png").convert_alpha()
                S_logo = pygame.transform.scale(S_logo, (308, 56))
                R_S_logo = S_logo.get_rect(midtop = (R_S_background.centerx, R_S_background.top + 4))

                S_back_button = pygame.image.load("images/back-button.png")
                S_back_button = pygame.transform.scale(S_back_button, (56, 56))
                R_S_back_button = S_back_button.get_rect(topleft = (R_S_background.left + 45, R_S_logo.top))

                S_last_laptime_1 = Minfont_times.render(lap_times[0][1], None, (0, 0, 0))
                S_last_laptime_2 = Minfont_times.render(lap_times[0][2], None, (0, 0, 0))
                S_last_laptime_3 = Minfont_times.render(lap_times[0][3], None, (0, 0, 0))
                S_last_car = pygame.image.load(lap_times[0][4]).convert_alpha()
                S_last_car = pygame.transform.scale(S_last_car, (27, 95))
                S_last_laptime_text = Minfont_times.render(lap_times[0][0], None, (0, 0, 0))

                R_S_last_laptime_1 = S_last_laptime_1.get_rect(center = (472, 191))
                R_S_last_laptime_2 = S_last_laptime_1.get_rect(midtop = (R_S_last_laptime_1.centerx, R_S_last_laptime_1.bottom + 15))
                R_S_last_laptime_3 = S_last_laptime_1.get_rect(midtop = (R_S_last_laptime_2.centerx, R_S_last_laptime_2.bottom + 14))
                R_S_last_car = S_last_car.get_rect(topleft = (R_S_last_laptime_1.left - 65, R_S_last_laptime_1.top - 10))
                R_S_last_laptime_text = S_last_laptime_text.get_rect(center = (R_S_last_laptime_1.centerx - 22, R_S_last_laptime_1.top - 60))

                S_best_laptime_1 = Minfont_times.render(lap_times[1][1], None, (0, 0, 0))
                S_best_laptime_2 = Minfont_times.render(lap_times[1][2], None, (0, 0, 0))
                S_best_laptime_3 = Minfont_times.render(lap_times[1][3], None, (0, 0, 0))
                S_best_car = pygame.image.load(lap_times[1][4])
                S_best_car = pygame.transform.scale(S_best_car, (27, 95))

                R_S_best_laptime_1 = S_best_laptime_1.get_rect(center = (472, 333))
                R_S_best_laptime_2 = S_best_laptime_1.get_rect(midtop = (R_S_best_laptime_1.centerx, R_S_best_laptime_1.bottom + 15))
                R_S_best_laptime_3 = S_best_laptime_1.get_rect(midtop = (R_S_best_laptime_2.centerx, R_S_best_laptime_2.bottom + 14))
                R_S_best_car = S_best_car.get_rect(topleft = (R_S_best_laptime_1.left - 65, R_S_best_laptime_1.top - 10))

                S_back_key = Minfont_times.render("Brake", None, (0, 0, 0))
                S_reverse_key = Minfont_times.render("Reverse", None, (0, 0, 0))
                S_esc_key = Minfont_times.render("Menu", None, (0, 0, 0))
                S_up_key = Minfont_times.render("Accelerate", None, (0, 0, 0))
                S_left_key = Minfont_times.render("Left", None, (0, 0, 0))
                S_right_key = Minfont_times.render("Right", None, (0, 0, 0))
                
                R_S_back_key = S_back_key.get_rect(center = (R_S_background.left + 173, R_S_background.top + 295))
                R_S_reverse_key = S_reverse_key.get_rect(topleft = (R_S_back_key.right + 18, R_S_back_key.top))
                R_S_esc_key = S_esc_key.get_rect(topright = (R_S_back_key.left - 32, R_S_back_key.top))
                R_S_up_key = S_up_key.get_rect(center = (R_S_back_key.centerx, R_S_back_key.top - 125))
                R_S_left_key = S_left_key.get_rect(topright = (R_S_up_key.centerx - 57, R_S_up_key.bottom + 32))
                R_S_right_key = S_right_key.get_rect(topleft = (R_S_up_key.centerx + 55, R_S_left_key.top))
                

                screen.blit(S_best_laps_background, R_S_best_laps_background)
                screen.blit(S_lights_background, R_S_lights_background)
                screen.blit(S_background, R_S_background)
                screen.blit(S_logo, R_S_logo)
                screen.blit(S_last_car, R_S_last_car)
                screen.blit(S_last_laptime_text, R_S_last_laptime_text)
                screen.blit(S_last_laptime_1, R_S_last_laptime_1)
                screen.blit(S_last_laptime_2, R_S_last_laptime_2)
                screen.blit(S_last_laptime_3, R_S_last_laptime_3)
                screen.blit(S_best_car, R_S_best_car)
                screen.blit(S_best_laptime_1, R_S_best_laptime_1)
                screen.blit(S_best_laptime_2, R_S_best_laptime_2)
                screen.blit(S_best_laptime_3, R_S_best_laptime_3)
                screen.blit(S_back_button, R_S_back_button)
                screen.blit(S_back_key, R_S_back_key)
                screen.blit(S_reverse_key, R_S_reverse_key)
                screen.blit(S_esc_key, R_S_esc_key)
                screen.blit(S_up_key, R_S_up_key)
                screen.blit(S_left_key, R_S_left_key)
                screen.blit(S_right_key, R_S_right_key)


                if R_S_lights_background.collidepoint(mouse_pos_x, mouse_pos_y):
                    S_lights_background.fill(team_color)
                    if mouse_buttons[0]:
                        lights_out = True
                        game_active = False
                        lights_out_time = current_time
                elif R_S_back_button.collidepoint(mouse_pos_x, mouse_pos_y):
                    if mouse_buttons[0]:
                        audio_soundtrack.set_volume(0, 0)
                        car_set_up(team_name, lap_times)
                else:
                    S_lights_background.fill((245, 245, 245))
            
            #############################################################################################################

            if lights_out == True:
                audio_soundtrack.set_volume(0.0)
                screen.blit(S_finish_line, R_S_finish_line)
                screen.blit(S_barriers_L, R_S_barriers_L3)
                screen.blit(S_pits_logos, R_S_pits_logos2)
                screen.blit(S_start, R_S_base2)
                screen.blit(S_barriers_L, R_S_barriers_L4)
                screen.blit(S_pits_logos, R_S_pits2)

                current_time -= lights_out_time - 1500
                S_lights_out = pygame.image.load("images/lights-out.png")
                S_lights_out = pygame.transform.scale(S_lights_out, (300, 50))
                R_S_lights_out = S_lights_out.get_rect(center = (300, 250))

                R_S_lights_1 = S_lights.get_rect(topleft = (R_S_lights_out.left + 16, R_S_lights_out.top + 9))
                R_S_lights_2 = S_lights.get_rect(topleft = (R_S_lights_1.right + 27, R_S_lights_1.top))
                R_S_lights_3 = S_lights.get_rect(topleft = (R_S_lights_2.right + 27, R_S_lights_2.top))
                R_S_lights_4 = S_lights.get_rect(topleft = (R_S_lights_3.right + 27, R_S_lights_3.top))
                R_S_lights_5 = S_lights.get_rect(topleft = (R_S_lights_4.right + 27, R_S_lights_4.top))
                if current_time > 3000:
                    play_sound(audio, 3050 - current_time)
                    S_lights.fill((239, 0, 1))
                    screen.blit(S_lights, R_S_lights_1)
                    if current_time > 4000:
                        play_sound(audio, 4050 - current_time)
                        screen.blit(S_lights, R_S_lights_2)
                        if current_time > 5000:
                            play_sound(audio, 5050 - current_time)
                            screen.blit(S_lights, R_S_lights_3)
                            if current_time > 6000:
                                play_sound(audio, 6050 - current_time)
                                screen.blit(S_lights, R_S_lights_4)
                                if current_time > 7000:
                                    play_sound(audio, 7050 - current_time)
                                    screen.blit(S_lights, R_S_lights_5)
                                    if current_time > 9000 - disappear_time:
                                        S_lights.fill((0, 0, 0))
                                        if current_time > 9000 + 500 - disappear_time:
                                            game_active = True
                                            start_menu = False
                                            screen.fill((0, 0, 0))
                screen.blit(S_lights_out, R_S_lights_out)
                screen.blit(car, R_car)
                car = pygame.image.load(chosen_car)
                car = pygame.transform.scale(car, (27, 95))

    ########################################################################################################################

            

            if game_active == True:
                aum_x = 0

                start_time = get_lap_time(start_time)

                if laps < 4:
                    end_time = datetime.datetime.now()
                    lap_times[0][lap_counter + 1] = str(end_time - start_time)[:-3]
                    Time = Minfont.render(lap_times[0][lap_counter + 1], False, "Black")
                    
                elif laps >= 4:
                    start_menu = True
                    game_active = False
                    lights_out = False

                audio_soundtrack.set_volume(0.0)
                audio_accelerating.set_volume(0.0)
                audio_braking.set_volume(0.0)
                audio_cornering.set_volume(0.0)

                rotated_car = pygame.transform.rotate(car, angle)
                R_rotated_car = rotated_car.get_rect(center = R_car.center)            
                if R_rotated_car.top == R_S_finish_line.top:
                    laps += 1

                keys = pygame.key.get_pressed() #Get all the keys getting pressed in every frame


                if keys[pygame.K_ESCAPE]:
                    lights_out = True
                    game_active = False
                if keys[pygame.K_UP]:
                    audio_accelerating.set_volume(1.0)
                    if keys[pygame.K_LEFT]:
                        car_pos_x_increment += acceleration(0.75, 0.75, acc, fw, rw, deg, angle)[0]
                        car_pos_y_increment += acceleration(0.75, 0.75, acc, fw, rw, deg, angle)[1]
                        angle += 1.40
                        
                    elif keys[pygame.K_RIGHT]:
                        car_pos_x_increment += acceleration(0.75, 0.75, acc, fw, rw, deg, angle)[0]
                        car_pos_y_increment += acceleration(0.75, 0.75, acc, fw, rw, deg, angle)[1]
                        angle -= 1.40
                    else:
                        car_pos_y_increment += acceleration(0, 0.75, acc, fw, rw, deg, angle)[1]
                elif keys[pygame.K_DOWN] and (car_pos_y_increment >= 0):
                    audio_braking.set_volume(1.0)
                    if keys[pygame.K_LEFT]:
                        car_pos_x_increment -= acceleration(0.80, 0.50, acc, fw, rw, deg, angle)[0]
                        car_pos_y_increment -= acceleration(0.80, 0.50, acc, fw, rw, deg, angle)[1]
                        angle += 1.40
                    if keys[pygame.K_RIGHT]:
                        car_pos_x_increment += acceleration(0.80, 0.50, acc, fw, rw, deg, angle)[0]
                        car_pos_y_increment -= acceleration(0.80, 0.50, acc, fw, rw, deg, angle)[1]
                        angle -= 1.40
                    else:
                        car_pos_y_increment -= acceleration(0, -0.50, acc, fw, rw, deg, angle)[1]
                elif car_pos_y_increment > 0:
                    audio_cornering.set_volume(1.0)
                    if keys[pygame.K_LEFT]:
                        car_pos_x_increment += acceleration (0.60, 0.025, acc, fw, rw, deg, angle)[1]
                        car_pos_y_increment -= acceleration (0.60, 0.025, acc, fw, rw, deg, angle)[0]
                        angle += 1.40
                        
                    elif keys[pygame.K_RIGHT]:
                        car_pos_y_increment -= acceleration (0.60, 0.025, acc, fw, rw, deg, angle)[1]
                        car_pos_x_increment -= acceleration (0.60, 0.025, acc, fw, rw, deg, angle)[0]
                        angle -= 1.40
                    else:
                        car_pos_y_increment -= (0, 0.025, acc, fw, rw, deg, angle)[1]
                elif car_pos_y_increment < 0:
                    audio_cornering.set_volume(1.0)
                    if keys[pygame.K_DOWN] and keys[pygame.K_r]:
                        car_pos_y_increment += reverse(car_pos_y_increment, -0.30, acc, fw, rw, deg, angle)
                        if keys[pygame.K_LEFT]:
                            aum = reverse (-0.15, 0, acc, fw, rw, deg, angle) - 0.1
                            car_pos_x_increment += aum
                            angle += 1.40
                        elif keys[pygame.K_RIGHT]:
                            aum_x= reverse (0.15, 0, acc, fw, rw, deg, angle) + 0.1
                            car_pos_x_increment += aum_x
                            angle -= 1.40
                    elif car_pos_y_increment >= 0.5 or car_pos_y_increment <= -0.5:
                        if keys[pygame.K_LEFT]:
                            aum_x= reverse (-0.15, 0, acc, fw, rw, deg, angle) - 0.1
                            car_pos_x_increment += aum_x
                            angle += 1.40
                        elif keys[pygame.K_RIGHT]:
                            aum_x= reverse (0.15, 0, acc, fw, rw, deg, angle) + 0.1
                            car_pos_x_increment += aum_x
                            angle -= 1.40
                        else:
                            car_pos_x_increment = 0
                            car_pos_y_increment += acceleration(0, 0.025, acc, fw, rw, deg, angle)[1]
                    else: car_pos_x_increment = 0
                    
                R_S_left = [R_S_barriers_L1, R_S_barriers_L2, R_S_barriers_L3, R_S_barriers_L4, R_S_barriers_L5, R_S_barriers_L6, R_S_barriers_L7, R_S_barriers_L8, R_S_barriers_L9, R_S_barriers_L10, R_S_barriers_L11, R_S_barriers_L12]
                R_S_right = [R_S_pits_logos, R_S_pits_logos2, R_S_pits1, R_S_pits2, R_S_pits3, R_S_pits4, R_S_pits_exit, R_S_barriers_R8, R_S_barriers_R9, R_S_barriers_R10, R_S_barriers_R11, R_S_barriers_R12]
                rect = pygame.Rect(0, 0, 0, 0)

                for rect in R_S_left:
                    if R_rotated_car.colliderect(rect):
                        car_pos_x_increment = -1

                for rect in R_S_right:
                    if R_rotated_car.colliderect(rect):
                        car_pos_x_increment = 1


                if angle >= 360:
                    angle = 0
                condition 
                for rect in R_S_obstacles:
                    if R_rotated_car.colliderect(rect):
                        car_pos_y_increment = -2
                        car_pos_x_increment = -car_pos_y_increment

                if R_S_base_final.bottom >= 500 and R_S_base_final.bottom <= 550:
                    game_active = False
                    start_menu = True
                    lights_out = False
                    R_S_base_final.bottom = 3000
                    print("AAAAAA")
                    


                #SHOW BACKGROUND
                R_S_start.x += int(car_pos_x_increment)
                R_S_barriers_L1.x += int(car_pos_x_increment)
                R_S_pits1.x += int(car_pos_x_increment)

                R_S_base2.x += int(car_pos_x_increment)
                R_S_barriers_L2.x += int(car_pos_x_increment)
                R_S_pits2.x += int(car_pos_x_increment)
                R_S_grid.x += int(car_pos_x_increment)
                R_S_barriers_L3.x += int(car_pos_x_increment)
                R_S_pits_logos.x += int(car_pos_x_increment)
                R_S_finish_line.x += int(car_pos_x_increment)
                R_S_barriers_L4.x += int(car_pos_x_increment)
                R_S_pits_logos2.x += int(car_pos_x_increment)
                R_S_base3.x += int(car_pos_x_increment)
                R_S_barriers_L5.x += int(car_pos_x_increment)
                R_S_pits3.x += int(car_pos_x_increment)
                R_S_base4.x += int(car_pos_x_increment)
                R_S_barriers_L6.x += int(car_pos_x_increment)
                R_S_pits4.x += int(car_pos_x_increment)
                R_S_base5.x += int(car_pos_x_increment)
                R_S_barriers_L7.x += int(car_pos_x_increment)
                R_S_pits_exit.x += int(car_pos_x_increment)
                R_S_chicane_1.x += int(car_pos_x_increment)

                R_S_base6.x += int(car_pos_x_increment)
                R_S_base7.x += int(car_pos_x_increment)
                R_S_chicane_2.x += int(car_pos_x_increment)
                R_S_base_final. x+= int(car_pos_x_increment)

                R_S_barriers_L8.x += int(car_pos_x_increment)
                R_S_barriers_L9.x += int(car_pos_x_increment)
                R_S_barriers_L10.x += int(car_pos_x_increment)
                R_S_barriers_L11.x += int(car_pos_x_increment)
                R_S_barriers_L12.x += int(car_pos_x_increment)

                R_S_barriers_R8.x += int(car_pos_x_increment)
                R_S_barriers_R9.x += int(car_pos_x_increment)
                R_S_barriers_R10.x += int(car_pos_x_increment)
                R_S_barriers_R11.x += int(car_pos_x_increment)
                R_S_barriers_R12.x += int(car_pos_x_increment)

                R_S_obstacle.x += int(car_pos_x_increment)
                R_S_obstacle_2.x += int(car_pos_x_increment)
                R_S_obstacle_3.x += int(car_pos_x_increment)
                R_S_obstacle_4.x += int(car_pos_x_increment)


                R_S_start.y += int(car_pos_y_increment)
                R_S_barriers_L1.y += int(car_pos_y_increment)
                R_S_pits1.y += int(car_pos_y_increment)

                R_S_base2.y += int(car_pos_y_increment)
                R_S_barriers_L2.y += int(car_pos_y_increment)
                R_S_pits2.y += int(car_pos_y_increment)
                R_S_grid.y += int(car_pos_y_increment)
                R_S_barriers_L3.y += int(car_pos_y_increment)
                R_S_pits_logos.y += int(car_pos_y_increment)
                R_S_finish_line.y += int(car_pos_y_increment)
                R_S_barriers_L4.y += int(car_pos_y_increment)
                R_S_pits_logos2.y += int(car_pos_y_increment)
                R_S_base3.y += int(car_pos_y_increment)
                R_S_barriers_L5.y += int(car_pos_y_increment)
                R_S_pits3.y += int(car_pos_y_increment)
                R_S_base4.y += int(car_pos_y_increment)
                R_S_barriers_L6.y += int(car_pos_y_increment)
                R_S_pits4.y += int(car_pos_y_increment)
                R_S_base5.y += int(car_pos_y_increment)
                R_S_barriers_L7.y += int(car_pos_y_increment)
                R_S_pits_exit.y += int(car_pos_y_increment)
                R_S_chicane_1.y += int(car_pos_y_increment)
                R_S_base6.y += int(car_pos_y_increment)
                R_S_base7.y += int(car_pos_y_increment)
                R_S_chicane_2.y += int(car_pos_y_increment)
                R_S_base_final. y+= int(car_pos_y_increment)

                R_S_barriers_L8.y += int(car_pos_y_increment)
                R_S_barriers_L9.y += int(car_pos_y_increment)
                R_S_barriers_L10.y += int(car_pos_y_increment)
                R_S_barriers_L11.y += int(car_pos_y_increment)
                R_S_barriers_L12.y += int(car_pos_y_increment)

                R_S_barriers_R8.y += int(car_pos_y_increment)
                R_S_barriers_R9.y += int(car_pos_y_increment)
                R_S_barriers_R10.y += int(car_pos_y_increment)
                R_S_barriers_R11.y += int(car_pos_y_increment)
                R_S_barriers_R12.y += int(car_pos_y_increment)

                R_S_obstacle.y += int(car_pos_y_increment)
                R_S_obstacle_2.y += int(car_pos_y_increment)
                R_S_obstacle_3.y += int(car_pos_y_increment)
                R_S_obstacle_4.y += int(car_pos_y_increment)


                screen.blit(S_start, R_S_start)
                screen.blit(S_barriers_L, R_S_barriers_L1)        
                screen.blit(S_pits, R_S_pits1)

                screen.blit(S_start, R_S_base2)
                screen.blit(S_barriers_L, R_S_barriers_L2)
                screen.blit(S_pits_logos, R_S_pits_logos)
                screen.blit(S_grid, R_S_grid)
                screen.blit(S_barriers_L, R_S_barriers_L3)
                screen.blit(S_pits_logos, R_S_pits_logos2)
                screen.blit(S_finish_line, R_S_finish_line)
                screen.blit(S_barriers_L, R_S_barriers_L4)
                screen.blit(S_pits, R_S_pits2)
                screen.blit(S_start, R_S_base3)
                screen.blit(S_barriers_L, R_S_barriers_L5)
                screen.blit(S_pits, R_S_pits3)
                screen.blit(S_start, R_S_base4)
                screen.blit(S_barriers_L, R_S_barriers_L6)
                screen.blit(S_pits, R_S_pits4)
                screen.blit(S_start, R_S_base5)
                screen.blit(S_barriers_L, R_S_barriers_L7)
                screen.blit(S_pits_exit, R_S_pits_exit)
                screen.blit(S_chicane_1, R_S_chicane_1)
                screen.blit(S_barriers_L, R_S_barriers_L8)
                screen.blit(S_barriers_R, R_S_barriers_R8)
                screen.blit(S_start, R_S_base6)
                screen.blit(S_barriers_L, R_S_barriers_L9)
                screen.blit(S_barriers_R, R_S_barriers_R9)
                screen.blit(S_start, R_S_base7)
                screen.blit(S_barriers_L, R_S_barriers_L10)
                screen.blit(S_barriers_R, R_S_barriers_R10)
                screen.blit(S_chicane_1, R_S_chicane_2)
                screen.blit(S_barriers_L, R_S_barriers_L11)
                screen.blit(S_barriers_R, R_S_barriers_R11)
                screen.blit(S_finish_line, R_S_base_final)
                screen.blit(S_barriers_L, R_S_barriers_L12)
                screen.blit(S_barriers_R, R_S_barriers_R12)

                screen.blit(S_obstacle, R_S_obstacle)
                screen.blit(S_obstacle, R_S_obstacle_2)
                screen.blit(S_obstacle, R_S_obstacle_3)
                screen.blit(S_obstacle, R_S_obstacle_4)



                screen.blit(S_start, R_S_base2)
                screen.blit(S_barriers_L, R_S_barriers_L4)
                screen.blit(S_pits_exit, R_S_pits_exit)

                #SHOW CAR
                screen.blit(rotated_car, R_rotated_car)

                screen.blit(Time, (225,15))
            pygame.display.update()
            clock.tick(30)

    menu(video, lap_times)      

f1()