
format_of_dictionary = {
    'add': 'r', 'and': 'r', 'or': 'r', 'srl': 'r', 'sll': 'r', 'slt': 'r', 'sra': 'r', 'sub': 'r', 'xor': 'r', 'mul': 'r', 'div': 'r', 'rem': 'r',
    'addi': 'i', 'andi': 'i', 'ori': 'i', 'lb': 'i', 'ld': 'i', 'lh': 'i', 'lw': 'i', 'jalr': 'i',
    'sb': 's', 'sw': 's', 'sh': 's','sd': 's',
    'beq': 'sb', 'bne': 'sb', 'bge': 'sb', 'blt': 'sb',
    'auipc': 'u', 'lui': 'u',
    'jal': 'uj'
}


opcode_for_dictionary = {
    'add': '0110011', 'and': '0110011', 'or': '0110011', 'srl': '0110011', 'sll': '0110011', 'slt': '0110011', 'sra': '0110011', 'sub': '0110011', 'xor': '0110011',
    'mul': '0110011', 'div': '0110011', 'rem': '0110011',
    'addi': '0010011', 'andi': '0010011', 'ori': '0010011', 'lb': '0000011', 'ld': '0000011', 'lh': '0000011', 'lw': '0000011', 'jalr': '1100111',
    'sb': '0100011', 'sw': '0100011', 'sd': '0100011', 'sh': '0100011',
    'beq': '1100011', 'bne': '1100011', 'bge': '1100011', 'blt': '1100011',
    'auipc': '0010111', 'lui': '0110111', 'jal': '1101111'
}

dictionary7 = {
    "add": "0000000", "and": "0000000", "or": "0000000", "sll": "0000000", "slt": "0000000", "sra": "0100000", "srl": "0000000", "sub": "0100000", "xor": "0000000",
    "mul": "0000001", "div": "0000001", "rem": "0000001"
}

dictionary3 = {
    "add": "000", "and": "111", "or": "110", "sll": "001", "slt": "010", "sra": "101", "srl": "101", "sub": "000", "xor": "100", "mul": "000", "div": "100", "rem": "110",
    "addi": "000", "andi": "111", "ori": "110", "lb": "000", "ld": "011", "lh": "001", "lw": "010", "jalr": "000",
    "sb": "000", "sw": "010", "sd": "011", "sh": "001",
    "beq": "000", "bne": "001", "bge": "101", "blt": "100",
    "auipc": "", "lui": "",
    "jal": ""
}


def register_getting(string):
    if (string[0] == 'x'):
        s1 = int(string[1::])
        if (-1 < s1 and s1 < 32 ):
            return format(s1, '05b')
        else:
            print ("There are only 32 registers available, and the register is not identified}.")
            return ("00000")
    elif (string[0] == 'a'):
        s1 = int(string[1::])
        if ( -1 < s1 and s1 < 8):
            return format(s1+10, '05b')
        else:
            print ("Unfortunately, the register is not Identified. Assume instead the register is a0\n")
            return ("01010")
    else:
        print ("Unfortunately, the register is not Identified.. \n")
        return ("00000")


def for_12bi_immediatet(string):
    if(len(string) > 1):
        if(string[0] == '0' and string[1] == 'x'):
            if(len(string) > 5):
                print ("Immediate value should be 12 bit wide, problem is immediate value is out of range {Range: [-2048,2047]}.")
                return ("000000000000")
            else:
                return bin(int(string[2::], 16))[2::].zfill(12) 
        elif (string[0] == '-'): 
            n = int(string[1::])
            if (n<2049):
                n = 2**12 - n
                return (format(n, '012b'))
            else:
                print ("Immediate value should be 12 bit wide, problem is immediate value is out of range {Range: [-2048,2047]}.")
                return ("000000000000")
        else:
            check_of_mic = int(string)
            if (check_of_mic < 2048):
                return (format(int(string), '012b'))
            else:
                print ("Immediate value should be 12 bit wide, problem is immediate value is out of range {Range: [-2048,2047]}.")
                return ("000000000000")
    else:
        if (len(string) == 1):
            if (string[0] != '0' and string[0] != '1' and string[0] != '2' and string[0] != '3' and string[0] != '4' and string[0] != '5' and string[0] != '6' and string[0] != '7' and string[0] != '8' and string[0] != '9'):
                print ("Immediate value must be a digit {Range: [-2048,2047]}.")
                return ("000000000000")
        check_of_mic = int(string)
        if (check_of_mic < 2048):
            return (format(int(string), '012b'))
        else:
            print ("Immediate value should be 12 bit wide, problem is immediate value is out of range {Range: [-2048,2047]}.")
            return ("000000000000")


