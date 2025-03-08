from grid import Grid, GameController



def main():
    grid=Grid(10,10)
    game_controller = GameController(10,10)
    game_controller.grid.randomize(percent_alive=40)
    game_controller.run_auto()


if __name__ =='__main__':
    main()