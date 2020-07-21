def parse(kakao_text):
    p_list = []
    counter = 0

    while counter < 100:
        line = kakao_text.readline()

        if line[0:4] == '2019' and (line.find(',') != -1):
            counter = 0
            pos_y = line.find('년')
            pos_m = line.find('월')
            pos_d = line.find('일')
            pos_o = line.find('오')
            pos_t = line.find(':')
            pos_comma = line.find(',')

            m = int(line[pos_y+2: pos_m])
            d = int(line[pos_m+2: pos_d])
            t = int(line[pos_o+3:pos_t])
            mi = int(line[pos_t+1:pos_comma])
            who = line[pos_comma+2:  pos_comma+5]

            if line[pos_o+1] == '후' and t != 12:
                t = t + 12

            if line[pos_o+1] == '전' and t == 12:
                t = 0

            new_tup = (m, d, t, mi, who)
            # (월,일,시간,분,이름)
            if m >= 9:
                p_list.append(new_tup)

        else:
            counter = counter+1

    return p_list


def response_list(parsed_list, name):
    r_list = []

    for i in range(0, len(parsed_list)-1):

        if parsed_list[i][4] == name and parsed_list[i][4] != parsed_list[i+1][4]:

            if parsed_list[i+1][0] != parsed_list[i][0]:
                if parsed_list[i][0] == 2:
                    time = (((28 + parsed_list[i+1][1]-parsed_list[i][1])*24 + parsed_list[i+1][2]-parsed_list[i][2])*60
                            + parsed_list[i+1][3]-parsed_list[i][3])
                elif parsed_list[i][0] == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    time = (((31 + parsed_list[i+1][1]-parsed_list[i][1])*24 + parsed_list[i+1][2]-parsed_list[i][2])*60
                            + parsed_list[i+1][3]-parsed_list[i][3])
                else:
                    time = (((30 + parsed_list[i+1][1]-parsed_list[i][1])*24 + parsed_list[i+1][2]-parsed_list[i][2])*60
                            + parsed_list[i+1][3]-parsed_list[i][3])
            else:
                time = (((parsed_list[i+1][1]-parsed_list[i][1])*24 + parsed_list[i+1][2]-parsed_list[i][2])*60
                        + parsed_list[i+1][3]-parsed_list[i][3])

            if 10 < time <= 60*24:
                r_list.append((parsed_list[i], parsed_list[i+1], time))

    return r_list


def avg_res_time(r_list):
    s = 0
    for i in r_list:
        s = s + i[2]

    return s / len(r_list)


def time_sort(parsed_list):
    t_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in parsed_list:
        for j in range(0, 24):
            if i[2] == j:
                t_list[j] = t_list[j] + 1

    return t_list


txt = open('C:/Users/ksc/Desktop/KakaoTalkChat.txt', encoding='utf_8')

p_list = parse(txt)

t_list = time_sort(p_list)

s = 0

for i in t_list:
    s = s + i

for i in range(0, 24):
    print(i, ":", t_list[i], "(", round(t_list[i]/s*100,2), "%)")
print(s)
txt.close()
