#!/usr/bin/env python3

main_char = 'U'
chars = ["U", "R", "A", "C", "I", "J", "S"]

chars_dict = {}
for i in range(len(chars)):
    chars_dict[chars[i].lower()] = True

def valid(s):
    if len(s)<3:
        return False
    for i in range(len(s)):
        if s[i]=="\n":
            continue
        if s[i].lower() in chars_dict:
            continue
        else:
            return False
    return True

out = []
with open ("./DISC2-LP.txt", "r") as file:
    for line in file:
        if main_char.lower() in line.lower():
            line = line.strip('\n')
            line = line.strip('\t')
            if valid(line)==True:
                out.append(line)

print("let words=", out)
print(
"""
let keyCodes = {"0":48,"1":49,"2":50,"3":51,"4":52,"5":53,"6":54,"7":55,"8":56,"9":57,"d":68,"b":66,"a":65,"s":83,"i":73,"f":70,"k":75,"ß":219,"Dead":220,"+":187,"ü":186,"p":80,"o":79,"u":85,"z":90,"t":84,"r":82,"e":69,"w":87,"g":71,"h":72,"j":74,"l":76,"ö":192,"ä":222,"#":191,"y":89,"x":88,"c":67,"v":86,"n":78,"m":77,",":188,".":190,"-":189,"ArrowRight":39,"ArrowLeft":37,"ArrowUp":38,"ArrowDown":40,"PageDown":34,"Clear":12,"Home":36,"PageUp":33,"End":35,"Delete":46,"Insert":45,"Control":17,"AltGraph":18,"Meta":92,"Alt":18,"Shift":16,"CapsLock":20,"Tab":9,"Escape":27,"F1":112,"F2":113,";":188,":":190,"_":189,"'":191,"*":187,"Q":81,"W":87,"E":69,"R":82,"T":84,"Z":90,"S":83,"A":65,"D":68,"I":73,"U":85,"O":79,"Y":89,"X":88,"C":67,"F":70,"V":86,"G":71,"B":66,"H":72,"N":78,"J":74,"M":77,"K":75,"L":76,"P":80,"Ö":192,"Ä":222,"Ü":186,"!":49,"§":51,"$":52,"%":53,"&":54,"/":55,"(":56,")":57,"=":48,"?":219,"°":220};

let btn = document.getElementById("submit-button");

function useWord(w) {
	for(let i=0; i<w.length; i++) {
		document.body.dispatchEvent(new KeyboardEvent('keydown', {
		  'keyCode': keyCodes[w[i]]
		}));
	}
	btn.click();
}

for (let i = 0; words.length; i++) {
	useWord(words[i]);
}
""")
