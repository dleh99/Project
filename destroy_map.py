import game_world
import server

def destroy():
    game_world.objects[server.Door_num].clear()             # 문 파괴 훠훠
    game_world.objects[server.Obs_num].clear()              # 장애물 파괴
    game_world.objects[server.Background_num].clear()       # 타일 파괴
    game_world.objects[server.Tear_num].clear()             # 눈물 파괴
    game_world.objects[server.Item_num].clear()             # 아이템 파괴
    server.do = 0
    server.doors.clear()                                    # 문 리스트 정리
    server.tile.clear()                                     # 타일 리스트 정리