def for_20bit_immediate(string):
    if(len(string) > 1):
        if(string[0] == '0' and string[1] == 'x'):
            if(len(string) > 7):
                return ("Immediate value of range, must be 20 bit wide {Range: [-524288,524287]}.")
                return ("00000000000000000000")
            else: 
                return bin(int(string[2::], 16))[2::].zfill(20)
        elif(string[0] == '-'):
            n = int(string[1::])
            if (n < 524289):
                n = 2**20 - n
                return format(n, '020b')
            else:
                return ("Immediate value of range, must be 20 bit wide {Range: [-524288,524287]}.")
                return ("00000000000000000000")
        else:
            bigcheck_of_mic = int(string)
            if (bigcheck_of_mic < 524288):
                return format(int(string), '020b')
            else:
                print ("Immediate value of range, must be 20 bit wide {Range: [-524288,524287]}.")
                return ("00000000000000000000")
    else:
        if (len(string) == 1):
            if (string[0] != '0' and string[0] != '1' and string[0] != '2' and string[0] != '3' and string[0] != '4' and string[0] != '5' and string[0] != '6' and string[0] != '7' and string[0] != '8' and string[0] != '9'):
                print ("Immediate value must be a digit {Range: [-524288,524287]}.")
                return ("00000000000000000000")
        bigcheck_of_mic = int(string)
        if (bigcheck_of_mic < 524288):
            return format(int(string), '020b')
        else:
            print ("Immediate value of range, must be 20 bit wide {Range: [-524288,524287]}. ")
            return ("00000000000000000000")


