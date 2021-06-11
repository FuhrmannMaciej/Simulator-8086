from tkinter import *
from variables import InputField
from itertools import chain
from queue import LifoQueue

root = Tk()
root.title("Simulator 8086")

axValue = InputField()
bxValue = InputField()
cxValue = InputField()
dxValue = InputField()

axInput = Entry(root, width=7)
bxInput = Entry(root, width=7)
cxInput = Entry(root, width=7)
dxInput = Entry(root, width=7)

siValue = InputField()
diValue = InputField()
bpValue = InputField()
spValue = InputField()

siInput = Entry(root, width=7)
diInput = Entry(root, width=7)
bpInput = Entry(root, width=7)
# spInput = Entry(root, width=7)

displaceValue = InputField()

MAX_4_HEX = int('FFFF',16)
MIN_4_HEX = int('0000',16)

memory = []

stack = LifoQueue(maxsize=MAX_4_HEX)

registers = {'AX': axValue, 'BX': bxValue, 'CX': cxValue, 'DX': dxValue}

inputs = {'AX': axInput, 'BX': bxInput, 'CX': cxInput, 'DX': dxInput}

index_registers = {'SI': siValue, 'DI': diValue, 'BP': bpValue, 'SP': spValue}

index_inputs = {'SI': siInput, 'DI': diInput, 'BP': bpInput}

all_registers = dict(chain.from_iterable(d.items() for d in (registers, index_registers)))


def move_registry_memory():
    memory_index = get_memory_index()
    if memory_index >= MAX_4_HEX:
        memory_index = 0
    if registerMemoryDirection.get() == 'RM':
        value = registers[toMemoryOrRegister.get()].get()
        memory[memory_index] = value
    elif registerMemoryDirection.get() == 'MR':
        value = memory[memory_index]
        registers[toMemoryOrRegister.get()].set(value)

def exchange_registry_memory():
    memory_index = get_memory_index()
    if memory_index >= MAX_4_HEX:
        memory_index = 0
    value = registers[toMemoryOrRegister.get()].get()
    temp = memory[memory_index]
    memory[memory_index] = value
    registers[toMemoryOrRegister.get()].set(temp)


def get_memory_index():

    if addressType.get() == 'I':
        return to_hex_number(index_registers[indexTypeValue.get()].get())
    elif addressType.get() == 'B':
        return to_hex_number(all_registers[baseTypeValue.get()].get())
    elif addressType.get() == 'IB':
        first_register_name = indexBaseTypeValue.get()[0:2]
        second_register_name = indexBaseTypeValue.get()[2:4]
        return sum_hex(all_registers[first_register_name].get(), all_registers[second_register_name].get())

def to_hex_number(hex_str):
    return int(hex_str,16) + int(displaceValue.get(), 16)

def sum_hex(hex1, hex2):
    max_value = MAX_4_HEX + 1
    result_num = ((int(hex1,16) + int(hex2,16)) % max_value) + int(displaceValue.get(), 16)
    return result_num

def to_hex_string(num):
    result_str = hex(num)[2:]
    number_of_prefix_zeros = 4 - len(result_str)
    prefix_zeros = ''
    for i in range(number_of_prefix_zeros):
        prefix_zeros += '0'
    return prefix_zeros + result_str

def init_memory():
    for i in range(MAX_4_HEX):
        memory.append('0000')

def saveRegisterValues():
    for name, input in inputs.items():
        input_value = input.get()
        if len(input_value) == 4:
            registers[name].set(input_value)
            input.delete(0,END)

def resetRegisterValues():
    for register in registers.values():
        register.reset()

def moveRegisterValue():

    to_value = registers[toRegister.get()].get()
    registers[fromRegister.get()].set(to_value)


def exchangeRegisterValue():

    from_value = registers[fromRegister.get()].get()
    to_value = registers[toRegister.get()].get()
    registers[toRegister.get()].set(from_value)
    registers[fromRegister.get()].set(to_value)

init_memory()

axLabel = Label(root, text="AX").grid(row=0, column=0, pady=5)
bxLabel = Label(root, text="BX").grid(row=1, column=0, pady=5)
cxLabel = Label(root, text="CX").grid(row=2, column=0, pady=5)
dxLabel = Label(root, text="DX").grid(row=3, column=0, pady=5)

ax = Entry(root, width=7, textvariable=axValue, state="readonly")
bx = Entry(root, width=7, textvariable=bxValue, state="readonly")
cx = Entry(root, width=7, textvariable=cxValue, state="readonly")
dx = Entry(root, width=7, textvariable=dxValue, state="readonly")

