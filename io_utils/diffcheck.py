import os
from decimal import *
getcontext().prec=100
good = "\\<green>"
bad = "\\<red__>"
clear = "\\<clear>"
bold = "\\<bold_>"
def evaluate_output(directory, input_name):
    ans, out = f"{directory}{input_name}.ans",f"{directory}{input_name}.out" 
    ans_exists = os.path.isfile(ans)
    out_exists = os.path.isfile(out)
    if not ans_exists or not out_exists:
        adne = f"{input_name}.ans does not exist"
        odne = f"{input_name}.out does not exist"
        if not ans_exists and not out_exists:
            return "\\<red__>neither .ans nor .out exists\\<clear>", adne, odne
        if not ans_exists:
            return "\\<green>no solution\\<clear>", adne, open(out).read().strip()
        if not os.path.isfile(out):
            return "\\<red__>no output\\<clear>", open(ans).read().strip(), odne
    return diff_text(open(ans).read().strip(), open(out).read().strip())

def check_int(s):
    if not s:
        return False
    if s[0] == '-':
        return s[1:].isdigit()
    return s.isdigit()

def diff_text(correct, output):
    a = correct.split('\n')
    o = output.split('\n')
    wa = bad + "wrong answer" + clear
    float_difference = 0
    c = True
    left, right = [], []
    if len(a) != len(o):
        if not output:
            output = "\\<itali>empty.\\<clear>"
        return wa, correct, output

    for i in range(len(a)):
        l = a[i].split()
        r = o[i].split()
        if len(l) != len(r):
            c = False
            left.append(good+a[i]+clear)
            right.append(bad+o[i]+clear)
        else:
            lline,rline = [], []
            for token_a, token_b in zip(l,r):
                if token_a != token_b:
                    if check_int(token_a) or check_int(token_b):
                        c = False
                    else:
                        try:
                            fa = Decimal(token_a)
                            fb = Decimal(token_b)
                            float_difference = max(float_difference, abs(fa-fb))
                            if float_difference > Decimal(.5):
                                c = False
                        except:
                            c = False
                    ta,tb=[],[]
                    for i in range(max(len(token_a), len(token_b))):
                        if i >= len(token_a):
                            tb.append(bad+bold+token_b[i]+clear)
                        elif i >= len(token_b):
                            ta.append(good+bold+token_a[i]+clear)
                        else:
                            if token_a[i]==token_b[i]:
                                ta.append(token_a[i])
                                tb.append(token_a[i])
                            else:
                                ta.append(good+bold+token_a[i]+clear)
                                tb.append(bad+bold+token_b[i]+clear)
                    lline.append(''.join(ta))
                    rline.append(''.join(tb))

                else:
                    lline.append(token_a)
                    rline.append(token_b)
            left.append(' '.join(lline))
            right.append(' '.join(rline))
    left = '\n'.join(left)
    right = '\n'.join(right)
    if c:
        if float_difference != 0:
            pow = 0
            while float_difference < 1:
                float_difference *= 10
                pow -=1
            return good + f"passed \\<dim__>±{int(float_difference)}e{pow}" + clear, left, right
        return good + "passed" + clear, left, right
    else:
        return wa, left, right
def evaluate_last_line(directory, input_name):
    ans, out = f"{directory}{input_name}.ans",f"{directory}{input_name}.out" 
    ans_exists = os.path.isfile(ans)
    out_exists = os.path.isfile(out)
    if not ans_exists or not out_exists:
        adne = f"{input_name}.ans does not exist"
        odne = f"{input_name}.out does not exist"
        if not ans_exists and not out_exists:
            return "\\<red__>neither .ans nor .out exists\\<clear>", adne, odne
        if not ans_exists:
            return "\\<green>no solution\\<clear>", adne, open(out).read().strip()
        if not os.path.isfile(out):
            return "\\<red__>no output\\<clear>", open(ans).read().strip(), odne
    lla=open(ans).read().strip().split('\n')[-1]
    llo=open(out).read().strip().split('\n')[-1]
    return diff_text(lla, llo)