def for_mc_getting(l, pc, labels,data):
    if(format_of_dictionary.get(l[0],-1)==-1):
        print("incorrect command",l[0],end='')
        return -2,-2,''
    elif format_of_dictionary[l[0]] == 'r':
       
        exp = 4
        land = len(l)
        if (land != exp):
            print ("Expected",exp - 1,"arguments but received",land - 1,end='')
            return -2,-2,''
        f7 = dictionary7[l[0]]
        f3 = dictionary3[l[0]]
        rd = register_getting(l[1])
        rs1 = register_getting(l[2])
        rs2 = register_getting(l[3])
        opcode = opcode_for_dictionary[l[0]]
        mc = f7 + rs2 + rs1 + f3 + rd + opcode
        return '%#010x' % (int('0b'+mc, 0)),-1,l[0]+" "+l[1]+" "+l[2]+" "+l[3]+"   "
    if(format_of_dictionary[l[0]] == 'i'):
        exp = 4
        land = len(l)
        if (land != exp and data.get(l[2],-1)==-1):
            print ("Expected",exp - 1,"arguments but received",land - 1,end='')
            return -2,-2,''
        rd = register_getting(l[1])
        opcode = opcode_for_dictionary[l[0]]
        f3 = dictionary3[l[0]]
        if(opcode !='0000011'): 
            rs1 = register_getting(l[2])
            imm = for_12bi_immediatet(l[3])
        else: 
            if(len(l)==4):
                rs1 = register_getting(l[2])
                imm = for_12bi_immediatet(str(l[3]))
            elif(len(l)==3 and data.get(l[2],-1)!=-1):
                new_l = ['auipc',l[1],'0x10000']

                mc1 = for_mc_getting(new_l,pc,labels,data)
                print(mc1[2])
                pc+=4
                new_l = [l[0],l[1],l[1],int(data[l[2]],16) - 268435456 - pc + 4] 
                mc2 = for_mc_getting(new_l,pc,labels,data)
                return mc1[0],mc2[0],mc1[2]+" $ "+l[0]+" "+ l[1]+" " + str(int(data[l[2]],16) - 268435456 - pc + 4) +"("+l[1]+")"
            else:
                print("instruction has incorrect format. either",l[2],"not defined, or could be more than expected number of parameters passed")
        mc = imm + rs1 + f3 + rd + opcode
        rep = l[0] +" "+ l[1]+ " " +l[2]+ " " +l[3]+ "   "
        if(opcode=='0000011'):
            rep = str(l[0])+" "+str(l[1])+" "+str(l[3])+"("+l[2]+")   "
        return '%#010x' % (int('0b'+mc, 0)),-1,rep
    if(format_of_dictionary[l[0]] == 's'):
        exp = 4
        land = len(l)
        if (land != exp):
            print ("Expected",exp - 1,"arguments, however received",land - 1,end='')
            return -2,-2,''
        imm = for_12bi_immediatet(l[3])
        rs1 = register_getting(l[2])
        rs2 = register_getting(l[1])
        f3 = dictionary3[l[0]]
        opcode = opcode_for_dictionary[l[0]]
        mc = imm[0:7:] + rs2 + rs1 + f3 + imm[7::] + opcode
        return '%#010x' % (int('0b'+mc, 0)),-1,l[0] + " "+l[1]+" "+l[3]+"("+l[2]+")   "
    elif(format_of_dictionary[l[0]] == 'sb'):
        exp = 4
        land = len(l)
        if (land != exp):
            print ("Expected",exp - 1,"arguments, however received",land - 1,end='')
            return -2,-2,''
        imm = int((labels[l[3]]*4 - pc)/2)
        rs1 = register_getting(l[1])
        rs2 = register_getting(l[2])
        f3 = dictionary3[l[0]]
        opcode = opcode_for_dictionary[l[0]]
        if(str(imm)[0] != '-'):
            imm = format(int(imm), '#014b')[2::]
        else:
            imm = format(2**12 - abs(int(imm)), '#014b')[2::]
        mc = imm[0] + imm[2:8:] + rs2 + rs1 + f3 + imm[8::] + imm[1] + opcode
        return '%#010x' % (int('0b'+mc, 0)),-1,l[0]+" "+l[1]+" "+l[2]+" "+str((labels[l[3]]*4 - pc))+"   "
    if(format_of_dictionary[l[0]] == 'u'):
        exp = 3
        land = len(l)
        if (land != exp):
            print ("Expected",exp - 1,"arguments, however received",land - 1,end='')
            return -2,-2,''
        imm = for_20bit_immediate(l[2])
        rd = register_getting(l[1])
        opcode = opcode_for_dictionary[l[0]]
        mc = imm+rd+opcode
        tttt = l[2]
        if(l[2][0]=='0' and l[2][1]=='x'):
            tttt = int(l[2],16)
        return '%#010x' % (int('0b'+mc, 0)),-1,l[0]+" "+l[1]+" "+str(tttt)+"  "
    if(format_of_dictionary[l[0]] == 'uj'): 
        exp = 3
        land = len(l)
        if (land != exp):
            print ("Expected",exp - 1,"arguments, however received",land - 1,end='')
            return -2,-2,''
        opcode = opcode_for_dictionary[l[0]]
        rd = register_getting(l[1])
        imm = int(labels[l[2]])*4 - pc
        tttt = imm
        if(str(imm)[0] != '-'):
            imm = format(imm, "#022b")[2::]
        else:
            imm = format(2**20 - abs(imm), '#022b')[2::]
        imm = imm[0] + imm[0:19]
        imm = imm[0] + imm[10::] + imm[9] + imm[1:9:]
        mc = str(imm) + rd + opcode
        return '%#010x' % (int('0b'+mc, 0)),-1,l[0]+" "+l[1]+" "+str(tttt)+"   "


