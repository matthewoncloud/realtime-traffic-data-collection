
from datetime import datetime

N = 0
N1 = 0
N1_LIGHT = 0
N1_MEDIUM = 0
N1_HEAVY = 0
N1_BUS = 0
N1_MOTO = 0
N2 = 0
N2_LIGHT = 0
N2_MEDIUM = 0
N2_HEAVY = 0
N2_BUS = 0
N2_MOTO = 0
N3 = 0
N3_LIGHT = 0
N3_MEDIUM = 0
N3_HEAVY = 0
N3_BUS = 0
N3_MOTO = 0
NX = 0
NX_LIGHT = 0
NX_MEDIUM = 0
NX_HEAVY = 0
NX_BUS = 0
NX_MOTO = 0

S = 0
S1 = 0
S1_LIGHT = 0
S1_MEDIUM = 0
S1_HEAVY = 0
S1_BUS = 0
S1_MOTO = 0
S2 = 0
S2_LIGHT = 0
S2_MEDIUM = 0
S2_HEAVY = 0
S2_BUS = 0
S2_MOTO = 0
S3 = 0
S3_LIGHT = 0
S3_MEDIUM = 0
S3_HEAVY = 0
S3_BUS = 0
S3_MOTO = 0
SX = 0
SX_LIGHT = 0
SX_MEDIUM = 0
SX_HEAVY = 0
SX_BUS = 0
SX_MOTO = 0

ID_COUNTED = []

CONFIDENCES = []


start_time = datetime.now()
end_time = datetime.now()
truth = {}

def reset(filename,vc):
    # FILE_NAME="/Users/matthew/Jupyter/Thesis/Outputs/Loop/TEST.txt"
    file = open(filename, "w")
    file.write("FRM \t ID \t CLS \t CNF \t LANE \t BBx\n------\t-------\t-------\t-------\t-------\t-------\n")
    file.close()
    global N, N1, N1_LIGHT, N1_MEDIUM, N1_HEAVY, N1_BUS, N1_MOTO, N2, N2_LIGHT, N2_MEDIUM, N2_HEAVY, N2_BUS, N2_MOTO, N3, N3_LIGHT, N3_MEDIUM, N3_HEAVY, N3_BUS, N3_MOTO, NX, NX_LIGHT, NX_MEDIUM, NX_HEAVY, NX_BUS, NX_MOTO, S, S1, S1_LIGHT, S1_MEDIUM, S1_HEAVY, S1_BUS, S1_MOTO, S2, S2_LIGHT, S2_MEDIUM, S2_HEAVY, S2_BUS, S2_MOTO, S3, S3_LIGHT, S3_MEDIUM, S3_HEAVY, S3_BUS, S3_MOTO, SX, SX_LIGHT, SX_MEDIUM, SX_HEAVY, SX_BUS, SX_MOTO, ID_COUNTED, start_time, end_time, truth
    #
    truth = vc
    start_time = datetime.now()
    N = 0
    N1 = 0
    N1_LIGHT = 0
    N1_MEDIUM = 0
    N1_HEAVY = 0
    N1_BUS = 0
    N1_MOTO = 0
    N2 = 0
    N2_LIGHT = 0
    N2_MEDIUM = 0
    N2_HEAVY = 0
    N2_BUS = 0
    N2_MOTO = 0
    N3 = 0
    N3_LIGHT = 0
    N3_MEDIUM = 0
    N3_HEAVY = 0
    N3_BUS = 0
    N3_MOTO = 0
    NX = 0
    NX_LIGHT = 0
    NX_MEDIUM = 0
    NX_HEAVY = 0
    NX_BUS = 0
    NX_MOTO = 0

    S = 0
    S1 = 0
    S1_LIGHT = 0
    S1_MEDIUM = 0
    S1_HEAVY = 0
    S1_BUS = 0
    S1_MOTO = 0
    S2 = 0
    S2_LIGHT = 0
    S2_MEDIUM = 0
    S2_HEAVY = 0
    S2_BUS = 0
    S2_MOTO = 0
    S3 = 0
    S3_LIGHT = 0
    S3_MEDIUM = 0
    S3_HEAVY = 0
    S3_BUS = 0
    S3_MOTO = 0
    SX = 0
    SX_LIGHT = 0
    SX_MEDIUM = 0
    SX_HEAVY = 0
    SX_BUS = 0
    SX_MOTO = 0

    ID_COUNTED = [] 

    CONFIDENCES = []


