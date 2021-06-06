from tkinter import *

root = Tk()
root.title("Simulator 8086")

axValue = StringVar()
axValue.set("0000")

bxValue = StringVar()
bxValue.set("0000")

cxValue = StringVar()
cxValue.set("0000")

dxValue = StringVar()
dxValue.set("0000")

def saveRegisterValues():
    ax = axInput.get()
    bx = bxInput.get()
    cx = cxInput.get()
    dx = dxInput.get()
    if ax == "":
        pass
    else:
        axValue.set(ax)
        axInput.delete(0,END)
    
    if bx == "":
        pass
    else:
        bxValue.set(bx)
        bxInput.delete(0,END)

    if cx == "":
        pass
    else:
        cxValue.set(cx)
        cxInput.delete(0,END)

    if dx == "":
        pass
    else:
        dxValue.set(dx)
        dxInput.delete(0,END)

def resetRegisterValues():
    axValue.set("0000")
    bxValue.set("0000")
    cxValue.set("0000")
    dxValue.set("0000")

def moveRegisterValue():
    if fromRegister.get() == "AX":
        if toRegister.get() == "AX":
            pass
        elif toRegister.get() == "BX":
            bxValue.set(axValue.get())
        elif toRegister.get() == "CX":
            cxValue.set(axValue.get())
        elif toRegister.get() == "DX":
            dxValue.set(axValue.get())

    if fromRegister.get() == "BX":
        if toRegister.get() == "BX":
            pass
        elif toRegister.get() == "AX":
            axValue.set(bxValue.get())
        elif toRegister.get() == "CX":
            cxValue.set(bxValue.get())
        elif toRegister.get() == "DX":
            dxValue.set(bxValue.get())

    if fromRegister.get() == "CX":
        if toRegister.get() == "CX":
            pass
        elif toRegister.get() == "BX":
            bxValue.set(cxValue.get())
        elif toRegister.get() == "AX":
            axValue.set(cxValue.get())
        elif toRegister.get() == "DX":
            dxValue.set(cxValue.get())

    if fromRegister.get() == "DX":
        if toRegister.get() == "DX":
            pass
        elif toRegister.get() == "BX":
            bxValue.set(dxValue.get())
        elif toRegister.get() == "CX":
            cxValue.set(dxValue.get())
        elif toRegister.get() == "AX":
            axValue.set(dxValue.get())

def exchangeRegisterValue():
    if fromRegister.get() == "AX":
        if toRegister.get() == "AX":
            pass
        elif toRegister.get() == "BX":
            temp = bxValue.get()
            bxValue.set(axValue.get())
            axValue.set(temp)
        elif toRegister.get() == "CX":
            temp = cxValue.get()
            cxValue.set(axValue.get())
            axValue.set(temp)
        elif toRegister.get() == "DX":
            temp = dxValue.get()
            dxValue.set(axValue.get())
            axValue.set(temp)

    if fromRegister.get() == "BX":
        if toRegister.get() == "BX":
            pass
        elif toRegister.get() == "AX":
            temp = axValue.get()
            axValue.set(bxValue.get())
            bxValue.set(temp)
        elif toRegister.get() == "CX":
            temp = cxValue.get()
            cxValue.set(bxValue.get())
            bxValue.set(temp)
        elif toRegister.get() == "DX":
            temp = dxValue.get()
            dxValue.set(bxValue.get())
            bxValue.set(temp)

    if fromRegister.get() == "CX":
        if toRegister.get() == "CX":
            pass
        elif toRegister.get() == "BX":
            temp = bxValue.get()
            bxValue.set(cxValue.get())
            cxValue.set(temp)
        elif toRegister.get() == "AX":
            temp = axValue.get()
            axValue.set(cxValue.get())
            cxValue.set(temp)
        elif toRegister.get() == "DX":
            temp = dxValue.get()
            dxValue.set(cxValue.get())
            cxValue.set(temp)

    if fromRegister.get() == "DX":
        if toRegister.get() == "DX":
            pass
        elif toRegister.get() == "BX":
            temp = bxValue.get()
            bxValue.set(dxValue.get())
            dxValue.set(temp)
        elif toRegister.get() == "CX":
            temp = cxValue.get()
            cxValue.set(dxValue.get())
            dxValue.set(temp)
        elif toRegister.get() == "AX":
            temp = axValue.get()
            axValue.set(dxValue.get())
            dxValue.set(temp)

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

axInput = Entry(root, width=7)
bxInput = Entry(root, width=7)
cxInput = Entry(root, width=7)
dxInput = Entry(root, width=7)

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

root.mainloop()