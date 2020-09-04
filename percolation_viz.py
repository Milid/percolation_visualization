

import pygame
import math
from percolation import Percolation, Trial
from percolationVizStats import PercolationStats
import time
from utilities import *

color  = {"red":(255,0,0), "blue":(0,0,255),"light_blue":(173,216,230), "yelllow":(255,249,10),\
          "dark_brown":(77,38,2), "brown":(247,125,10),  "orange":(247,46,10),\
          "yellow":(247,239,10), "bright_blue":(10,247,208), "lilac":(247,10,232),\
          "pink":(247,10,10), "grey":(150,150,150), "light_grey":(210,210,210), "bright_green":(0,255,0),\
          "green":(0,200,0), "bright_red":(255,0,0), "red":(200,0,0)}

pygame.init()
largeText = pygame.font.Font('freesansbold.ttf',100)
mediumText = pygame.font.Font('freesansbold.ttf',45)
smallText = pygame.font.Font('freesansbold.ttf',20)


white = (255,255,255)
black = (0,0,0)


display_width = 800
display_height = 800
clock = pygame.time.Clock()
def_font = pygame.font.get_default_font() 


gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(white)
mouse = pygame.mouse.get_pos
click = pygame.mouse.get_pressed
grid_offset = 100
start_point = (grid_offset, grid_offset // 2)
n = 10
trials = 5
pause = False

def get_site_dim(n):
    return (display_width - 2 * grid_offset)//n


def get_viz_stats(percolation_stats, font_size, coords):
    trials, mean, stddev, conf_int_lo, conf_int_hi = percolation_stats.getStats()
    x, y = coords
    text1 = f'trials = {trials}, mean = {mean}, stddev = {stddev}'
    text2 = f'confidence interval = ({conf_int_lo}, {conf_int_hi})'
    font = pygame.font.Font(def_font, font_size)
    text = font.render(text1, False, black)
    gameDisplay.blit(text,coords)
    stats = font.render(text2, False, black)
    gameDisplay.blit(stats,(x, y+font_size+10))
    

def quit_viz():
    pygame.quit()
    quit()


        

def get_trial_info(site_grid, trial):
    gameDisplay.fill(white)
    site_grid.display(gameDisplay)
    open_sites = trial.getNumberOfOpenSites()
    text = "Total open sites: " + str(open_sites) + " or "
    text_1 = str(round(open_sites / (n * n), 3)) + " out of " + str(n * n) + " sites"                                                                
    
    message = Message(gameDisplay, text, def_font, 20, (display_width/2, display_height/2), black, color['light_grey'])
    message.display_msg()
    message_1 = Message(gameDisplay, text_1, def_font, 20, (display_width/2, display_height/2 + 40), black, color['light_grey'])
    message_1.display_msg()
    
    
    
def get_series_stats(percolation_stats):
    gameDisplay.fill(white)

    
    
    button_continue = Button(150,700, 100, 50, color['blue'], color['light_blue'],"Continue", viz_intro)
            
    button_quit = Button(550,700, 100, 50, color['red'], color['bright_red'], "Quit", quit_viz)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         
            button_continue.button_check(event)
            button_quit.button_check(event)
                
      
        

        get_viz_stats(percolation_stats, 35, (55, 350))
        pygame.draw.rect(gameDisplay, color['red'], (25,300,750,200), 2)

        button_continue.button_draw(gameDisplay)
        button_quit.button_draw(gameDisplay)
 
        pygame.display.update()
        clock.tick(10)
       
    


def viz_intro():
    global n
    global trials
    button_run = Button(150,700, 100, 50, color['blue'], color['light_blue'],"Run", viz_loop)
            
    button_quit = Button(550,700, 100, 50, color['red'], color['bright_red'], "Quit", quit_viz)
    pick_n_scale = Scale(gameDisplay, 100, display_height/2 - 150, 600, 40, 10, 20, 60, 10,
                        color['red'], black, color['yellow'], color['blue'])
    pick_n_scale.set_scale()
    pick_trials_scale = Scale(gameDisplay, 100, display_height/2 + 50, 600, 40, 5, 10, 50, 10,
                        color['bright_green'], black, color['yellow'], color['green'])
    pick_trials_scale.set_scale()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pick_n_scale.check_scale(event)
            pick_trials_scale.check_scale(event)
            button_run.button_check(event)
            button_quit.button_check(event)
                
        gameDisplay.fill(white)
        
        message = Message(gameDisplay, "Percolation simulation", 'freesansbold.ttf', 45,
                          (display_width/2, display_height/2 - 300), color['blue'], white)
        message.display_msg()

        pick_n_message = Message(gameDisplay, "Pick the dimension n for n x n grid", 'freesansbold.ttf', 30,
                                      (display_width/2, display_height/2 - 200), color['blue'], white)

        pick_n_default = Message(gameDisplay, "(default grid is 10 x 10)", 'freesansbold.ttf', 20,
                                      (display_width/2, display_height/2 - 180), color['blue'], white)
        

        pick_trials_message = Message(gameDisplay, "Pick the number of trials", 'freesansbold.ttf', 30,
                                      (display_width/2, display_height/2 ), color['blue'], white)
        pick_trials_default = Message(gameDisplay, "(default value is 5)", 'freesansbold.ttf', 20,
                                      (display_width/2, display_height/2 + 20), color['blue'], white)
        
                                      
        pick_n_message.display_msg()
        pick_n_default.display_msg()
        pick_n_scale.display_scale()
        n = pick_n_scale.get_choice()
        pick_n_choice_msg = Message(gameDisplay, "You picked " + str(n) + " x " + str(n) + " grid", 'freesansbold.ttf', 25,
                                      (display_width/2, display_height/2 + 200), color['blue'], white)
        pick_n_choice_msg.display_msg()
        pick_trials_message.display_msg()
        pick_trials_default.display_msg()
        pick_trials_scale.display_scale()
        trials = pick_trials_scale.get_choice()
        pick_trials_choice_msg = Message(gameDisplay, "You picked " + str(trials) + " trials", 'freesansbold.ttf', 25,
                                      (display_width/2, display_height/2 + 250), color['blue'], white)
        pick_trials_choice_msg.display_msg()
        
       
     
        button_run.button_draw(gameDisplay)
        button_quit.button_draw(gameDisplay)
        pygame.display.update()
        clock.tick(10)


def viz_loop():
    global n
    global trials
    gameDisplay.fill(white)
    site_size = get_site_dim(n)
    count = 0
    percolation_stats = PercolationStats(n)
    get_stats = lambda : get_series_stats(percolation_stats)
    button_quit = Button(550,700, 100, 50, color['red'], color['bright_red'], "Quit", quit_viz)
    button_estimate = Button(150,700, 100, 50, color['blue'], color['light_blue'],"Estimate", get_stats)
    for k in range(trials):
        grid = SiteGrid(n, start_point, site_size, color['red'], white)
        trial = Trial(n)
        nGrid = trial.getNGrid()
        grid.display(gameDisplay)
        
        
        
        
        
        while True:
            filledUnion = nGrid.unions[0]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                button_quit.button_check(event)
                button_estimate.button_check(event)
                
                
            index = trial.getIndexFromQueue()
            trial.openSite(index)
            grid.site_grid[index-1].redraw_site(gameDisplay, white, color['red'])
          

            if nGrid.percolates():
                nGrid.unions[0].remove(0)
                nGrid.unions[0].remove(n*n+1)
                for i in nGrid.unions[0]:
                
                    grid.site_grid[i - 1].redraw_site(gameDisplay, color['blue'], white)
                    button_quit.button_draw(gameDisplay)
                    button_estimate.button_draw(gameDisplay)
                    pygame.display.update()
           
                    

                percolation_stats.add_res(trial.getNumberOfOpenSites())
                
                
                get_trial_info(grid, trial)
                button_quit.button_draw(gameDisplay)
                button_estimate.button_draw(gameDisplay)
                pygame.display.update()
                time.sleep(1)
                
                break
            if k == 0:
                continue
            get_viz_stats(percolation_stats, 20, (10,10) )
            button_quit.button_draw(gameDisplay)
            button_estimate.button_draw(gameDisplay)
            pygame.display.update()
            clock.tick(60)
    get_series_stats(percolation_stats)
   
    


viz_intro() 


        