def update(img, frm, x, y, h, w, id, cls, conf, lane, sp=0):

    # if id in ID_COUNTED:
    #     # print(f"\nDouble Counting Prevented. ID {id}")
    #     return False
    # else:
    #     ID_COUNTED.append(id)

    CONFIDENCES.append(conf)
        
    weight = h * w
    bbx_thres = 3000
    if "DC" in FILE_NAME or "NC" in FILE_NAME:
        bbx_thres = 3500
        
    if cls=="car":
        cls = "LIGHT"
    elif cls=="truck":
        if w * h < bbx_thres:
            cls = "LIGHT"
        else:
            cls = "HEAVY"
    elif cls=="bus":
        if w * h < bbx_thres:
            cls = "LIGHT"
        else:
            cls = "BUS"
    elif cls=="motorcycle":
        cls = "MOTO"
    
    #  DYNAMIC VARIABLE NAME
    lane_cls = f"{lane}_{cls}"
    try:
        globals()[lane[0]] += 1
        globals()[lane] += 1
        globals()[lane_cls] += 1
    except KeyError:
        print(f"Invalid variable name: {lane_cls}")

    #  WRITE TO FILE
    file = open(FILE_NAME, "a")
    file.write(str(frm) + " \t " + str(id) + " \t " + str(cls) + " \t " + str(int(conf*100)) + " \t " + str(lane) + " \t " + str(weight) + "\n")
    file.close()

    return True