ax.grid(row=0, column=1, pady=5, padx= 3)
bx.grid(row=1, column=1, pady=5, padx= 3)
cx.grid(row=2, column=1, pady=5, padx= 3)
dx.grid(row=3, column=1, pady=5, padx= 3)

axInput.grid(row=0, column=2, pady=5, padx= 3)
bxInput.grid(row=1, column=2, pady=5, padx= 3)
cxInput.grid(row=2, column=2, pady=5, padx= 3)
dxInput.grid(row=3, column=2, pady=5, padx= 3)

resetButton = Button(root, text="Reset", command=resetRegisterValues).grid(row=4, column=1)
saveButton = Button(root, text="Save", command=saveRegisterValues).grid(row=4, column=2)

fromRegister = StringVar()
fromRegister.set("AX")

fromAx = Radiobutton(root,variable=fromRegister, text="AX", value="AX").grid(row=5, column=1, pady=5, padx= 3)
fromBx = Radiobutton(root,variable=fromRegister, text="BX", value="BX").grid(row=6, column=1, pady=5, padx= 3)
fromCx = Radiobutton(root,variable=fromRegister, text="CX", value="CX").grid(row=7, column=1, pady=5, padx= 3)
fromDx = Radiobutton(root,variable=fromRegister, text="DX", value="DX").grid(row=8, column=1, pady=5, padx= 3)

toRegister = StringVar()
toRegister.set("AX")

toAx = Radiobutton(root,variable=toRegister, text="AX", value="AX").grid(row=5, column=2, pady=5, padx= 3)
toBx = Radiobutton(root,variable=toRegister, text="BX", value="BX").grid(row=6, column=2, pady=5, padx= 3)
toCx = Radiobutton(root,variable=toRegister, text="CX", value="CX").grid(row=7, column=2, pady=5, padx= 3)
toDx = Radiobutton(root,variable=toRegister, text="DX", value="DX").grid(row=8, column=2, pady=5, padx= 3)

movRegister = Button(root, text="MOV", command=moveRegisterValue).grid(row=9, column=1, pady=5, padx= 3)
xchgRegister = Button(root, text="XCHG", command=exchangeRegisterValue).grid(row=9, column=2, pady=5, padx= 3)

registerMemoryDirection = StringVar()
registerMemoryDirection.set("RM")

fromRegisterToMemory = Radiobutton(root,variable=registerMemoryDirection, text="from register to memory", value="RM").grid(row=0, column=4, pady=5, padx= 3)
fromMemoryToRegister = Radiobutton(root,variable=registerMemoryDirection, text="from memory to register", value="MR").grid(row=1, column=4, pady=5, padx= 3)

addressType = StringVar()
addressType.set("I")

indexAddressType = Radiobutton(root,variable=addressType, text="index", value="I").grid(row=2, column=4, pady=5, padx= 3)
baseAddressType = Radiobutton(root,variable=addressType, text="base", value="B").grid(row=3, column=4, pady=5, padx= 3)
indexBaseAddressType = Radiobutton(root,variable=addressType, text="index-base", value="IB").grid(row=4, column=4, pady=5, padx= 3)

indexTypeValue = StringVar()
indexTypeValue.set("SI")

sourceIndexRegister = Radiobutton(root,variable=indexTypeValue, text="SI", value="SI").grid(row=5, column=4, pady=5, padx= 3)
destinationIndexRegister = Radiobutton(root,variable=indexTypeValue, text="DI", value="DI").grid(row=6, column=4, pady=5, padx= 3)

baseTypeValue = StringVar()
baseTypeValue.set("BX")

basisRegister = Radiobutton(root,variable=baseTypeValue, text="BX", value="BX").grid(row=5, column=5, pady=5, padx= 3)
basisPointer = Radiobutton(root,variable=baseTypeValue, text="BP", value="BP").grid(row=6, column=5, pady=5, padx= 3)

indexBaseTypeValue = StringVar()
indexBaseTypeValue.set("SIBX")

sourceIndexBasisRegister = Radiobutton(root,variable=indexBaseTypeValue, text="SI BX", value="SIBX").grid(row=7, column=4, pady=5, padx= 3)
destinationIndexBasisRegister = Radiobutton(root,variable=indexBaseTypeValue, text="DI BX", value="DIBX").grid(row=8, column=4, pady=5, padx= 3)
sourceIndexBasisPointer = Radiobutton(root,variable=indexBaseTypeValue, text="SI BP", value="SIBP").grid(row=9, column=4, pady=5, padx= 3)
destinationIndexBasisPointer = Radiobutton(root,variable=indexBaseTypeValue, text="DI BP", value="DIBP").grid(row=10, column=4, pady=5, padx= 3)

def resetAddressValues():
    for register in index_registers.values():
        register.reset()
    displaceValue.set("0000")