def for_conversion_to_MC(instruction, labels,datas):
    instructionAddress = 0
    for x in instruction:
        flag = False
        if(x.strip("\r\n") == "" or x.strip()==''):
            print("Empty line encountered meaning no instruction found here")
            continue
        
        s = str(x)
        s = s.strip("\r\n")
        s = s.strip()
        l = []
        s = s.replace(",", " ")
        s = s.replace(":", " ")
        if (s.count('(') != 0):
            flag = True
            s = s.replace("(", " ")
            s = s.replace(")", "")
        l = s.split()
        if flag == True:
            l[2], l[3] = l[3], l[2]
            s = l[0]+" " + l[1] + " " + l[2] + " " + l[3]
        
        machineCode1,machineCode2,basicCode = for_mc_getting(l, instructionAddress, labels,datas)



def getDirectives_function():
    rf = open("test.asm", "r")
    file = rf.read()
    s = ''
    ins = []
    textsegment = True
    labels = {}
    data = {}
    tocheck = []
    for x in file:
        if(x == '\n'):
            if(s.strip(" \r\n") != '' or s.strip()!=''):
                if(s.find("#")!=-1):
                    s=s[0:s.find('#'):]
                if(s.strip() == '.data'):
                    textsegment = False
                elif(s.strip()== '.text'):
                    textsegment = True
                elif(s.find(":") != -1 and textsegment == True):
                    labels[s[0: s.find(":"):].strip()] = len(ins)
                    if(s[s.find(":")+1::].strip().replace(" ", "") != ''):
                        ins.append(s[s.find(":")+1::])
                elif(textsegment==True):
                    ins.append(s)
                    y = s
                    y = y.replace(",",' ')
                    y = y.strip()
                    yy = y.split()
                    if(len(yy)==3 and data.get(yy[2],-1)!=-1):
                        tocheck.append(len(ins))
                elif(textsegment==False):
                    s=s.strip()
                    dd = s.split(":")
                    dd[0]=dd[0].strip()
                    dd[1]=dd[1].strip()
                    dd.append(dd[1][dd[1].find(" ")::].strip())
                    
                    dd[1] = dd[1][:dd[1].find(" "):].strip()
                    dd[2] = dd[2].replace('"','')
                    data[dd[0]] = dd[1],dd[2]
                    address_for_stored_variable = M.add_data(data[dd[0]][0],data[dd[0]][1])
                    data[dd[0]] = address_for_stored_variable
            s = ''
        else:
            s += x
    if(s.strip("\r\n") != '' or s.strip()!=''):  
        s=s.strip()
        if(textsegment == False and s.find(':')!=-1 and s.strip('\r\n')!='.data' and s.strip('\r\n')!='.text'):
            s=s.strip()
            dd = s.split(":")
            dd[0]=dd[0].strip()
            dd[1]=dd[1].strip()
            dd.append(dd[1][dd[1].find(" ")::].strip())
            dd[1] = dd[1][:dd[1].find(" "):].strip()
            dd[2] = dd[2].replace('"','')
            data[dd[0]] = dd[1],dd[2]
            address_for_stored_variable = M.add_data(data[dd[0]][0],data[dd[0]][1])
            data[dd[0]] = address_for_stored_variable
        elif(textsegment == True and s.find(':')==-1 and s.strip('\r\n')!='.data' and s.strip('\r\n')!='.text'):
            ins.append(s)
        elif(s.find(":") != -1 and textsegment == True and s.strip('\r\n')!='.data' and s.strip('\r\n')!='.text'):
            labels[s[0: s.find(":"):].replace(" ",'')] = len(ins)
            if(s[s.find(":")+1::].strip("\r\n").replace(" ","")!=''):
                ins.append(s[s.find(":")+1::])
            

    rf.close()
    

    for o in tocheck:
        for k in labels.keys():
  
            if((labels[k])>=o):
                labels[k]+=1
     
    
    
    return ins, labels , data

instructions, labela,dataa = getDirectives_function() 
for_conversion_to_MC(instructions, labela,dataa)


