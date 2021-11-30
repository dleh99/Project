import game_world
import server

def destroy():
    game_world.objects[5].clear()       # 문 파괴 훠훠
    game_world.objects[4].clear()       # 장애물 파괴
    game_world.objects[0].clear()       # 타일 파괴
    server.doors.clear()                # 문 리스트 정리
    server.tile.clear()                 # 타일 리스트 정리