def end():
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    file = open(FILE_NAME, "a")
    file.write("\n-------------\n")
    file.write("-------------\n")
    file.write("SUMMARY\n")
    file.write("-------------\n")
    file.write("Total Vehicles: " + str(N+S) + "\n")
    file.write("-------------\n")
    file.write("Northbound\n")
    file.write("-------------\n")
    file.write("Northbound Total: " + str(N) + "\n")
    file.write("N1 Total: " + str(N1) + ", Light: " + str(N1_LIGHT) + ", Heavy: " + str(N1_HEAVY) + ", Bus: " + str(N1_BUS) + ", Motorcycle: " + str(N1_MOTO) + "\n")
    file.write("N2 Total: " + str(N2) + ", Light: " + str(N2_LIGHT) + ", Heavy: " + str(N2_HEAVY) + ", Bus: " + str(N2_BUS) + ", Motorcycle: " + str(N2_MOTO) + "\n")
    file.write("N3 Total: " + str(N3) + ", Light: " + str(N3_LIGHT) + ", Heavy: " + str(N3_HEAVY) + ", Bus: " + str(N3_BUS) + ", Motorcycle: " + str(N3_MOTO) + "\n")
    # file.write("NX Total: " + str(NX) + ", Light: " + str(NX_LIGHT) + ", Heavy: " + str(NX_HEAVY) + ", Bus: " + str(NX_BUS) + ", Motorcycle: " + str(NX_MOTO) + "\n")
    file.write("-------------\n")
    file.write("Southbound\n")
    file.write("-------------\n")
    file.write("Southbound Total: " + str(S) + "\n")
    file.write("S1 Total: " + str(S1) + ", Light: " + str(S1_LIGHT) + ", Heavy: " + str(S1_HEAVY) + ", Bus: " + str(S1_BUS) + ", Motorcycle: " + str(S1_MOTO) + "\n")
    file.write("S2 Total: " + str(S2) + ", Light: " + str(S2_LIGHT) + ", Heavy: " + str(S2_HEAVY) + ", Bus: " + str(S2_BUS) + ", Motorcycle: " + str(S2_MOTO) + "\n")
    file.write("S3 Total: " + str(S3) + ", Light: " + str(S3_LIGHT) + ", Heavy: " + str(S3_HEAVY) + ", Bus: " + str(S3_BUS) + ", Motorcycle: " + str(S3_MOTO) + "\n")
    # file.write("SX Total: " + str(SX) + ", Light: " + str(SX_LIGHT) + ", Heavy: " + str(SX_HEAVY) + ", Bus: " + str(SX_BUS) + ", Motorcycle: " + str(SX_MOTO) + "\n")
    file.write("-------------\n")
    file.write(f"{FILE_NAME.split('/')[-1]}\n")
    file.write(f"Execution time: {elapsed_time}\n")
    avg_conf = sum(CONFIDENCES) / len(CONFIDENCES)
    file.write(f"Confidence: {avg_conf * 100:.2f}%\n")

    accuracy_count = (N+S)/(truth['total'])
    file.write(f"Count: {accuracy_count * 100:.2f}%\n")

    total_light = N1_LIGHT+N2_LIGHT+N3_LIGHT+S1_LIGHT+S2_LIGHT+S3_LIGHT
    total_heavy = N1_HEAVY+N2_HEAVY+N3_HEAVY+S1_HEAVY+S2_HEAVY+S3_HEAVY
    total_bus = N1_BUS+N2_BUS+N3_BUS+S1_BUS+S2_BUS+S3_BUS
    total_moto = N1_MOTO+N2_MOTO+N3_MOTO+S1_MOTO+S2_MOTO+S3_MOTO
    accuracy_class_light = acc(total_light, truth['total_light'])
    accuracy_class_heavy = acc(total_heavy, truth['total_heavy'])
    accuracy_class_bus = acc(total_bus, truth['total_bus'])
    accuracy_class_moto = acc(total_moto, truth['total_moto'])
    accuracy_class_weighted_light = accuracy_class_light * total_light
    accuracy_class_weighted_heavy = accuracy_class_heavy * total_heavy
    accuracy_class_weighted_bus = accuracy_class_bus * total_bus
    accuracy_class_weighted_moto = accuracy_class_moto * total_moto
    accuracy_class_weighted_average = (accuracy_class_weighted_light+accuracy_class_weighted_heavy+accuracy_class_weighted_bus+accuracy_class_weighted_moto)/(N+S)
    file.write(f"Class: {accuracy_class_weighted_average * 100:.2f}%\n")
    file.write(f"Light: {accuracy_class_light * 100:.2f}%\n")
    file.write(f"Heavy: {accuracy_class_heavy * 100:.2f}%\n")
    file.write(f"Bus: {accuracy_class_bus * 100:.2f}%\n")
    file.write(f"Moto: {accuracy_class_moto * 100:.2f}%\n")

    accuracy_lane_n1 = acc(N1,truth['n1']['total'])
    accuracy_lane_n2 = acc(N2,truth['n2']['total'])
    accuracy_lane_n3 = acc(N3,truth['n3']['total'])
    accuracy_lane_s1 = acc(S1,truth['s1']['total'])
    accuracy_lane_s2 = acc(S2,truth['s2']['total'])
    accuracy_lane_s3 = acc(S3,truth['s3']['total'])
    accuracy_lane_avg = (accuracy_lane_n1+accuracy_lane_n2+accuracy_lane_n3+accuracy_lane_s1+accuracy_lane_s2+accuracy_lane_s3)/6
    file.write(f"Lane Accuracy: {accuracy_lane_avg * 100:.2f}%\n")


    # file.write("Northbound average speed :\t" + str(self.exceeded) + "\n")
    # file.write("Southbound average speed :\t" + str(self.exceeded) + "\n")
    file.close()

def progressbar(current, total, bar_length=50, fill_char='▓', empty_char='░'):
    
    percent = (current / total) * 100
    filled_length = int(bar_length * percent / 100)
    empty_length = bar_length - filled_length

    bar = fill_char * filled_length + empty_char * empty_length
    percent_str = f"{percent:.2f}%"

    print(f"\r ({current}/{total})\tN: {N}\tS: {S}\t{percent_str}\t{bar}", end="")

    if current == total:
        print()  # Print a newline to complete the progress bar

def acc(pred, grnd):
    if pred == 0 and grnd == 0:
        return 1
    elif grnd == 0 and pred != 0:
        return 0
    else:
        return pred/grnd