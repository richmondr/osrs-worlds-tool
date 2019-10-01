import subprocess

WORLDS =    [5,6,7,13,14,15,19,20,21,22,23,
            24,29,30,31,32,37,38,39,40,46,47,
            48,53,54,55,56,57,61,62,69,70,74,77,
            78,86,115,116,120,121,122,128,129,144,
            145,146,167,191,192,193,194,195,196]

lowest_ping = 1000
lowest_ping_world = -1

for i in range(len(WORLDS)):
    cmd_string = "ping oldschool" + str(WORLDS[i]) + ".runescape.com"
    raw_output_string = subprocess.check_output(cmd_string, shell=True)
    average_ping = int(raw_output_string.split()[-1][:-2])
    #print(average_ping)

    if average_ping < lowest_ping:
        lowest_ping = average_ping
        lowest_ping_world = WORLDS[i]

print("\nLowest ping: World " + str(lowest_ping_world) + ", Ping " + str(lowest_ping) + "ms")
