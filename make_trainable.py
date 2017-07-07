import os


def time_to_frame(time, framerate):
    h, m, s = time.split(':')
    seconds = float(s) + 60*int(m) + (60*60*int(h))
    return int(seconds * framerate)


def parse_vtt(lines):
    lines = list(lines)
    data = []
    if len(lines) > 3:
        lang = lines[2].strip()
        if lang == 'Language: en':
            times = []
            buf = []
            for line in lines[2:]:
                if line.strip() == '':
                    data.append((times,
                                 path,
                                 ' '.join(buf)))
                    buf, times = [], []
                else:
                    if ' --> ' in line:
                        start, stop = line.split(' --> ')
                        times.append((start, stop))
                    else:
                        buf.append(line.strip())
    return data


RAW = 'raw'
dialogues = []
errcount = 0
for file in os.listdir(RAW):
    path = os.path.join(RAW, file)
    is_wav = file.split('.')[-1] == 'wav'
    if not is_wav:
        try:
            with open(path, 'r') as fl:
                dialogues.append(len(parse_vtt(fl.readlines())))
        except:
            errcount += 1
print(sum(dialogues) / len(dialogues))
print(sum(dialogues))
print(errcount)
print(len(os.listdir(RAW)))
