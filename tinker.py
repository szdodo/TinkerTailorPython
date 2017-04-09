class Tinker:

    def game(self,players,counter):
        player_list=list(range(1,players+1))
        excluded=[]
        starter=0
        while len(player_list)>1:
            starter=(starter+counter-1) % len(player_list)
            excluded.append(player_list[starter])
            player_list.remove(player_list[starter])
        excluded.append(player_list[0])
        print("ex:",excluded)
        print("winner:",player_list)

game=Tinker()
game.game(5,3)



