# def fix_wiring(cables, sockets, plugs):
#     cables_str = [c for c in cables if type(c) is str]
#     sockets_str = [s for s in sockets if type(s) is str]
#     plugs_str = [p for p in plugs if type(p) is str]
#     pairs = []
#     plug_index = 0
#     for cable, socket in zip(cables_str, sockets_str):
#         if plug_index < len(plugs_str):
#             pairs.append(
#                 f"plug {cable} into {socket} using {plugs_str[plug_index]}")
#             plug_index += 1
#         else:
#             pairs.append(f"weld {cable} to {socket} without plug")
#     return pairs

def fix_wiring(cables, sockets, plugs):
    return (f"plug {cable} into {socket} using {plugs_str[plug_index]}" if plug_index < len(plugs_str) else f"weld {cable} to {socket} without plug" for plug_index, (cable, socket) in enumerate(zip([c for c in cables if type(c) is str], [s for s in sockets if type(s) is str])) for plugs_str in [[p for p in plugs if type(p) is str]])


if __name__ == '__main__':
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