def saveAddressValues():
    disp = displaceInput.get()
    for name, input in index_inputs.items():
        input_value = input.get()
        if len(input_value) == 4:
            index_registers[name].set(input_value)
            input.delete(0,END)
    if len(disp) == 4:
        displaceValue.set(disp)
        displaceInput.delete(0,END)

def pushStack(registerName):
    stackPointer = int(spValue.get(), 16)
    if stackPointer == MAX_4_HEX:
        pass
    else:
        value = registers[registerName].get()
        stack.put(value)
        raisePointer = stackPointer + int('0002',16)
        spValue.set(to_hex_string(raisePointer))

def popStack(registerName):
    stackPointer = int(spValue.get(), 16)
    if stackPointer == MIN_4_HEX:
        pass
    else:
        value = stack.get()
        registers[registerName].set(value)
        decreasePointer = stackPointer - int('0002',16)
        spValue.set(to_hex_string(decreasePointer))

toMemoryOrRegister = StringVar()
toMemoryOrRegister.set("AX")

toOrFromAx = Radiobutton(root,variable=toMemoryOrRegister, text="AX", value="AX").grid(row=7, column=5, pady=5, padx= 3)
toOrFromoBx = Radiobutton(root,variable=toMemoryOrRegister, text="BX", value="BX").grid(row=8, column=5, pady=5, padx= 3)
toOrFromCx = Radiobutton(root,variable=toMemoryOrRegister, text="CX", value="CX").grid(row=9, column=5, pady=5, padx= 3)
toOrFromDx = Radiobutton(root,variable=toMemoryOrRegister, text="DX", value="DX").grid(row=10, column=5, pady=5, padx= 3)


siLabel = Label(root, text="SI").grid(row=0, column=6, pady=5)
diLabel = Label(root, text="DI").grid(row=1, column=6, pady=5)
bpLabel = Label(root, text="BP").grid(row=2, column=6, pady=5)
spLabel = Label(root, text="SP").grid(row=3, column=6, pady=5)

si = Entry(root, width=7, textvariable=siValue, state="readonly")
di = Entry(root, width=7, textvariable=diValue, state="readonly")
bp = Entry(root, width=7, textvariable=bpValue, state="readonly")
sp = Entry(root, width=7, textvariable=spValue, state="readonly")

si.grid(row=0, column=7, pady=5, padx= 3)
di.grid(row=1, column=7, pady=5, padx= 3)
bp.grid(row=2, column=7, pady=5, padx= 3)
sp.grid(row=3, column=7, pady=5, padx= 3)


siInput.grid(row=0, column=8, pady=5, padx= 3)
diInput.grid(row=1, column=8, pady=5, padx= 3)
bpInput.grid(row=2, column=8, pady=5, padx= 3)
# spInput.grid(row=3, column=8, pady=5, padx= 3)

displacementLabel = Label(root, text="DISP").grid(row=4, column=6, pady=5)
displace = Entry(root, width=7, textvariable=displaceValue, state="readonly")
displace.grid(row=4, column=7, pady=5, padx= 3)
displaceInput = Entry(root, width=7)
displaceInput.grid(row=4, column=8, pady=5, padx= 3)

resetAddressButton = Button(root, text="Reset", command=resetAddressValues).grid(row=5, column=7)
saveAddressButton = Button(root, text="Save", command=saveAddressValues).grid(row=5, column=8)

movAddress = Button(root, text="MOV", command=move_registry_memory).grid(row=6, column=7, pady=5, padx= 3)
xchgAddress = Button(root, text="XCHG", command=exchange_registry_memory).grid(row=6, column=8, pady=5, padx= 3)

pushAX = Button(root, text="PUSH AX", command=lambda: pushStack('AX')).grid(row=7, column=7, pady=5, padx= 3)
pushBX = Button(root, text="PUSH BX", command=lambda: pushStack('BX')).grid(row=8, column=7, pady=5, padx= 3)
pushCX = Button(root, text="PUSH CX", command=lambda: pushStack('CX')).grid(row=9, column=7, pady=5, padx= 3)
pushDX = Button(root, text="PUSH DX", command=lambda: pushStack('DX')).grid(row=10, column=7, pady=5, padx= 3)

popAX = Button(root, text="POP AX", command=lambda: popStack('AX')).grid(row=7, column=8, pady=5, padx= 3)
popBX = Button(root, text="POP BX", command=lambda: popStack('BX')).grid(row=8, column=8, pady=5, padx= 3)
popCX = Button(root, text="POP CX", command=lambda: popStack('CX')).grid(row=9, column=8, pady=5, padx= 3)
popDX = Button(root, text="POP DX", command=lambda: popStack('DX')).grid(row=10, column=8, pady=5, padx= 3)

root.mainloop()